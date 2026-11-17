# Purpose: compact the pinned scientific source-binding display for issue1453.
# Inputs: output of review_culturemech_intake_second_1453.py --claims-only.
# Outputs: all source descriptor/change/held claims and current owner identity.
# Date: 2026-11-17. Excluded owner history/roles/statistics are not re-approved;
# full owner and occurrence coordinates remain hash-bound in the source packet.
.display_scope = "Current owner identity, components, notes, mapping evidence and synonyms; all scientific source payloads retained. Owner history/roles/statistics and occurrence coordinate display omitted only from this view, not the pinned packet or native review."
| del(.owner_payload.curation_history,
      .owner_payload.occurrence_statistics,
      .owner_payload.nutritional_roles,
      .owner_payload.biological_roles,
      .owner_payload.medium_roles,
      .owner_payload.functional_roles,
      .cases[].occurrence_coordinate_display.source_scope_signatures)
