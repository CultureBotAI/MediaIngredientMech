# `data/ingredients/mapped/Nicotinic_Acid.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:15940` nicotinic acid identity,
CAS-backed structure, source-backed `VITAMIN_SOURCE` role, occurrence count,
and final SSSOM row pass, but a stray auto-proposed PubMed search snippet is
attached as mapping evidence.

## Identity

- Reviewed record: `data/ingredients/mapped/Nicotinic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:15940` with
  `ontology_mapping.ontology_id: CHEBI:15940`, label `nicotinic acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 2222 CultureMech recipe occurrences across 2221 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Nicotine_Fluka` through `Nisin`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:15940` as active
  `nicotinic acid` with formula `C6H5NO2`, CAS `59-67-6`, and the same InChI
  and SMILES as the record.
- A fresh PubChem CAS lookup for `59-67-6` resolves to nicotinic acid with the
  same InChI, confirming the chemical block.
- `VITAMIN_SOURCE` is backed by the imported CultureMech `Vitamin` role text,
  and the raw `Role:`/`Properties:` labels are filtered from final SSSOM.
- The final SSSOM row maps `MIM:Nicotinic_Acid` exactly to `CHEBI:15940` and
  the exported `other` values are same-substance aliases plus `CAS:59-67-6`.
- Minor: `ontology_mapping.evidence` still includes `pmid: 41213409` from
  `PubMed search ('Nicotinic acid')`; the snippet mentions nicotinic acid but
  does not support the CultureMech grounding any more narrowly than the
  database evidence.

## Completeness

- The active ChEBI term, CAS RN, formula, structure, role evidence, 2221/2222
  occurrence count, and final exact row agree.
- The remaining cleanup is a redundant auto-proposed PubMed evidence item.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Nicotinic_Acid.yaml`, remove the
  auto-proposed `pmid: 41213409` evidence object from `ontology_mapping`.
