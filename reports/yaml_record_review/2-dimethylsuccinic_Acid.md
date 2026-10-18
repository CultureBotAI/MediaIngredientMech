# `data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`

## Verdict

Needs curation, blocker. The record publishes an exact identity row to
`CHEBI:167506`, but `CHEBI:167506` is the 2,3 isomer and the record itself only
documents a non-exact truncated-label rationale.

## Identity

- Reviewed record: `data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`.
- Current identifier and grounding: `identifier: CHEBI:167506` with
  `ontology_mapping.ontology_id: CHEBI:167506`, source `CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:167506`
  resolves to `2,3-dimethylsuccinic acid`; `CHEBI:86537` resolves separately to
  `2,2-dimethylsuccinic acid`.
- The local `truncated_locants.tsv` and hidden-inclusive
  `record_research_validation.tsv` hits agree that the active `2,3` target is
  disputed and that the raw `2-dimethylsuccinic acid` label is not enough to
  select the 2,3 isomer.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-deoxyinosine.yaml data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/2-deoxyuridine.yaml data/ingredients/mapped/2-dichloroethane.yaml data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains a synchronized exact
  `MIM:2-dimethylsuccinic_Acid` to `CHEBI:167506` row. That proves product
  consistency, but the row itself is the problem: an own-identifier exact row
  cannot represent the record's `CLOSE_MATCH` rationale.

## Evidence

- `CHEBI:167506` and `CHEBI:86537` are distinct live ChEBI terms for the 2,3
  and 2,2 isomers, so selecting one isomer from the truncated
  `2-dimethylsuccinic acid` source string requires curation evidence.
- The active evidence note says the raw label was a truncation of
  `2,3-dimethylsuccinic acid`, but then says a single locant cannot carry two
  methyl groups. The second premise is wrong for choosing between the 2,2 and
  2,3 isomers.
- `mappings/record_research_validation.tsv` already marks this as a P1
  cross-lane dispute, including a Claude-lane recommendation to investigate
  `CHEBI:86537` or revert to unmapped rather than leave `CHEBI:167506`
  unexamined.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the source microbedecoder row, `truncated_locants.tsv`, the active
  YAML/aggregate/SSSOM rows, and the cross-lane P1 dispute.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is populated, but chemical properties are
  absent.
- The key missing representation is not optional chemistry; it is a defensible
  identity model. If the exact isomer is known, the YAML identifier, label,
  mapping quality, and SSSOM row should say so. If not, the record should retain
  a local identity and only point at external isomer candidates non-exactly.

## Recommended Edits

1. Revisit the source truncation for
   `data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml` using
   `mappings/truncated_locants.tsv`, `data/custom/microbedecoder/ingredient_candidates.tsv`,
   and the candidate ChEBI terms.
2. If the source can be proven to be `2,2-dimethylsuccinic acid`, reground the
   record to `CHEBI:86537`; if the source cannot be proven, change the primary
   identifier to a local fallback and remove the exact own-identifier row to
   `CHEBI:167506`.
3. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`, `just validate-terms
   data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml` if the result is
   CHEBI-backed, `just qc-sssom`, and `just qc-flat-coverage` after that
   curation edit.
