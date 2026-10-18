# `data/ingredients/mapped/4-aminobenzoate.yaml`

## Verdict

Needs curation, major. The high-occurrence `CHEBI:17836` identity, CAS,
chemistry, exact synonym, SSSOM row, and occurrence counts pass, but the
`VITAMIN_SOURCE` role is a provisional LLM assertion with no inspected source.

## Identity

- Reviewed record: `data/ingredients/mapped/4-aminobenzoate.yaml`.
- Identifier and grounding: `identifier: CHEBI:17836` with
  `ontology_mapping.ontology_id: CHEBI:17836`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:17836` is active, resolves to
  `4-aminobenzoate`, has formula `C7H6NO2`, CAS `2906-28-7`, SMILES
  `Nc1ccc(C(=O)[O-])cc1`, and the stored InChI.
- PubChem CAS lookup for `2906-28-7` resolves to CID `4876` with the same InChI
  for the anion.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-acetoxyphenol.yaml data/ingredients/mapped/4-aminobenzoate.yaml data/ingredients/mapped/4-aminobutyrate.yaml data/ingredients/mapped/4-azido-L-phenylalanine.yaml data/ingredients/mapped/4-benzoyl-L-phenylalanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-aminobenzoate` to `CHEBI:17836` row.

## Evidence

- The CultureMech mapping, ChEBI CAS xref, PubChem CAS lookup, formula, InChI,
  SMILES, and `p-Aminobenzoate` synonym support the same 4-aminobenzoate anion.
- The occurrence count was corrected by #337 and is backed by the current
  CultureMech occurrence table: `138` total occurrences in `138` media.
- The OAK/OLS row-review manifest confirmed this mapping and asked for no
  curation action.
- Major: `nutritional_roles.VITAMIN_SOURCE` is supported only by
  `reference_type: COMPUTATIONAL_PREDICTION` with `reference_text: Assigned by
  in-session Claude reasoning (no external API)`. That is not an inspected
  medium or physiology source, and the curator note still says review is
  recommended.
- Minor: the `RAW_TEXT` synonym `Cross-references: KEGG:4abz` is a source-field
  fragment, not a synonym of 4-aminobenzoate. It does not currently publish in
  the SSSOM `other` field, but it should not remain as synonym text.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, merged duplicate history, aggregate copy, SSSOM row, OAK/OLS
  confirmation row, generated docs, microbedecoder residual labels, stale
  advisory rows, a separate potassium-salt record, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, exact synonym, `ingredient_type`, and occurrence
  statistics are populated.
- No component, environment, or discussion entries need review.
- The vitamin-source role needs a real external source or a bounded rejection.

## Recommended Edits

1. Replace the provisional `VITAMIN_SOURCE` evidence with an inspected source
   proving 4-aminobenzoate is being curated as a supplied vitamin source, or
   remove the role.
2. Remove the `Cross-references: KEGG:4abz` RAW_TEXT synonym.
3. Resync `data/curated/mapped_ingredients.yaml`, rebuild SSSOM and docs, and
   rerun strict, roundtrip, SSSOM, and term validation.
