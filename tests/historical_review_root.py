"""Exact pre-mint native review fixtures; no review or owner hash is restamped.

The fixed Git baseline supplies the full original review input closure and corpus.
A materialized pytest-only root is needed where the native reader deliberately
uses descriptor-level reads that an in-memory Path view cannot intercept.
"""
from functools import lru_cache
import importlib.util
import subprocess
from pathlib import Path

from mediaingredientmech.identity_projection import git_files, record_paths, document, sha

ROOT = Path(__file__).parents[1]
REVIEW = "reports/sssom_completion_20260921/review.json"
REVIEW_SHA = "ab301d1f66276cdfeefea79080ce49f26ebb02c1920a53c71512c14b283b16cf"
ASSEMBLER = "reports/sssom_completion_20260921/assemble_review.py"


@lru_cache(maxsize=1)
def historical_review_bytes():
    original = git_files(ROOT, [REVIEW])[REVIEW]
    assert sha(original) == REVIEW_SHA
    review = document(original)
    names = sorted({*review["inputs"], *review["record_inputs"], REVIEW, ASSEMBLER,
                    review["source_sssom"], *record_paths(ROOT, historical=True)})
    contents = git_files(ROOT, names)
    assert all(sha(contents[name]) == expected for group in ("inputs", "record_inputs")
               for name, expected in review[group].items())
    return contents


def assemble_at_baseline(tmp_path):
    root = tmp_path / "exact-pre-mint-review"
    assert not root.exists()
    for name, raw in historical_review_bytes().items():
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
    # Retain actual Git-object verification, including committed historical review
    # inputs. This disposable fixture has its own metadata and borrows only the
    # original object store through Git's read-only alternates mechanism.
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    objects = subprocess.check_output(["git", "rev-parse", "--git-path", "objects"], cwd=ROOT, text=True).strip()
    object_path = Path(objects)
    if not object_path.is_absolute():
        object_path = (ROOT / object_path).resolve()
    (root / ".git/objects/info/alternates").write_text(str(object_path) + "\n")
    subprocess.run(["git", "remote", "add", "origin", "https://github.com/CultureBotAI/MediaIngredientMech.git"], cwd=root, check=True)
    path = root / ASSEMBLER
    spec = importlib.util.spec_from_file_location("exact_pre_mint_native_review", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.assemble()
