# `data/ingredients/mapped/Hcl.yaml`

## Verdict

Needs curation. The exact hydrogen-chloride ChEBI identity, CAS RN, structure
fields, occurrence count, and ChEBI-derived synonyms pass, but final SSSOM
exports punctuation- and concentration-qualified HCl labels as exact synonyms.

## Identity

- Reviewed record: `data/ingredients/mapped/Hcl.yaml`.
- Identifier and grounding: `identifier: CHEBI:17883` with
  `ontology_mapping.ontology_id: CHEBI:17883`, label `hydrogen chloride`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `7647-01-0`, formula `HCl`, InChI
  `InChI=1S/ClH/h1H`, and SMILES `[H]Cl`.
- Occurrence statistics: `total_occurrences: 1208` and `media_count: 1208`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Harmol.yaml data/ingredients/mapped/Harmol_Hydrochloride.yaml data/ingredients/mapped/Hcl.yaml data/ingredients/mapped/Heart_Infusion_Agar_BD_211065.yaml data/ingredients/mapped/Hecogenin.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:17883` and the CAS registry CURIE.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:17883` as active `hydrogen chloride` with CAS
  `7647-01-0`, formula `HCl`, the same InChI, and the same SMILES.
- The core final SSSOM ChEBI-derived synonym tokens are real ChEBI synonyms,
  and the final `CAS:7647-01-0` token matches `chemical_properties.cas_rn`.
- The raw CultureMech `Role:`/`Properties:` synonyms and bare concentration
  synonyms `(0.05 molar)` and `(1M)` are correctly filtered from final SSSOM.
- Major: `HCl.` is a punctuation variant, and the eight `HCl (...)` tokens are
  concentration-specific CultureMech surface forms for prepared acid solutions,
  not exact synonyms of hydrogen chloride. All nine strings are currently
  exported in the final SSSOM `other` column.
- The final SSSOM otherwise publishes one `skos:exactMatch` row from `MIM:Hcl`
  to `CHEBI:17883`.

## Completeness

- The active ChEBI identifier, CAS RN, formula, InChI, SMILES, occurrence
  statistics, and exact hydrogen-chloride SSSOM row are present and consistent.
- The final synonym export is incomplete until punctuation and
  concentration-qualified HCl labels are suppressed from exact-match `other`
  tokens.

## Recommended Edits

- Major: suppress or retype `HCl.` and all `HCl (...)` concentration labels so
  they no longer appear in final SSSOM as exact synonyms.
