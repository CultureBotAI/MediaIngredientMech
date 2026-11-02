# Step 7c source and mapping corrections

Approved-plan base: `54eadef802d2ff159bf4ba9bec51492fe3bb99d4`. This batch covers #751, #313 and the bounded alias part of #235. The broader corrected-catalogue ingestion and salt/CAS review on #235 remain open. No unified snapshot, provenance sidecar, evidence workflow or vendored pin change belongs to this batch.

- WC Trace Elements Solution receives a distinct local ingredient identity and a broader mapping to the generic MicrO class; source-label routing is exact. The provisional role and missing component assessment are not approved.
- Five comma-split fragments become rejected provenance on butanediol and the O/129 phosphate record. Existing identities and counts remain unchanged.
- The mono-keto gluconate rejects the di-keto fragment. The recovered original source supports a separate CHEBI:11449 record with two production-field occurrences; the mono-keto count remains 288. The damaged raw label resolves only to the recovered di-keto owner. These field counts do not assert positive biological production or recipe use.
- Phenethylamine retains the previously chosen free-base identity and chemistry. Its hydrochloride alias becomes rejected provenance; creating a salt record from the corrected catalogue is a separate decision on #235.

Primary sources, retrieval hashes, exact preimages and issue decisions are in `../step7c_source_labels_313_235_20261102/` and `../step7c_wc_stock_751_20261102/`. Guarded source writers preserve history and reserve receipts before changing data. The first source phase was verified before the WC phase; its all-owner input census is historical after the WC change. Later replay must reconstruct that explicitly bounded earlier input, rather than claim both receipts describe the same live census.

The maintained policy manifest `mappings/ingredient_mappings.sssom.tsv.manifest.json`, suppression sidecar and Rule K baseline are preserved as historical policy evidence through receipt 23. Their old artifact and owner hashes are not claims about the new generation. The new native mapping receipt and this batch's generation/projection evidence bind the Step 7c endpoint. No changed or added row inherits scientific approval from a prior row or from structural validation.

Generation and final validation evidence will be added after applying the guarded source corrections. The producer is the isolated Claw copy at `3022b8738dcc9e01c7464a8d5c95aa9be2eef141`; the repository's validator pin remains unchanged. CultureMech and Mediadive outputs are comparison inputs, not bulk-import authority.

Independent pre-review found #1111: the two BacDive result cells contain explicit negative-production icons. Text extraction had lost their attributes and incorrectly described the cells as blank. The original source phase, creation history and archived captures remain immutable historical evidence. The corrective phase changes the active evidence note and appends a superseding event; counts, identity and roles do not change. Candidate v1 is retained as diagnostic-only and will not be promoted. A new input checkpoint and generation are required after the correction.
