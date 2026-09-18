# `data/ingredients/mapped/Dimethylfraxetin.yaml`

## Verdict

Pass with minor issues. The CAS primary and PubChem CID support the #326
regrade to exact `CHEBI:93172`, the final SSSOM has exact rows for both ChEBI
and `cas:6035-49-0`, and only stale pre-#326 evidence wording remains.

## Identity

- Reviewed record: `data/ingredients/mapped/Dimethylfraxetin.yaml`.
- Identifier and grounding: `identifier: cas:6035-49-0` with exact
  `ontology_mapping.ontology_id: CHEBI:93172`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:93172` to active
  `6,7,8-trimethoxy-1-benzopyran-2-one` with formula `C12H12O5`, the stored
  InChI, and matching InChIKey `RAYQKHLZHPFYEJ-UHFFFAOYSA-N`.
- PubChem CID `3083928` resolves to the stored CAS-backed formula, SMILES,
  InChI, and the same InChIKey, confirming that the formerly broader ChEBI row
  is an exact identity row.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28262 CHEBI:17170 CHEBI:93172 CHEBI:16457 CHEBI:141155`:
  returned the active ChEBI label and structure metadata for `CHEBI:93172`.
- `curl -L -sS --max-time 20 "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/3083928/property/MolecularFormula,InChI,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"`:
  returned formula `C12H12O5`, the stored InChI, and InChIKey
  `RAYQKHLZHPFYEJ-UHFFFAOYSA-N`.
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
  found the expected active record, aggregate copy, SSSOM rows, #326 regrade
  script, row-review rows, generated products, and ignored aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:93172`, `6035-49-0`, and `3083928` found only
  `data/ingredients/mapped/Dimethylfraxetin.yaml`.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records the
  `CHEBI:93172` row as already represented, and
  `mappings/ingredient_mappings_unknown_term_triage.tsv` records the
  `cas:6035-49-0` object as an expected registry identifier.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Dimethylfraxetin` to `CHEBI:93172` and `cas:6035-49-0` with
  `skos:exactMatch`; both rows keep only `CAS:6035-49-0` in `other`.
- Minor: the first `ontology_mapping.evidence` entry still says no ChEBI entry
  exists and points a curator at future CHEBI promotion. The later #326
  evidence supersedes that pre-regrade text.

## Completeness

- CAS RN, PubChem CID, formula, InChI, SMILES, PubChem-xref provenance,
  same-formula regrade history, ingredient type, and exact CAS registry mapping
  are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT record with no
  tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- Minor: refresh the stale import-era `ontology_mapping.evidence` note in
  `data/ingredients/mapped/Dimethylfraxetin.yaml`, then synchronize
  `data/curated/mapped_ingredients.yaml`.
