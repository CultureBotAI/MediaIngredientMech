# `data/ingredients/mapped/Na2seo35h2o.yaml`

## Verdict

Pass with minor issues. The middle-dot sodium selenite pentahydrate record is a
rejected tombstone that now points at the live `CHEBI:131361` disodium selenite
pentahydrate identity and emits no final SSSOM row, but it still carries stale
anhydrous CAS and structure fields.

## Identity

- Reviewed record: `data/ingredients/mapped/Na2seo35h2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:131361` with
  `ontology_mapping.ontology_id: CHEBI:131361`, label
  `disodium selenite pentahydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: REJECTED`.
- Occurrences: 0 CultureMech recipe occurrences across 0 media after merge into
  the live `Na2seo3_X_5_H2o` record.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na2seo35h2o` through `Na2so3`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  tombstone.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:131361` as active
  `disodium selenite pentahydrate` with formula `5H2O.2Na.O3Se`, CAS
  `26970-82-1`, and a pentahydrate InChI.
- The #334/#360 tombstone repair correctly moved this loser off the anhydrous
  `CHEBI:48843` identity and onto the same `CHEBI:131361` identity used by the
  live `Na2SeO3 x 5 H2O` record.
- A hidden/ignored-inclusive `rg --no-ignore --hidden` search of
  `mappings/ingredient_mappings.sssom.tsv` found no `MIM:Na2seo35h2o` row, so
  this rejected tombstone itself does not publish a final mapping row.
- Minor: `chemical_properties.cas_rn` still stores the anhydrous CAS
  `10102-18-8`, and the stored InChI/SMILES are still anhydrous even though the
  molecular formula was patched to include five waters.

## Completeness

- The rejected status, zero occurrence count, refreshed identifier, refreshed
  `kg_microbe_node_id`, and absence from final SSSOM agree with the
  pentahydrate duplicate merge.
- The only remaining gaps are stale inert tombstone fields.

## Recommended Edits

- Minor: in `data/ingredients/mapped/Na2seo35h2o.yaml`, either remove the
  `chemical_properties` block from the rejected tombstone or refresh its CAS RN,
  InChI, and SMILES from `CHEBI:131361` so every retained field denotes the
  pentahydrate. Rerun strict validation after the tombstone cleanup.
