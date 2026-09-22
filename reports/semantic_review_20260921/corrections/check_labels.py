import csv, hashlib, importlib.util, json, sys
from pathlib import Path

root = Path(__file__).resolve().parents[3]
kg = root.parents[1] / "KG-Hub/KG-Microbe/kg-microbe"
out = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "mim_invariants", root / "scripts/validate_sssom_invariants.py"
)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
p = root / "mappings/ingredient_mappings.sssom.tsv"
initial = p.read_bytes()
_, _, rows = m._read_sssom(p)
orig = m._load_ontology_labels
loaded = {}
inputs = {}


def labels(prefix):
    if prefix not in loaded:
        directory = (
            kg
            / "data/transformed"
            / ("ontologies_stubs" if prefix in {"BTO", "MICRO"} else "ontologies")
        )
        m.KGM_TRANSFORMS_DIR = directory
        path = directory / f"{prefix.lower()}_nodes.tsv"
        assert path.is_file(), path
        inputs[str(path)] = hashlib.sha256(path.read_bytes()).hexdigest()
        loaded[prefix] = orig(prefix)
    return loaded[prefix]


m._load_ontology_labels = labels
findings = list(m.evaluate_rule_b4(rows))
eligible = [r for r in rows if r["object_id"].split(":")[0] in m.B4_PREFIXES]
missing = [
    r["object_id"] for r in eligible if r["object_id"] not in labels(r["object_id"].split(":")[0])
]
assert p.read_bytes() == initial
assert all(
    hashlib.sha256(Path(path).read_bytes()).hexdigest() == sha for path, sha in inputs.items()
)
with (out / "label-findings.tsv").open("w") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["row", "subject_id", "object_id", "object_label", "finding"])
    for n, r, reason in findings:
        w.writerow([n, r["subject_id"], r["object_id"], r["object_label"], reason])
subjects = {r["subject_id"] for r in rows}
objects = {r["object_id"] for r in rows}
result = {
    "sssom_sha256": hashlib.sha256(initial).hexdigest(),
    "mapping_rows": len(rows),
    "mim_subjects": len(subjects),
    "distinct_targets": len(objects),
    "distinct_endpoint_ids": len(subjects | objects),
    "unique_mapping_triples": len(
        {(r["subject_id"], r["predicate_id"], r["object_id"]) for r in rows}
    ),
    "B4_eligible_rows": len(eligible),
    "B4_absent_term_rows": len(missing),
    "B4_absent_term_ids": sorted(set(missing)),
    "B4_label_findings": len(findings),
    "authority_hashes": inputs,
    "inputs_unchanged": True,
}
(out / "counts-and-label-check.json").write_text(json.dumps(result, indent=2) + "\n")
print(
    json.dumps(
        {k: v for k, v in result.items() if k not in {"authority_hashes", "B4_absent_term_ids"}},
        indent=2,
    )
)
print(
    "Examples:",
    [(r["subject_id"], r["object_id"], r["object_label"], reason) for _, r, reason in findings[:5]],
)
