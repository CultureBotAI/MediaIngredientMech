# `data/ingredients/mapped/H2so4.yaml`

## Verdict

Needs curation. The exact sulfuric-acid ChEBI identity, CAS RN, chemical
structure, occurrence count, and ChEBI-derived synonyms pass, but the final
SSSOM `other` column exports `H2SO4 (0.1 N)` as if it were an exact synonym of
pure sulfuric acid.

## Identity

- Reviewed record: `data/ingredients/mapped/H2so4.yaml`.
- Identifier and grounding: `identifier: CHEBI:26836` with
  `ontology_mapping.ontology_id: CHEBI:26836`, label `sulfuric acid`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7664-93-9`, formula `H2O4S`, InChI
  `InChI=1S/H2O4S/c1-5(2,3)4/h(H2,1,2,3,4)`, and SMILES
  `[H]OS(=O)(=O)O[H]`.
- Occurrence statistics: `total_occurrences: 337` and `media_count: 337`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H2_CO2.yaml data/ingredients/mapped/H2dimethylsulfide.yaml data/ingredients/mapped/H2methanol.yaml data/ingredients/mapped/H2seo3.yaml data/ingredients/mapped/H2so4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:26836` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:26836` as active `sulfuric acid` with CAS `7664-93-9`,
  formula `H2O4S`, the same InChI, and the same SMILES.
- The final SSSOM ChEBI-derived synonym tokens occur as ChEBI synonyms for
  `CHEBI:26836`, and the final `CAS:7664-93-9` token matches
  `chemical_properties.cas_rn`.
- The raw CultureMech `Role:`/`Properties:` synonyms and bare `(10 N)` synonym
  are correctly filtered from final SSSOM.
- Major: `H2SO4 (0.1 N)` is a concentration-specific CultureMech surface form
  for dilute sulfuric acid, not an exact synonym of pure sulfuric acid. It is
  currently exported in the final SSSOM `other` column.
- The final SSSOM otherwise publishes one `skos:exactMatch` row from
  `MIM:H2so4` to `CHEBI:26836`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  statistics, and exact sulfuric-acid SSSOM row are present and consistent.
- The final synonym export is incomplete until concentration-qualified H2SO4
  labels are suppressed from exact-match `other` tokens.

## Recommended Edits

- Major: remove `H2SO4 (0.1 N)` as an exported exact synonym, either by
  deleting it from this record or by extending the final-SSSOM synonym policy to
  reject concentration-qualified surface forms.
