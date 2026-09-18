# `data/ingredients/mapped/Dimethyl_Sulfoxide.yaml`

## Verdict

Pass. The CultureMech record exact-matches active `CHEBI:28262`, its CAS RN,
formula, InChI, SMILES, and kg-microbe synonyms agree with ChEBI/PubChem, and
the final SSSOM row exports only true synonyms plus `CAS:67-68-5`.

## Identity

- Reviewed record: `data/ingredients/mapped/Dimethyl_Sulfoxide.yaml`.
- Identifier and grounding: `identifier: CHEBI:28262` with
  `ontology_mapping.ontology_id: CHEBI:28262`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `ingredient_type: SINGLE_INGREDIENT`, and 161/161 CultureMech occurrences.
- Local OAK resolves `CHEBI:28262` to active `dimethyl sulfoxide`, CAS xref
  `67-68-5`, formula `C2H6OS`, the stored InChI, and the same same-compound
  synonyms retained from kg-microbe.
- PubChem resolves CAS `67-68-5` to CID `679` with the same formula, InChI, and
  InChIKey `IAZDPXIOMUYVGZ-UHFFFAOYSA-N`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28262 CHEBI:17170 CHEBI:93172 CHEBI:16457 CHEBI:141155`:
  returned the expected active ChEBI label, formula, InChI, SMILES, charge,
  and synonym/xref metadata for `CHEBI:28262`.
- `curl -L -sS --max-time 20 "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/67-68-5/property/MolecularFormula,InChI,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"`:
  returned PubChem CID `679` with matching formula, InChI, and InChIKey.
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
  `CHEBI:28262` found only `data/ingredients/mapped/Dimethyl_Sulfoxide.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` both record the
  `CHEBI:28262` mapping as confirmed with no row-review action required.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Dimethyl_Sulfoxide` to `CHEBI:28262` with `skos:exactMatch`, canonical
  object label `dimethyl sulfoxide`, CHEBI object source, ChEBI-backed
  same-substance aliases, the CultureMech raw alias `dimethyl sulfoxide
  (DMSO)`, and `CAS:67-68-5`.

## Completeness

- CAS RN, formula, InChI, SMILES, kg-microbe synonym provenance, CultureMech
  occurrence statistics, ingredient type, and the corrected role history are
  populated.
- The import-only `Role: ...` raw synonym is correctly filtered from final
  SSSOM `other`; current ingredient roles, supplied forms, mixture components,
  and environmental contexts are correctly empty.

## Recommended Edits

- None.
