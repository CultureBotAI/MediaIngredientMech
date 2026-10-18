# Final TSV consumer and adversarial review

This review applies to the supported MIM assertion subset. It does not approve
the complete source graph or resolve the scientific backlog in
[#718](https://github.com/CultureBotAI/MediaIngredientMech/issues/718).

## Findings

1. [#724](https://github.com/CultureBotAI/MediaIngredientMech/issues/724): the
   supported `MIM:Aromatic_Compound` mapping still carried the organism-trait
   phrase `degradation: aromatic compound` in its synonym annotation. Preserve
   the whole unchanged mapping in the separate backlog pending source cleanup
   in [#703](https://github.com/CultureBotAI/MediaIngredientMech/issues/703).
2. [#725](https://github.com/CultureBotAI/MediaIngredientMech/issues/725): the
   initial hold implementation trusted its required inventory from the same
   editable ledger. An independent reviewer removed both hold lists, restored
   approval, and refreshed hashes; the full gate and exporter accepted the
   assertion. A related test retargeted the same hold ID to another assertion
   for the same owner. The negative policy must be anchored independently of
   the review ledger and bind the exact intended assertion.

## Verification after correction

The independent reviewer replayed both bypasses against the maintained policy.
Deleting both hold arrays, renaming the hold, restoring an approved disposition,
and retargeting the hold to a second assertion all failed validation. All 115
focused builder, gate, supported-exporter, and adversarial tests passed.
The source YAML and complete source SSSOM were preserved unchanged.

See [the consumer receipt](tsv-consumer-validation.json) for the regenerated
artifact counts and hashes, [SSSOM validation](supported-sssom-validation.json),
and [native KGX validation](native-kgx-reader.json).

## Consumer interpretation

The SSSOM and KGX mapping payloads must agree exactly. All active ingredient
records remain as conservative source-reference nodes, including isolated
records with no approved outgoing assertions. Their presence does not approve
raw identity annotations. The separate backlog retains all raw node payloads
and excluded assertions and is not a member of the KGX archive.

Source confidence annotations remain verbatim. In particular, the grading
provenance of `0.8` and `0.95` values is still discussed in
[#662](https://github.com/CultureBotAI/MediaIngredientMech/issues/662), which
explicitly treats that ambiguity as nonblocking. This release does not resolve
the grading-policy question or silently rescale values.

The native KGX reader receipt records the exact archive and offline helper/model
hashes. It demonstrates reader compatibility, endpoint/predicate preservation,
and JSON annotation preservation; it does not claim strict Biolink schema
conformance. Agent adversarial review is not human sign-off.
