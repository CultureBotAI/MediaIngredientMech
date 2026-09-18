# `data/ingredients/mapped/Na2s2o4.yaml`

## Verdict

Pass with minor issues. The record is now a rejected tombstone that points to
the live `CHEBI:66870` sodium dithionite identity and emits no final SSSOM row,
but it still carries stale scutellarin synonyms, scutellarin structure fields,
and a provisional role from the pre-merge wrong ChEBI grounding.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2s2o4.yaml`.
- Identifier and grounding: `identifier: CHEBI:66870` with
  `ontology_mapping.ontology_id: CHEBI:66870`, label `sodium dithionite`,
  source `CHEBI`, `mapping_quality: SYNONYM_MATCH`, and
  `mapping_status: REJECTED`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media after merge into
  the live `Sodium_Dithionite` record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2s2o3_X_5_H2o` through `Na2seo3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  tombstone.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:66870` as active
  `sodium dithionite`, CAS `7775-14-6`, and formula `2Na.O4S2`; a fresh
  PubChem CAS lookup for `7775-14-6` resolves to the same anhydrous dithionite
  formula and stored InChI.
- The `reground_263` history records the root fix: `Na2S2O4` was sodium
  dithionite, its old `CHEBI:61278` scutellarin grounding was wrong, and this
  duplicate was merged into the live `Sodium_Dithionite` record.
- A hidden/ignored-inclusive `rg --no-ignore --hidden` search of
  `mappings/ingredient_mappings.sssom.tsv` found no `MIM:Na2s2o4` row, so the
  rejected tombstone itself does not publish a final mapping row.
- Minor: the tombstone still carries six scutellarin exact synonyms, the
  scutellarin molecular formula/InChI/SMILES, `ingredient_type:
  SINGLE_INGREDIENT`, and a provisional `REDUCING_AGENT` role. Those fields
  document stale live-shape content from the wrong pre-#263 identity.
- The live `MIM:Sodium_Dithionite` final SSSOM row also still publishes the
  scutellarin aliases inherited during the merge; that active-row cleanup
  belongs to `data/ingredients/mapped/Sodium_Dithionite.yaml`, not this
  tombstone.

## Completeness

- The rejected status, zero occurrence count, refreshed identifier, refreshed
  ontology mapping, and absence from the final SSSOM agree with the
  sodium-dithionite merge.
- The only gaps on this file are stale inert tombstone fields. They should be
  cleaned to prevent label-index confusion, but they are not emitted as this
  record's own final SSSOM row.

## Recommended Edits

- Minor: prune or demote the stale scutellarin synonyms and remove the
  scutellarin chemical block plus provisional role from
  `data/ingredients/mapped/Na2s2o4.yaml`. Rerun strict validation and the label
  index/product checks after the tombstone cleanup.
- Major, for the live target: remove the same scutellarin aliases from
  `data/ingredients/mapped/Sodium_Dithionite.yaml` before rebuilding final
  SSSOM, so `MIM:Sodium_Dithionite` no longer publishes synonyms for the old
  unrelated `CHEBI:61278` target.
