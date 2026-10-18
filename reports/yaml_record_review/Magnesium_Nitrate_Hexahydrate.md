# `data/ingredients/mapped/Magnesium_Nitrate_Hexahydrate.yaml`

## Verdict

Needs curation. The CAS-primary exact identity and close parent mapping to
anhydrous `CHEBI:64736` are appropriate, but the final SSSOM is missing the
local exact `kgmicrobe.compound` anchor row expected for this CAS-primary
hydrate pattern.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Magnesium_Nitrate_Hexahydrate.yaml`.
- Identifier and grounding: `identifier: cas:13446-18-9` with
  `ontology_mapping.ontology_id: CHEBI:64736`, label `magnesium nitrate`,
  source `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: two total occurrences in two CultureMech recipes.
- Local subject: magnesium nitrate hexahydrate, with the anhydrous ChEBI term
  retained only as a close parent.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Magnesium_Acetate` through `Malachite_Green`: exited 0 and wrote zero
  ERROR rows.
- LinkML term validation was skipped for this CAS-primary record because the
  subject identifier is outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves `CHEBI:64736` as active `magnesium nitrate`, CAS
  `10377-60-3`, and formula `Mg.2NO3`, which confirms that the ChEBI term is
  the anhydrous parent rather than the hexahydrate.
- PubChem resolves CAS `13446-18-9` to magnesium nitrate hexahydrate with
  formula `H12MgN2O12` and a hydrate InChI for one magnesium nitrate plus six
  waters.
- The final SSSOM has the expected close row to `CHEBI:64736` and exact row to
  `cas:13446-18-9`.
- `reports/hydrate_grounding.tsv` classifies this record as
  `CAS_MISSING_ANCHOR_ROWS`.

## Completeness

- The record has the right CAS subject and does not overclaim an exact match to
  the anhydrous ChEBI parent.
- The final SSSOM lacks the exact `kgmicrobe.compound` local registry row that
  should sit alongside the parent ChEBI row and exact CAS row for
  CAS-primary hydrate identities.

## Recommended Edits

- Add or regenerate the missing exact local `kgmicrobe.compound` registry
  anchor for `magnesium nitrate hexahydrate` while keeping the ChEBI relation
  at `CLOSE_MATCH`.
