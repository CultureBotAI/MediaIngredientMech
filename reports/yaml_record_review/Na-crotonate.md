# `data/ingredients/mapped/Na-crotonate.yaml`

## Verdict

Needs curation - major. The #315 salt/ion repair gives `Na-crotonate` its own
local sodium-crotonate identity, preserves `CHEBI:41131` crotonic acid as a
narrow parent, rejects bare-crotonate labels, and publishes the required final
SSSOM sibling rows, but the `CARBON_SOURCE` facet is still unsupported.

## Identity

- Reviewed record: `data/ingredients/mapped/Na-crotonate.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:na-crotonate` with
  `ontology_mapping.ontology_id: CHEBI:41131`, label `crotonic acid`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 9 CultureMech recipe occurrences across 9 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Na-benzoate` through `Na-crotonate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.

## Evidence

- A fresh EBI OLS4 lookup resolves `CHEBI:41131` as active `crotonic acid`, and
  a fresh OLS4 search found no exact CHEBI candidate for `sodium crotonate`;
  keeping `kgmicrobe.compound:na-crotonate` as the exact identity with a narrow
  ChEBI acid parent is therefore still the right #315 repair.
- The previous bare-anion `CHEBI:35899` enrichment labels are marked
  `REJECTED_LABEL`, so they no longer assert that this sodium-salt record is the
  crotonate anion.
- The final SSSOM output carries both required rows:
  `MIM:Na-crotonate skos:narrowMatch CHEBI:41131` and
  `MIM:Na-crotonate skos:exactMatch kgmicrobe.compound:na-crotonate`, with only
  `Sodium crotonate` left in `other`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by a
  `COMPUTATIONAL_PREDICTION` whose curator note calls it a provisional
  in-session LLM assignment. No inspected source in this record supports sodium
  crotonate's use as a carbon source.

## Completeness

- The local exact identity, ChEBI parent mapping, rejected bare-ion synonyms,
  9/9 label-aware occurrence count, empty chemical-properties block, and final
  SSSOM sibling rows agree.
- The only consequential gap is the unsupported `CARBON_SOURCE` role facet.

## Recommended Edits

- Major: in `data/ingredients/mapped/Na-crotonate.yaml`, either remove
  `nutritional_roles.CARBON_SOURCE` or replace its computational placeholder
  with source-backed evidence from maintained occurrence, role-text, or
  literature inputs. Rerun strict validation and final SSSOM validation after
  the role facet changes.
