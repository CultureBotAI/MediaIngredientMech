# Buffer and preparation source review

This partition reviews all 43 indices assigned in `buffers-indices.json`, comprising 135 frozen occurrences and 93 distinct complete recipe snapshots. The exact case objects, original source labels, occurrence IDs and all inherited holds remain bound by the case digests in `decisions.json`. This is one partition of worker 10's 188-case shard; it does not claim the remainder.

The evidence ledger contains 87 primary-source captures, eight ontology captures, the frozen case/recipe snapshots and the before bytes of three existing owners. Primary sources include JCM, NBRC, DSMZ, TOGO, UTEX and the named manufacturers. Actual retrieval URLs, access times and capture hashes are retained. TOGO frontend application shells, failed JCM PDF guesses and failed ontology web requests are not treated as scientific evidence. The follow-up request log records timeouts separately. No shared-owner-cache evidence was reused in this partition. One exact TOGO M2186 response was copied from the parallel chemical partition with its original retrieval timestamp and hash; its applicability to the concentrated-HCl occurrence was independently assessed.

Eight exact isolated payloads are proposed:

| Proposal | Supported change | Scope boundary |
|---|---|---|
| `buffers-aces-aliases` | Add the two weighed ACES reagent spellings to the existing CHEBI:39060 owner | Preserve prior #320/#334 ruling and the rejected duplicate; no adjusted stock identity |
| `buffers-hepes-acid-alias` | Add the explicitly acid-qualified Sigma H3375 spelling | HEPES acid powder remains separate from pH-adjusted stocks |
| `buffers-phosphate-m3225` | Source-defined TOGO M3225 phosphate stock | 47 g KH2PO4 and 113 g K2HPO4 per litre of water; no calculated final-volume molarity |
| `buffers-phosphate-jcm1142` | Source-defined stock printed identically in JCM 1142/1143 | 12.5 g KH2PO4, 20 g K2HPO4 and 1 litre water |
| `buffers-kp-nbrc857` | Source-defined KP stock printed identically in NBRC 857/936 | 119 g KH2PO4, 21 g K2HPO4 and 1 litre water; autoclaved under N2 |
| `buffers-phosphate-jcm822` | JCM 822 stock composed of two input solutions | 50 mL of each 1 M phosphate input; the input stocks are not mapped as pure salts |
| `buffers-riboflavin-jcm462` | Promote the existing source-1893 owner to the JCM 462 riboflavin stock | JCM 772 supplies the catalog cross-reference; DSMZ 462 is not substituted |
| `buffers-antifoam-wako` | Named Wako Antifoam SI product | Opaque silicone-type product; composition and identity of its diluted working stock are not invented |

The four phosphate/KP payloads use source-qualified preferred terms. Independent review identified that generic source-local raw labels would become globally resolving aliases. The revised payloads therefore preserve those labels only in provenance notes. The riboflavin payload similarly moves both inherited and newly encountered “see Medium No. 462” navigation strings into nonresolving provenance, retaining the original history. The reviewer must bind approval to these revised bytes.

The other cases retain explicit material boundaries and exact missing requirements: missing stock constituent ratios or titrant/counterion specifications, unspecified antibiotic form or percentage basis, and opaque aquarium-salt formulations. Two cases remain explicitly unresolved because their printed recipes conflict internally: the reducing-stock sulfide amount mixes concentration denominators, and JCM 556 specifies 28 mL plus 78 mL while claiming 100 mL. Neither discrepancy was repaired by guesswork.

`findings.json` records the source-volume/nesting defect already tracked by CultureMech #408, inherited Tris aliases tracked by MIM #1157, the JCM 556 discrepancy, and the inherited HCl solution-alias concern for coordinator deduplication. No external message or issue mutation was performed by this subagent.

`proposal-validation.json` records eight successful guarded writes and zero component-partonomy violations for the proposed owner identifiers. `strict-validation.log` records eight files checked with zero errors. `partition-integrity.json` verifies exact assigned case coverage, source fields, every occurrence, evidence/proposal capture hashes, before-owner hashes and proposal backlinks. These checks do not establish scientific or publication approval. Only isolated report payloads were written; maintained data, aggregates, SSSOM and exports were not changed.

The independent review lives outside this author directory under `reviews/bio-review-of-buffers-v1.json`. It covers all 43 cases, 135 frozen occurrences and eight revised proposals, and reports four findings resolved. In addition to the source-local alias correction, the final ledger binds JCM 1036 to the case 107 preparation cross-reference and adds three occurrence-specific concentrated-HCl primary records to case 65. The author fragments retain pending review fields so the coordinator can attach the independent capture and status in the integrated ledger. The coordinator must union the KG179 backlink into the single riboflavin proposal, perform final complete-owner publication review, and reconcile any cross-shard owner conflict before integration. The existing riboflavin owner is under `unmapped`; its intended destination is under `mapped`, while the proposal retains the actual baseline path and hash for audit.
