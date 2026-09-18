# `data/ingredients/mapped/Diosgenin.yaml`

## Verdict

Pass. The CultureBotHT record exact-matches active `CHEBI:4629`, the stored CAS
RN, formula, InChI, SMILES, and exact synonym agree with ChEBI/PubChem, and the
final SSSOM row exports only the exact ChEBI synonym plus `CAS:512-04-9`.

## Identity

- Reviewed record: `data/ingredients/mapped/Diosgenin.yaml`.
- Identifier and grounding: `identifier: CHEBI:4629` with
  `ontology_mapping.ontology_id: CHEBI:4629`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 0/0 CultureMech occurrences.
- Local OAK resolves `CHEBI:4629` to active `diosgenin`, CAS xref `512-04-9`,
  formula `C27H42O3`, the stored InChI, the stored stereospecific SMILES, and
  exact synonym `(3beta,25R)-spirost-5-en-3-ol`.
- PubChem resolves CAS `512-04-9` to CID `99474` with matching formula, InChI,
  and InChIKey `WQLVFSAGQJTQCK-VKROHFNGSA-N`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Glutarate.yaml data/ingredients/mapped/Disodium_Malate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Diosgenin.yaml data/ingredients/mapped/Dioxygen.yaml data/ingredients/mapped/Dipicolinic_Acid.yaml data/ingredients/mapped/Disodium_Malate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the 4 CHEBI-label records in the batch; the lowercase MeSH parent
  in `Disodium_Glutarate.yaml` was left to Engine B/product validation.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:4629 CHEBI:15379 CHEBI:46837 CHEBI:91260`:
  returned the expected active ChEBI label, formula, InChI, SMILES, CAS xref,
  and synonym metadata for `CHEBI:4629`.
- `curl -L -sS --max-time 20 "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/512-04-9/property/MolecularFormula,InChI,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"`:
  returned PubChem CID `99474` with matching formula, InChI, and InChIKey.
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
  row-review confirmations, and ignored aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:4629` and `512-04-9` found only
  `data/ingredients/mapped/Diosgenin.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:4629` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Diosgenin` to `CHEBI:4629` with `skos:exactMatch`, canonical object
  label `diosgenin`, CHEBI object source, exact synonym
  `(3beta,25R)-spirost-5-en-3-ol`, and `CAS:512-04-9`.

## Completeness

- CAS RN, formula, InChI, SMILES, CultureBotHT provenance, synonym review
  provenance, and ingredient type are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT panel record with
  no tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
