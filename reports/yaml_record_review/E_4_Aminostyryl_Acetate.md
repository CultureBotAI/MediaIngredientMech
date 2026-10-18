# `data/ingredients/mapped/E_4_Aminostyryl_Acetate.yaml`

## Verdict

Pass. The record intentionally preserves a local
`kgmicrobe.compound:e_4_aminostyryl_acetate` identity for a source label whose
reviewed OLS candidates were unrelated acetate lexical hits, and a fresh exact
OLS search still found no external ChEBI, NCIT, or MeSH replacement.

## Identity

- Reviewed record: `data/ingredients/mapped/E_4_Aminostyryl_Acetate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.compound:e_4_aminostyryl_acetate` with matching
  `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: PLACEHOLDER`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The curated synonym `(E)-4-Aminostyryl acetate` is the same E-isomer label
  with punctuation restored.
- A fresh exact OLS query for `E 4 Aminostyryl Acetate` across ChEBI, NCIT, and
  MeSH returned zero documents.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml data/ingredients/mapped/E_4_Aminostyryl_Acetate.yaml data/ingredients/mapped/Ebselen.yaml data/ingredients/mapped/Econazole_Nitrate_Salt.yaml --out /tmp/mim_e_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- The LinkML term-label gate was skipped for this file because its identifier
  uses the local `kgmicrobe.compound` prefix that the justfile excludes from
  Engine A.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  local identifier, placeholder ontology mapping, exact synonym, and manual
  candidate-review note as the per-record YAML.
- `mappings/ingredient_mappings_unknown_term_manual_candidate_review.tsv`
  records `NO_IDENTITY_PROMOTION` for the OLS low-confidence candidates
  `CHEBI:179185`, `CHEBI:179340`, and `CHEBI:192125` because they were
  unrelated acetate lexical hits.
- `mappings/ingredient_mappings_unknown_term_placeholder_ols_candidates.tsv`
  recorded `NO_EXACT_CANDIDATE` for this MIM subject in the 2026-05-06 EBI OLS
  placeholder search across ChEBI, MeSH, NCIT, MICRO, BTO, and FOODON.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:E_4_Aminostyryl_Acetate` to the same local
  `kgmicrobe.compound` CURIE with `skos:exactMatch`, and its only `other`
  token is the true same-substance synonym `(E)-4-Aminostyryl acetate`.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` found the active YAML, aggregate copy, final
  SSSOM row, and expected row-review TSVs; it did not expose a curated exact
  external ontology target for this label.

## Completeness

- No CAS RN, molecular structure, nutritional role, physicochemical role,
  biological role, component, or environmental context is asserted, which is
  appropriate for the placeholder identity until exact chemical grounding is
  curated.

## Recommended Edits

- None.
