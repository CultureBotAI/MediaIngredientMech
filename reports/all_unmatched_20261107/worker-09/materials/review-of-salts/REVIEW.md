# Independent review of worker09 salts

Reviewer `/root/materials` independently reviewed all 69 source cases and all 15 final proposals authored by `/root/salts`. The final review has no open reviewer findings. This means the source-bound decisions are supported, including their explicit unresolved boundaries; it does not release inherited holds or declare all chemical identities resolved.

`review-final.json` binds every case's complete scientific payload, excluding only `independent_review`, and the exact final decisions, evidence and proposals files. Its SHA256 is `834ece02e50e27acdf878f503a7080e996c3cbd2850e043c2e01a5138059a046`. Original and final input snapshots are preserved. The separate round2 review captures the state before the final successful M683 retry.

Four findings were raised and independently rechecked after primary-author remediation:

- SA-SR-01: stale JCM retrieval failures no longer imply that the recovered JCM1118 recipe is unavailable. Missing JCM1119/1120 evidence remains distinct.
- SA-SR-02: stock mass and added water no longer become unsupported final-volume concentrations. Provider-declared strengths remain explicitly distinguished from calculations.
- SA-SR-03: the recovered M2231 JSON supported a concrete calcium chloride dihydrate stock, replacing an unnecessary retrieval hold. Its registry proposal preserves the exact hydrate, source-declared 2.5 g/L strength, deionized-water carrier and separate 10 mL dose. The water grade remains UNMAPPED rather than being equated with distilled water.
- SA-SR-04: unrelated M190 evidence was removed from M1901, and the shared frozen JCM665 recipe locator now distinguishes both stock positions. The final successful M683 retry establishes 0.1 mL of each stock per 10 mL medium, while leaving calcium percentage basis and both stock carriers unspecified.

Scientific checks included the OECD iron-dichloride hydrate CAS table, NBRC1326 and PubChem for the new dihydrate owner; direct ChEBI definitions for salt ratios, beta positional identity and hydrates; supplier Merck35675 and SigmaP3556 scope; full original recipe and stock tables; and every KG occurrence's contradictory identifiers and embedded holds. CHEBI86658 encodes a single phosphatidylcholine structure and cannot identify the whole variable egg-yolk product. Generic ammonium citrate, glycerophosphate and contradictory hydrate fields retain precise limitations.

Validation passed for all 302 evidence captures, 41 baseline owners, 86 occurrences in 83 full frozen recipes, and all 15 proposed after payloads. Exact raw labels, original case hashes, occurrence positions, proposal backlinks, closed schema, ignored-inclusive new-identifier/path checks and component partonomy were verified. The reviewer also checked cached OAK term definitions and performed fresh JCM665 retrieval attempts, preserving unsuccessful bytes and metadata. These are independent checks, not reused primary-author completion claims.

Complete inherited synonym payloads still include known conflicts, including the cobalt water(1/7) alias, calcium hydrate fragments and manganese MnCl4 labels. Narrow alias proposals do not endorse those full rows. Worker02's manganese owner dependency, coordinator native review, publication closure and source fixes remain explicit obligations. No maintained records, SSSOM, hold ledgers or downstream products were changed by this reviewer.
