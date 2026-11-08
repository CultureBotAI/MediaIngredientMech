# RIFAMYCIN-PACKAGE-META-001

Minor metadata attribution ambiguity, not a candidate/science defect.

The new wrapper calls 2026-11-08T14:25:17Z the time of the coordinator publication readback. The exact saved GitHub JSON contains this as created_at/updated_at; it does not contain a retrieval timestamp. The separate publication receipt records at=2026-11-08T14:25:17.739189+00:00 without a distinct readback acquisition timestamp. The issue creation time is therefore being presented ambiguously as a readback time.

Clarify that 14:25:17Z is the issue created_at; identify the exact publication receipt time separately and state that the precise readback acquisition time was not separately retained. Preserve every archived input byte and the initial wrapper/hash; apply only an explicitly versioned metadata correction and derived case-hash joins.
