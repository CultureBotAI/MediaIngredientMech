# `data/ingredients/mapped/Diammonium_tartrate.yaml`

## Verdict

Pass with minor issues. The record maps the CultureMech residual surface to
active `CHEBI:63075` diammonium L-tartrate, and its empty final SSSOM `other`
payload is clean. One stale residual-triage row still treats the label as an
alias candidate even though the mapped record already exists.

## Identity

- Reviewed record: `data/ingredients/mapped/Diammonium_tartrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:63075` with
  `ontology_mapping.ontology_id: CHEBI:63075`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`,
  `mapping_status: MAPPED`, and one CultureMech occurrence.
- Local OAK resolves `CHEBI:63075` to active `diammonium L-tartrate`, the
  diammonium salt of L-(+)-tartaric acid, with formula `C4H4O6.2H4N`,
  InChI, SMILES, CAS xref `3164-29-2`, and related synonym
  `diammonium tartrate`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diammonium_tartrate.yaml data/ingredients/mapped/Dibenzofuran.yaml data/ingredients/mapped/Dibenzothiophene.yaml data/ingredients/mapped/Dibucaine.yaml data/ingredients/mapped/Dichloran_02_in_ethanol.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diammonium_tartrate.yaml data/ingredients/mapped/Dibenzofuran.yaml data/ingredients/mapped/Dibenzothiophene.yaml data/ingredients/mapped/Dibucaine.yaml data/ingredients/mapped/Dichloran_02_in_ethanol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:63075 CHEBI:28145 CHEBI:23681 CHEBI:247956 CHEBI:27864`:
  returned the canonical ChEBI label, definition, synonyms, CAS xref,
  formula, InChI, SMILES, charge, and mass for `CHEBI:63075`.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus
  plausibility warnings.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record, generated/indexed copies, and
  CultureMech residual rows.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:63075` found only
  `data/ingredients/mapped/Diammonium_tartrate.yaml`.
- `mappings/culturemech_residual_groundings.tsv` records the
  `Diammonium tartrate` residual as a new `CHEBI:63075` record, matching the
  creation history and the single occurrence in `occurrence_statistics`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Diammonium_tartrate` to `CHEBI:63075` with `skos:exactMatch`,
  canonical object label `diammonium L-tartrate`, CHEBI object source, and no
  `other` tokens.

## Completeness

- The ChEBI identity, CultureMech occurrence count, structured mapping
  evidence, and provenance-restoration history are populated.
- Supplied forms, mixture components, ingredient roles, chemical properties,
  and environmental contexts are correctly empty for this sparse single-salt
  residual record.

## Recommended Edits

- Minor: refresh or retire `mappings/culturemech_residual_triage.tsv` row 201
  after the residual-grounding state is reconciled; it still lists
  `Diammonium tartrate` as an `ALIAS` triage row despite the active
  `CHEBI:63075` record.
