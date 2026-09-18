# `data/ingredients/mapped/Defibrinated_horse_blood.yaml`

## Verdict

Pass with a minor stale-triage issue. The record exact-maps defibrinated horse
blood to active `MICRO:0001572`, preserves the supplier-qualified CultureMech
alias as a same-subject synonym in final SSSOM, and has a matching 5/5
CultureMech occurrence count; only an older residual-triage row still lists the
now-curated alias as unresolved.

## Identity

- Reviewed record: `data/ingredients/mapped/Defibrinated_horse_blood.yaml`.
- Identifier and grounding: `identifier: MICRO:0001572` with
  `ontology_mapping.ontology_id: MICRO:0001572`,
  `ontology_label: defibrinated horse blood`, `ontology_source: MICRO`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: UNDEFINED_MIXTURE`.
- Live OLS exact search in the `micro` ontology for `defibrinated horse blood`
  returned one active result, `MICRO:0001572`, with label
  `defibrinated horse blood`.
- `src/mediaingredientmech/curie.py` lists `MICRO:0001572` in the verified
  MICRO set and documents that it was checked as defining, non-obsolete, and
  round-tripping through the canonical OLS4 IRI for issue #260.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Decanoic_Acid.yaml data/ingredients/mapped/Decaplanin.yaml data/ingredients/mapped/Decoyinine.yaml data/ingredients/mapped/Decyl_Alcohol.yaml data/ingredients/mapped/Defibrinated_horse_blood.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the four CHEBI/MeSH rows and then failed on `MICRO:0001572` with the
  known local sqlite `rdfs_label_statement` lookup error.
- `curl -L ... q=defibrinated horse blood&ontology=micro&exact=true`: live OLS
  returned the exact `MICRO:0001572` row.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `scripts/add_culturemech_gap_labels.py` is the maintained input that created
  this record and maps `Defibrinated horse blood` to `MICRO:0001572`, distinct
  from `MICRO:0001234` `horse blood`.
- A hidden/ignored-inclusive exact search over active `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML for `MICRO:0001572`.
- The hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found five `MICRO:0001572`
  rows with occurrence weights summing to 5, matching the explicit 5/5
  `occurrence_statistics`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Defibrinated_horse_blood` to `MICRO:0001572` with `skos:exactMatch`,
  MICRO object source, the supplier-qualified raw label
  `defibrinated horse blood (TCS Biologicals)` in `other`, and a manual
  curation validation stamp.
- Minor: `mappings/culturemech_residual_triage.tsv` still has an old
  `ALIAS` row for `defibrinated horse blood (TCS Biologicals)` saying the
  label was not in the pinned MIM index, but the synonym is now curated here
  and present in `docs/data/label_index.csv`.

## Completeness

- The MICRO identity, undefined-mixture classification, raw supplier synonym,
  occurrence count, membership rows, final SSSOM row, and generated docs rows
  are populated and agree.
- No chemical properties, CAS RN, component list, or nutritional roles are
  asserted; leaving them empty is appropriate for this undefined blood-product
  mixture.

## Recommended Edits

- Minor: refresh or retire the stale
  `mappings/culturemech_residual_triage.tsv` row for
  `defibrinated horse blood (TCS Biologicals)` so the triage file no longer
  claims the now-curated alias is missing from MIM.
