# Exact source lineage of the two MediaDive hexahydrate rows

The original selected recipe occurrence is recoverable for both assigned KG cases. The admitted producer takes the first embedded recipe row for each `compound_id`, traversing media in catalogue order and then solutions and recipes in their retained list order. Replaying that contract against the hash-bound admitted inputs selects **medium 14, solution 20, Trace element solution SL-4** for both rows. This conclusion uses the producer's ordering contract; matching amounts alone would not identify a unique recipe.

| Frozen case | MediaDive ID | Original response locator | Provider recipe order | Original row |
|---|---|---|---:|---|
| `KG_CASE:9732bb704373e55707bb613086c396ecca4455bc7d99e05079cf6d8f0254c465` | `mediadive.ingredient:38` | `/data/solutions/1/recipe/5` | 6 | `CoCl2 x 6 H2O`, 0.2 g |
| `KG_CASE:f527458e161f77cc363140a6708e6cd18be73f9432b5d565e017b2fac4d84b63` | `mediadive.ingredient:40` | `/data/solutions/1/recipe/7` | 8 | `NiCl2 x 6 H2O`, 0.02 g |

The selected medium is at catalogue index 16 (zero-based), with provider metadata `CLOSTRIDIUM FORMICACETICUM MEDIUM`, source `DSMZ`. The retained response itself links to `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium14.pdf`. This establishes a direct provider-document lead for the coordinator's separate scientific comparison. This local investigation did not fetch or assess that PDF.

## Bound evidence and reproducible derivation

The frozen audit is rooted at `/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5/inputs/kg-source-audit`. Its manifest pins KG revision `f10fb3909ed32898a54176ca77e509a950d16b84`, the frozen `current.json`, the admitted generation manifest, `compounds.json`, and the source-candidate ledger. The two full follow-up case objects retain the exact candidate fields from that ledger. Their `source_record` values equal the selected entries in the frozen compound table, with the same typed JSON values and canonical row hashes.

The frozen compound file is 228,388 bytes, SHA256 `5401db0bc697249c9b2b0ad0b950fd3c2b7629f0cdd10c7feaf1e40b0a3a4729`. It is byte-identical to the admitted generation's file. The admitted generation manifest is byte-identical to the frozen audit copy and has SHA256 `fa3c9e47bad5ff298b35e32382de7bd642e6be6ed95540db128d7d674058924f`. Its entries bind `media_detailed.json`, `solutions.json`, `catalogue.json`, endpoint outcomes, the observation ledger and retained response bodies. Although the audit snapshot contains only selected generation files, the remaining admitted files are available read-only at the manifest-pinned paths under:

`/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-mim-1788-20261107/data/raw/mediadive/generations/resolution-admitted-r2/`

The script checks current producer bytes against `git show` at the frozen KG revision. The relevant code is copied under [captures/code](captures/code):

- `endpoint_outcomes.py:101–118`, `catalogue_scope`: preserves the catalogue's ordered medium IDs and rejects duplicate IDs.
- `acquisition.py:451–470`, `_native_payloads`: builds `details` in that catalogue order and passes it to the production extractors.
- `mediadive_bulk_download.py:499–530`, `extract_compounds_from_media`: traverses embedded solution/recipe lists and stores only the first row for each compound ID. It adds no parent-medium or parent-solution field.
- `acquisition.py:473–514`, `_rebuild_staging`: reconstructs native payloads from retained observations; an existing protected seed must have equal canonical values. Byte serialization can retain seed formatting, which does not change selected row values.
- `endpoint_outcomes.py:330–379`, `validate_native`: documents the same ordered extraction/value contract.
- `dump_unmapped_mediadive_ingredients.py:55–63,107`: the helper reads transformed ingredient IDs/names and emits a constant occurrence value of 1. That field is not measured recipe frequency.

[replay_lineage.py](replay_lineage.py) isolates the two pure extraction functions from the hash-checked producer AST; it does not import or execute acquisition/download workflows. It separately reconstructs the ordered input/response bindings. The run recorded in [replay-validation.json](replay-validation.json) passed:

- all 3,344 catalogue-ordered medium payloads equal their manifest-pinned raw response `data` values;
- the 6,737-event observation ledger has valid sequence and chained observation hashes, and retained medium outcome records point to their latest ledger observations;
- all 1,214 compound values **and key insertion order** equal the producer replay;
- all 5,442 solution values **and key insertion order** equal the producer replay;
- both exact frozen case records match their selected raw recipe values; all nine linked owner files retain their frozen hashes.

