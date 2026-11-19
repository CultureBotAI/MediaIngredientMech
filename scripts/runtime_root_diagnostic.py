"""Read-only pytest failure operands for the non-gating Linux diagnostic (#1450).

Run with the ordinary pytest arguments. This plugin never changes an outcome,
executes a guard, imports production code, or changes environment/search paths.
Only a matching failed traceback frame can produce a bounded operand receipt.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import pytest

TARGET = ("src", "mediaingredientmech", "curate", "curation_successor.py")
OUTPUT = Path(".temp/runtime-ci-diagnostic-1450")


def _frames(error):
    """Include the native ValueError wrapped by pytest.raises' regex failure."""
    seen = set()
    for _ in range(8):
        if error is None or id(error) in seen:
            return
        seen.add(id(error))
        traceback = error.__traceback__
        for _ in range(128):
            if traceback is None:
                break
            frame = traceback.tb_frame
            if (
                frame.f_code.co_name == "_runtime_root"
                and Path(frame.f_code.co_filename).parts[-4:] == TARGET
            ):
                yield error, traceback
            traceback = traceback.tb_next
        error = error.__cause__ or error.__context__


def _operands(error, traceback):
    frame = traceback.tb_frame
    local = frame.f_locals
    runtime = frame.f_globals["sys"]
    # These are explicit allowlists, not serialization of locals, cfg or env.
    root, prefix, base = (local[name] for name in ("root", "prefix", "base"))
    if not all(isinstance(value, Path) for value in (root, prefix, base)):
        raise TypeError("Unexpected runtime-root path operand")
    values = local["values"]
    cfg = {key: values[key] for key in ("home", "version", "version_info") if key in values}
    if not all(isinstance(value, str) and len(value) <= 4096 for value in cfg.values()):
        raise TypeError("Unexpected selected configuration operand")
    versions = local["versions"]
    if not isinstance(versions, set) or not all(isinstance(value, str) for value in versions):
        raise TypeError("Unexpected runtime version operand")
    expected = ".".join(map(str, runtime.version_info[:3]))
    home = Path(cfg["home"]).resolve()
    binary = (prefix / "bin/python3").resolve()
    return {
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Traceback operands plus read-only post-failure path resolution; not authentication or approval",
        "frame": {
            "filename": frame.f_code.co_filename,
            "function": frame.f_code.co_name,
            "line": traceback.tb_lineno,
            "exception_type": type(error).__name__,
        },
        "captured_frame_operands": {
            "root": str(root),
            "prefix": str(prefix),
            "base": str(base),
            "cfg_fields": cfg,
            "versions": sorted(versions),
        },
        "selected_process_readback": {
            "_base_executable": runtime._base_executable,
            "base_prefix": runtime.base_prefix,
            "version": runtime.version,
            "version_info": list(runtime.version_info),
        },
        "post_failure_resolution": {
            "cfg_home": str(home),
            "base_parent": str(base.parent),
            "prefix_bin_python3": str(binary),
            "expected_version": expected,
            "home_equals_base_parent": home == base.parent,
            "versions_equal_selected_version": versions == {expected},
            "bin_python3_equals_base": binary == base,
        },
    }


class RuntimeRootDiagnostic:
    def __init__(self, output=OUTPUT):
        self.output = output
        self.written = 0
        self.unmatched_failures = 0
        self.errors = []

    @pytest.hookimpl(hookwrapper=True)
    def pytest_runtest_makereport(self, item, call):
        outcome = yield
        report = outcome.get_result()
        if not report.failed or call.excinfo is None:
            return
        try:
            match = next(_frames(call.excinfo.value), None)
            if match is None:
                self.unmatched_failures += 1
                return
            record = _operands(*match)
            record["test_nodeid"] = item.nodeid
            record["test_phase"] = call.when
            self.output.mkdir(parents=True, exist_ok=True)
            destination = self.output / f"runtime-root-operands-{self.written + 1:04d}.json"
            with destination.open("x", encoding="utf-8") as handle:
                json.dump(record, handle, indent=2)
                handle.write("\n")
            self.written += 1
        except Exception as error:
            # Diagnostic failure must never replace the original pytest result.
            self.errors.append(type(error).__name__)


def main():
    plugin = RuntimeRootDiagnostic()
    result = pytest.main(sys.argv[1:], plugins=[plugin])
    print(
        json.dumps(
            {
                "runtime_root_diagnostic": {
                    "written": plugin.written,
                    "failed_reports_without_target_frame": plugin.unmatched_failures,
                    "diagnostic_error_types": plugin.errors,
                }
            }
        )
    )
    return int(result)


if __name__ == "__main__":
    raise SystemExit(main())
