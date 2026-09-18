# `data/ingredients/mapped/Asparagine.yaml`

## Verdict

Needs curation; severity major. The record's exact `CHEBI:22653` asparagine
identity, CAS-backed formula and structure, rejected hydrate boundary,
nutritional role, SSSOM row, and aggregate copy pass, but two old
CultureMech role/property strings remain in `synonyms`.

## Identity

- Reviewed record: `data/ingredients/mapped/Asparagine.yaml`.
- Identifier and grounding: `identifier: CHEBI:22653` with
  `ontology_mapping.ontology_id: CHEBI:22653`, `ontology_label: asparagine`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`, and
  `mapping_status: MAPPED`.
- OLS resolves `CHEBI:22653` to non-obsolete `asparagine` with CAS xref
  `3130-87-8`, formula `C4H8N2O3`, and the same InChI and SMILES used in
  `chemical_properties`.
- PubChem resolves CAS `3130-87-8` to the anhydrous `DL-Asparagine` formula and
  InChI as one returned CID; it also returns `DL-Asparagine monohydrate` for the
  same registry search, but the active record rejects the raw
  `DL-Asparagine x H2O` hydrate label and a separate
  `data/ingredients/mapped/L-Asparagine_Monohydrate.yaml` record preserves the
  L-asparagine monohydrate CAS identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Asparagine.yaml data/ingredients/mapped/Aspartate.yaml data/ingredients/mapped/Astaxanthin.yaml data/ingredients/mapped/Astromicin.yaml data/ingredients/mapped/Atorvastatin_Calcium_Salt_Trihydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Asparagine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- OLS4 lookup for `CHEBI:22653` resolved the non-obsolete `asparagine` term and
  confirmed the CAS xref, formula, InChI, and SMILES.
- PubChem lookup for CAS `3130-87-8` found the matching anhydrous structure and
  the adjacent `DL-Asparagine monohydrate` boundary.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 489 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/culturemech_recipe_membership.tsv` has 28 `CHEBI:22653`
  memberships, matching `occurrence_statistics`.
- `mappings/ingredient_mappings_row_review_manifest.tsv` documents that the
  `kgmicrobe.compound:asparagine` registry row was intentionally kept and that
  the synonym-enrichment proposal was already represented.
- `mappings/other_cross_record_baseline.tsv` still tracks the
  `MIM:L-asparagine` to `MIM:Asparagine` same-name boundary as unreviewed; the
  current `Asparagine` and `L-Asparagine` records nonetheless keep distinct
  CHEBI identifiers and structures.
- The `NITROGEN_SOURCE` role is backed by a narrow CultureMech database-entry
  evidence item.
- Two strings beginning `Role: Nitrogen source; Properties:` remain in
  `synonyms`. They describe CultureMech role/property facets rather than
  lexical names for asparagine, and the nutritional role now preserves the role
  claim explicitly.

## Completeness

- The exact identity, CAS RN, formula, InChI, SMILES, role, SSSOM row, and
  occurrence counts are populated.
- The hidden hydrate synonym collapse has already been resolved by marking
  `DL-Asparagine x H2O` as `REJECTED_LABEL`.
- The hidden/ignored-inclusive corpus searches found no unresolved
  `Asparagine` review row that would require a second maintained input.

## Recommended Edits

- Remove the two `Role: Nitrogen source; Properties: ...` strings from
  `synonyms` in `data/ingredients/mapped/Asparagine.yaml`; synchronize
  `data/curated/mapped_ingredients.yaml`, regenerate the affected SSSOM and
  flat exports, then rerun focused strict and term validation plus the SSSOM
  and flat-export checks.
