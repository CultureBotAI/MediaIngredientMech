#!/usr/bin/env python3
"""Retire seven source-verified generated aliases, preserving all other bytes (#669).

Dry-run by default. This is a bounded migration, not the SSSOM generator. An
up-to-date native candidate must independently omit every selected token.
Owner YAML remains byte-identical; native review receipts remain required.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLANS = [{'subject_id': 'MIM:4-Methyl-2-oxopentanoic_Acid_Sodium_Salt',
  'predicate_id': 'skos:broadMatch',
  'object_id': 'CHEBI:48430',
  'token': '4-Methyl-2-oxovaleric acid',
  'owned_by': 'MIM:4-Methyl-2-oxovaleric_Acid',
  'source_record': 'data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml',
  'owner_sha256': '8d5da3b1c891a79adf823a2ea778b04ef2658cc6bc175469631251c3874a314b',
  'verification': 'PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430 '
                  'is the acid C6H10O3. The parent preferred name cannot assert exact substance '
                  'identity for this sodium salt.',
  'evidence_files': ['sources/PubChem-CAS-4502-00-5.json', 'sources/CHEBI_48430.ols.json'],
  'baseline_disposition': 'UNREVIEWED'},
 {'subject_id': 'MIM:84_GL_NaHCO3_Solution',
  'predicate_id': 'skos:broadMatch',
  'object_id': 'CHEBI:32139',
  'token': 'NaHCO3',
  'owned_by': 'MIM:Nahco3',
  'source_record': 'data/ingredients/mapped/84_GL_NaHCO3_Solution.yaml',
  'owner_sha256': '1a8f4136f2de11105febf3112e5ca27fd95fcf9266ca1bb2283210267f70a509',
  'verification': 'The maintained identity is explicitly a stock solution '
                  'kgmicrobe.ingredient:84_gl_nahco3_solution, with concentration and solution '
                  'curation; the owner NaHCO3 is neat sodium hydrogencarbonate CHEBI:32139. This '
                  'is a mixture/concentration boundary, not merely spelling.',
  'evidence_files': ['sources/CHEBI_32139.ols.json'],
  'baseline_disposition': 'UNREVIEWED'},
 {'subject_id': 'MIM:Betaine_Hydrochloride',
  'predicate_id': 'skos:broadMatch',
  'object_id': 'CHEBI:17750',
  'token': 'Betaine x H2O',
  'owned_by': 'MIM:Betaine_X_H2o',
  'source_record': 'data/ingredients/mapped/Betaine_Hydrochloride.yaml',
  'owner_sha256': '77cf04f3fafb04a92080656711b7807ed4e9af7c79f7852ffd31a09fe428f4ac',
  'verification': 'PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242 is '
                  'glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate '
                  'identities differ.',
  'evidence_files': ['sources/PubChem-CAS-590-46-5.json', 'sources/CHEBI_91242.ols.json'],
  'baseline_disposition': 'HYDRATE_FAMILY_UNREVIEWED'},
 {'subject_id': 'MIM:D-Mannose_6-phosphate_Sodium_Salt',
  'predicate_id': 'skos:broadMatch',
  'object_id': 'CHEBI:17369',
  'token': 'Mannose-6-Phosphate',
  'owned_by': 'MIM:Mannose-6-Phosphate',
  'source_record': 'data/ingredients/mapped/D-Mannose_6-phosphate_Sodium_Salt.yaml',
  'owner_sha256': '280c8b5687a3ccd348984cd3b37518d2d1d298a80d1cd0c2b9a911b06f9a0535',
  'verification': 'PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369 is '
                  'D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material.',
  'evidence_files': ['sources/PubChem-CAS-70442-25-0.json', 'sources/CHEBI_17369.ols.json'],
  'baseline_disposition': 'UNREVIEWED'},
 {'subject_id': 'MIM:MES_Hydrat',
  'predicate_id': 'skos:broadMatch',
  'object_id': 'CHEBI:39005',
  'token': 'MES [2-(N-morpholino) ethane sulfonic acid]',
  'owned_by': 'MIM:Mes_2-_N-morpholino_Ethane_Sulfonic_Acid',
  'source_record': 'data/ingredients/mapped/MES_Hydrat.yaml',
  'owner_sha256': '24292497ec7bae482bb3611b8afb9cd1f795332d655be8900f4c59f8d929ebb6',
  'verification': 'PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S. '
                  'This evidence supports a form boundary independent of KG alias availability.',
  'evidence_files': ['sources/PubChem-CAS-145224-94-8.json', 'sources/CHEBI_39005.ols.json'],
  'baseline_disposition': 'UNREVIEWED'},
 {'subject_id': 'MIM:Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt',
  'predicate_id': 'skos:broadMatch',
  'object_id': 'CHEBI:15978',
  'token': 'Glycerol 3-phosphate',
  'owned_by': 'MIM:Glycerol_3-phosphate',
  'source_record': 'data/ingredients/mapped/Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt.yaml',
  'owner_sha256': '185d299a1d5a117e5ce42e2826e3f9fb83cba57459c5fc7e09f2dcf263a660f1',
  'verification': 'PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P; '
                  'ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias '
                  'does not require guessing the salt identity.',
  'evidence_files': ['sources/PubChem-CAS-29849-82-9.json', 'sources/CHEBI_15978.ols.json'],
  'baseline_disposition': 'UNREVIEWED'},
 {'subject_id': 'MIM:Sodium_Perchlorate',
  'predicate_id': 'skos:exactMatch',
  'object_id': 'CHEBI:132103',
  'token': 'Sodium perchlorate monohydrate',
  'owned_by': 'MIM:Sodium_Perchlorate_Monohydrate',
  'source_record': 'data/ingredients/mapped/Sodium_Perchlorate.yaml',
  'owner_sha256': '5b8a68b008ebce2e98c040b9dfff7b5b16f2370b320bb77cf0d3db32e680e0e0',
  'verification': 'PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is '
                  'monohydrate ClH2NaO5. ChEBI:132103 confirms the anhydrous subject.',
  'evidence_files': ['sources/PubChem-CAS-7601-89-0.json',
                     'sources/PubChem-CAS-7791-07-3.json',
                     'sources/CHEBI_132103.ols.json'],
  'baseline_disposition': 'HYDRATE_FAMILY_UNREVIEWED'}]


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def parsed_rows(data: bytes):
    """Retain physical line endings and cells; reject ambiguous TSV structure."""
    lines = data.decode("utf-8").splitlines(keepends=True)
    header = None
    rows = []
    for index, line in enumerate(lines):
        if line.startswith("#") or not line.strip():
            continue
        ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
        content = line[:-len(ending)] if ending else line
        cells = content.split("\t")
        if header is None:
            header = cells
            if len(header) != len(set(header)):
                raise ValueError("Duplicate TSV columns")
            continue
        if len(cells) != len(header):
            raise ValueError("Ambiguous TSV cell count; refusing byte surgery")
        rows.append((index, dict(zip(header, cells, strict=True)), cells, ending))
    if header is None:
        raise ValueError("Missing TSV header")
    return lines, header, rows


def transform_sssom(data: bytes, candidate: bytes) -> bytes:
    """Remove exactly seven verified tokens, with no other field/line change."""
    lines, header, rows = parsed_rows(data)
    _, _, candidate_rows = parsed_rows(candidate)
    for required in ("subject_id", "predicate_id", "object_id", "other"):
        if required not in header:
            raise ValueError(f"Missing canonical column {required}")
    other_index = header.index("other")
    for plan in PLANS:
        def matches(row, current_plan=plan):
            return all(row.get(k) == current_plan[k] for k in ("subject_id", "predicate_id", "object_id"))
        matching = [row for row in rows if matches(row[1])]
        generated = [row for row in candidate_rows if matches(row[1])]
        if len(matching) != 1 or len(generated) != 1:
            raise ValueError(f"Expected one canonical and generated row: {plan['subject_id']}")
        if any(t.casefold() == plan["token"].casefold() for t in generated[0][1].get("other", "").split("|")):
            raise ValueError(f"Native candidate still publishes retired token: {plan['subject_id']}")
        index, row, cells, ending = matching[0]
        tokens = row["other"].split("|")
        if tokens.count(plan["token"]) != 1:
            raise ValueError(f"Expected one exact reviewed token: {plan['subject_id']}")
        # Any differently cased second copy is an unreviewed payload, not a free removal.
        if sum(t.casefold() == plan["token"].casefold() for t in tokens) != 1:
            raise ValueError(f"Ambiguous case-variant token: {plan['subject_id']}")
        tokens.remove(plan["token"])
        cells = list(cells)
        cells[other_index] = "|".join(tokens)
        lines[index] = "\t".join(cells) + ending
    return "".join(lines).encode("utf-8")


def transform_baseline(data: bytes) -> bytes:
    """Remove only the seven exact reviewed obligations; preserve the other 38."""
    lines, header, rows = parsed_rows(data)
    if header != ["subject_id", "token", "owned_by", "disposition"]:
        raise ValueError("Unexpected native Rule K baseline columns")
    if len(rows) != 45:
        raise ValueError("Expected the reviewed 45-entry baseline")
    removed = set()
    for plan in PLANS:
        matching = [row for row in rows if row[1]["subject_id"] == plan["subject_id"]
                    and row[1]["token"] == plan["token"]]
        if len(matching) != 1:
            raise ValueError(f"Expected one reviewed baseline entry: {plan['subject_id']}")
        index, row, _, _ = matching[0]
        if row["owned_by"] != plan["owned_by"] or row["disposition"] != plan["baseline_disposition"]:
            raise ValueError("Baseline owner changed; review it before retirement")
        removed.add(index)
    if len(removed) != 7:
        raise ValueError("Expected seven distinct baseline retirements")
    return "".join(line for i, line in enumerate(lines) if i not in removed).encode("utf-8")


def verified_owners(root: Path) -> list[dict]:
    """Bind every row-only change to unchanged, reviewed maintained owner bytes."""
    records = []
    for plan in PLANS:
        actual = digest((root / plan["source_record"]).read_bytes())
        if actual != plan["owner_sha256"]:
            raise ValueError(f"Owner bytes changed: {plan['source_record']}")
        records.append({
            "source_record": plan["source_record"], "shape": "generated_synonym_retirement",
            "before_yaml_sha256": actual, "after_yaml_sha256": actual,
            "change": f"Removed only '{plan['token']}' from other on {plan['subject_id']} / "
                      f"{plan['predicate_id']} / {plan['object_id']}; retired its exact Rule K baseline entry. "
                      "All YAML and every other row field retained. No approval is asserted (#669).",
            "verification": plan["verification"],
        })
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--log", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    canonical = ROOT / "mappings/ingredient_mappings.sssom.tsv"
    baseline = ROOT / "mappings/other_cross_record_baseline.tsv"
    before, baseline_before = canonical.read_bytes(), baseline.read_bytes()
    candidate_bytes = args.candidate.read_bytes()
    records = verified_owners(ROOT)
    after = transform_sssom(before, candidate_bytes)
    baseline_after = transform_baseline(baseline_before)
    receipt = {
        "records": records,
        "candidate_path": str(args.candidate.resolve()), "candidate_sha256": digest(candidate_bytes),
        "sssom_before_sha256": digest(before), "sssom_after_sha256": digest(after),
        "baseline_before_sha256": digest(baseline_before), "baseline_after_sha256": digest(baseline_after),
        "baseline_before_count": 45, "baseline_after_count": 38,
        "changed_rows": 7, "removed_tokens": 7, "plans": PLANS,
        "approval": "NONE; existing withheld decisions remain withheld",
    }
    if args.apply:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        if args.log.exists() or args.log.with_suffix(".before.tsv").exists() or args.log.with_suffix(".baseline-before.tsv").exists():
            raise ValueError("Refusing to overwrite existing audit evidence")
        # Validate the complete operation before writing either maintained output.
        if canonical.read_bytes() != before or baseline.read_bytes() != baseline_before:
            raise ValueError("A maintained input changed during review")
        verified_owners(ROOT)
        args.log.with_suffix(".before.tsv").write_bytes(before)
        args.log.with_suffix(".baseline-before.tsv").write_bytes(baseline_before)
        canonical.write_bytes(after)
        baseline.write_bytes(baseline_after)
        args.log.write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps({"applied": args.apply, **receipt}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
