"""Read-only source-binding checks; outputs confined to this science directory."""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

R = Path(__file__).resolve().parents[3]
O = Path(__file__).resolve().parent
W = R.parents[1] / "w07/worktree/.temp/columbia-continuity-independent-v1"
A = R / "reports/all_unmatched_20261107/worker-10"
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
    return json.loads(p.read_text())
def bind(p):
    return {"path": str(p), "sha256": sha(p), "bytes": p.stat().st_size}
checks = []
def check(name, condition):
    checks.append({"check": name, "pass": bool(condition)})
    assert condition, name
head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=R, text=True).strip()
check("unchanged source HEAD", head == "c66d6d3665368fe1ae8986fb7c16340a103582c1")
raw_path = W / "review/science/inputs/8213af97ae3fa7b9ce529557456536ee9fb30b25d6ab3b6a4da5b13e463ee025"
check("full TOGO raw corpus hash", sha(raw_path) == raw_path.name)
corpus = read(raw_path)
selected = read(W / "review/science/cached-togo-selected-objects.json")
objects = []
for row in selected["objects"]:
    value = row["object"]
    uri = value["meta"]["gm"]
    matches = [v for v in corpus if v.get("meta", {}).get("gm") == uri]
    check(uri + " unique corpus membership", len(matches) == 1)
    check(uri + " complete exact object", matches[0] == value)
    h = hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    check(uri + " canonical object hash", h == row["source_object_sha256"])
    objects.append({"uri": uri, "source_object_sha256": h, "full_object_equal": True})
matrix_path = W / "review/science/current-source-occurrence-matrix.json"
matrix = read(matrix_path)
recipes = []
for row in matrix["rows"]:
    p = W / "review/science" / row["recipe_capture"]["snapshot"]
    check(row["recipe_id"] + " recipe snapshot hash", sha(p) == row["recipe_capture"]["sha256"])
    recipes.append({"recipe_id": row["recipe_id"], "binding": bind(p), "quantity": row["source_quantity_preserved"], "independently_supported_route": row["disposition"]})
check("seven external context rows", len(recipes) == 7)
source_ledger = read(W / "review/science/current-proposals-and-primary-sources.json")
positive = {
    "2b29f541e504b0240dc3f9511521af6aff4e10a658af9353ebcd8fc6240e0c15": "Full four-page Oxoid specification; page-one raster directly viewed. Typical four-input formula; 39 g in 1 L added water is preparation instruction, not proof of final yield or source300 dose.",
    "3a2c163a3a247e9a8aca187b9c8993c6a436601cb1860d1c838c6a52874e44cf": "Full TOGO M2224 body: Oxoid 39 g dry base and four named product inputs, with receiving water separate; no historical catalogue number.",
    "81419407374ef31800f5297a96e1e96567b04b8927df098af3938aa88a95eb93": "Full generic MediaDive ingredient2046: only identity/source context; no global Difco identity or adoption of component CHEBI annotation.",
    "6114dc359e93d2634433847bc1dd7a373866ee08b508e200e8e9b1827afa72c3": "Full JCM1270: explicit BD-Difco 44 g dry input, 950 mL water and 50 mL sheep blood separate.",
    "fdeb922401814cf87f5bfd0969223a93f12e263999c3879e1a3899ef6cb4a146": "Full MediaDive J1270: compound2046 attribute BD-Difco 44 g supports only this occurrence; receiving-medium sheep/horse and quantity conflict retained.",
    "e5e836a75f13283d477467b20ffc0d332531e0f3a0effb5d64a7147a6985c0b7": "Genuine BD2009 manual, Columbia section text and printed158 raster directly viewed. Seven nominal Difco names; version, performance adjustments and unknown actual historical lot retained. BBL/EH columns separate."
}
primary = []
seen = set()
for row in source_ledger["primary_sources"]:
    capture = row["capture"]
    h = capture["sha256"]
    if h not in positive or h in seen:
        continue
    seen.add(h)
    p = Path(capture["path"])
    check("primary exact bytes " + h, sha(p) == h)
    primary.append({**bind(p), "url": capture["url"], "original_accessed_at": capture["original_accessed_at"], "actual_review_scope": positive[h]})
