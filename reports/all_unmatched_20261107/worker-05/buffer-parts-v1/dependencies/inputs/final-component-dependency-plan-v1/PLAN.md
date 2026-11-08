# Conditional component dependency plan

The accounting cutoff is 2026-11-08T07:59:05.182653+00:00. This is a closed reference-coupling plan, not a source/corpus or export approval. Every proposed final owner and consumer must be rebound to the final accepted heads before application.

| Consumer | Selector | Existing identifier | Action | Tracker |
|---|---|---|---|---|
| Casitone_Yeast_Extract_Rumen_Fluid.yaml | components[2] | MICRO:0000520 | PREPARED_WITHDRAW_UNSUPPORTED_CLARIFIED_REFERENCE | #1204 |
| Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml | components[0] | FOODON:03305103 | EXISTING_PROPOSAL_WITHDRAWS_UNSUPPORTED_FOOD_OR_PRODUCT_REFERENCE | #1193 |
| Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml | components[1] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| GYPS.yaml | components[2] | MICRO:0000178 | RETAIN_SOURCE_SPECIFIC_BACTO_REFERENCE | #1176 |
| Glucose_Peptone-yeast_Extract.yaml | components[1] | MICRO:0000178 | GENERIC_REFERENCE_MIGRATION_CANDIDATE | #1176 |
| Marine_Broth_2216.yaml | components[0] | MICRO:0000178 | EXISTING_PROPOSAL_WITHDRAWS_REFERENCE | #1176 |
| Marine_agar_2216.yaml | components[0] | MICRO:0000178 | GENERIC_REFERENCE_MIGRATION_CANDIDATE | #1176 |
| Modified_Cooked_Meat_Medium.yaml | components[0] | FOODON:03305103 | EXISTING_PROPOSAL_WITHDRAWS_UNSUPPORTED_FOOD_OR_PRODUCT_REFERENCE | #1193 |
| PY-cellobiose.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PY-fructose.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PY-glucose-rumen_Fluid.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PY-glucose-rumen_Fluid.yaml | components[3] | MICRO:0000520 | PREPARED_WITHDRAW_UNSUPPORTED_CLARIFIED_REFERENCE | #1204 |
| PY-maltose.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PY-pectin.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PYEG.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PYG-002_Tween_80.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PYG.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PYGS.yaml | components[0] | MICRO:0000178 | GENERIC_REFERENCE_MIGRATION_CANDIDATE | #1176 |
| PYG_Rumen_Fluid.yaml | components[0] | MICRO:0000178 | HOLD_SOURCE_COMPONENT_IDENTITY | #1176 |
| PYG_Rumen_Fluid.yaml | components[3] | MICRO:0000520 | PREPARED_WITHDRAW_UNSUPPORTED_CLARIFIED_REFERENCE | #1204 |
| Peptone-yeast_Extract-glucose.yaml | components[0] | MICRO:0000178 | GENERIC_REFERENCE_MIGRATION_CANDIDATE | #1176 |
| Peptone_Beef_Extract_Yeast_Extract.yaml | components[0] | MICRO:0000178 | GENERIC_REFERENCE_MIGRATION_CANDIDATE | #1176 |
| Peptone_Yeast_Extract.yaml | components[0] | MICRO:0000178 | GENERIC_REFERENCE_MIGRATION_CANDIDATE | #1176 |
| UW_Concentrated_Base.yaml | components[10] | CHEBI:131366 | PREPARED_SAME_SUBSTANCE_REFERENCE_CORRECTION | #1168 |
| UW_Concentrated_Base_No_Mo.yaml | components[9] | CHEBI:131366 | PREPARED_SAME_SUBSTANCE_REFERENCE_CORRECTION | #1168 |
| UW_Concentrated_Base_No_Sulfur.yaml | components[10] | CHEBI:131366 | PREPARED_SAME_SUBSTANCE_REFERENCE_CORRECTION | #1168 |
| Yeast_Extract_Peptone.yaml | components[1] | MICRO:0000178 | GENERIC_REFERENCE_MIGRATION_CANDIDATE | #1176 |
| togo_m2491_mrssi_base.yaml | components[8] | MICRO:0000178 | GENERIC_REFERENCE_MIGRATION_CANDIDATE | #1176 |

Read `minimal-couplings-28.json` for exact source/consumer hashes, actions and limits; `new-target-obligations-11.json` for new owner dependencies; `composed-consumer-obligations.json` for consumers with multiple changes.

Peptone has20 distinct claims:8 generic reference migration candidates,10 unresolved source-identity claims,1 deliberately retained Bacto-specific GYPS claim and1 already-prepared Marine Broth withdrawal. The published W05 payloads contain7 old-ID claim versions, not7 extra consumers. Native partonomy reports zero for a generic-Peptone-only transition because Bacto remains; that green result is not authority to retarget or retain wrong scope.

Three same-substance UW borax retargets are already prepared under1168. Three generic rumen references must remain literal UNMAPPED under1204. Two cooked-meat references have prepared unsupported-ID withdrawals, not a substitution to a named whole product.

No global replace, automatic owner merge, new namespace choice, sidecar reattribution or new gate is proposed. #1245 Mg/Cr code coupling and #1211 PIPES node pointer remain independently tracked. #710 is closed historical context; #1176 is the live peptone tracker.

The original incomplete collector-v1 and superseded collector-v2 remain immutable. Only `analysis-v3` and the final files named above are authoritative for counts.
