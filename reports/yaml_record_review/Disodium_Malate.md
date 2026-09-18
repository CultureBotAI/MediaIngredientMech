# `data/ingredients/mapped/Disodium_Malate.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-matches active `CHEBI:91260` disodium
malate, OLS/OAK both resolve the racemic ChEBI term, and the final SSSOM row
has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Disodium_Malate.yaml`.
- Identifier and grounding: `identifier: CHEBI:91260` with
  `ontology_mapping.ontology_id: CHEBI:91260`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and seven
  MicrobeDecoder source occurrences from `BacDive_Metabolite_utilization`.
- Local OAK resolves `CHEBI:91260` to active `disodium malate` with definition
  as a racemate, CAS xref `676-46-0`, and exact synonym
  `disodium 2-hydroxybutanedioate`.
- EBI OLS exact search for `disodium malate` resolves `CHEBI:91260`; it also
  returns the related stereospecific siblings `CHEBI:91261` and `CHEBI:91262`
  as separate terms, so the unqualified MicrobeDecoder label is correctly
  mapped to the racemic parent term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Glutarate.yaml data/ingredients/mapped/Disodium_Malate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Malate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the 4 CHEBI-label records in the batch; the lowercase MeSH parent
  in `Disodium_Glutarate.yaml` was left to Engine B/product validation.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:91260`:
  returned the canonical ChEBI label, definition, CAS xref, and synonyms for
  `CHEBI:91260`.
- `curl -L -sS --max-time 20 "https://www.ebi.ac.uk/ols/api/search?q=disodium%20malate&ontology=chebi&exact=true"`:
  returned live `CHEBI:91260` with label `disodium malate`.
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
  found the expected active record, aggregate copy, generated products,
  MicrobeDecoder review rows, and ignored aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:91260` found only `data/ingredients/mapped/Disodium_Malate.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the row as
  `APPROVED` after local OAK resolution and case-insensitive canonical-label
  confirmation.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Disodium_Malate` to `CHEBI:91260` with `skos:exactMatch`, canonical
  object label `disodium malate`, CHEBI object source, MicrobeDecoder
  provenance, and no `other` tokens.

## Completeness

- MicrobeDecoder source occurrence and mapping promotion history are populated.
- ChEBI does not expose a local structure block for `CHEBI:91260`, so empty
  `chemical_properties` are acceptable; CultureMech occurrence statistics,
  ingredient roles, supplied forms, mixture components, and environmental
  contexts are correctly empty.

## Recommended Edits

- None.
