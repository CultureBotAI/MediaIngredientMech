# `data/ingredients/mapped/N-acetyltyramine.yaml`

## Verdict

Pass. The exact `CHEBI:125610` N-acetyltyramine identity, MicrobeDecoder source
occurrence, structural properties, review promotion, and final exact row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetyltyramine.yaml`.
- Identifier and grounding: `identifier: CHEBI:125610` with
  `ontology_mapping.ontology_id: CHEBI:125610`, label `N-acetyltyramine`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one MicrobeDecoder BacDive metabolite-production source
  occurrence and no CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetylneuraminate` through `N-decanoyl-DL-Homoserine_Lactone`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:125610` as active
  `N-acetyltyramine` with formula `C10H13NO2`, the stored InChI/SMILES, and
  same-substance aliases for the acetylated tyramine.
- The MicrobeDecoder source row records
  `kgmicrobe.trait:n_acetyltyramine`, raw label `N-acetyltyramine`, source
  column `BacDive_Metabolite_production`, and count 1;
  `mappings/microbedecoder_auto_mapped_review.tsv` records the later
  `APPROVED` promotion.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetyltyramine` to `CHEBI:125610` with empty `other`.

## Completeness

- The active ChEBI target, structure, MicrobeDecoder occurrence count, source
  provenance, review promotion, and final row agree.
- The record does not assert components, roles, or unsupported synonyms.

## Recommended Edits

- None.
