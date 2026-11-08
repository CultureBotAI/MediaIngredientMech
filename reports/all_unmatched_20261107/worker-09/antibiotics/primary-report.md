# Worker09 antibiotic primary source review

Authored by in-process subagent `/root/antibiotics`. Primary scope: 58 frozen source cases, 38 distinct source names, all 38 existing owner payloads. This is a research/proposal supplement; the coordinator owns the native structured review and final full-shard audit. Independent skepticism is pending and must be separately authored.

The complete source objects, owner bytes and native row decisions were read. The graph only exposes provider, source node fields and incident-edge counts. It does not expose the underlying strain/recipe observations; `occurrence_ids: []` retains that representation without claiming no observations. The separate metatraits and metatraits_gtdb cases remain individually accounted, and their equal names do not establish independent observations.

Outcomes: {'existing_identity_or_alias': 31, 'broad_parent_relation_only': 5, 'unresolved': 12, 'stock_product_mixture_context': 10}. There are seven exact after-payload proposals; no maintained record or publication surface was edited.

| Proposal | Intended action |
|---|---|
| ab-proposal-collinomycin | Promote existing distinct source owner to CHEBI:220350 alpha-Rubromycin. |
| ab-proposal-aburamycin-a | Promote existing distinct source owner to CHEBI:202873 Chromomycin A2. |
| ab-proposal-cinerubin-a | Promote existing distinct source owner to mesh:C000481 cinerubine A. |
| ab-proposal-angustmycin | Propose curator-selected Step5 AMBIGUOUS disposition for bare Angustmycin; no mapping row. Withdraw false A=C evidence and C-derived chemistry from active assertion fields, preserve all history/raw synonym provenance. |
| ab-proposal-glebomycin | Enrich existing mapping with independent chemical synonym evidence and correct quality to SYNONYM_MATCH. |
| ab-proposal-hitachimycin | Enrich existing mapping with independent chemical synonym evidence and correct quality to SYNONYM_MATCH. |
| ab-proposal-vulgamycin | Enrich existing mapping with independent chemical synonym evidence and correct quality to SYNONYM_MATCH. |

Angustmycin follows the explicit #741 Step5 ruling: AMBIGUOUS, no mapping row, original source label retained. The legitimate absorbed Psicofuranine raw synonym remains provenance and points to C; old C-derived chemistry is no longer an active assertion in the proposed ambiguous payload. All historical events remain. #745 integration obligation is unresolved.

