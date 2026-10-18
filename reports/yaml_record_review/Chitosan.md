# `data/ingredients/mapped/Chitosan.yaml`

## Verdict

Needs curation; major issue. The exact `CHEBI:16261` chitosan identity, CAS,
formula, InChI, SMILES, valid ChEBI synonyms, 3/3 CultureMech occurrence count,
carbon-source role, SSSOM row, and aggregate copy pass. The record still
exports `hydrolysis: cationic chitosan` as an exact, resolvable synonym even
though it is a source relation statement.

## Identity

- Reviewed record: `data/ingredients/mapped/Chitosan.yaml`.
- Identifier and grounding: `identifier: CHEBI:16261`,
  `ontology_mapping.ontology_id: CHEBI:16261`, `ontology_label: chitosan`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:16261` returns one active ChEBI term labelled
  `chitosan` with CAS `9012-76-4`, formula `(C6H11NO4)n.H2O`, the same InChI
  and SMILES stored in `chemical_properties`, and the same structural synonyms
  retained in YAML except for the non-name `hydrolysis:` row.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chenodeoxycholic_Acid.yaml data/ingredients/mapped/Chitin.yaml data/ingredients/mapped/Chitosan.yaml data/ingredients/mapped/Chloramphenicol.yaml data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chenodeoxycholic_Acid.yaml data/ingredients/mapped/Chitin.yaml data/ingredients/mapped/Chitosan.yaml data/ingredients/mapped/Chloramphenicol.yaml data/ingredients/mapped/Chlorhexidine_Diacetate_Salt_Hydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chitosan` SSSOM row, the
  synonym-enrichment `ALREADY_REPRESENTED` row, and matching aggregate and docs
  rows for `CHEBI:16261`.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found exactly three
  `CHEBI:16261` rows, matching the explicit 3/3 `occurrence_statistics`.
- The CultureMech `Role: Carbon source; Properties: ...` raw text is filtered
  by `src/mediaingredientmech/synonym_policy.py`, but the
  `hydrolysis: cationic chitosan` exact synonym is not: current `docs/data`
  exports still resolve it as a `Chitosan` synonym.
- `CARBON_SOURCE` is backed by the imported CultureMech `Carbon Source` role,
  so the active nutritional role has claim-level database evidence for this
  corpus.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, true ChEBI
  synonyms, occurrence count, role, SSSOM row, aggregate copy, and docs row are
  populated and agree.
- The only consequential gap is the false exact synonym for a hydrolysis source
  statement.

## Recommended Edits

- Major: either remove `hydrolysis: cationic chitosan` from
  `data/ingredients/mapped/Chitosan.yaml` or extend
  `src/mediaingredientmech/synonym_policy.py` so `hydrolysis:` source
  statements stay in provenance without resolving as ingredient synonyms.
- Regenerate synchronized outputs and rerun strict validation, SSSOM QC,
  aggregate roundtrip, docs generation, and `git diff --check`.
