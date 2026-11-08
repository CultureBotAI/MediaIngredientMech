Worker-02 continuation of #1201. These are isolated review proposals against the campaign's unchanged maintained owner bytes, not applied data changes. All artifact paths are repository relative. The published predecessor at `58f885fef05f8ff6e8b9b56fcb2479fef23b55c8` remains unchanged.

A bounded correction is proposed on the mapped Fe2(SO4)3 variable-hydrate owner. It does not resolve the separate UNMAPPED_0385 owner or the competing-label problem reported here.

The mapped owner's inherited `Fe(SO4)3 x n H2O` synonym omits the Fe coefficient required by the balanced ferric-sulfate formula. The exact composed successor changes that one token from RAW_TEXT to REJECTED_LABEL, retaining the original source. It also preserves the two published B source aliases and adds the two independently supported A variable-hydrate spellings. The local primary identity and NARROW_MATCH to the anhydrous parent CHEBI53438 remain; no fixed water number, monohydrate identity or anhydrous exact equivalence is asserted.

- Proposal `w02-v2-ferric-variable-composed`. Current campaign-baseline owner: `data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml` (SHA256 `5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447`).
- Exact proposed payload: `reports/all_unmatched_20261107/worker-02/continuation-1201-v1/integration/after/Fe2_So43_X_N_H2o.yaml` (SHA256 `ca1c64bdf0ab2178eb19f91ab46103783b39343787f5bdd151cb28f12b3fe20c`).
- Separate owner still requiring reconciliation: `data/ingredients/unmapped/FeSO43_X_N_H2O.yaml` (SHA256 `41b93858dfbb033525efacf2d146118d52325d5f9a4b67fa47ba6fd0b2bd3fe3`). It remains UNMAPPED_0385 and still contains the competing RAW_TEXT alias `Fe2(SO4)3 x n H2O`.

- `CM_NAME:00a3e88bd9a0cf52be00e83ae953c81b7d7b0cc5a4747298a072116a8c3259b9`; source `Fe2(SO4)3・nH2O`; raw source label `Fe2(SO4)3・nH2O`.
- `CM_NAME:08a5ede51cf7349256e39e613fcc764f54b0db496fc8d65b16c34c4f068af98d`; source `Fe2(SO4)3·nH2O`; raw source label `Fe2(SO4)3·nH2O`.
- `CM_NAME:aca0ced1cebaf48710115d1d1048003669aa170c8a2a2a147e70e0ef1b3941af`; source `Fe2(SO4)3·xH2O`; raw source label `Fe2(SO4)3·xH2O`.
- `CM_NAME:f213efe6bf2953d857acd5aee19a62908c8d525c7ad4f5ec418bfc91a9d00a01`; source `Fe2(SO4)3・xH2O`; raw source label `Fe2(SO4)3・xH2O`.

- `a-primary-primary-4ac0f41bc31f358e`: [https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1327](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1327); accessed `2026-11-08T05:06:57.157105+00:00`; `reports/all_unmatched_20261107/worker-02/a/captures/primary-4ac0f41bc31f358e.html` (SHA256 `4808c73af076ca543323747bd7e2d5b8e9a8067f572053dcf86e85785d2a69d7`).
- `a-primary-primary-84d6ae660e2442ec`: [https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=830](https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=830); accessed `2026-11-08T05:06:56.972834+00:00`; `reports/all_unmatched_20261107/worker-02/a/captures/primary-84d6ae660e2442ec.html` (SHA256 `c653a7368c6cd18992f92eff93e4aa288270b7417c1fd34a1a67ae65086a4cee`).
- `a-primary-togo-M1344`: [https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1344](https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1344); accessed `2026-11-08T05:06:52.055283+00:00`; `reports/all_unmatched_20261107/worker-02/a/captures/togo-M1344.json` (SHA256 `26e0d27bce9e3d8820ab43e4480ab85f711e844756cb1a3d4a8803e1f8f8bfa8`).

Independent reviewer `/root/research_c` approved these exact bounded payloads in `reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/independent-review-ferric-composition-v2.json` (SHA256 `b5e7e9d06a47c9b763c9c8cac348bf1b44594e5ab347dfdc63f6f5e940a6b8cd`). This is not a whole-owner, merge or publication approval.

Primary source support is bound in that review: NBRC830 and JCM1327 explicitly retain balanced variable-hydrate formulas. JCM1250-derived evidence is the frozen source plus TOGO M1344; the current JCM1250 page returns Nothing found and is not positive recipe evidence. The exact composition evidence and original proposal fragments remain preserved under `continuation-1201-v1/integration/`; correcting the mapped-owner typo cannot establish source identity or select a survivor for the separate placeholder.

The existing owner/name collision and any row-order-sensitive downstream routing in #873 therefore remain open. No new runtime rerun is claimed by this comment. Reconcile both current owners and their provenance before considering a merge or label-ownership change, and reassess exact downstream routing separately. Do not close #873 because the mapped owner's different malformed alias has been corrected in a proposal.

Before applying any accepted delta, compare the then-current owner bytes and reconcile concurrent proposals. Preserve every raw label, original source reference, existing REJECTED_LABEL, WITHHOLD, source-quantity and downstream hold. Use guarded curation with history and the required maintained-surface/SSSOM synchronization and native validation. This draft requests no merge, downstream rebuild, automatic owner release or closure of broader issues.

<!-- mim-review-round: worker02-continuation1201-v1 -->
<!-- mim-review-bundle: comment-873-ferric-alias -->
<!-- mim-fingerprints: d0dbe3eff9c6533e83e48968762f68e174cbc49d9b405d4bcd4723c0125cc65c -->
