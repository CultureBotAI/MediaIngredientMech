# Bounded alignment design assessment before implementation

Root proposed an explicit maintained publisher alignment helper, using deterministic full local object keys, while preserving the captured native maker parser, original MAKER_SHA, historical receipts and unchanged complete receipt/owner-chain/replay validators. This is a reviewable narrow capability change; monkeypatching the loaded maker or silently skipping a row would not satisfy it. No implementation or approval is supplied by this note.

The new helper must detect duplicate keys before insertion, cover every old/new row and position exactly once, preserve ordinary ontology/CAS replacement behavior, and leave unselected canonical physical lines untouched. Native generation and B1/B2/B3/B5 remain the independent contract; this code may not infer a scientific identity or suppress either distinct local row.

There is a specific equivalence qualification. With one local row before and one after, changing `kgmicrobe.ingredient:a` to `kgmicrobe.ingredient:b` is a `changed` row under legacy namespace alignment but `removed` plus `added` under a full-local-object key. Thus universal 'unambiguous alignment equivalence' would be false. The author should prove equivalence where local IDs persist (and for ordinary ontology/CAS replacements), and explicitly test/document local-ID replacement and its position/hold semantics. Complete historical receipt bytes and replay must remain unchanged; no prior approval may carry across a new identity simply to preserve an old position.

The separate selected-suppression review obligations remain open. Projection or receipt representability does not waive policy/source evidence, owner-chain, provenance preservation or scientific admission requirements.
