# `data/ingredients/mapped/Tetrachloroethene.yaml`

## Verdict

Needs curation - major. The exact `CHEBI:17300` identity, CAS RN, structure
fields, occurrence count, aggregate row, and final SSSOM row pass, but
`ELECTRON_ACCEPTOR` is still only a provisional in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Tetrachloroethene.yaml`.
- Identifier and grounding: `identifier: CHEBI:17300` with
  `ontology_mapping.ontology_id: CHEBI:17300`, label `tetrachloroethene`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `127-18-4`, formula `C2Cl4`, and PubChem-backed
  InChI and SMILES for tetrachloroethene.
- Occurrences: 11 CultureMech recipe occurrences across 11 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tertiomycin_B` through `Tetrachloroethene`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:17300` as `tetrachloroethene`, lists
  `cas:127-18-4` as a database cross-reference, and includes all nine curated
  synonyms.
- Fresh PubChem lookup by CAS `127-18-4` resolves CID 31373, confirms the same
  `C2Cl4` formula and InChI, and lists CAS `127-18-4`.
- The final SSSOM has exactly one exact CHEBI row for `MIM:Tetrachloroethene`,
  points at `CHEBI:17300`, names `obo:chebi.owl`, and publishes only the
  curated same-substance names plus `CAS:127-18-4` in `other`.
- Major: `cellular_metabolic_roles.ELECTRON_ACCEPTOR` cites only
  `reference_type: COMPUTATIONAL_PREDICTION` from in-session Claude reasoning
  and explicitly notes that review is recommended.

## Completeness

- The CHEBI identity, CAS, structure fields, occurrence count, aggregate row,
  and final SSSOM row agree.
- The electron-acceptor role is incomplete until it is replaced with
  source-backed evidence for tetrachloroethene as a medium electron acceptor or
  removed.
- An ignored/hidden search of active local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureMech import,
  synonym enrichment, occurrence refresh, aggregate, row-review, final SSSOM,
  and generated rows.

## Recommended Edits

- Major: replace the provisional LLM-only `ELECTRON_ACCEPTOR` role in
  `data/ingredients/mapped/Tetrachloroethene.yaml` with source-backed evidence
  for tetrachloroethene as an electron acceptor, or remove the role if no
  maintained source supports it.
- Major: after any role edit, synchronize `data/curated/mapped_ingredients.yaml`
  and regenerate generated products so the role facets match the per-record
  YAML.
