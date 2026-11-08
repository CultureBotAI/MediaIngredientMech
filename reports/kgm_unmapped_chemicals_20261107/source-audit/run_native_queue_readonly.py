"""Run the exact KG helper with writes confined to this MIM audit directory."""
import csv
import datetime
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parent
KG = Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-mim-1788-20261107")
kind = sys.argv[1]
assert kind in {"mediadive", "microbedecoder"}
script = KG / "scripts" / ("dump_unmapped_mediadive_ingredients.py" if kind == "mediadive"
                            else "dump_unmapped_microbedecoder_labels.py")
output = ROOT / "queues" / (kind + "-fresh.tsv")
assert not output.exists(), "Never overwrite a prior queue"
sys.dont_write_bytecode = True
sys.path.insert(0, str(KG))
os.environ.update({"TMPDIR": str(ROOT / "runtime-tmp"),
                   "XDG_CACHE_HOME": str(ROOT / "runtime-cache"),
                   "MPLCONFIGDIR": str(ROOT / "runtime-cache" / "matplotlib"),
                   "PYTHONDONTWRITEBYTECODE": "1"})
reads, writes, denied = set(), set(), []


def pathof(value):
    if isinstance(value, (str, bytes, os.PathLike)):
        return Path(os.fsdecode(value)).resolve()
    return None


def allow_write(value, event):
    path = pathof(value)
    if path is not None and (path == ROOT or ROOT in path.parents):
        writes.add(str(path))
        return
    denied.append({"event": event, "path": str(path)})
    raise PermissionError("Native queue audit forbids writes outside MIM source-audit: " + str(path))


def audit(event, args):
    if event == "open":
        path = pathof(args[0])
        mode, flags = args[1], args[2]
        writable = (isinstance(mode, str) and any(c in mode for c in "wax+")) or (
            isinstance(flags, int) and bool(flags & (os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_TRUNC | os.O_APPEND)))
        if writable:
            allow_write(args[0], event)
        elif path is not None and (path == KG or KG in path.parents):
            reads.add(str(path))
    elif event in {"os.mkdir", "os.remove", "os.rmdir", "os.chmod", "os.truncate", "os.utime"}:
        allow_write(args[0], event)
    elif event in {"os.rename", "os.link", "os.symlink"}:
        allow_write(args[0], event)
        allow_write(args[1], event)
    elif event in {"socket.connect", "socket.bind", "socket.getaddrinfo", "subprocess.Popen", "os.system"}:
        denied.append({"event": event})
        raise PermissionError("Native queue audit forbids network and subprocess side effects: " + event)


sys.addaudithook(audit)
started = datetime.datetime.now(datetime.timezone.utc).isoformat()
if kind == "mediadive":
    sys.argv = [str(script), "--nodes", str(KG / "data/transformed/mediadive/nodes.tsv"), "--output", str(output)]
else:
    sys.argv = [str(script), "--input", str(KG / "data/transformed/microbedecoder/unmapped_labels.tsv"),
                "--prefix", "compound", "--min-occurrences", "0", "--output", str(output)]
arguments = list(sys.argv)
status = "FAILED"
try:
    namespace = runpy.run_path(str(script), run_name="__main__")
    if kind == "mediadive":
        loader = namespace["ChemicalMappingLoader"]()
        with (ROOT / "queues" / "mediadive-native-identity-retry.tsv").open("x", newline="") as handle:
            writer = csv.writer(handle, delimiter="\t")
            writer.writerow(["source_id", "source_label", "native_identity_target", "queue_disposition"])
            for source_id, label in namespace["iter_unmapped_rows"](KG / "data/transformed/mediadive/nodes.tsv"):
                target = loader.find_chebi_by_name(label) if label else None
                writer.writerow([source_id, label, target or "", "RECOVERED_BY_NATIVE_LOOKUP" if target else
                                 ("STILL_UNMAPPED" if label else "EMPTY_LABEL_SKIPPED_BY_HELPER")])
    status = "PASS"
finally:
    modules = []
    for name, module in sorted(sys.modules.items()):
        value = getattr(module, "__file__", None)
        if value:
            path = Path(value).resolve()
            if KG in path.parents and path.is_file():
                modules.append({"module": name, "path": str(path),
                                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
    result = {"kind": kind, "status": status, "started_at": started,
              "finished_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "python": sys.version, "python_executable": sys.executable,
              "helper_argv": arguments, "helper_sha256": hashlib.sha256(script.read_bytes()).hexdigest(),
              "output": str(output), "output_sha256": hashlib.sha256(output.read_bytes()).hexdigest()
              if output.exists() else None, "kg_read_paths": sorted(reads),
              "write_paths": sorted(writes), "denied_events": denied, "loaded_kg_modules": modules,
              "network_calls_allowed": False, "kg_writes_allowed": False,
              "mediadive_occurrences_contract": "Helper constant 1; not a measured recipe frequency"}
    with (ROOT / "native-runs" / (kind + "-run.json")).open("x") as handle:
        json.dump(result, handle, indent=2)
        handle.write("\n")
