# `data/ingredients/mapped/4-Hydroxynonenal.yaml`

## Verdict

Needs curation, major. The active ChEBI grounding and formula are plausible, but
the record stores ChEBI's wildcard aldehyde-fragment SMILES as if it were a full
structure while also carrying a CAS RN that PubChem resolves to a specific
4-hydroxy-2E-nonenal molecule.

## Identity

- Reviewed record: `data/ingredients/mapped/4-Hydroxynonenal.yaml`.
- Identifier and grounding: `identifier: CHEBI:142593` with
  `ontology_mapping.ontology_id: CHEBI:142593`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:142593` is active, resolves to
  `4-hydroxynonenal`, has generalized formula `C9H16O2`, and exposes SMILES
  `*C([H])=O`.
- PubChem CAS lookup for `75899-68-2` resolves to CID `5283344`, formula
  `C9H16O2`, SMILES `CCCCCC(/C=C/C=O)O`, and an InChI with the explicit
  `2E` bond layer `/b7-5+`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml data/ingredients/mapped/4-Hydroxynonanoic_Acid.yaml data/ingredients/mapped/4-Hydroxynonenal.yaml data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Hydroxybenzaldehyde.yaml data/ingredients/mapped/4-Hydroxymandelic_Acid_Monohydrate.yaml data/ingredients/mapped/4-Hydroxynonanoic_Acid.yaml data/ingredients/mapped/4-Hydroxynonenal.yaml data/ingredients/mapped/4-Hydroxyphenylpropionic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:4-Hydroxynonenal` to `CHEBI:142593` row.

## Evidence

- Supported: the official ChEBI label and generalized empirical formula agree
  with `4-Hydroxynonenal` and `C9H16O2`.
- Major: `chemical_properties.smiles` is `*C([H])=O`, which is only the
  wildcard aldehyde fragment exposed by the ChEBI class, not a complete C9 HNE
  structure. The record therefore mixes a complete empirical formula with an
  incomplete structure string.
- Major: the stored CAS `75899-68-2` resolves in PubChem to a specific
  4-hydroxy-2E-nonenal structure, while the active ChEBI term is a generalized
  ChEBI class and the OLS response for `CHEBI:142593` does not cross-reference
  that CAS.
- Stale: `mappings/record_research_validation.tsv` still treats the ChEBI
  grounding as unresolved before the OAK/OLS confirmation, but its structural
  concern about the wildcard SMILES remains valid.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, OAK/OLS confirmation row, generated
  docs, stale advisory rows, and ignored aggregate backups.

## Completeness

- The formula and `ingredient_type` are populated.
- There is no full InChI and no full SMILES for the modeled form.
- This CultureBotHT import has no recipe-count occurrence; no role, component,
  environment, or discussion entries need review.

## Recommended Edits

1. Decide whether the supplied CultureBotHT ingredient is the generic
   `CHEBI:142593` class or CAS `75899-68-2` 4-hydroxy-2E-nonenal.
2. If CAS `75899-68-2` is the intended form, replace the wildcard SMILES with
   the full PubChem structure and map to a specific exact ontology term if one
   exists; otherwise keep `CHEBI:142593` only as a non-exact parent.
3. If the generic ChEBI class is intended, remove or reject the CAS-specific
   structure claim so the record no longer mixes a ChEBI class with a specific
   registry compound.
4. Resync `data/curated/mapped_ingredients.yaml`, rebuild SSSOM and docs, then
   rerun strict, SSSOM, roundtrip, and term validation.
