"""External read-only-W regression controls for orchestration finding #1126.

Uses a fresh disposable Git fixture. No maintained repository edits or native
refresh execution. Invokes the exact inventory assignments and equality guard
extracted from each immutable orchestration version.
"""
from __future__ import annotations
import ast
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

D = Path(__file__).resolve().parent
W = D.parent / "step7d"
BASE = "7d35035f6c521c69fad94f73381c6a6eb7251fff"
ROOTS = ("data/ingredients", "data/curated", "src", "scripts", "tests", ".github/workflows")
OLD = D / "refresh_post1122_v3.py"
NEW = D / "refresh_post1122_v4.py"
RESULT = D / "post1122-orchestration-readonly-checks-v4.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def demand(condition, message):
    if not condition:
        raise ValueError(message)


def preflight_ast(path):
    tree = ast.parse(path.read_bytes())
    return tree, next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "preflight")


def inventory_program(path):
    _, preflight = preflight_ast(path)
    statements = []
    for node in preflight.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id in {"baseline_paths", "current_paths"}
            for t in node.targets
        ):
            statements.append(node)
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            if any(isinstance(a, ast.Constant) and a.value == "source/code/test/workflow tracked membership changed" for a in node.value.args):
                statements.append(node)
    demand(len(statements) == 3, "exact native inventory assignments and guard not located")
    return compile(ast.fix_missing_locations(ast.Module(body=statements, type_ignores=[])), str(path), "exec")


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], stderr=subprocess.PIPE)


def evaluate(path, repo, base):
    namespace = {
        "git": lambda *args: git(repo, *args),
        "tracked": lambda: [p for p in git(repo, "ls-files", "-z").decode().split("\0") if p],
        "BASE": base,
        "source_roots": ROOTS,
        "require": demand,
    }
    exec(inventory_program(path), namespace)
    return len(namespace["baseline_paths"]), len(namespace["current_paths"])


def reject(path, repo, base):
    try:
        evaluate(path, repo, base)
    except ValueError as error:
        demand(str(error) == "source/code/test/workflow tracked membership changed", "unexpected failure")
        return str(error)
    raise AssertionError("unexpected inventory accepted")


def main():
    demand(not RESULT.exists(), "result already exists")
    checks = []
    old_bytes = OLD.read_bytes()
    new_bytes = NEW.read_bytes()
    old_expression = b"baseline_paths=set(git('ls-tree','-r','--name-only',BASE,'--',*source_roots).decode().splitlines())"
    new_expression = b"baseline_paths={n for n in git('ls-tree','-r','--name-only','-z',BASE,'--',*source_roots).decode().split('\\0')if n}"
    demand(old_bytes.count(old_expression) == 1, "ambiguous predecessor expression")
    demand(new_bytes == old_bytes.replace(old_expression, new_expression), "v4 changed more than exact NUL parser")
    checks.append("v4 bytes differ from v3 only in baseline inventory parser; exact membership guard retained")
    old_tree, _ = preflight_ast(OLD)
    new_tree, _ = preflight_ast(NEW)
    for tree in (old_tree, new_tree):
        preflight = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "preflight")
        preflight.body = [n for n in preflight.body if not (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "baseline_paths" for t in n.targets))]
    demand(ast.dump(old_tree) == ast.dump(new_tree), "unexpected AST drift outside baseline inventory assignment")
    checks.append("all other code, preflight gates, protected-input checks, mutations and native commands AST-identical")
    paths = [
        "data/ingredients/mapped/L-α-phosphatidylinositol_From_Glycine_Max_Soybean.yaml",
        "data/ingredients/mapped/Α-lipoic_Acid.yaml",
        "data/ingredients/mapped/Α1-Acid_Glycoprotein_From_Bovine_Plasma.yaml",
        "data/ingredients/unmapped/Poly-ß-hydroxybutyric_Acid.yaml",
        "data/ingredients/unmapped/Α-D-Glucose_Monohydrate.yaml",
        "tests/filename with spaces and\nnewline.py",
        ".github/workflows/plain.yaml",
    ]
    fixture = {}
    with tempfile.TemporaryDirectory(prefix="step7d-1126-git-fixture-", dir="/private/tmp") as temporary:
        repo = Path(temporary)
        git(repo, "init", "-q")
        git(repo, "config", "core.quotePath", "true")
        for name in paths:
            target = repo / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("fixture only\n")
        git(repo, "add", "--all")
        git(repo, "-c", "user.name=External regression fixture", "-c", "user.email=fixture@example.invalid", "commit", "-qm", "Native membership fixture")
        baseline = git(repo, "rev-parse", "HEAD").decode().strip()
        fixture["baseline_commit"] = baseline
        fixture["paths"] = paths
        fixture["v3_false_rejection"] = reject(OLD, repo, baseline)
        checks.append("positive fixture reproduces v3 false failure on quoted non-ASCII and newline names")
        demand(evaluate(NEW, repo, baseline) == (7, 7), "v4 positive fixture count")
        checks.append("v4 accepts identical seven-file Git membership including five Unicode names and newline/space name")
        git(repo, "rm", "--cached", "--", paths[0])
        fixture["missing_rejection"] = reject(NEW, repo, baseline)
        checks.append("v4 rejects genuinely missing Unicode member through unchanged exact-set guard")
        git(repo, "add", "--", paths[0])
        extra = repo / "tests/actually_added.py"
        extra.write_text("fixture only\n")
        git(repo, "add", "--", "tests/actually_added.py")
        fixture["extra_rejection"] = reject(NEW, repo, baseline)
        checks.append("v4 rejects genuinely added tracked member through unchanged exact-set guard")
        git(repo, "rm", "--cached", "--", "tests/actually_added.py")
        git(repo, "config", "core.quotePath", "false")
        demand(evaluate(NEW, repo, baseline) == (7, 7), "quotePath=false changes NUL membership")
        checks.append("v4 exact membership also passes with core.quotePath=false")
    actual_counts = evaluate(NEW, W, BASE)
    demand(actual_counts == (3582, 3582), "actual maintained inventory differs from expected frozen scope")
    checks.append("read-only actual protected inventories match exactly: 3582 baseline and current tracked paths")
    failed_receipt = D.parent / "logs/step7d-independent-post1122-v3-preflight.json"
    failed_log = failed_receipt.with_suffix(".log")
    failure = json.loads(failed_receipt.read_text())
    demand(failure["exit_code"] == 1 and failure["log_sha256"] == sha(failed_log), "v3 failure evidence changed")
    checks.append("original failed v3 native preflight receipt and log preserved")
    result = {
        "issue": "https://github.com/CultureBotAI/MediaIngredientMech/issues/1126",
        "operator_sha256": sha(NEW),
        "predecessor_sha256": sha(OLD),
        "controls_sha256": sha(Path(__file__)),
        "checks": checks,
        "checks_passed": len(checks),
        "actual_inventory_counts": actual_counts,
        "fixture": fixture,
        "preserved_v3_failure": {str(failed_receipt): sha(failed_receipt), str(failed_log): sha(failed_log)},
        "maintained_refresh_executed": False,
        "full_native_preflight_executed": False,
        "maintained_writes": False,
        "required_order": "Root executes v4 native refresh before separately authorized #1123/#1124 test edits.",
    }
    with RESULT.open("x") as output:
        json.dump(result, output, indent=2, ensure_ascii=False)
        output.write("\n")
    print(json.dumps({"checks_passed": len(checks), "result": str(RESULT), "sha256": sha(RESULT)}, indent=2))


if __name__ == "__main__":
    main()
