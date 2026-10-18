# `data/ingredients/mapped/Dimethylamine.yaml`

## Verdict

Pass. The MicrobeDecoder import exact-matches active `CHEBI:17170`
dimethylamine, the stored formula, InChI, SMILES, and mass agree with ChEBI and
PubChem, and the final SSSOM row has no unsafe `other` payload.

## Identity

- Reviewed record: `data/ingredients/mapped/Dimethylamine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17170` with
  `ontology_mapping.ontology_id: CHEBI:17170`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and two MicrobeDecoder source
  occurrences from `BacDive_Metabolite_utilization`.
- Local OAK resolves `CHEBI:17170` to active `dimethylamine`, CAS xref
  `124-40-3`, formula `C2H7N`, the stored InChI, the stored mass, and
  dimethylamine synonyms.
- PubChem resolves CAS `124-40-3` to CID `674` with the same formula, InChI,
  and InChIKey `ROSDSFDQCJNGOL-UHFFFAOYSA-N`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28262 CHEBI:17170 CHEBI:93172 CHEBI:16457 CHEBI:141155`:
  returned the expected active ChEBI label, formula, InChI, SMILES, charge,
  and synonym/xref metadata for `CHEBI:17170`.
- `curl -L -sS --max-time 20 "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/124-40-3/property/MolecularFormula,InChI,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"`:
  returned PubChem CID `674` with matching formula, InChI, and InChIKey.
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
  found the expected active record, generated/indexed copies,
  MicrobeDecoder review rows, source-provenance references, and ignored
  aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:17170` found only `data/ingredients/mapped/Dimethylamine.yaml`.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the row as
  `APPROVED` after local OAK resolution and case-insensitive canonical-label
  confirmation.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dimethylamine` to `CHEBI:17170` with `skos:exactMatch`, canonical
  object label `dimethylamine`, CHEBI object source, MicrobeDecoder
  provenance, and no `other` tokens.

## Completeness

- Formula, InChI, SMILES, mass, PubChem/ChEBI retrieval provenance,
  MicrobeDecoder source occurrence, ingredient type, and mapping promotion
  history are populated.
- CAS RN is available as a ChEBI xref, and CultureMech occurrence statistics,
  ingredient roles, supplied forms, mixture components, and environmental
  contexts are correctly empty.

## Recommended Edits

- None.
