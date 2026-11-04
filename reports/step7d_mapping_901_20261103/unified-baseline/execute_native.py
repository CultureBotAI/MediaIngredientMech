"""Execute the unchanged native builder with one explicit output and write barrier."""
from pathlib import Path
import hashlib
import json
import os
import sys
import traceback

HERE = Path(__file__).resolve().parent
RUN = HERE.parents[1]
CLAW = RUN / "step7c-claw"
W = RUN / "step7d"
CULTURE = Path("/Users/marcin/Documents/VIMSS/ontology/Mechs/CultureMech")
PRODUCER = CLAW / "scripts/build_unified_ingredient_mapping.py"
OUTPUT_DIR = HERE / "output"
OUTPUT = OUTPUT_DIR / "unified-diagnostic.tsv"
AUDIT = HERE / "worker-audit.json"
assert OUTPUT_DIR.is_dir() and not OUTPUT.exists() and not AUDIT.exists()
raw = (HERE / "executed-producer.py").read_bytes()
assert raw == PRODUCER.read_bytes()
assert hashlib.sha256(raw).hexdigest() == "26d0c6808728ddaef5201ccebe24fff8c4174c4a5b37753e79c671a628c521d1"
sys.dont_write_bytecode = True
sys.pycache_prefix = str(HERE / "unused-bytecode-cache")
read_paths = set()
writes = []
refusals = []
allowed_processes = []
write_flags = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND


def safe_path(value):
    path = Path(os.fsdecode(value)).absolute()
    if any(parent.is_symlink() for parent in (path, *path.parents)):
        raise PermissionError("Aliased write path: " + str(path))
    return path.resolve()


def audit(event, args):
    if event == "open":
        target, mode, flags = args
        writing = bool((flags or 0) & write_flags) or (isinstance(mode, str) and any(char in mode for char in "wax+"))
        if isinstance(target, int):
            if writing and target not in (1, 2):
                raise PermissionError("Unexpected fd write")
            return
        if writing:
            path = safe_path(target)
            if path not in {OUTPUT, AUDIT, Path("/dev/null")}:
                refusals.append({"event": event, "path": str(path)})
                raise PermissionError("Write outside diagnostic outputs: " + str(path))
            writes.append({"event": event, "path": str(path), "mode": mode, "flags": flags})
        else:
            read_paths.add(str(Path(os.fsdecode(target)).absolute()))
    elif event == "os.mkdir":
        path = safe_path(args[0])
        if path != OUTPUT_DIR:
            refusals.append({"event": event, "path": str(path)})
            raise PermissionError("Unexpected directory creation")
    elif event == "subprocess.Popen" and args[0] == "/usr/bin/git" and list(args[1]) == ["/usr/bin/git", "version"]:
        allowed_processes.append({"executable": args[0], "argv": list(args[1])})
    elif event.startswith(("socket.", "subprocess.", "os.exec", "os.spawn", "os.posix_spawn")) or event in {
        "os.system", "os.remove", "os.rmdir", "os.rename", "os.link", "os.symlink", "os.chmod", "os.chown", "os.truncate", "os.utime",
    }:
        refusals.append({"event": event})
        raise PermissionError("Forbidden side effect: " + event)


sys.addaudithook(audit)
sys.argv = [str(PRODUCER), "--culturemech", str(CULTURE), "--mim", str(W), "--output", str(OUTPUT), "--format", "tsv"]
error = None
try:
    exec(compile(raw, str(PRODUCER), "exec"), {"__name__": "__main__", "__file__": str(PRODUCER)})
except BaseException as exc:
    error = {"type": type(exc).__name__, "message": str(exc)}
    traceback.print_exc()
finally:
    module_inputs = {}
    for name, module in sorted(sys.modules.items()):
        location = getattr(module, "__file__", None)
        if location and Path(location).is_file() and any(name == prefix or name.startswith(prefix + ".") for prefix in ("kg_microbe_fleet", "plugins", "yaml", "dotenv")):
            path = Path(location).resolve()
            module_inputs[name] = {"path": str(path), "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    assert module_inputs["kg_microbe_fleet"]["path"] == str(CLAW / "src/kg_microbe_fleet/__init__.py")
    if error is None:
        assert module_inputs["plugins.ingredient_name_normalizer"]["path"] == str(CLAW / "plugins/ingredient_name_normalizer.py")
    doc = {"status": "PASS" if error is None else "FAILED", "argv": sys.argv,
           "executed_producer_sha256": hashlib.sha256(raw).hexdigest(), "python": sys.version,
           "executable": sys.executable, "read_paths": sorted(read_paths), "write_events": writes,
           "refused_events": refusals, "allowed_read_only_processes": allowed_processes, "module_inputs": module_inputs, "error": error,
           "limitations": "Python audit barrier for this inspected native program, not a general hostile-code sandbox. No stamping, promotion or provider invocation; only /usr/bin/git version may run for native import initialization, with its /dev/null I/O allowed."}
    with AUDIT.open("x") as stream:
        json.dump(doc, stream, indent=2)
        stream.write("\n")
if error:
    raise SystemExit(1)
