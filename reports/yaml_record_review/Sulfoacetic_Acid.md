# `data/ingredients/mapped/Sulfoacetic_Acid.yaml`

## Verdict

Pass. The exact `CHEBI:50519` sulfoacetic-acid identity, CAS RN, formula,
structure fields, aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfoacetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:50519` with
  `ontology_mapping.ontology_id: CHEBI:50519`, label `sulfoacetic acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `123-43-3`, formula `C2H4O5S`, and ChEBI/PubChem
  InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfite` through `Sulfur`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:50519` with label
  `sulfoacetic acid`, CAS `123-43-3`, formula `C2H4O5S`, and structure fields
  matching the YAML.
- The CultureBotHT import preserved CAS `123-43-3` in
  `chemical_properties.cas_rn`, and the later chemistry backfill kept the exact
  CHEBI formula and structure on the same record.
- The final SSSOM row exact-matches `CHEBI:50519`, uses
  `semapv:LexicalMatching`, and publishes only the same `CAS:123-43-3` in
  `other`.

## Completeness

- The exact sulfoacetic-acid identity, CAS, aggregate row, structure fields,
  and final SSSOM row agree.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, aggregate,
  generated index, and final SSSOM rows, and no second active MIM record for
  `CHEBI:50519` or CAS `123-43-3`.

## Recommended Edits

- None.
