# `data/ingredients/mapped/Anabasine_Hydrochloride.yaml`

## Verdict

Pass. The CAS-primary identity, broader `NCIT:C216370` parent, PubChem
chemistry, exact CAS and local SSSOM rows, row-review disposition, aggregate
copy, and zero CultureMech memberships agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Anabasine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: cas:53912-89-3` with
  `ontology_mapping.ontology_id: NCIT:C216370`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` confirms that the
  prefix-specific EBI OLS lookup resolves `NCIT:C216370` exactly as
  `Anabasine Hydrochloride`; the `UNKNOWN_TERM` trailer came from earlier
  validator prefix coverage rather than a mapping defect.
- PubChem resolves CAS `53912-89-3` to the stored CID `3041330`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Amylopectin_From_Maize.yaml data/ingredients/mapped/Amylose_From_Potato.yaml data/ingredients/mapped/Anabasine_Hydrochloride.yaml data/ingredients/mapped/Anaerobic_water.yaml data/ingredients/mapped/Andirobin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anabasine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` rows 420-422 export the expected
  `skos:narrowMatch` row to `NCIT:C216370`, the exact CAS registry row, and
  the exact `kgmicrobe.compound:anabasine_hydrochloride` companion row.
- `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the NCIT
  `UNKNOWN_TERM` trailer as missing prefix coverage, and classifies the CAS and
  kg-microbe companion rows as expected registry identifiers.
- The YAML formula `C10H15ClN2`, SMILES
  `C1CCNC(C1)C2=CN=CC=C2.Cl`, InChI, and `pubchem_cid: 3041330` are
  internally aligned with the PubChem CAS identity.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, CultureMech memberships, SSSOM and row-review TSVs, and batch
  review reports found the active YAML, aggregate copy, SSSOM identity rows,
  row-review rows, and no `culturemech_recipe_membership.tsv` rows for
  `cas:53912-89-3`.

## Completeness

- CAS, formula, SMILES, InChI, PubChem CID, NCIT parent mapping, exact CAS and
  local SSSOM rows, curation history, and `ingredient_type` are populated.
- No synonym, component, role, environmental context, discussion, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

None.