Geomycin has a substantiated source-sense collision: the original1954 paper describes an A/B/C/D antibiotic complex from S.xanthophaeus, whereas MeSH also carries the oxytetracycline trade sense. Both frozen cases lack the underlying strain/paper. Parent filed [#1171](https://github.com/CultureBotAI/MediaIngredientMech/issues/1171); current owner and WITHHOLD remain.

Both bis-labelled assay substrates retain their exact strings. BacDive crossreferences mono-nitrophenyl ChEBI structures; neither field is silently privileged. Actual substrate catalogue/protocol is required.

The original unspecified Bafilomycin, Phoslactomycin, Destomycin, Bandamycin, Danubomycin, Eurocidin, Actinomycin A and Candimycin contexts are not converted to popular congeners. The precise registry names remain distinct from vague parent ontology terms. Existing holds remain explicit in each decision.

Evidence captures preserve actual tool responses, URLs, access timestamps and SHA256. Official search-result excerpts are used only for the content they actually return; failed page opens are retained as diagnostics. Historical title-only records establish nomenclature, not chemical structure. Supplier identity sheets establish reported chemical aliases; ontology labels alone are not treated as exact synonym scope. The 44 OLS searches return at most20 hits each; zero hits are bounded negatives, never a global absence proof.

The shared-owner primary cache README was read. Its18 owners fall outside this antibiotic group, so no chemistry or approval was borrowed from that cache. Local CHEBI/NCIT/MeSH SQL queries are read-only. MeSH initially returned no rows for lowercase publication prefix; successful uppercase MESH local-prefix queries are separately preserved.

Checks actually run: native `scripts/validate_strict.py` on seven proposed YAML payloads (zero errors); subgroup contract auditor on exact58-case extraction (PASS, explicitly not the full187-case audit); original owner hashes against frozen case values; hash/reference integrity; hidden/ignored-inclusive duplicate search under `data/ingredients` for the three proposed target IDs and canonical names (zero matches in that bounded surface). No downstream rebuild or release validation was claimed.

Per-name scientific rationale follows; exact individual applicability, source fields, original case digests, owner hashes and hold details are in [decisions.json](decisions.json). Primary captures/locators are in [evidence.json](evidence.json).

## tertiomycin a

Retain the distinct named source registry Tertiomycin A. Original1959 literature recognizes A; current bounded OLS returns no term. A and B designations are not interchangeable. Neither the former fuzzy A83094A candidates nor general antibiotic activity gives exact identity.

Applies individually to 1 frozen case(s): `KG_CASE:0240b832334234930818c2210302daf26ed6460e399caa5cb2b836c086e1ab48`.

Evidence: `ab-primary-tertiomycin-a`, `ab-ols-36`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: A primary structural/CAS characterization explicitly tied to Tertiomycin A is needed for external promotion.

## racemomycin e

Retain E-specific registry identity and only an asymmetric relation to MeSH racemomycin. NLM explicitly places E as a narrower concept; descriptor includes B/D/E, so exact identity with the descriptor is wrong. New scope evidence addresses one hold obligation, but existing row WITHHOLD remains until complete content-bound review.

Applies individually to 1 frozen case(s): `KG_CASE:13b25797b7931e6f679a3b2750035144c275ad1a4caf24149a81cac903fc1518`.

Evidence: `ab-term-mesh-C019594`, `ab-primary-racemomycin`, `ab-ols-33`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Coordinator must independently validate the E-concept scope and complete parent row before releasing it.

## collinomycin

Propose promotion to CHEBI:220350 alpha-Rubromycin. MCE HY-119787 explicitly supplies Collinomycin as synonym and formula agrees with live ChEBI. Query by raw Collinomycin alone had no ontology hit; verified synonym resolves that search gap. Preserve source preferred label and historical registry provenance.

Applies individually to 1 frozen case(s): `KG_CASE:13fd8c4ffb2c95fdb2c2ec2e6aa3eae22f067ab53cd3f058c2d20b407db1f9aa`.

Evidence: `ab-term-CHEBI-220350`, `ab-primary-collinomycin`, `ab-ols-18`, `ab-frozen-cases`, `ab-owner-snapshots`.

## carcinomycin

Retain named Carcinomycin source registry. DSMZ explicitly lists the product; a PubChem Carcinomycin/H5342 lead exists but retrieved evidence does not independently establish the source material structure. No fuzzy correction to Carminomycin is justified.

Applies individually to 1 frozen case(s): `KG_CASE:1477176bb725ffc16e92f169e2be9f276e9ada355a2787873cf384b9bd0155a8`.

Evidence: `ab-primary-dsmz`, `ab-ols-13`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Obtain original H5342/Carcinomycin characterization and verified registry-to-structure link before promoting the bare producer name.

## azureomycin

Azureomycin is an unresolved glycopeptide producer label. OLS has separate A and B and 2025 primary research still reports its structure unresolved. A BGC does not prove the purified chemical identity, and the bare graph provides neither fraction nor structure. Preserve source registry without external mapping.

Applies individually to 2 frozen case(s): `KG_CASE:156a72bad032d3908aafa216145161307b9e2b9efc6deb816b065bcecb7fb5fe`, `KG_CASE:9768119caf72716bbcf2a7df010f23be5b1efb4a3d5cc52f2b803ad2ff640be4`.

Evidence: `ab-primary-azureomycin`, `ab-ols-06`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover the provider strain/paper and A-versus-B assignment, then an experimentally characterized structure or verified congener-specific ontology identity.

## phoslactomycin

Retain unspecified phoslactomycin family/product context. Original structural work distinguishes A-F; OLS hits are numbered/lettered congeners. The source graph lacks any fraction selection, so B/E/H/I terms cannot replace the generic label.

Applies individually to 2 frozen case(s): `KG_CASE:16cd6c76b25287a990bde6939fdc070ebbf3151f86761cc98b2f627dd8714ac0`, `KG_CASE:43ae7535292e00b293fd09f2adc16d4bc1d4a7de5bd031f62e75bafb9bd87613`.

Evidence: `ab-primary-phoslactomycin`, `ab-ols-30`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Source-specific factor designation or a true unspecified-sense ontology class is required before external grounding.

## bafilomycin

Retain generic bafilomycin context. Original isolation distinguishes A1,A2,B1,B2,C1,C2. Source is a producer trait with no formulation or factor; mapping it to common A1 would discard identity scope.

Applies individually to 1 frozen case(s): `KG_CASE:193900aa19713cba907ddd40ee880aec870e285ea8e7e09a76837ce4f12b6806`.

Evidence: `ab-primary-bafilomycin`, `ab-ols-07`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover congener or explicitly characterized mixture/class from the provider before external grounding.

## danubomycin

Retain Danubomycin product/mixture context. The original patent distinguishes B fractions and salts; neither a bare name nor resemblance to daunomycin identifies a pure factor. Existing registry retains the source claim without inventing components.

Applies individually to 1 frozen case(s): `KG_CASE:1e2558fa54fc7179fe6b1014271caa9666b98aa673d855a549982483eaeb0aeb`.

Evidence: `ab-primary-danubomycin`, `ab-ols-20`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Provider-specific fraction/salt and original characterization are needed before a pure-compound target or component assertions.

## danomycin

Retain distinct Danomycin source registry. Original work identifies an iron-containing polypeptide and only relates it to albomycin/ferrimycin. No live OLS hit or exact alias establishes that any related siderophore antibiotic is identical.

Applies individually to 2 frozen case(s): `KG_CASE:27ae1d106388368d00459a9d7ffd5aad31ad780d2a3bb21ac886e4769821930b`, `KG_CASE:a4f44e28d496fa8184e72c47cf2effd77665194e04edbbaf55eb7001fc06873a`.

Evidence: `ab-primary-danomycin`, `ab-ols-19`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: An exact structure/CAS and validated external term for the original Danomycin is needed for promotion.

## pactamycin

Existing mesh:D010142 directly denotes Pactamycin. Frozen source label has no salt, derivative or mixture qualifier and no contradictory source identifier. Preserve current identity; this review does not approve inferred medium roles.

Applies individually to 1 frozen case(s): `KG_CASE:36dad603023df0ef94d37825e00cb94da3e2bb840be9a806b97267255b839f80`.

Evidence: `ab-primary-pactamycin`, `ab-ols-29`, `ab-frozen-cases`, `ab-owner-snapshots`.

## achromoviromycin

Retain Achromoviromycin registry as the specifically named historical antibiotic. Original isolation from S.achromogenes supports the name, but extraction and antiviral activity do not determine a modern structure. OLS returned no term for this query.

Applies individually to 2 frozen case(s): `KG_CASE:3c14b492c7bc0a650c8d0a36add073ccb270b85ae6cccc4e2e4212111bff9c16`, `KG_CASE:cc1d01ab576d924872d2cf2c923628ca8638c1697e2f84d38635ce19c73f09f5`.

Evidence: `ab-primary-achromoviromycin`, `ab-ols-02`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover primary structural/CAS identification of the original Achromoviromycin; do not substitute similarly spelled antibiotics.

## camphomycin

Retain Camphomycin registry. DSMZ associates the exact named product with S.castelarensis; there is no verified structure/CAS link from that source and the bounded OLS query is empty. Producer identity alone cannot select another metabolite.

Applies individually to 2 frozen case(s): `KG_CASE:3c9f127156392d16a019d581641d497c6e53290f73ae53d44c9d6b35a816485f`, `KG_CASE:f419beea6cc2bb60088a6d1477f641016c60c358ce819dbcabfa6bf18aea9cc7`.

Evidence: `ab-primary-dsmz`, `ab-ols-11`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Primary chemical characterization or supplier specification directly linking Camphomycin to an exact external term is required.

## pluramycin a

Retain A-specific registry. DSMZ distinguishes A and B while mesh:C003169 is generic pluramycin. At most a broad parent relation is appropriate; existing WITHHOLD on that parent remains because the nomenclatural catalogue alone is not full relation evidence.

Applies individually to 2 frozen case(s): `KG_CASE:3dffb43ee84681dcce08a18ae8f26d6662349a302a05b29bae020a7ff8937ed8`, `KG_CASE:a3f5db12c9d28150bb1b035668268f2832055e02b4ac928a6bf4a77a5d28c285`.

Evidence: `ab-term-mesh-C003169`, `ab-primary-dsmz`, `ab-ols-32`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Primary structure/synonym evidence for Pluramycin A and NLM concept scope must settle the exact broad relation before release.

## champamycin b

Retain B-specific Champamycin registry. BCRC explicitly distinguishes champamycin A/B from champavatin. OLS has no exact result; no A/B collapse or fuzzy unrelated ontology mapping is supported.

Applies individually to 2 frozen case(s): `KG_CASE:41def302095dcfc60349fcb934f66cc4d92a880cd72c960e0ef4addbdd7c8850`, `KG_CASE:8a032b6d8c3fbc4b205163cc7ac430d471d0270169c8dba80464352dc2b88cc6`.

Evidence: `ab-primary-champamycin`, `ab-ols-15`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Obtain primary purified Champamycin B structure/CAS and exact ontology bridge.

## glebomycin

Independent1990 biosynthetic research explicitly identifies Bluensomycin(glebomycin), corroborating NCIT:C90636. This supplies chemical identity evidence that the prior hold lacked. Propose evidence enrichment and SYNONYM_MATCH grade, preserving all inherited release holds until fresh full-payload review.

Applies individually to 2 frozen case(s): `KG_CASE:4386590aa16f403589f31e38422bc8d99a1b53cb2fbfaa47e0889c5ec22744a4`, `KG_CASE:6989e61ec701125fde733f22457e20134886d123f3ff7c50abaecb8b1261db94`.

Evidence: `ab-term-NCIT-C90636`, `ab-primary-glebomycin`, `ab-ols-26`, `ab-frozen-cases`, `ab-owner-snapshots`.

## caryomycin

Retain Caryomycin registry. DSMZ explicitly records the named product from S.filamentosus, but strain co-production does not make it daptomycin or another better-known antibiotic. Bounded OLS search has no hit.

Applies individually to 1 frozen case(s): `KG_CASE:477bfc984a8f330407f560b71de738179e1ccb08dd2a651fc9965ff521c18f39`.

Evidence: `ab-primary-dsmz`, `ab-ols-14`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: A primary chemical identity characterization, not only a producer catalogue, is required for external promotion.

## aburamycin a

Propose CHEBI:202873 Chromomycin A2 from BioAustralis explicit Aburamycin A synonym and matching C59H86O26 formula. Reject OLS raw-query hits Chromomycin A3: the source A is a historical name, not permission to choose an A3 congener. Preserve source preferred name.

Applies individually to 2 frozen case(s): `KG_CASE:4a7c7ebea24f383d05164c205cd90f4ca55ffb8cbc32dc77c0aeaa68a4fca825`, `KG_CASE:76b5bef18c522fbd5d3928b7fe22ea1f91884b886dc694df7b3505d221cf6772`.

Evidence: `ab-term-CHEBI-202873`, `ab-primary-aburamycin`, `ab-ols-01`, `ab-frozen-cases`, `ab-owner-snapshots`.

## angustmycin

Primary literature distinguishes A from C; C is psicofuranine. Current A=psicofuranin authorizing note is false and derived C chemistry does not independently disambiguate the source. Propose Step5 AMBIGUOUS with no ontology mapping row, preserve original name, RAW_TEXT Psicofuranine and rejected trait phrase. Follow curator #741 ruling; #745 integration blocker remains.

Applies individually to 2 frozen case(s): `KG_CASE:4b79b661593ffc55ea301458bd3418323914b523dd52e9f19ada9fb07d364cf8`, `KG_CASE:f6ae6d20f4c2b5360590b86732480ef64b3fa2b0b7d6168633287f17c38a34a2`.

Evidence: `ab-term-CHEBI-8612`, `ab-term-CHEBI-191094`, `ab-primary-angustmycin`, `ab-ols-04`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover original provider evidence specifying A or C. Separately resolve how the absorbed legitimate Psicofuranine source should be represented, and satisfy #745/native publication obligations before integration.

## vulgamycin

Original synthesis work and an explicit supplier specification identify the polyketide Vulgamycin with enterocin, corroborating mesh:C012306 beyond its untyped synonym. Propose evidence refresh and SYNONYM_MATCH. Do not conflate this polyketide with enterococcal peptide bacteriocins; inherited WITHHOLD needs fresh full-payload review.

Applies individually to 2 frozen case(s): `KG_CASE:52b9f7b5436bf45389bc371a671a05d53d6f5439557c2ced295ad7f8fdee9bfc`, `KG_CASE:fa8dcaeae943e911484df218fc1a8aa7f87200cd7905807ab88493e70a2b80ac`.

Evidence: `ab-term-mesh-C012306`, `ab-primary-vulga-synthesis`, `ab-primary-vulgamycin`, `ab-ols-38`, `ab-frozen-cases`, `ab-owner-snapshots`.

## geomycin

Bare Geomycin is not safely resolved by the MeSH oxytetracycline trade-name synonym. Original1954 primary work instead names a basic A/B/C/D mixture from S.xanthophaeus; modern fungal Geomycin A/B/C are additional specific names, not a rescue mapping. Frozen node gives no strain/product/paper to choose senses. Preserve current owner bytes and WITHHOLD; no positive exact identity approval.

Applies individually to 2 frozen case(s): `KG_CASE:5a444eaeede983a3fae3da7b1db5d9a65dac593e2799b173f834ac3b4ae00ee5`, `KG_CASE:d31fc228e50c8322a6c1b80059a5db3a757e46335e97230e3fa2d6bbf9d93cf1`.

Evidence: `ab-term-mesh-D010118`, `ab-primary-geomycin`, `ab-ols-25`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover the underlying metatraits/BacDive producer strain and original citation or marketed-product specification, then distinguish historical Geomycin mixture, oxytetracycline trade product and fungal congeners.

## cinerubin a

Propose mesh:C000481 cinerubine A. DC Chemicals explicitly equates Cinerubin A/Cinerubine A with same CAS and formula. Exact A designation is preserved; ChEBI Cinerubin B/R/Y query hits are rejected. New payload must retain hold until re-reviewed.

Applies individually to 2 frozen case(s): `KG_CASE:6331e616ce5732724c366db8d76839b4d370342514b29aaa2587f9b67393e9e6`, `KG_CASE:ae749368869d7e96437db525fe05f187b2f729b86634b8eab210e7bf03d18802`.

Evidence: `ab-term-mesh-C000481`, `ab-primary-cinerubin`, `ab-ols-16`, `ab-frozen-cases`, `ab-owner-snapshots`.

## bandamycin

DSMZ explicitly lists Bandamycin A and B, so bare Bandamycin retains an unspecified product/family sense. Do not choose one fraction or equate all pentaene antibiotics. No component composition is inferred.

Applies individually to 2 frozen case(s): `KG_CASE:6f05d56cabd5d31d3ca5be3429cc18968970b0ac8a2d0b6f6888a30d63840a09`, `KG_CASE:ff9c61159588c678ffb82510253e2de10653b674c8837d44f90abf602e31797e`.

Evidence: `ab-primary-bandamycin`, `ab-ols-08`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover source factor/mixture definition or an exact unspecified-sense ontology term.

## cladomycin

Retain Cladomycin registry. Primary culture-collection documentation supports this legacy product from S.lilacinus; no molecular alias or exact OLS target was established. Similar spelling to cladosporin is insufficient.

Applies individually to 1 frozen case(s): `KG_CASE:71a3633a84475203563951a6d741fed5fd69c18dde2711dcd70990b6839b271b`.

Evidence: `ab-primary-cladomycin`, `ab-ols-17`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Primary purified Cladomycin structure/CAS evidence is required before external mapping.

## destomycin

Retain generic Destomycin context. Original work distinguishes A and B; OLS also offers C and differently spelled Destomysin. The bare production label cannot choose a factor, and no mixture composition is supplied.

Applies individually to 1 frozen case(s): `KG_CASE:7e8d4fb4b5e488e92c7bdedea47eec5af880e7b64c2191f562b7522fd8f062ed`.

Evidence: `ab-primary-destomycin`, `ab-ols-21`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover exact factor or composition from provider-linked original isolation before external identity selection.

## staphylomycin m1

NCIT:C1295 Streptogramin A explicitly includes staphylomycin M1 and virginiamycin M1, with CAS21411-53-0. The M1 factor label is preserved and is not replaced with the virginiamycin multi-component product. Existing mapping remains; no role approval.

Applies individually to 2 frozen case(s): `KG_CASE:7f844a440365230c668065e85d2b190f7ece72f4c79a28142a123e979c0170bf`, `KG_CASE:bb7039292ec1743621cd3908a68717b999d710d5da808475b7deb2f673d0c9bf`.

Evidence: `ab-term-NCIT-C1295`, `ab-ols-35`, `ab-frozen-cases`, `ab-owner-snapshots`.

## bis-4-nitrophenyl-phenyl phosphonate

Source name includes bis. BacDive crossreference CHEBI:91050 denotes p-nitrophenyl phenyl phosphonate whose captured formula/SMILES contain one nitrophenyl group and a different phosphorus substitution pattern from the literal bis name. The upstream ID is contradictory evidence, not authority to delete bis. Preserve exact raw assay token and source registry.

Applies individually to 2 frozen case(s): `KG_CASE:7f8fe6714739ec034ab245e5a11d8c9ce1e306d07dedc05a8a25aa8496f65f70`, `KG_CASE:b7505c4a7dd6b233c972555cd74160221aa8f94dd6e1a23805b6760568d2bf96`.

Evidence: `ab-primary-bis-assays`, `ab-term-CHEBI-91050`, `ab-ols-09`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover original substrate supplier/catalogue or assay protocol with chemical structure and bis-versus-mono stoichiometry, then correct the upstream label or target with explicit evidence.

## rhodomycin a

Retain Rhodomycin A-specific registry; MeSH C004977 is a broader rhodomycin concept. OLS beta-Rhodomycin CHEBI:81879 is linked to Rhodomycin B, and D/epsilon congeners are not A. Existing parent WITHHOLD stays; nomenclatural beta-rhodomycin II leads need original structural verification.

Applies individually to 2 frozen case(s): `KG_CASE:88762d7e6dbfd72399a93315b9e28b2f5c96fe2f9be57d151c62b8708c4fbe4e`, `KG_CASE:f7962ac4b3511ec2b48c87cb9ec4c1ed80fd88d57f175c4680383be2b856a740`.

Evidence: `ab-term-mesh-C004977`, `ab-ols-34`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Obtain original A/beta-rhodomycinII structure equivalence and exact NLM concept relationship before release or identifier promotion.

## eurocidin

Original1970 paper reports Eurocidin as A/B mixture. Preserve generic source product identity, not a newer E/D/C congener from OLS. Existing registry support does not establish component proportions or authorize automatic ingredient-type/role rewriting.

Applies individually to 1 frozen case(s): `KG_CASE:892953976d393fcf99a3dc836f07435d64e305454d739a5b116dbf1fa77a0a97`.

Evidence: `ab-primary-eurocidin`, `ab-ols-23`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Provider-specific fraction or batch composition is required before a single-congener mapping or component model.

## durhamycin

Original1966 Durhamycin is a pentaene antifungal. Current OLS hits Durhamycin A/B have extra congener labels; the bare graph supplies no strain/publication context proving continuity or selecting either. Preserve source registry and do not infer identity from the prefix.

Applies individually to 2 frozen case(s): `KG_CASE:8f4931295197327c660cc7b4a7b4df5e3a9a4691b923eae6c3b39b527e4e6518`, `KG_CASE:98d1cba4b8a5d95eb7b332e1ce5897aa30a633b7f79923df32708e76a9d19570`.

Evidence: `ab-primary-durhamycin`, `ab-ols-22`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Retrieve underlying producer strain/citation and characterize the original pentaene versus later A/B substances before exact external grounding.

## ascosin

Retain named Ascosin registry. Primary1961 research supports the historical product and its biological study; neither polyene class nor respiratory effect identifies antimycin or another antibiotic. Existing source-level registry identity survives; no new external identity is claimed.

Applies individually to 2 frozen case(s): `KG_CASE:94be203edf9cc9f7848e07b1ad5097ac94d674b18219c51d0538a2099c8bd628`, `KG_CASE:c924317eaf012e603186d9d89a6ef7f6b6a249c37fc6355cc32380ae96f795eb`.

Evidence: `ab-primary-ascosin`, `ab-ols-05`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: A direct structural/CAS-to-ontology correspondence for Ascosin is needed for external promotion.

## bis-4-nitrophenyl-phosphorylcholine

The source specifically says bis-4-nitrophenyl-phosphorylcholine, while BacDive points to CHEBI:55394 p-nitrophenylphosphocholine with one nitrophenyl ring and charge+1. Do not normalize away a chemically significant bis prefix. Exact source registry/raw synonym retained; no sodium/salt form guessed.

Applies individually to 2 frozen case(s): `KG_CASE:95ef91bffa349e236f9bd4fdd547f10511cfcaf099d6543017ef35f81ebe4745`, `KG_CASE:bf2e24ef1bbddb861e3b91f5dedca3ad46729b3ba7c6fdd963fc7cebaefa6331`.

Evidence: `ab-primary-bis-assays`, `ab-term-CHEBI-55394`, `ab-ols-10`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Obtain original assay substrate formula/structure/catalogue to decide whether bis is a source transcription error or indicates a distinct material; establish supplied ion/salt form.

## hitachimycin

Original physicochemical comparison identifies Hitachimycin with stubomycin despite different producing strains, independently supporting mesh:C031780. Propose evidence refresh and SYNONYM_MATCH grade. Inherited WITHHOLD is preserved until fresh complete payload assessment.

Applies individually to 1 frozen case(s): `KG_CASE:b0c6140569a119ad8856b9a261905203c1f690124a8afd10d989a65c3108c712`.

Evidence: `ab-term-mesh-C031780`, `ab-primary-hitachimycin`, `ab-ols-28`, `ab-frozen-cases`, `ab-owner-snapshots`.

## phyllomycin

Retain named Phyllomycin registry. DSMZ separately lists Phyllomycin and Phleomycin, so spelling similarity cannot justify a merge. Current OLS query has no hit; no exact molecular identity was established.

Applies individually to 1 frozen case(s): `KG_CASE:c10e940af9974fe12adc1a430da864d2c75e38c8025999b9d2b94c18762f30ad`.

Evidence: `ab-primary-dsmz`, `ab-ols-31`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Obtain original Phyllomycin chemical characterization and registry correspondence distinct from Phleomycin.

## actinomycin a

Retain Actinomycin A historical complex context and distinct source registry. Actinomycin CHEBI:15369 is a generic class; the bare A source lacks a component suffix or composition and cannot be silently mapped to D. Existing rejected produces-phrase and both row WITHHOLD obligations persist, including changed-owner refresh.

Applies individually to 1 frozen case(s): `KG_CASE:c1b8080cf230fe9d70aa08ef1df3ba9b08b3386250e2acc19ec00e6d656c6fd3`.

Evidence: `ab-term-CHEBI-15369`, `ab-primary-actinomycin`, `ab-ols-03`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover provider-specific component/complex meaning and assess full broad-parent row plus rejected alias scope before release.

## tertiomycin b

Retain distinct Tertiomycin B registry. Authored antibiotic nomenclature lists A and B separately; neither A production paper nor bare Tertiomycin establishes B structure. OLS search returns no exact target.

Applies individually to 1 frozen case(s): `KG_CASE:da3469b49ac826f45c97e9efbd808a100f1b1e5420f0271b3d0e23f81dab7908`.

Evidence: `ab-primary-tertiomycin-b`, `ab-ols-37`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Primary B-specific isolation/structural or CAS evidence is needed; A evidence cannot substitute.

## flavensomycin

Retain Flavensomycin registry. Primary1977 study explicitly says flavensomycinoic acid is only a shared molecular moiety; OLS MeSH fragment hit cannot represent the whole antibiotic. No source-backed exact whole-molecule ontology term was established.

Applies individually to 1 frozen case(s): `KG_CASE:f1e09e50983410d9ba925cd336150a022b2f940e6b9ddf7dcf402c8d992b420a`.

Evidence: `ab-primary-flavensomycin`, `ab-ols-24`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Verify complete Flavensomycin structure/CAS and external target; do not map a whole antibiotic to its degradative fragment.

## grasseriomycin

Retain Grasseriomycin registry. Original1955 literature names the antibiotic in silkworm-virus experiments; this corroborates a legacy name only. No exact target appears in the bounded OLS query and biological activity is not chemical identity.

Applies individually to 1 frozen case(s): `KG_CASE:f3efb6dbcc62ca093f0e5102aa4561e9b4b4c3589d932138ad3499d4042f465c`.

Evidence: `ab-primary-grasseriomycin`, `ab-ols-27`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover purified Grasseriomycin structure/CAS or a validated direct external nomenclatural identity.

## candimycin

Retain unsuffixed Candimycin product context. Primary papers distinguish Candimycin from Candicidin and separately mention Candimycin A. Neither spelling similarity nor a shared heptaene classification allows congener or product collapse.

Applies individually to 1 frozen case(s): `KG_CASE:f521bf9858b1bc3f56844c7eb9af74c6bad3099eedbd53900ebb08f978875f4b`.

Evidence: `ab-primary-candimycin`, `ab-ols-12`, `ab-frozen-cases`, `ab-owner-snapshots`.

Remaining requirement: Recover factor designation/complex composition and primary structural correspondence for the source Candimycin.

