# `data/ingredients/mapped/Stearic_Acid.yaml`

## Verdict

Pass. The stearic-acid record has an exact CHEBI identity, matching CAS and
PubChem structure fields, true fatty-acid synonyms, refreshed occurrences, and
a clean final SSSOM row.

## Identity

- Reviewed record: `data/ingredients/mapped/Stearic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:28842` with
  `ontology_mapping.ontology_id: CHEBI:28842`, label `octadecanoic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 57-11-4`, formula `C18H36O2`, and the expected
  straight-chain saturated fatty-acid InChI and SMILES.
- Occurrences: 6 source occurrences across 6 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Stallimycin` through `Stearic_Acid`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:28842` with label
  `octadecanoic acid` and synonyms covering the curated fatty-acid aliases.
- PubChem resolves CAS `57-11-4` to CID `5281`, with formula `C18H36O2`, IUPAC
  name `octadecanoic acid`, and the same InChI and SMILES stored in YAML.
- The final SSSOM row exact-matches `CHEBI:28842` and its `other` payload is
  limited to true fatty-acid synonyms plus `CAS:57-11-4`.

## Completeness

- The raw `Role: Carbon source` label is correctly filtered from final SSSOM.
- No unsupported active synonym, role, component, or final SSSOM payload was
  found.

## Recommended Edits

- None.
