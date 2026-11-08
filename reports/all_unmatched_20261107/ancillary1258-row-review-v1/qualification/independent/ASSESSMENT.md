# W03 historical input case-alias transport assessment

The original content is available. A qualified, explicit transport map is sufficient for historical evidence archival; it is not a replacement native source root or fresh review validation. This is a mechanical content/path assessment, not another scientific vote or publication approval.

The readback independently checked all 55 `source.inputs` hashes in the exact original YAML/Markdown pair, literal directory membership using `os.scandir`, the root manifest's exact path strings, and `lstat` identities. Ignored and hidden files were included. All declared hashes match. There are 54 physical input files and 54 exact literal manifest members. The only duplicate physical input is the assessment alias pair. Original source bytes and file metadata were stable at final readback.

The original pair is unchanged: YAML `b0e405ab71146a52c894d962361e64102febcae96b8f462452f01c536f03c7a6`, Markdown `6b1d6ed609198c84c89ea175cb2d5f8af564e0e506c8b0d7fc4b1f3769d6099c`. Its completion is `completed`, verdict `needs_curation`, and source state `working_tree` at `7b7a4fb1e557c2115d48aebedfeda0cc5eb7bbb5`. These historical claims must remain intact.

Both joins must be explicit:

| Historical upstream name | Actual upstream literal | Historical fixture name | Actual fixture literal |
|---|---|---|---|
| `science/ASSESSMENT.json` | `science/assessment.json` | `reports/actual-xanthine-review-evidence/science-ASSESSMENT-json.json` | uppercase `science-ASSESSMENT-json.json` |
| `science/assessment.json` | `science/assessment.json` | `reports/actual-xanthine-review-evidence/science-assessment-json.json` | uppercase `science-ASSESSMENT-json.json` |

Each refers to the same 3,000-byte assessment content, SHA-256 `d4eb97ae92328753a4b7c9e897ee6ebd62132ef3ca607bfb96e887e6735d172f`. The upstream inode is 158701986; the fixture inode is 158702565, both on device 16777233 with link count 1. The two spellings are filesystem lookups of one directory entry, not two hardlinked original files. The upstream root-manifest member is lowercase; the fixture root-manifest member is uppercase. `READBACK.json` binds the full historical copy-map entries and exact manifest entries.

A subsequent transport selection can store one unambiguous physical assessment file and map both original logical references to it, binding original logical name, actual original literal name, historical fixture logical name, actual fixture literal member, content hash/size and final archive path. The two references are one assessment and must not be counted as separate independent evidence. Preserve the original pair, copy map, manifests and save/validation receipts byte-for-byte; list omissions if selecting only part of the original packet. Do not claim the original manifest describes the archive's physical layout. The actual selected copies and map still require their own byte readback.

The pinned native `scripts/record_review.py` `_input`/`file_sha256` opens the declared filesystem spelling (lines 410–436); `assert_current_source` checks those paths and the original source revision (lines 486–505). It does not consume an archival transport map. Thus preserving only the one literal file on a case-sensitive archive filesystem does not make the unchanged pair directly current-valid there: the other declared spelling has no literal file. Pair parsing/render agreement is separate from native source provenance. No Linux fixture, new native validation, review resave, source-root relabel, second alias file, archive copy or maintained change was performed here.

The occurrence was filed before transport selection under [#1254 comment 6723268855](https://github.com/CultureBotAI/MediaIngredientMech/issues/1254#issuecomment-6723268855), bound through the root's readback receipt. This assessment finds no missing content among the 55 declared inputs. It does not supersede the original scientific `needs_curation` finding or authorize the selected Xanthine row.
