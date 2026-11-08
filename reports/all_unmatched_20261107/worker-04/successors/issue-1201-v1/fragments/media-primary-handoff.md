# Worker04 media successor handoff

All 26 assigned cases reassessed. Final fragments contain 30 full decisions (including 65/92/89/123 superseding bindings), 18 isolated proposals and 77 new evidence records. All eight retained holds name source facts rather than unperformed curation work. Independent scientific review is complete and accepted within narrow scope; final metadata correction is bound by `independent-review/media-reviewed-by-chemistry-v4.json`, SHA256 `9bbef7521a60cd955e2f36bf3089fd946ebba7865408ef33d2252bd81c273a32`. Whole-owner/export holds persist.

The coordinator's initial whole-shard audit failed because 27 evidence rows used an unsupported kind. That failed attempt is retained under `validation/attempt-1`. The correction changes only 26 local lookup rows to `local_validation` and one frozen cross-shard case/owner capture to `source_snapshot`; every other evidence field, capture byte, URL and original access time is unchanged. All decisions and payloads are byte-identical to the prior scientific review. See `captures/media/evidence-kind-correction-v3.json`.

Narrow author validation passed: native closed schema, component partonomy against baseline plus active predecessor/successor proposals, allowed evidence kinds, unique evidence IDs, all new capture hashes, evidence/proposal backlinks, identifier collisions and original e000 owner hashes. This is not a claim that the coordinator's whole-shard rerun passed. No maintained data, role, hold, global alias, SSSOM, GitHub or downstream mutation was made. A fresh predecessor check verified all 974 published files and maintained inputs unchanged.

Final author integrity receipt: `captures/media/integrity-v3.json`. Prior reviewed fragments and payloads are preserved under `superseded/media-v1/` and `superseded/media-v2/`; prior review receipts remain available and must not be treated as approvals of revised evidence bytes.

Final fragment SHA256:

- `media-reassessments.json`: `563be8ab85620d8299d224ce5004c3bab7d521851fee0d55f6f5f8fca4484828`
- `media-decisions.json`: `9f294f8c36103c6190830b37ac4c56296a675b68ba8cc46e5fcf59cff68ba77f`
- `media-evidence.json`: `a94f7ad683f6c03dd1f9eb5188424c2775a355417e96c051a84f9979bbc85fc3`
- `media-proposals.json`: `22de1b6b3ba5765121b3710c260e913a77168ad9b6be43ee6446b11c3fdb52c5`

Final scientific holds:

- Case0: Identify the actual M2964 product or preparation and establish whether it is historicalGibco042-1545, a different supplied concentrate, or a locally glutamine-supplemented preparation. This comparison fact is required to avoid a duplicate or broader overlapping owner.
- Case7: Identify the actual Columbia basal product/formulation for each of M2508,M2836,M2189, or demonstrate they share the same base; no full-formula requirement is imposed once a specific product is known.
- Case57: The specific Difco agar grade used by DSMZ1144 is unstated; recover a catalog, grade label or contemporaneous source clarification before binding to Bacto or Noble.
- Case96: The source leaves the selected purified agar and its purification/grade criteria unspecified; OxoidL28 is an example, not proof of the actual chosen product. No owner-creation task is treated as missing evidence.
- Case111: The particular prepared basal Bordet-Gengou product/formulation in TOGOM2850 is unknown; source evidence must identify it before equating it to the Difco438 preparation or dry product.
- Case113: Upstream repair must reconstruct the complete biphasic MR_MErds_MY75S recipe with separate phases/stocks and faithful quantities, not merely delete the bad token. Existing issue1192/source review remains applicable.
- Case121: Obtain ATCC/source-owner clarification of whether Noble grade or BD214050 Bacto product was intended. Neither catalog nor label is selected as a winner.
- Case176: Recover an occurrence-level source recipe/vendor for this pooled KG row, or split its supplier-specific assertions upstream. Existing generic Corn_Meal_Agar also pools these suppliers and cannot be narrowed to one from this record.

