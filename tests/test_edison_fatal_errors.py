"""Guard test: account-level API refusals abort the batch, transient ones do not.

A 402 was once treated as a per-record failure. The runner dutifully logged it,
moved to the next record, failed again, and the supervisor relaunched the shard
-- 1,121 records "attempted" and 1,731 rate-limit responses in half an hour, not
one of which could have succeeded, against an API already refusing service.

The distinction is therefore load-bearing in both directions, and both are
tested here: a 402/401/403 must stop everything, and a ConnectTimeout must not.
"""

import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))


def _load():
    spec = importlib.util.spec_from_file_location(
        "research_ingredient_edison", ROOT / "scripts" / "research_ingredient_edison.py"
    )
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class _Response:
    def __init__(self, status_code):
        self.status_code = status_code


class _HTTPStatusError(Exception):
    """Stand-in for httpx.HTTPStatusError: carries a .response with a status."""

    def __init__(self, status_code):
        super().__init__(f"Client error '{status_code}'")
        self.response = _Response(status_code)


class _RetryError(Exception):
    """Stand-in for tenacity.RetryError, which wraps the real cause."""

    def __init__(self, cause):
        super().__init__("RetryError")
        self.last_attempt = _Attempt(cause)


class _Attempt:
    def __init__(self, cause):
        self.failed = True
        self._cause = cause

    def exception(self):
        return self._cause


@pytest.mark.parametrize("status", [401, 402, 403])
def test_account_level_statuses_are_terminal(status):
    mod = _load()
    reason = mod._terminal_api_error(_HTTPStatusError(status))
    assert reason and str(status) in reason


@pytest.mark.parametrize("status", [408, 429, 500, 502, 503])
def test_transient_statuses_are_not_terminal(status):
    """429 in particular must stay retryable -- it is backpressure, not refusal."""
    mod = _load()
    assert mod._terminal_api_error(_HTTPStatusError(status)) is None


def test_unwraps_tenacity_retry_error():
    """The SDK retries internally, so the 402 arrives wrapped, not bare.

    Inspecting only the outermost exception is what let the original 402 through
    as an ordinary per-record failure.
    """
    mod = _load()
    assert mod._terminal_api_error(_RetryError(_HTTPStatusError(402)))


def test_unwraps_chained_cause():
    mod = _load()
    outer = RuntimeError("submitting failed")
    outer.__cause__ = _HTTPStatusError(402)
    assert mod._terminal_api_error(outer)


def test_plain_transient_errors_are_not_terminal():
    mod = _load()
    assert mod._terminal_api_error(ConnectionError("connect timeout")) is None
    assert mod._terminal_api_error(_RetryError(ConnectionError("connect timeout"))) is None


def test_cyclic_exception_chain_terminates():
    """A self-referential __context__ must not hang the unwrap loop."""
    mod = _load()
    a = RuntimeError("a")
    b = RuntimeError("b")
    a.__context__ = b
    b.__context__ = a
    assert mod._terminal_api_error(a) is None


def test_fatal_exit_code_is_distinct():
    """The supervisor keys on this to stop relaunching; 2 already means 'done'."""
    mod = _load()
    assert mod.EXIT_FATAL_API == 3
