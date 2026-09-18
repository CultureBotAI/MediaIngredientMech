# `data/ingredients/mapped/Edta_Chelating_Agent.yaml`

## Verdict

Needs curation. The NCIT CURIE itself resolves, but `NCIT:C360` denotes the
generic class `Chelating Agent`; it is not an EDTA identity and should not be
published as an exact match for `MIM:Edta_Chelating_Agent`.

## Identity

- Reviewed record: `data/ingredients/mapped/Edta_Chelating_Agent.yaml`.
- Current grounding: `identifier: NCIT:C360`,
  `ontology_mapping.ontology_id: NCIT:C360`, canonical label
  `Chelating Agent`, source `NCIT`, `mapping_quality: LEXICAL_MATCH`,
  `mapping_status: MAPPED`, zero occurrences, and no `ingredient_type`.
- `runoak -i ols:ncit info` and a direct EBI OLS query both resolved
  `NCIT:C360` to `Chelating Agent`.
- EBI OLS describes `NCIT:C360` as the generic class for molecules that bind
  metal ions; it does not denote EDTA specifically.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ectoine.yaml data/ingredients/mapped/Edta.yaml data/ingredients/mapped/Edta_Acid_Form.yaml data/ingredients/mapped/Edta_Chelating_Agent.yaml data/ingredients/mapped/Edta_Stock.yaml --out /tmp/mim_edta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Edta_Chelating_Agent.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  NCIT class identifier, stem-match provenance, zero occurrence count, and
  provisional `CHELATOR` role as the per-record YAML.
- The original 2026-05-01 history and top-level note say the imported
  communitymech label had no CAS RN or CHEBI/NCIT match and needed curator
  review; the next event auto-upgraded it to `NCIT:C360` by stem-substring
  match.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` only proves
  that `NCIT:C360` resolves as a valid NCIT CURIE. It does not prove that the
  generic NCIT class is exact identity for EDTA.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Edta_Chelating_Agent` to `NCIT:C360` with `skos:exactMatch`, conflating
  a specific EDTA-labeled source record with the broader chelator class.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` found this active YAML, aggregate copy, final
  SSSOM row, and the row-review TSVs that kept it only because the NCIT CURIE
  resolved; it did not expose evidence that `NCIT:C360` denotes EDTA.
- The only `CHELATOR` role evidence is
  `reference_type: COMPUTATIONAL_PREDICTION` from
  `infer_roles_from_name_lists`, with a curator note explicitly marking the
  name-pattern role provisional.

## Completeness

- The record has no source occurrences, no component evidence, and no evidence
  for the current generic NCIT grounding beyond the stem-substring match.

## Recommended Edits

- Blocker: tombstone `data/ingredients/mapped/Edta_Chelating_Agent.yaml` as a
  zero-occurrence duplicate or reground it to `CHEBI:4735` if the
  `communitymech-unmapped` provenance must be preserved; either way, stop
  exporting `MIM:Edta_Chelating_Agent skos:exactMatch NCIT:C360`.
- Major: remove the provisional `CHELATOR` role when tombstoning or regrounding
  the record unless claim-level evidence is curated.
- After editing the per-record YAML, run `sync-curated`, rebuild or reconcile
  SSSOM, and rerun `validate-all`, `qc-sssom`, strict validation, and id-label
  correspondence.