Cross-shard dependency: exact frozen shard07 case170 `KG_CASE:87a3023cb2b6523988122d33d722774edb88942f02c97e21dd816a7954a0e850`, source `mediadive.ingredient:1680`, already imports historicalGibco042-1545 into `data/ingredients/unmapped/CMRL_1066.yaml`. The successor now edits that existing owner using original SHA256 `5ec81ababe3130834fa8e46faebf4b4c321bbbbb65e340685e5e597dbe2342b0`; coordinator must reconcile worker07 and all catalog aliases, with one active owner payload and no last-writer-wins. See `captures/media/w07-cmrl-owner-dependency.json` and exhaustive frozen-owner-path scan `captures/media/cross-shard-dependencies.json`. No worker07 payload was adopted.

Important boundaries: Bacto84 has exact three-unwashed/one-washed occurrence bindings; Noble8 joins89/123 while121 remains conflicted; NBRC1096 is explicitly a named recipe family with invariant partial components and unselected seawater/agar branches; CMRL0 is held to avoid an overlapping new owner; MH prepared-medium identity is separate from its frozen dose-unit error.

Proposal inventory:

- `I1201-MEDIA-P-gibco_042_1545_cmrl_1066`: edit_existing_owner; `data/ingredients/unmapped/CMRL_1066.yaml`
- `I1201-MEDIA-P-jcm_1305_skirrow_supplement_stock`: new_owner; `data/ingredients/mapped/JCM_1305_Skirrow_Supplement_Stock.yaml`
- `I1201-MEDIA-P-oxoid_wilkins_chalgren_agar_plates`: new_owner; `data/ingredients/mapped/Oxoid_Wilkins_Chalgren_Agar_Plates.yaml`
- `I1201-MEDIA-P-bd_bbl_columbia_agar_5pct_sheep_blood`: new_owner; `data/ingredients/mapped/BD_BBL_Columbia_Agar_5pct_Sheep_Blood.yaml`
- `I1201-MEDIA-P-bd_difco_noble_agar`: new_owner; `data/ingredients/mapped/BD_Difco_Noble_Agar.yaml` (supersedes media-followup-bd_difco_noble_agar)
- `I1201-MEDIA-P-bd_difco_bacto_agar`: new_owner; `data/ingredients/mapped/BD_Difco_Bacto_Agar.yaml` (supersedes media-product-bd_difco_bacto_agar)
- `I1201-MEDIA-P-p1_washed_bacto_agar`: new_owner; `data/ingredients/mapped/P1_Washed_Bacto_Agar.yaml`
- `I1201-MEDIA-P-chocolate_agar`: edit_existing_owner; `data/ingredients/mapped/Chocolate_agar.yaml`
- `I1201-MEDIA-P-agarose`: edit_existing_owner; `data/ingredients/mapped/Agarose.yaml`
- `I1201-MEDIA-P-nbrc_1096_one_fifth_marine_preparation`: new_owner; `data/ingredients/mapped/NBRC_1096_One_Fifth_Marine_Preparation.yaml`
- `I1201-MEDIA-P-togo_m2942_mueller_hinton_agar`: new_owner; `data/ingredients/mapped/TOGO_M2942_Mueller_Hinton_Agar.yaml`
- `I1201-MEDIA-P-jcm_13_bl_agar`: edit_existing_owner; `data/ingredients/unmapped/BL_Agar.yaml`
- `I1201-MEDIA-P-jcm_26_r_agar`: edit_existing_owner; `data/ingredients/unmapped/R_Agar.yaml`
- `I1201-MEDIA-P-jcm_50_isp3_oatmeal_agar`: new_owner; `data/ingredients/mapped/JCM_50_ISP3_Oatmeal_Agar.yaml`
- `I1201-MEDIA-P-bd_difco_bcye_agar_base_jcm119`: new_owner; `data/ingredients/mapped/BD_Difco_BCYE_Agar_Base_JCM119.yaml`
- `I1201-MEDIA-P-dichloran_glycerol_agar_base`: edit_existing_owner; `data/ingredients/unmapped/Dichloran-Glycerol-agar_Base.yaml`
- `I1201-MEDIA-P-dsmz_438_difco_bordet_gengou_prepared_base`: edit_existing_owner; `data/ingredients/unmapped/Bordet-Gengou-Agar-Base.yaml`
- `I1201-MEDIA-P-dsmz_585_oxoid_cye_bcye_preparation`: edit_existing_owner; `data/ingredients/unmapped/OXOID_Legionella_CYE-Agar_Base.yaml`