This is a provenance/extraction replay, not a rerun of the complete production acquisition validator. It does not deserialize SQLite response caches, redo request-intent admission, or claim a separately witnessed historical execution log. The reconstructed parent is established by the frozen producer contract and retained generation values; it is not a parent identifier literally present in the flattened row.

Run without writes from the worker worktree:

```sh
PYTHONDONTWRITEBYTECODE=1 .temp/all-unmatched-worker-09/venv/bin/python reports/all_unmatched_20261107/worker-09/followups/hexahydrates-v1/provenance/replay_lineage.py
```

## Original response and ambiguity boundary

[captures/original-medium-14.body](captures/original-medium-14.body) preserves the exact 9,208 response bytes from `https://mediadive.dsmz.de/rest/medium/14`, observed `2026-11-05T06:23:28.282363+00:00`, SHA256 `eae2b02dd9bf80cafe07a5758681fb72ec3a4590de7d25a620c071802fc23144`. The source link is at original line 12, the selected solution at line 132, the cobalt label at line 187, and the nickel label at line 207. The original response retains every row field, including `mmol_l`; no quantity or label was corrected.

The admitted event is sequence 3821, observation `8be8d31833dc1d60a8a719262612ac664f8e2102e3ade7b974e9a08403b7b8b7`, imported from `evidence/full-ledger.jsonl` line 17. The imported original line SHA256 is `be3ca9d7db4d4b7132b767356d0e592d5eeb196f1982230eb40b826a9e7f8c2e`. The replay checks that line's URL, original timestamp and body hash. The published event derivative omits session-bearing request headers; it records the exact original event path/hash and does not pretend to be the original event bytes. Copy time and original HTTP observation time are separate.

The original medium's main solution (ID 19) explicitly references solution 20. The latter contains these rows in its stock recipe, which lists 1,000 ml distilled water and a provider `volume` field of 1000. The selected 0.2 g and 0.02 g values therefore belong to that embedded stock recipe; this investigation does not reinterpret them as final-medium concentrations or assert a separately measured final stock volume.

The full admitted embedded-media scan finds 1,063 appearances of compound 38 and 1,196 appearances of compound 40. Among those, 84 cobalt rows across 13 distinct solution IDs and 45 nickel rows across four distinct solution IDs have exactly the flattened row values. [captures/all-target-occurrences.json](captures/all-target-occurrences.json) retains every locator. These counts demonstrate why an equality join or a quantity match is insufficient. They count embedded row appearances in this one generation and are not estimates of independent experiments or ingredient usage.

## Issue 344 and owner limits

The full current [issue 344 capture](../common/issue-344.json), including both comments, was read. The August 13 comment expressly retracts the sulfate-to-chloride hypothesis and identifies `NiCl2 x 6 H2O` as an example of a genuine hydrate carrying an anhydrous mass in MediaDive. This means a provider mass mismatch alone cannot settle the supplied form. The August 21 comment concerns other sulfate labels and still calls for original source rows. Neither comment licenses changing either selected hexahydrate into an anhydrous substance. The issue's closed status does not itself approve these cases.

All nine linked owner YAML files were loaded and copied byte-for-byte under [captures/owners](captures/owners), with their original hashes in [source-associations.json](source-associations.json). The active canonical owners are `Cobalt_chloride_hexahydrate.yaml` (`CHEBI:53503`) and `Nickel_II_chloride_hexahydrate.yaml` (`CHEBI:53542`); both preserve the selected formula spelling as `RAW_TEXT`. Their native rows 799 and 2097 remain `WITHHOLD` pending whole-payload review. Cobalt's canonical synonym payload includes the separate `water (1/7)` concern. The formula-named six-water records are rejected merge tombstones; their remaining anhydrous structure fields do not establish the source row's supplied form. The linked different-form owners preserve the selected six-water strings as rejected aliases. No owner, alias, role, formula, predicate, SSSOM row, publication selector or hold was changed here.

The result closes the **source-locator gap for these two selected flattened records**. It does not approve every use of either source ID, transfer approval to another hydrate, review the entire owner payload, or release a downstream hold. Provider-document comparison, exact form identity and final case disposition remain the coordinator's scientific synthesis and the separate skeptic's responsibility.

Search commands, complete captured outputs and return codes are in [searches.json](searches.json); they explicitly include hidden and ignored files within their stated scopes. Exact read input paths/hashes are in [input-hashes.json](input-hashes.json). No repository-wide absence claim, current upstream-main claim, maintained write, network request, downstream rebuild or additional external session is made by this investigation.
