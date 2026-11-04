# Native Rule B4 with real read-only transforms

**Result: zero current or baseline mismatches; no new/existing/resolved mismatches.** This is native label validation, not fresh scientific approval. Only the imported validator’s `KGM_TRANSFORMS_DIR` was rebound externally. Native code equals baseline467aa319 exactly, SHA `3ae75d54a76b7b99a5018c4f8b0582f6a1563b35e43a8c29c1a3a88d7b592303`. No checkout, rule, test, symlink, download or maintained file was changed.

Authoritative run: `rerun-v2/summary.json`, at Step 7d head `7d35035f6c521c69fad94f73381c6a6eb7251fff`. Current canonical SHA `cd7775a22114ea2d5dd324a532e4cc0d1f335504cd3cfe8c4efe93961cc148e4`; baseline SHA `62fd37c2ed8ace9b9295618d44e251d11fc35feb711053b66d322e5a7bce14f1`. Full source snapshots and empty native reject tables are retained.

| Scope | Rows | Canonical-label pass | Outside B4 prefixes | Missing-transform skips | Mismatches |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline467aa319 | 2,985 | 2,052 | 859 | 74 | 0 |
| Current | 3,014 | 2,050 | 890 | 74 | 0 |
| Current 38 selected owners | 105 | 36 | 69 | 0 | 0 |

The missing exact transform paths are `micro_nodes.tsv` (73 current rows) and `bto_nodes.tsv` (1 current row). These existence checks use filesystem paths directly and include gitignored files. CHEBI, ENVO, FOODON, PATO and UBERON transforms exist and their SHA256, sizes and mtimes are unchanged before/after. There are no term-absent or empty-label skips in either checked canonical file.

All 36 selected CHEBI target rows match their transform canonical labels exactly. D-Maltose_Monohydrate and Sodium_Carbonate_Monohydrate now use NCIT primary identities, which native B4 does not check. CAS/local registry rows are also outside its prefix scope; these 69 rows must not be reported as B4 label passes. All 38 selected owners have explicit per-row coverage in `rerun-v2/selected-38-owner-coverage.json`.

KG checkout: `d6baf5b90003a2032747559d94c00f86a7a4c615` on ``. Its pre-existing untracked entries are saved verbatim in `kg-before.json` and `kg-after.json`; both files are byte-identical. No KG modifications or provider calls occurred. Canonical bytes and scientific B4 cells remained unchanged during the run. `postrun-state.json` separately confirms that MIM head, actual short status and canonical hash still equal the version-2 start observation.

Version 1 is preserved. Its B4 results were valid, but its `current_status_at_start` metadata field was accidentally overwritten by a coverage loop variable. Version 2 fixes only the external harness metadata and adds explicit baseline/selected coverage counts; it reruns the same native check and reproduces zero mismatches. Use the version-2 summary, not that version-1 status field. Both logs and all captures remain available.

The parent’s pending #1122 comment-only corrections will change the full canonical hash. This report binds the exact current hash above. A final-head claim must rebind/check the new hash and compare B4-relevant fields or rerun this read-only check; do not silently relabel this capture as the later head.

| Selected owner | Native current-row coverage |
| --- | --- |
| `2-Deoxyadenosine_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `4-Hydroxymandelic_Acid_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `5-Fluoroorotic_Acid_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Cadmium_Acetate_Dihydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Cecl3_X_7_H2o.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Cefsulodin_Sodium_Salt_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 1, PASS_CANONICAL: 1 |
| `Chlorhexidine_Diacetate_Salt_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 1, PASS_CANONICAL: 1 |
| `Cocl2_X_2_H2o.yaml` | OUT_OF_B4_PREFIX_SCOPE: 1, PASS_CANONICAL: 1 |
| `Cu_No32_X_3_H2o.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `D-Fructose_6-phosphate_Disodium_Salt_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `D-Galacturonic_Acid_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `D-Glucuronic_Acid_Sodium_Salt_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `D-Maltose_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 1 |
| `D-_-melezitose_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `DL-Glycerol_1-phosphate_Sodium_Salt_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `EDTA_Tetrasodium_Tetrahydrate_Salt.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Galactose_1-phosphate_Dipotassium_Salt_Pentahydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Gly-Gln_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `L-Cysteic_Acid_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `L-Rhamnose_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Lithium_Chloride_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Magnesium_Nitrate_Hexahydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Maltose_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 1, PASS_CANONICAL: 1 |
| `Maltotriose_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Nicl2_X_2_H2o.yaml` | OUT_OF_B4_PREFIX_SCOPE: 1, PASS_CANONICAL: 1 |
| `Palatinose_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Potassium_Citramalate_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Potassium_Tellurate_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Sodium_Carbonate_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 1 |
| `Sodium_Cholate_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Sodium_Deoxycholate_Monohydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Sodium_Phosphite_Dibasic_Pentahydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Sodium_Thiophosphate_Tribasic_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
| `Stachyose_Hydrate.yaml` | OUT_OF_B4_PREFIX_SCOPE: 2, PASS_CANONICAL: 1 |
