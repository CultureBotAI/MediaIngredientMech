# `data/ingredients/mapped/Deuterated_Glucose.yaml`

## Verdict

Needs curation. The CAS primary identity and NCIT parent mapping are shaped
correctly for the more specific isotope reagent, and final SSSOM preserves the
CAS and kg-microbe registry rows beside the NCIT parent row. The record still
carries generic glucose chemistry in `smiles` and two unsupported
name-inferred nutritional roles.

## Identity

- Reviewed record: `data/ingredients/mapped/Deuterated_Glucose.yaml`.
- Identifier and grounding: `identifier: cas:201417-01-8` with
  `ontology_mapping.ontology_id: NCIT:C200498`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, and `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS resolves `NCIT:C200498` to the broader class
  `Deuterated Glucose`.
- Live PubChem lookup of CID `71777455` resolves CAS `201417-01-8` as
  `D-Glucose-13C6,1,2,3,4,5,6,6-d7`; the stored InChI matches the current
  PubChem InChI for that CID.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Destomycin.yaml data/ingredients/mapped/Desulfovibrio_Trace_Elements.yaml data/ingredients/mapped/Deuterated_Glucose.yaml data/ingredients/mapped/Dextran.yaml data/ingredients/mapped/Dextrin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data ...` over the mixed
  five-record batch aborted at `kgmicrobe.compound:destomycin`, before the
  NCIT/CAS rows were reached.
- `curl -L ... q=Deuterated Glucose&ontology=ncit&exact=true`: live OLS
  returned exact `NCIT:C200498`.
- `curl -L https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/71777455/property/MolecularFormula,IsomericSMILES,InChI,InChIKey/JSON`:
  returned the stored CID and InChI.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with only full-corpus plausibility
  warnings.

## Evidence

- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` confirms
  prefix-specific OLS resolution of `NCIT:C200498` to `Deuterated Glucose`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` explicitly triages
  the NCIT parent row, `cas:201417-01-8` identity row, and
  `kgmicrobe.compound:deuterated_glucose` identity row as expected.
- The hidden/ignored-inclusive exact search over `data/ingredients`,
  `data/curated`, `mappings`, `docs/data`, `src`, `scripts`, and `tests`
  found no second active per-record YAML for `cas:201417-01-8` or
  `NCIT:C200498`.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Deuterated_Glucose` to `NCIT:C200498` with `skos:narrowMatch`,
  `cas:201417-01-8` with `skos:exactMatch`, and
  `kgmicrobe.compound:deuterated_glucose` with `skos:exactMatch`; the two
  identity rows emit only `CAS:201417-01-8` in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` are both supported only by
  `COMPUTATIONAL_PREDICTION` role assignments and provisional curator notes.
- Major: `chemical_properties.pubchem_cid` and `chemical_properties.inchi`
  point at isotope-specific PubChem CID `71777455`, but the stored `smiles`
  string has no carbon-13 or deuterium isotope labels.

## Completeness

- The record correctly keeps the exact isotope reagent as a CAS primary and
  uses NCIT `Deuterated Glucose` only as a parent.
- Mixture components, synonyms, environmental contexts, and CultureMech
  occurrence rows are correctly empty.

## Recommended Edits

- Major: update the `chemical_properties.smiles` in
  `data/ingredients/mapped/Deuterated_Glucose.yaml` to the isotope-specific
  PubChem isomeric SMILES for CID `71777455`, then synchronize
  `data/curated/mapped_ingredients.yaml`.
- Major: source or remove `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE`; neither role should rest only on generic
  name-based inference for a labeled isotope reagent.
