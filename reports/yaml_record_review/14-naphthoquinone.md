# `data/ingredients/mapped/14-naphthoquinone.yaml`

## Verdict

Needs curation, minor. The active `CHEBI:27418` identity for
`1,4-Naphthoquinone` is correct and synchronized, but a CultureMech role marker
is still stored in the `synonyms` list as raw text.

## Identity

- Reviewed record: `data/ingredients/mapped/14-naphthoquinone.yaml`.
- Identifier and grounding: `identifier: CHEBI:27418` with
  `ontology_mapping.ontology_id: CHEBI:27418`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:27418`
  resolves to `1,4-naphthoquinone` and lists CAS `130-15-4`, formula
  `C10H6O2`, SMILES `O=C1C=CC(=O)c2ccccc21`, and InChI matching the record.
- The kg-microbe synonyms `alpha-naphthoquinone` and `naphthoquinone` are
  present on the ChEBI page for this exact term.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/14-naphthoquinone.yaml data/ingredients/mapped/15-Pentanediol.yaml data/ingredients/mapped/16-Hexanediamine.yaml data/ingredients/mapped/18-Crown-6.yaml data/ingredients/mapped/2-6-dihydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/14-naphthoquinone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/14-naphthoquinone.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  normalized semantic equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:14-naphthoquinone` to `CHEBI:27418` row, and docs/label-index outputs
  carry the exact kg-microbe labels without publishing `Role: Growth factor` as
  an exact label.

## Evidence

- The active ChEBI target confirms the mapped identity, CAS RN, formula, SMILES,
  InChI, and the exact text of the potentially ambiguous legacy names retained
  from kg-microbe.
- Minor: `Role: Growth factor` is not a chemical name and should not be stored
  in `synonyms`, even as `RAW_TEXT`. The field is label-bearing in aggregate
  surfaces, while this string describes a CultureMech role facet.
- Stale: `mappings/record_research_validation.tsv` still includes old rows that
  requested direct ChEBI verification or questioned ChEBI-listed aliases; the
  live ChEBI page now resolves the identity and synonyms.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored
  backups, and generated review output found the active YAML/aggregate/SSSOM
  rows, old advisory rows, and no unresolved active duplicate for `CHEBI:27418`.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, formula, SMILES, and InChI are populated for the active chemical
  form.
- Empty component and role slots are acceptable for this single ChEBI chemical;
  the CultureMech growth-factor marker should not be converted into a global
  nutritional role without direct medium-specific evidence.

## Recommended Edits

1. In `data/ingredients/mapped/14-naphthoquinone.yaml`, remove
   `Role: Growth factor` from `synonyms` or move the original CultureMech facet
   into a non-label provenance slot if the source wording must be retained.
2. Regenerate `data/curated/mapped_ingredients.yaml` after the maintained YAML
   edit.
3. If `mappings/record_research_validation.tsv` is intended to be a live queue,
   regenerate it so stale ChEBI-verification rows no longer imply pending work.
