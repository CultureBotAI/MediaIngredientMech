# Step7d science-a: author review of all22 assigned owners

Current source base: `467aa319a06ef992035f509f66fe251082b44ae1`. This is a full owner-field review and a proposed data transaction, not an independent release approval. 11 INCLUDE; 11 DROP. No maintained files, Git refs or GitHub objects were changed.

Every owner has identity, ontology, synonym, supplied-form, component, chemistry, role, occurrence, context, evidence, history and synchronized-surface assessments in decisions.json. All active fields are carried into that assessment; absent domains are explicit and are not presented as validated completeness.

The YAML grade NARROW_MATCH exports **skos:broadMatch** to the ontology parent under #390. Own identifiers remain exact; B1 local identities come only from the supported producer. No new exact ontology term was selected by this partition; finite CAS/name searches and their limits are preserved.

| # | Owner | Decision | Principal reason |
|---|---|---|---|
|1|2-Deoxyadenosine_Monohydrate|INCLUDE|The historical D7400 monohydrate and fresh supplier deposit/PubChem CAS16373-93-6 agree. Keep this own CAS distinct from the separate CHEBI17256 parent owner.|
|2|2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate|INCLUDE|CAS1040352-40-6 and K6250 source name agree on hemicalcium salt hydrate with unspecified xH2O. Keep distinct from the separately curated monohydrate/MPBio owner.|
|3|4-Hydroxymandelic_Acid_Monohydrate|INCLUDE|Historical168327 and current supplier/PubChem agree on CAS184901-84-6 monohydrate, not the water-free parent.|
|4|5-Fluoroorotic_Acid_Hydrate|INCLUDE|Historical/current F5013 support a distinct hydrate CAS207291-81-4; water count is unspecified. Preserve own CAS, do not rename it monohydrate.|
|5|A-Ketoglutaric_Acid_Disodium_Salt_Hydrate|DROP|K3752 source names disodium salt xH2O but current primary CAS305-72-6 also identifies the water-free representation. This review does not settle whether the existing CAS owner or a distinct local supplied-hydrate owner is the correct material boundary.|
|6|Adenine_Hydrochloride_Hydrate|DROP|A8751 denotes hydrochloride xH2O, but primary CAS2922-28-3/PubChem76219 is water-free hydrochloride. Do not decide a new local-vs-CAS owner boundary by inference.|
|7|Bathophenanthrolinedisulfonic_Acid_Disodium_Salt_Hydrate|DROP|Actual historical catalogue146617 is a trihydrate, but apparent exact CHEBI234116 has phenanthroline3,8-disulfonate structure, whereas current CHEBI78157 is phenyl4′,4″-disulfonate. Label agreement cannot resolve this positional boundary.|
|8|Beta-Glycerophosphate_Disodium_Salt_Hydrate|INCLUDE|CAS154804-51-0 denotes beta/2-glycerophosphate disodium hydrate in the inspected supplier comparator and historical source label. Preserve this hydrate owner separately from CHEBI132089 sodium beta-glycerophosphate and the distinct fixed-water sibling.|
|9|Cacl2_X_7_H2o|DROP|Raw MediaDive479 genuinely names CaCl2 x7H2O, but its CAS/formula/mass are dry-parent metadata. The physical/source form remains unresolved; do not silently choose dihydrate, hexahydrate or anhydrous.|
|10|Cadmium_Acetate_Dihydrate|INCLUDE|Source CAS5743-04-4 plus supplier/PubChem confirms cadmium acetate dihydrate; keep own CAS distinct from CHEBI232796 dry parent.|
|11|Caso4_X_7_H2o|DROP|Raw MediaDive2000 names seven-water calcium sulfate but uses dry-parent metadata. Computed PubChemCID140700884 does not settle intended source or physical form.|
|12|Cecl3_X_7_H2o|INCLUDE|Four current source recipes and MediaDive1444 name CeCl3·7H2O. Independent supplier/PubChem agree on specific CAS18618-55-8 and formula. The complete ignored-inclusive neighbor scan found no other current owner of this CAS.|
|13|Cefsulodin_Sodium_Salt_Hydrate|INCLUDE|Historical C8145 and current supplier describe the same source-defined cefsulodin sodium salt hydrate xH2O. Retain local hydrate identity; CAS52152-93-9 resolves to the water-free salt and is not selected as exact hydrate primary.|
|14|Ceftazidime_Hydrate|DROP|Actual historical product C3809 contains stabilized ceftazidime hydrate with sodium carbonate. Evidence does not settle whether this owner denotes active hydrate or whole stabilized preparation. Drop the entire owner from this transaction.|
|15|Chlorhexidine_Diacetate_Salt_Hydrate|INCLUDE|Historical C6143 and current supplier explicitly identify chlorhexidine diacetate salt hydrate, current formula xH2O. This settles the source-defined variable hydrate, not a fixed monohydrate. Retain its local identity distinct from water-free CHEBI81711.|
|16|Cocl2_X_2_H2o|INCLUDE|MediaDive578 and five current source recipes name CoCl2·2H2O; publisher-deposited primary abstract reports single-crystal CoCl2·2H2O. Retain the local two-water identity, without selecting an unverified CAS lead.|
|17|Cocl2_X_4_H2o|DROP|MediaDive626/current recipes name CoCl2·4H2O and PubChem has a computed representation. A publisher-indexed crystallographic abstract is a promising lead, but direct primary article access failed during this bounded review. Do not claim complete primary verification.|
|18|CrKSO42_X_12_H2O|DROP|CAS7788-99-0/PubChem supports potassium chromium sulfate dodecahydrate. The whole double salt is not simply chromium(III) sulfate hydrate: potassium and sulfate stoichiometry differ from current parent CHEBI53471.|
|19|Cu_No32_X_3_H2o|INCLUDE|Historical source, current formula and independent GSRS/PubChem agree on copper(II) nitrate trihydrate CAS10031-43-3. The ignored-inclusive owner scan found no other current owner of this CAS.|
|20|Cucl2_X_6_H2o|DROP|MediaDive1056 and current recipes preserve CuCl2·6H2O wording while raw metadata describe water-free CuCl2. The intended supplied substance remains unresolved.|
|21|Cuso4_X_2_H2o|DROP|MediaDive719 and eight current recipe labels name CuSO4·2H2O but raw metadata use dry salt. Source-specific hydrate identity is not settled.|
|22|Cuso4_X_4_H2o|DROP|MediaDive1456 and two current recipe labels name CuSO4·4H2O but raw metadata use dry salt. Source-specific hydrate identity remains unresolved.|

