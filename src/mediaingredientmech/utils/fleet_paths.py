"""
Resolving another Mech checkout from its fleet environment variable.

The fleet addresses sibling repositories through ``<REPO>_ROOT`` variables --
``CULTUREMECH_ROOT``, ``KGMICROBE_ROOT``, ``MEDIAINGREDIENTMECH_ROOT``. The
obvious way to read one is wrong in two ways that both fail quietly:

.. code-block:: python

    Path(os.environ.get("CULTUREMECH_ROOT", REPO_ROOT.parent / "CultureMech"))

``os.environ.get`` falls back only when the variable is **absent**, so an
exported-but-empty value becomes ``Path("")``, which is ``.`` -- every path
built on it then resolves against whatever the working directory happens to
be, and the script reads a file that is not there instead of failing. And a
``~/checkouts/CultureMech`` value becomes a literal directory named ``~``.

An empty value is ordinary: a wrapper that sets the variable from an unset
one, or a CI step whose input was blank. See MediaIngredientMech#580.
"""

from __future__ import annotations

import logging
import os
from collections.abc import Sequence
from pathlib import Path

logger = logging.getLogger(__name__)


def _value_of(env_var: str) -> str | None:
    """
    Return the variable's value when it names something, else None.

    :param env_var: Environment variable to read.
    :return: The stripped value, or None when unset, empty or whitespace.
    """
    value = os.environ.get(env_var)
    return value.strip() if value and value.strip() else None


def checkout_root(env_var: str, fallback: Path, *, deprecated: Sequence[str] = ()) -> Path:
    """
    Return the checkout root named by ``env_var``, else ``fallback``.

    A variable that is unset, empty, or whitespace counts as unset. A value
    starting with ``~`` is expanded.

    ``deprecated`` names older spellings that still work. The fleet-standard
    ``env_var`` always wins; a deprecated name is honoured only when the
    standard one names nothing, and doing so logs a warning naming both. A
    silently-ignored variable is the defect this argument exists to prevent:
    before it, exporting ``CULTUREMECH_ROOT`` steered one script and was
    ignored by another that read ``CULTUREMECH_DIR``, with no indication
    (MediaIngredientMech#593).

    :param env_var: Fleet environment variable naming the checkout, e.g.
        ``"CULTUREMECH_ROOT"``.
    :param fallback: Path to use when no variable names one.
    :param deprecated: Older variable names, tried in order after ``env_var``.
    :return: The resolved checkout root. Existence is not checked -- callers
        report a missing checkout in their own terms.
    """
    value = _value_of(env_var)
    if value:
        return Path(value).expanduser()

    for old_name in deprecated:
        old_value = _value_of(old_name)
        if old_value:
            logger.warning(
                "%s is deprecated; use %s. Honouring %s=%s for now.",
                old_name,
                env_var,
                old_name,
                old_value,
            )
            return Path(old_value).expanduser()

    return Path(fallback).expanduser()
