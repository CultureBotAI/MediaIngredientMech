Independent technical lane for provisional archive selection v3.

All 1,016 current plus 1,539 prior references pass. The old 691 entries retain exact JSON types, order and values. The 325-entry delta adds 217 proposed files (10,948,146 bytes), giving 655 proposed files (25,737,294 bytes); all three proposed directories remain absent. The 1,077 actual prior copies and 310 legacy archive files remain exact.

Twelve complete portable manifests cover 596 members. The first verifier incorrectly joined a copied manifest to a neighboring outer handoff. Its failure was preserved and filed in #1254 comment6722465798 before correction. The immutable successor verifies explicit upstream/copy byte equality before selecting the member base. Distinct D post-filing review independently checked the real collision and refusals.

34 delta controls and nine new origin controls pass. No archived operator or mutable full-run result was executed or accepted. Source-code correctness, science, application and final-head approval remain outside this review.