## Bounded changes requiring issue-first guarded application

-11 proposed CLOSE_MATCH→NARROW_MATCH grade changes, producing broadMatch parent rows; β-glycerophosphate parent additionally changes CHEBI17270→132089 because the disodium salt is closer.
-Two proposed CAS primaries: cerium chloride heptahydrate18618-55-8 and copper nitrate trihydrate10031-43-3. Retain their existing local registry identities; no owner merge, extra owner or guessed hydrate.
-Withdraw four fixed-water structure fields each for generic F5013 and β-glycerophosphate hydrate, and three water-free structure fields for cadmium acetate dihydrate. Cadmium's correct dihydrate formula and all source history remain.
-For C8145 and C6143, keep the settled source-defined local hydrate; move procurement CAS out of substance chemistry to supplied_form. C6143 explicitly preserves historical56-95-1 versus current206986-79-0 without selecting an exact CAS identity. If independent review finds the material boundary unresolved, DROP that whole owner, not a partial cleanup.
-Parent-only exact synonym findings are listed separately with **no alias operations**. Root must exclude all deferred #669 pairs; this review does not authorize those later suppressions.

## Holds and limitations

Ceftazidime C3809 remains DROP: preferred default is an active-hydrate owner plus stabilized procurement form, but the whole-product/source-boundary decision is unresolved. Bathophenanthroline has a genuine exact-term positional-structure conflict. Cobalt tetrahydrate has a primary-access verification gap; no claim of impossibility. Ca/Cu unusual hydrate labels retain source-decision holds. The potassium chromium double salt needs a whole-substance parent decision. Adenine HCl and alpha-ketoglutarate CAS/hydrate boundaries remain unresolved and receive no partial cleanup.

All role hypotheses and native WITHHOLDs persist. There are three inherited SUPPORTED rows in this partition's44 current assertions; changed owner bytes are not permission to carry those approvals. Unchanged dropped owners retain the current exact claims without new approval.

Native current-input checks completed: strict validation22files/0errors, and all22 individual validate-terms commands exit0. These validate shape and stored ontology labels; they do not validate the proposed edits or replace independent scientific review. No fullsuite or generator was run by this partition.

Evidence-index.json binds primary capture URLs, paths, SHA256, timestamp basis and claim locators. Historical CultureBotHT catalogue is an explicitly untracked capture, not falsely bound to a Git blob. Source-occurrence comparison retains actual current CultureMech revision/hash and full matched recipes; it does not rewrite maintained counts. Failed requests, search-only leads and old reviews remain preserved and qualified.

No additional research is required to hand off these bounded proposals; dropped owners require the explicit follow-ups recorded per owner. Parent owns live issue dedup/update, combined native67 review, guarded writers, synchronized products and final independent review.
