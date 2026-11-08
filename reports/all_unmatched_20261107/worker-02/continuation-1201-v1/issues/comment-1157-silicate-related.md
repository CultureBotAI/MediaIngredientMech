Worker-02 continuation of #1201. These are isolated review proposals against the campaign's unchanged maintained owner bytes, not applied data changes. All artifact paths are repository relative. The published predecessor at `58f885fef05f8ff6e8b9b56fcb2479fef23b55c8` remains unchanged.

Additional bounded sodium-silicate owner finding; the MediaDive2160 pentahydrate/21.2 g/L stock hold in this issue remains unchanged.

The current Na-silicate owner types five source terms as EXACT_SYNONYM: `(5)  Sodium metasilicate`, `Sodium polysilicate`, `Sodium sesquisilicate`, `Sodium silicate glass`, and `Sodium siliconate`. In the inspected official ChEBI60720 response, each underlying term is explicitly `hasRelatedSynonym`. Flattening the ontology's synonym list lost that scope. The proposed v2 payload retains all five exact source strings and their kg_microbe provenance as REJECTED_LABEL. `disodium oxosilanediolate` also has an independent `hasExactSynonym` IUPAC assertion; it is not rejected merely because it additionally occurs with a related assertion.

- Proposal `c2-proposal-silicate-related-aliases`. Current campaign-baseline owner: `data/ingredients/mapped/Na-silicate.yaml` (SHA256 `5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2`).
- Exact proposed payload: `reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/proposed-owners/c2-proposal-silicate-related-aliases-v2.yaml` (SHA256 `46b1f79efe1001b6d413d00db7526bc90014767caabd8914dc5abd000784fff7`).

- `KG_CASE:b8e3bb79e349ae85ae0f77729aad4f1258693e3bfd1134f0eb13f05bdf6c4f17`; source `mediadive.ingredient:1596`; raw source label `Na silicate`.
- `KG_CASE:cb6c02faf6843214dc54dcd15660523b93f83e57866a0075a9a0f496a67c1a66`; source `mediadive.ingredient:524`; raw source label `Na-silicate`.

- `c-chebi-60720`: [https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:60720](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:60720); accessed `2026-11-08T05:07:43.149489+00:00`; `reports/all_unmatched_20261107/worker-02/c/captures/chebi-60720.json` (SHA256 `af98e31155fe0ceb595b99073f0628a006f1c9bbaa03d9359a42cf31053136cf`).
- `c2-ols-sodium-silicate`: [https://www.ebi.ac.uk/ols4/api/search?q=sodium+silicate&rows=100&ontology=chebi%2Cncit%2Cfoodon%2Cmesh%2Cenvo%2Cmicro%2Cbto%2Cuberon](https://www.ebi.ac.uk/ols4/api/search?q=sodium+silicate&rows=100&ontology=chebi%2Cncit%2Cfoodon%2Cmesh%2Cenvo%2Cmicro%2Cbto%2Cuberon); accessed `2026-11-08T05:55:51.573402+00:00`; `reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/captures/ols-sodium-silicate.json` (SHA256 `6c1219f1f5ac92a48fe4085bcbe7244686708b52160d2d21fb775f84e4f592e2`).

Independent reviewer `/root/research_a` approved these exact bounded payloads in `reports/all_unmatched_20261107/worker-02/continuation-1201-v1/a/review-c/independent-review.json` (SHA256 `37577be2e1881e5e32fb430f68ffd15a7dedc86994b135c9bd5764f3b3116a71`). This is not a whole-owner, merge or publication approval.

The two worker02 source entries remain source-bound: MediaDive1596/DSMZ1753 and MediaDive524/DSMZ511 do not establish modulus, hydration, vendor or an exact formulation. This correction therefore does not assign either generic source to a fixed unstated silicate form. It also does not resolve MediaDive2160, resurrect the rejected pentahydrate alias or approve worker03's separate hydrate/stock proposal. Preserve the existing numbered-source-artifact and full-owner release holds. No other row in #1157 is assessed or closed by this comment.

Before applying any accepted delta, compare the then-current owner bytes and reconcile concurrent proposals. Preserve every raw label, original source reference, existing REJECTED_LABEL, WITHHOLD, source-quantity and downstream hold. Use guarded curation with history and the required maintained-surface/SSSOM synchronization and native validation. This draft requests no merge, downstream rebuild, automatic owner release or closure of broader issues.

<!-- mim-review-round: worker02-continuation1201-v1 -->
<!-- mim-review-bundle: comment-1157-silicate-related -->
<!-- mim-fingerprints: 84b290bb367b2ab1d89c683c65ae0b6e3a63700a11802b184243ecfb951401cc -->
