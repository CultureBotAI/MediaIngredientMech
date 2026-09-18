# `data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml`

## Verdict

Pass. The local `cas:4337-33-1` identity preserves the hydrochloride/chloride
form, `CHEBI:16457` is retained only as a narrower parent mapping to
zwitterionic DMSP, and final SSSOM exports no rejected ChEBI label.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: cas:4337-33-1` with
  `ontology_mapping.ontology_id: CHEBI:16457`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Local OAK resolves `CHEBI:16457` to active
  `S,S-dimethyl-beta-propiothetin` with formula `C5H10O2S`, InChI
  `InChI=1S/C5H10O2S/c1-8(2)4-3-5(6)7/h3-4H2,1-2H3`, and CAS xref
  `7314-30-9`, confirming it is the zwitterionic no-chloride parent rather
  than the hydrochloride form.
- PubChem CID `5316899` resolves to formula `C5H11ClO2S` and InChI
  `InChI=1S/C5H10O2S.ClH/c1-8(2)4-3-5(6)7;/h3-4H2,1-2H3;1H`, matching the
  corrected CAS identity for the chloride form.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Dimethyl_Sulfoxide.yaml data/ingredients/mapped/Dimethylamine.yaml data/ingredients/mapped/Dimethylfraxetin.yaml data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml data/ingredients/mapped/Dimetridazole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 records.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:28262 CHEBI:17170 CHEBI:93172 CHEBI:16457 CHEBI:141155`:
  returned the active ChEBI label and structure metadata for `CHEBI:16457`.
- `curl -L -sS --max-time 20 "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/5316899/property/MolecularFormula,InChI,CanonicalSMILES,IsomericSMILES,InChIKey/JSON"`:
  returned formula `C5H11ClO2S` and the stored chloride-form InChI.
- `curl -L -sS --max-time 20 "https://www.ebi.ac.uk/ols/api/search?q=Dimethylsulfoniopropionate%20hydrochloride&ontology=chebi&exact=true"`:
  returned zero exact ChEBI documents for the full hydrochloride label.
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
  found the expected active record, aggregate copy, #455 counterion-conflict
  tests, SSSOM rows, row-review rows, generated products, and ignored
  aggregate backups.
- A focused hidden/ignored-inclusive search of `data/ingredients` for
  `CHEBI:16457`, `4337-33-1`, `7314-30-9`, and `5316899` found the expected
  superseded CAS provenance and the active corrected CAS identity only in
  `data/ingredients/mapped/Dimethylsulfoniopropionate_Hydrochloride.yaml`.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` records the
  `CHEBI:16457` candidate text as already represented for the intentionally
  narrower parent row.
- The final `mappings/ingredient_mappings.sssom.tsv` rows keep
  `MIM:Dimethylsulfoniopropionate_Hydrochloride skos:narrowMatch CHEBI:16457`,
  `skos:exactMatch cas:4337-33-1`, and the Rule B1 companion exact row to
  `kgmicrobe.compound:dimethylsulfoniopropionate_hydrochloride`. The
  `REJECTED_LABEL` synonym `3-(dimethylsulfonio)propanoate` is not exported in
  final SSSOM `other`.

## Completeness

- CAS RN, PubChem CID, formula, InChI, SMILES, parent-mapping evidence,
  rejected-label provenance, corrected CAS history, and required exact
  registry rows are populated.
- The 0/0 occurrence count is acceptable for a CultureBotHT record with no
  tracked CultureMech recipe memberships; ingredient roles, supplied forms,
  mixture components, and environmental contexts are correctly empty.

## Recommended Edits

- None.
