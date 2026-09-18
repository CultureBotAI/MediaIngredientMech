# `data/ingredients/mapped/L-cysteine.yaml`

## Verdict

Needs curation. The free L-cysteine identity, CAS value, PubChem structure,
claim-level nitrogen-source role, occurrence count, and filtered rejected
hydrate label pass, but final SSSOM still exports `L-cysteine zwitterion` as a
synonym even though that string belongs to a distinct CHEBI:35235 sibling.

## Identity

- Reviewed record: `data/ingredients/mapped/L-cysteine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17561` with
  `ontology_mapping.ontology_id: CHEBI:17561`, label `L-cysteine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `52-90-4`, molecular formula `C3H7NO2S`, InChI,
  and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-cysteine.yaml data/ingredients/mapped/L-cysteine_Hcl.yaml data/ingredients/mapped/L-cysteine_Hcl_X_H2o.yaml data/ingredients/mapped/L-cysteine_Hydrochloride_Monohydrate.yaml data/ingredients/mapped/L-cysteine_Zwitterion.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 ChEBI records.

## Evidence

- EBI OLS4 resolves `CHEBI:17561` as active `L-cysteine`, lists CAS
  `52-90-4`, and includes the exact and related ChEBI synonyms exported for
  the neutral free acid.
- PubChem resolves CAS RN `52-90-4` to CID `5862` with formula `C3H7NO2S` and
  the same InChI as the YAML record.
- `nutritional_roles.NITROGEN_SOURCE` has `DATABASE_ENTRY` evidence from the
  CultureMech pipeline with original role text `Nitrogen Source`, matching the
  migrated role enum.
- The hydrate/salt label that ends in `H2O` is typed `REJECTED_LABEL` in YAML
  and is correctly filtered out of final SSSOM `other`.
- Major: final SSSOM `other` still exports `L-cysteine zwitterion` for
  `MIM:L-cysteine`. EBI OLS exact search resolves that label to CHEBI:35235
  rather than CHEBI:17561, and the repository already has a separate
  `data/ingredients/mapped/L-cysteine_Zwitterion.yaml` record for CHEBI:35235.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, final
  SSSOM row, docs projections, the separate zwitterion and monohydrate sibling
  rows, and the row-review history for this cysteine family.

## Completeness

- The active ChEBI identity, CAS RN, formula, structure, occurrence count,
  nitrogen-source role, aggregate copy, and rejected hydrate label are present
  and internally consistent.
- The final SSSOM synonym surface is incomplete until the distinct zwitterion
  label is removed from this neutral L-cysteine row.

## Recommended Edits

- Major: remove `L-cysteine zwitterion` from
  `data/ingredients/mapped/L-cysteine.yaml`; keep that label only on
  `data/ingredients/mapped/L-cysteine_Zwitterion.yaml`.
- Sync the aggregate copy and regenerate the SSSOM/docs products so `other`
  stops publishing the cross-identity zwitterion synonym; rerun strict, term,
  round-trip, component, and SSSOM validation.
