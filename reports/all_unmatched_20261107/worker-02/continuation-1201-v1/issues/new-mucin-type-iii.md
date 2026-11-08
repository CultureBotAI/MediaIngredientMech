Worker-02 continuation of #1201. These are isolated review proposals against the campaign's unchanged maintained owner bytes, not applied data changes. All artifact paths are repository relative. The published predecessor at `58f885fef05f8ff6e8b9b56fcb2479fef23b55c8` remains unchanged.

The Type III porcine-stomach mucin owner is classified `SINGLE_INGREDIENT` because an automatic rule treated a CAS primary as a defined chemical. Its own curation history records that rule. The primary material evidence supports a partially purified biological preparation, so the isolated proposal changes `ingredient_type` to `UNDEFINED_MIXTURE` and appends the evidence/history.

DSMZ 1580 specifies 2 g of Type III porcine-stomach mucin. Sigma's M1778 documentation independently describes this named type as partially purified powder with a range of bound sialic acid. This supports the material classification without establishing that the DSMZ recipe purchased Sigma M1778. The supplier, complete composition, Type II/Type III shared-CAS relationship and grade identity remain unasserted or held. The CAS, preferred name, original aliases and occurrence statistics are preserved.

- Proposal `c2-proposal-mucin-type-iii-material`. Current campaign-baseline owner: `data/ingredients/mapped/Mucin_From_Porcine_Stomach_Type_III.yaml` (SHA256 `858d6f80087acfd16f225cb2f20bb60c6573594a53f79691bb5fc3e4b319a440`).
- Exact proposed payload: `reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/proposed-owners/c2-proposal-mucin-type-iii-material.yaml` (SHA256 `0bdb3709c3791ab4e5031a1b63b8bfe599a8737833de718fa5378b579d1e965c`).

- `KG_CASE:71286bc360cc71389bb0470c1f95ffb80dd5e44c71f6fbc6f5fb4ac7fda67aff`; source `mediadive.ingredient:1433`; raw source label `Mucin from porcine stomach Type III`.

- `c2-dsmz-1580`: [https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1580.pdf](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1580.pdf); accessed `2026-11-08T05:55:52.265085+00:00`; `reports/all_unmatched_20261107/worker-02/continuation-1201-v1/c/captures/dsmz-1580.pdf` (SHA256 `66b5b51686017f2cc5def1a87553ca6bddbcf9e2390f079c14c5a704ff01344a`).
- `c-sigma-mucin`: [https://www.sigmaaldrich.com/DM/en/product/sigma/m1778](https://www.sigmaaldrich.com/DM/en/product/sigma/m1778); accessed `2026-11-08T05:09:34.465Z`; `reports/all_unmatched_20261107/worker-02/c/captures/sigma-mucin.json` (SHA256 `dd57bb25c9d8f7e2f1fcd3b6eb470525e6d5728e1d02c5a9966fc7b513094f00`).

Independent reviewer `/root/research_a` approved these exact bounded payloads in `reports/all_unmatched_20261107/worker-02/continuation-1201-v1/a/review-c/independent-review.json` (SHA256 `37577be2e1881e5e32fb430f68ffd15a7dedc86994b135c9bd5764f3b3116a71`). This is not a whole-owner, merge or publication approval.

The inherited full-row hold about the bound-sialic-acid source text in the synonym channel is retained. Classification repair alone does not approve that alias or the owner for export. #478 is the broader ingredient-type schema-axis discussion; this is a concrete material misclassification that can be corrected within the current schema, without claiming that the schema discussion is resolved.

Before applying any accepted delta, compare the then-current owner bytes and reconcile concurrent proposals. Preserve every raw label, original source reference, existing REJECTED_LABEL, WITHHOLD, source-quantity and downstream hold. Use guarded curation with history and the required maintained-surface/SSSOM synchronization and native validation. This draft requests no merge, downstream rebuild, automatic owner release or closure of broader issues.

<!-- mim-review-round: worker02-continuation1201-v1 -->
<!-- mim-review-bundle: new-mucin-type-iii -->
<!-- mim-fingerprints: 61941af4e226873e412ddd6fe68a46057a30ff36329f14672e2b9e4e07706787 -->
