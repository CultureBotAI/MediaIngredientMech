The guarded campaign publisher cannot represent four row groups emitted by its pinned native generator. `row_projection()` creates a global `(subject_id, namespace)` dictionary for local registry rows and then requires that its length equal the full candidate row count. Two distinct object IDs in one local namespace overwrite each other in that dictionary, so it refuses before examining the selected row plan.

Actual read-only reproduction at MIM `7d4db26a2ce75e9942badaca954bb8e8f821c75c`, canonical3014 and exact W07 candidate3750 (`e99e5ea55c04d7b9d6e6b07feb603a556dc4785f4696553509aa0dd81ebc21de`), returns `Campaign publication: ambiguous native row slot`. The original canonical has no such duplicate slots. Three groups belong to selected source operations; the unchanged sodium-nitrate stock is outside scope but still trips the global assertion.

| Subject | Campaign scope | Native local object IDs |
|---|---|---|
| MIM:Desicatted_Ox-bile | selected | `kgmicrobe.ingredient:desiccated_ox_bile`; `kgmicrobe.ingredient:desicatted_ox-bile` |
| MIM:Na2so3_X_5_H2o | selected | `kgmicrobe.compound:sodium_sulfite_pentahydrate`; `kgmicrobe.compound:na2so3_x_5_h2o` |
| MIM:Sodium_Nitrate_070_M_Stock | unselected | `kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29`; `kgmicrobe.ingredient:sodium_nitrate_070_m_stock` |
| MIM:Trisodium_Citrate_X_3_H2o | selected | `kgmicrobe.compound:trisodium_citrate_trihydrate`; `kgmicrobe.compound:trisodium_citrate_x_3_h2o` |

This is deliberately supported by merged Claw PR683 (squash `d8f95e7e`), which resolved684/685 by preserving the curated registry primary and adding the lowercase B1 subject handle in the same namespace. The pinned76c generator descends from that squash; its actual sodium-nitrate and different-slug/mixed-case tests explicitly expect both local rows. Current MIM B1 requires the subject handle, while B2/B3 reject repeated subject/object claims and B5 prevents the opposing namespace for the same slug. Fresh unmodified native B1/B2/B3/B5 checks pass over all3750 rows. Removing each required handle fails B1; adding its opposite-namespace counterpart fails B5. These checks establish the mechanical contract, not scientific approval of new owner choices.

The bounded repair belongs to publication row identity/accounting: represent each distinct selected native row once, preserve every unselected canonical physical line, reject genuine duplicate pairs/positions, and retain complete old/new coverage, provenance restrictions, receipt replay and hold maps. Do not drop a generated row, invent a winner, change the generator or bypass other publication guards. A final actual-root candidate must still be generated after accepted source application; this diagnostic is not an application receipt.

The private packet binds complete row fields, authentic current and proposed owner hashes/identifiers/preferred names/mappings, live upstream issue/PR readbacks, pinned producer/test bytes, native negative controls and the actual refusal. Four separately observed new suppression obligations remain separate policy work.

Related implementation #1174 and PR #1205; this is distinct from the still-open #1256 live-transaction checks. Filed before correction. All-state GitHub search for the exact refusal returned no existing issue; #1174 remains the broader publication-contract tracker.

Evidence: `.temp/all-unmatched-20261107/preflight/final-publication-plan-construction-v1/slot-finding-v1/`; HANDOFF SHA256 `c259183db8c325d1fc98aa5a87f9ca7e1222b854b1e6518562ed1be03670c13c`, MANIFEST `2311ca53e5fedc52417c620d6dcc72ee93ca4648b486e37bafd1e92cfc0ba4eb`. Root verified all19 declared members before filing. No maintained source, native generator, canonical row, policy or receipt has been changed for this finding.
