# Stock CAS projection and replay contract

The intended canonical change is one row: MIM:02_Thiamine_Pyrophosphate.
Remove exactly CAS:154-87-0, preserve the six unresolved aliases in order,
derive source/date from the actual native candidate, and explicitly clear
the stale July ChEBI validation stamp. The native generator carries that
stamp forward; the cleared value is a separately reviewed curation override.
The historical basis and independent decision are in stamp-evidence/.
Identities, other rows, policy history and scientific holds remain unchanged.

The guarded source writer and promoter are execution-time tools bound to the
original root, source/projection logs, journals, pinned producer, and the
generation checkpoint. Their original replay requires those exact inputs.
They do not promise portable reconstruction from a squash checkout. Published
native mapping-change receipts and review consumers must instead replay from
committed inputs and the durable main baseline without a feature checkpoint.
Independent final consumer portability checks remain required.

Native integration tests use two explicit producer contexts: the historical
`MIM_OWNED_NAME_PRODUCER_ROOT` remains pinned to Claw
`9bd09b2ba163212a65289b91313f98cb0937476f`, while
`MIM_STOCK_CAS_PRODUCER_ROOT` identifies the isolated stock-CAS producer at
`33be66ab1b993e2a47792c13daa3e4f39635f2cb`. The stock fixture refuses the wrong
revision and never substitutes the historical context (#1103). This does not
change either production pin or the identities of earlier execution receipts.

At the source-corrected endpoint, the actual unified freshness check reports
26 changed owners against a limit of 25. The approved plan forbids step 7
snapshot changes. Snapshot and provenance are preserved; this is an unresolved
publication/merge blocker, not authorization to weaken the gate or restamp
provenance. No scientific approval is added by execution receipts.