check("all six principal Columbia captures bound", seen == set(positive))
controls = [
    ("941", "f8881b46c26d0843d107.pdf", "ee788f0a554faacf718ba6e2ccaa0cf17def72c0306ae06ce5f9d2010935ef44", "DSM273 full one-page PDF and raster: 250 mL named 0.2 M Tris-HCl pH7.5 stock; no full stock formulation or explicit omission; receiving seawater and nitrogen are not stock constituents."),
    ("955", "44445462ffa7bfa8f3a5.html", "f29deedeee69ccae81017babc33b8450a719834aed7134337338078bf8adb003", "Full JCM1200 HTML: 5 mL named 2 M HEPES pH7 stock; no solvent, counterion, titrant or omitted-ingredient assertion; receiving water and gas remain external."),
    ("955", "a5a4ec5e544b62f0112f.html", "8d1a45f14e72031f0dc3c8465461353af1d8a289fcbb42baaef616a8e2c61d68", "Full JCM556 HTML: same named HEPES stock; separately prepared receiving medium and other added stocks do not establish its internal composition.")
]
for target, name, h, scope in controls:
    p = A / "buffers/captures" / name
    check("control primary bytes " + name, sha(p) == h)
    primary.append({**bind(p), "control": target, "actual_review_scope": scope})
owner = R / "data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml"
check("authentic generic owner", sha(owner) == "29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324")
report = {
    "review_id": "W10-COLUMBIA-CONTROLS-PREREQUISITE-SCIENCE-V1",
    "completed_at": datetime.now(timezone.utc).isoformat(),
    "reviewer": "worker10:/root/preparation_skeptic (AI)",
    "source_head": head,
    "status": "SUPPORTED_PREREQUISITES_CANDIDATE_REVIEW_PENDING",
    "independence": "No authorship of original target W10 payloads or new root candidate. Prior W10 preparation-family and Difco successor skeptical review involvement is retained, not presented as a historically uninvolved reviewer. This review is separate from root authoring.",
    "checks": checks,
    "check_count": len(checks),
    "source_corpus": {**bind(raw_path), "parsed_objects": len(corpus), "original_fetch_time": selected["source_capture"]["original_accessed_at"], "fresh_fetch": False, "scientific_scope": "Seven exact selected objects only."},
    "source_objects": objects,
    "seven_current_owner_contexts": recipes,
    "primary_readings": primary,
    "authentic_generic_before": bind(owner),
    "source_limits": [
        "Three current dry Difco routes are source-specific; generic provider2046 is not globally identified as Difco.",
        "Four CM331 rows denote 1 L prepared base before blood. Do not convert to 39 g powder, add blood to dry parts, infer solvent or final yield.",
        "Source300 retains literal variable quantity and positive CM0331 label; source921 retains39g and no historical catalogue. Equal nominal mass tables do not establish exact prepared-stock or lot identity.",
        "W04 4a3d retained origin still has PARTIAL. It is not the final composed candidate. Coordinator must independently compose/select/review the sole combined Oxoid candidate; W10 unchanged37e8 is only an authentic source origin.",
        "Only941/955 completeness is in control scope. UNKNOWN reflects no explicit full-list or omitted-list evidence, not a chemistry change or missing-parts inference.",
        "Historical owner aliases/statistics/history retain their original time and denominator; seven external context rows do not add assigned W10 cases or occurrences.",
        "No new ontology absence claim, whole-owner, role, release, export, prepared-stock identity or maintained-data approval."
    ],
    "new_in_scope_findings": [],
    "review_attempt_notes": [
        "Initial guessed W07 decision path at packet root and initial relative central path failed; authoritative HANDOFF/absolute campaign paths were then read successfully. No absence inference was made.",
        "A broad ledger display exceeded tool-output budget; relevant complete payloads/source objects and targeted ledger sections were subsequently read separately. No claim is made that the truncated display itself constituted full review."
    ],
    "candidate_review": "Pending actual frozen full payloads and proposal/case objects. This prerequisite report grants no candidate acceptance."
}
p = O / "prerequisite-science-v1.json"
assert not p.exists()
p.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({"status": report["status"], "checks": len(checks), "output": bind(p)}))
