The current `data/normalized_yaml/algae/bb.yaml` (`CultureMech:000053`) retains `MoO` at `ingredients/2`, with `0.71 G_PER_L` at the medium root. The original CCAP recipe instead gives **MoO3, 0.71 g per litre of trace-element stock 7**, followed by **1 mL of stock 7 per litre of medium**.

Primary evidence: [CCAP Bold's Basal Medium PDF](https://www.ccap.ac.uk/wp-content/uploads/MR_BB.pdf), page 1, stock 7 table and final medium table. The captured PDF SHA256 is `2e9f5cfb8ab4df8e0db0ca08a274d2652abada40d075ed68a74478608ca7367a`. Current GitHub main file bytes, checked 2026-11-08 UTC, match the frozen source SHA256 `746699aed1ad8d8078dd48d8d5fd4186ca99fc91cc9d2761ee01fe5ff598dc69`.

This is a residual source transcription and stock hierarchy defect. Closed #276/#282 repaired other subscript losses; this file's history records a correction of `Co(NO ) .6H O`, while `MoO` remains. Closed #118 describes the broader stock concentration problem. Open #408 covers related unit ingestion. None of the reviewed issue bodies or #276 comments identifies this exact residual MoO occurrence.

Proposed follow-up:

- Reconstruct the BB stock and addition hierarchy from the primary recipe, including the other trace components now placed at the root.
- Restore this source token to MoO3 with primary-source provenance; establish its MIM identity through the normal guarded review.
- Keep 0.71 g/L as the stock composition. Where a final-medium concentration is represented, derive it transparently from the documented 1 mL/L addition (0.00071 g/L), without confusing the two stages.
- Preserve the original token in history and prevent a global `MoO` alias from hiding the parser defect. Validate against duplicate ingredients and missing stock constituents.

Found in authorized all-unmatched worker09 review, frozen case `CM_NAME:75d52d9f7d5b45ad6946c61474cb1f4c0e640d76c41680ab8fc544b6ca555b43`, occurrence `CM_OCC:fb0182bd4a6f07cc7f5618a1892150ebcc0c8c7867435ad8ab1c537b408636cf`. This issue does not claim other shards or authorize an MIM export release. No maintained source was changed by the review.
