# `data/ingredients/mapped/Dactimicin.yaml`

## Verdict

Pass. The MicrobeDecoder label `dactimicin` resolves to the active ChEBI term
for formimidoyl-fortimicin A, the two BacDive metabolite-production mentions
are traceable, the structural fields agree with ChEBI, and the final SSSOM row
has an empty `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Dactimicin.yaml`.
- Identifier and grounding: `identifier: CHEBI:81430` with
  `ontology_mapping.ontology_id: CHEBI:81430`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:81430` to active `Formimidoyl-fortimicin A`,
  formula `C18H36N6O6`, charge `0`, InChI, SMILES, CAS xref `73196-97-1`,
  and related synonym `Dactimicin`.
- The record's stored ChEBI/PubChem formula, SMILES, InChI, and molecular
  weight describe this exact ChEBI structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Danomycin.yaml data/ingredients/mapped/Danubomycin.yaml data/ingredients/mapped/Daptomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Danomycin.yaml data/ingredients/mapped/Danubomycin.yaml data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed through the two ChEBI records and then failed on
  `kgmicrobe.compound:danomycin` because local registry targets hit the known
  OAK SQL label-lookup error:
  `sqlite3.OperationalError: no such table: rdfs_label_statement`.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dactimicin.yaml data/ingredients/mapped/Daidzein.yaml data/ingredients/mapped/Daptomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed the 3-file ChEBI subset after skipping the two local placeholders.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:81430 CHEBI:28197 CHEBI:600103`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:81430`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/ingredient_candidates.tsv` and
  `data/custom/microbedecoder/unmapped_labels.tsv` both contain the exact
  `dactimicin` label with 2 BacDive metabolite-production mentions, matching
  `source_occurrences`.
- `mappings/culturemech_recipe_membership.tsv` has no rows for `CHEBI:81430`,
  matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The curation evidence cites MIM curation issue `#213` for the trivial-name
  synonym match to formimidoyl-fortimicin A, and local OAK confirms `Dactimicin`
  is a ChEBI synonym on `CHEBI:81430`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dactimicin` to `CHEBI:81430` with `skos:exactMatch`, canonical object
  label `Formimidoyl-fortimicin A`, CHEBI object source, and an empty `other`
  column.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record or
  parent-mapping record for `CHEBI:81430`.
- Molecular formula, InChI, SMILES, weight, and BacDive source-occurrence
  provenance are populated.
- The record does not assert nutritional roles, environmental contexts, or
  mixture components.

## Recommended Edits

- None.
