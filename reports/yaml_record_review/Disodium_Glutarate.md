# `data/ingredients/mapped/Disodium_Glutarate.yaml`

## Verdict

Needs curation, major. The local `cas:13521-83-0` identity, PubChem chemistry,
MeSH parent, registry rows, and final SSSOM `other` payload are coherent, but
the `CARBON_SOURCE` role is still only a provisional name-pattern prediction.

## Identity

- Reviewed record: `data/ingredients/mapped/Disodium_Glutarate.yaml`.
- Identifier and grounding: `identifier: cas:13521-83-0` with
  `ontology_mapping.ontology_id: mesh:C000730144`, source `MESH`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem CID `161742` resolves to formula `C5H6Na2O4`, SMILES
  `C(CC(=O)[O-])CC(=O)[O-].[Na+].[Na+]`, the stored InChI, and InChIKey
  `ZUDYLZOBWIAUPC-UHFFFAOYSA-L`, supporting the local CAS identity for
  disodium glutarate.
- EBI OLS exact search resolves `mesh:C000730144` to `sodium glutarate`,
  matching the broader parent row that anchors the local CAS identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Glutarate.yaml data/ingredients/mapped/Disodium_Malate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Malate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the 4 CHEBI-label records in the batch; this lowercase MeSH
  parent was skipped by Engine A and covered by Engine B.
- `curl -L -sS --max-time 20 "https://www.ebi.ac.uk/ols/api/search?q=sodium%20glutarate&ontology=mesh&exact=true"`:
  returned live `mesh:C000730144` with label `sodium glutarate`.
- `curl -L -sS --max-time 20 "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/161742/property/MolecularFormula,InChI,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"`:
  returned formula `C5H6Na2O4` and the stored InChI.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with the `mesh:C000730144` labels
  covered by `conf/id_label_targets.yaml` exceptions and only full-corpus
  plausibility warnings elsewhere.

## Evidence

- `data/curated/mapped_ingredients.yaml` contains the same maintained record
  body as the per-record YAML.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found the expected active record, aggregate copy, MeSH exception,
  external-prefix OLS validation row, generated products, row-review rows, and
  ignored aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `13521-83-0`, `mesh:C000730144`, and `161742` found only
  `data/ingredients/mapped/Disodium_Glutarate.yaml`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` records the MeSH row
  as a `missing_prefix_validator_coverage_issue` that exact-resolves in
  prefix-specific EBI OLS; it also records the CAS and kg-microbe rows as
  expected registry identifiers.
- The final `mappings/ingredient_mappings.sssom.tsv` rows keep
  `MIM:Disodium_Glutarate skos:narrowMatch mesh:C000730144`,
  `skos:exactMatch cas:13521-83-0`, and the Rule B1 companion exact row to
  `kgmicrobe.compound:disodium_glutarate`; only the true local CAS token
  appears in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is supported only by an
  `infer_roles_from_name_lists` `COMPUTATIONAL_PREDICTION` whose curator note
  explicitly calls the assignment provisional.
- Minor: the MeSH parent row in final SSSOM still carries
  `none|UNKNOWN_TERM|2026-07-07` even though
  `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` now
  confirms that `mesh:C000730144` exact-resolves to `sodium glutarate`.

## Completeness

- CAS RN, PubChem CID, formula, InChI, SMILES, MeSH parent evidence, and both
  exact registry rows are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT record with no
  tracked CultureMech recipe memberships; supplied forms, mixture components,
  and environmental contexts are correctly empty.
- The carbon-source role is consequential because generated users could read
  the record as evidence-backed support for carbon-source use.

## Recommended Edits

- Major: in `data/ingredients/mapped/Disodium_Glutarate.yaml`, either remove
  `nutritional_roles.CARBON_SOURCE` or replace it with inspected
  formulation-specific evidence that directly supports this exact ingredient
  as a carbon source.
- Minor: refresh the SSSOM MeSH validation method so it no longer reports
  `UNKNOWN_TERM` after the prefix-specific OLS resolution.
