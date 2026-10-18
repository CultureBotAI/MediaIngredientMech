# `data/ingredients/mapped/N-acetylneuraminate.yaml`

## Verdict

Pass. The exact `CHEBI:35418` N-acetylneuraminate identity, MicrobeDecoder
source occurrence, structural properties, review promotion, and final exact row
pass.

## Identity

- Reviewed record: `data/ingredients/mapped/N-acetylneuraminate.yaml`.
- Identifier and grounding: `identifier: CHEBI:35418` with
  `ontology_mapping.ontology_id: CHEBI:35418`, label
  `N-acetylneuraminate`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: one MicrobeDecoder BacDive metabolite-utilization source
  occurrence and no CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `N-acetylneuraminate` through `N-decanoyl-DL-Homoserine_Lactone`: exited 0
  and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:35418` as active
  `N-acetylneuraminate` with the stored deprotonated formula, charge, InChI,
  and SMILES.
- The MicrobeDecoder source row records
  `kgmicrobe.trait:n_acetylneuraminate`, raw label
  `n-acetylneuraminate`, source column `BacDive_Metabolite_utilization`, and
  count 1; `mappings/microbedecoder_auto_mapped_review.tsv` records the
  later `APPROVED` promotion.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:N-acetylneuraminate` to `CHEBI:35418` with empty `other`.

## Completeness

- The active ChEBI target, anion structure, MicrobeDecoder occurrence count,
  source provenance, review promotion, and final row agree.
- The record does not assert components, roles, or unsupported synonyms.

## Recommended Edits

- None.
