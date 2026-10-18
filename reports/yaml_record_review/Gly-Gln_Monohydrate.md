# `data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`

## Verdict

Needs curation. The CAS fallback identity, hydrate-specific PubChem structure,
close match to anhydrous `CHEBI:73898` Gly-Gln, and exact CAS registry row pass,
but the final ChEBI SSSOM row exports `glycyl-L-glutamine`, an anhydrous-parent
synonym, in `other` on the monohydrate subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:172669-64-6`, close-mapped to
  anhydrous `CHEBI:73898` with canonical label `Gly-Gln`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `172669-64-6`, formula `C7H15N3O5`, and
  anhydrate plus water InChI
  `InChI=1S/C7H13N3O4.H2O/c8-3-6(12)10-4(7(13)14)1-2-5(9)11;/h4H,1-3,8H2,(H2,9,11)(H,10,12)(H,13,14);1H2/t4-;/m0./s1`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glutaric_Acid.yaml data/ingredients/mapped/Glutathione.yaml data/ingredients/mapped/Glutathione_Oxidized.yaml data/ingredients/mapped/Gly-DL-Asp.yaml data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`:
  exited 0 for the 5-file batch.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Glutaric_Acid.yaml data/ingredients/mapped/Glutathione.yaml data/ingredients/mapped/Glutathione_Oxidized.yaml data/ingredients/mapped/Gly-DL-Asp.yaml data/ingredients/mapped/Gly-Gln_Monohydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five ChEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same CAS primary identifier, ChEBI close match, anhydrous exact synonym,
  hydrate chemical properties, singleton type, and #342 close-match evidence as
  the per-record YAML.
- OLS4 resolves `CHEBI:73898` as `Gly-Gln`, matching the YAML parent
  `ontology_mapping`.
- PubChem resolves CAS `172669-64-6` to formula `C7H15N3O5` and an IUPAC name
  ending in `hydrate`, matching the record's own hydrate identity and differing
  from the anhydrous ChEBI parent.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Gly-Gln_Monohydrate` to `CHEBI:73898` with `skos:closeMatch` and to the
  record's own `cas:172669-64-6` identifier with `skos:exactMatch`.
- Major: the final close-match row to anhydrous `CHEBI:73898` exports
  `glycyl-L-glutamine` in `other`. That token is a synonym for the anhydrous
  parent, and publishing it on `MIM:Gly-Gln_Monohydrate` erases the hydrate
  boundary that #342 deliberately preserved.
- The final CAS identity row keeps only `CAS:172669-64-6` in `other`, which is
  correct for the monohydrate subject.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `reports`, and `.claude` found the active YAML, aggregate copies, hydrate
  grounding report entry, final SSSOM rows, row-review decisions for the CAS
  registry row and already represented synonym enrichment, generated indexes,
  old batch validation reports, and ignored aggregate backups.

## Completeness

- The CAS primary identity, hydrate formula, InChI, SMILES, close ChEBI parent
  mapping, exact CAS SSSOM row, and close ChEBI SSSOM row are populated.
- The anhydrous-parent synonym needs removal from the monohydrate record before
  final SSSOM is rebuilt.

## Recommended Edits

- Major: remove `glycyl-L-glutamine` from the active exact-synonym set in
  `data/ingredients/mapped/Gly-Gln_Monohydrate.yaml`; keep it only as parent
  evidence if needed.
- Major: rebuild the final SSSOM so the close-match row to `CHEBI:73898` no
  longer publishes the anhydrous parent synonym in `other`.
