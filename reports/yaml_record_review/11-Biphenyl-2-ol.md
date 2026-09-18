# `data/ingredients/mapped/11-Biphenyl-2-ol.yaml`

## Verdict

Needs curation. The CultureMech residual row is correctly grounded to
`CHEBI:17043`/`biphenyl-2-ol`, but this newer ChEBI record is missing the
standard single-ingredient classification and ChEBI chemical-property backfill
that comparable structural ChEBI records carry.

## Identity

- Reviewed record: `data/ingredients/mapped/11-Biphenyl-2-ol.yaml`.
- Identifier and grounding: `identifier: CHEBI:17043` with
  `ontology_mapping.ontology_id: CHEBI:17043`, label `biphenyl-2-ol`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:17043`
  resolves to `biphenyl-2-ol`, lists the IUPAC name
  `[1,1'-biphenyl]-2-ol`, and exposes formula `C12H10O`, SMILES
  `Oc1ccccc1-c1ccccc1`, InChI
  `InChI=1S/C12H10O/c13-12-9-5-4-8-11(12)10-6-2-1-3-7-10/h1-9,13H`,
  and CAS RN `90-43-7`.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/11-Biphenyl-2-ol.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/11-Biphenyl-2-ol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/11-Biphenyl-2-ol.yaml data/ingredients/mapped/112-trichloroethane.yaml data/ingredients/mapped/1122-Tetrachloroethane.yaml data/ingredients/mapped/12-Propanediol.yaml data/ingredients/mapped/12-dichloropropane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed:
  strict validation, `validate_all.py --mode both`, SSSOM invariants, flat
  export coverage, duplicate-ID baseline, kg-microbe node-ID audit, component
  partonomy, and product id/label correspondence.
- Evidence-reference validation could not run because the sibling
  `culturebotai-claw` checkout was absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `CHEBI:17043` row, and generated docs expose the same ChEBI label.

## Evidence

- Current ChEBI supports the exact substance identity and shows that the source
  surface `[1,1'-Biphenyl]-2-ol` is the IUPAC name for `CHEBI:17043`.
- The structured evidence now names `culturemech:output/ingredient_occurrences.tsv`;
  that restores the provenance the SSSOM builder reads and avoids the #541
  dropped-source defect.
- Minor: `ingredient_type` and `chemical_properties` are absent even though the
  official ChEBI page has formula, SMILES, InChI, CAS, and molecular-weight
  data for this single chemical.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM/docs rows,
  the CultureMech residual triage row, and no duplicate active YAML for
  `CHEBI:17043`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- The 60 CultureMech occurrences are represented in `total_occurrences` and
  `media_count`.

## Recommended Edits

1. Add `ingredient_type: SINGLE_INGREDIENT` and ChEBI-backed chemical
   properties for `CHEBI:17043` through the normal enrichment path, then
   regenerate the aggregate, SSSOM, and docs.
2. No identifier, ontology mapping, occurrence count, or evidence-source edit is
   needed.
