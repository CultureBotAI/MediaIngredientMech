# Correction addendum to the frozen Step7(b) design

The original `../DESIGN.md`, SHA256
`c96ac71e3a27bb1c15332d1ecaa8cb99aac2b27785877e5befddccde6c53743d`,
and its original index remain unchanged.

Its statement that the approved plan “prohibits unified TSV/provenance
changes” is overbroad. The plan literally says: “None of them may touch the
unified snapshot.” It does **not** explicitly prohibit the provenance file
as a separate named artifact. Do not attribute that separate prohibition to
the user. This addendum supersedes that wording in the original design and
any accompanying preparatory prose that repeats it.

The practical restamping limitation follows from the repository’s truthful
build/provenance contract, not an invented user instruction. At the audited
feature head83d0375c6abc9eee97039315ba9b7d496aff8391:

- `justfile:150–170` documents stamping after an actual successful rebuild;
  a failed build must abort before the stamp because otherwise stale bytes
  are falsely recorded as current.
- The independent native Casein probe found the protected unified snapshot
  still carries `kg_microbe_node_id=CHEBI:3448`, while the current merged
  native loader/row builder and corrected owner produce an empty node field.
- That probe covers one real published row; it is not a full rebuild. It is
  sufficient to reject the unsupported assumption that the protected snapshot
  already matches the current source projection.
- Consequently a naked provenance stamp, revised digest/revision or changed
  history boundary is not an honest substitute for a successful rebuild.
  The current conditional26-owner versus25 gate conflict remains, without
  inferring a separate provenance-file ban.

The independent boundary review is
`../../step6-independent/step7b-current-boundary/review.json`,
SHA256 `2c7bdd64f4aecc034c4628a7d3ba2e1cb181fdceabde20ff7e23cbdf2baf0ee4`.
Its exact native Casein probe is `snapshot-result.json`,
SHA256 `b93871a8eff5dd5ecb2050f7ac941b17b640b4a06ab822dd1f05a0106eb9c6c3`.
The saved plan is SHA256
`99b7746742f70c7896ed163a833a8b214282dba84567dc3213ec0a2b194e4d90`.

This correction changes no source/guard proposal, approval, record, product,
threshold or GitHub state. Source preparation remains authorized; subsequent
execution requires the actual ordered merge/current-main checkpoint.
The unanswered publication clarification remains unanswered. The new adjacent
#871/#268 comments are local drafts only and are not evidence that a decision
has been posted or any work has passed its future checks.

