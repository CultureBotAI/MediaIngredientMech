"""Read-only helper extraction; real Git fixture proves rename-source coverage."""
from pathlib import Path
import ast
import hashlib
import json
import subprocess

OWN = Path(__file__).resolve().parent
source = OWN.parent / "verify_mim_merge_nul.py"
assert hashlib.sha256(source.read_bytes()).hexdigest() == "869d6925c57402f7867e8ab8f1c6a2b472125b57faa945332472993cea3b080a"
parsed = ast.parse(source.read_bytes())
function = next(n for n in parsed.body if isinstance(n, ast.FunctionDef) and n.name == "verified_changed_paths")
ns = {"subprocess": subprocess}
exec(compile(ast.Module(body=[function], type_ignores=[]), str(source), "exec"), ns)
verify = ns["verified_changed_paths"]
repo = OWN / "merge-rename-fixture"
repo.mkdir(exist_ok=False)
def git(*args):
    return subprocess.check_output(["git", *args], cwd=repo)
git("init", "-q")
git("config", "user.name", "Independent offline fixture")
git("config", "user.email", "independent@example.invalid")
git("config", "diff.renames", "true")
old, new = "Α-old.yaml", "β-new.yaml"
(repo / old).write_text("reviewed identity bytes\n")
git("add", "--", old); git("commit", "-qm", "fixture base")
base = git("rev-parse", "HEAD").decode().strip()
git("mv", "--", old, new); git("commit", "-qm", "reviewed rename")
head = git("rev-parse", "HEAD").decode().strip()
positive = verify(repo, base, head, head)
assert positive == [new]
(repo / old).write_text("unreviewed resurrected old owner\n")
git("add", "--", old); git("commit", "-qm", "simulated wrong merge")
wrong = git("rev-parse", "HEAD").decode().strip()
accepted = verify(repo, base, head, wrong)
assert accepted == [new]
all_changed = git("diff", "--name-only", "-z", "--no-renames", base, head, "--")
complete_paths = [p.decode() for p in all_changed.split(b"\0") if p]
difference = git("--literal-pathspecs", "diff", head, wrong, "--", *complete_paths)
assert set(complete_paths) == {old, new} and difference
proof = {"helper_sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "fixture_only": True,
         "changed_paths_with_default_rename_detection": positive,
         "all_changed_paths_without_rename_detection": complete_paths,
         "wrong_merge_resurrecting_old_path_accepted": True,
         "complete_path_comparison_detects_difference": True,
         "production_merge_mismatch_alleged": False, "production_mutations": False}
(OWN / "merge-rename-proof.json").write_text(json.dumps(proof, indent=2) + "\n")
print(json.dumps(proof, indent=2))
