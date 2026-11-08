# Collision and dependency supplement

This supplement distinguishes identifier equality from an unresolved active-owner conflict. It does not alter any primary decision, proposal, independent review, owner or publication selector. Exact owner bytes are preserved under `owners/`; `owner-dependencies.json` records their hashes, every matching JSON pointer and all ten immutable shard hashes.

| Proposed owner | Other owner sharing the identifier | Assessment and integration obligation |
|---|---|---|
| `Feso4_X_7_H2o.yaml`, MAPPED, CHEBI:75836 | `Feso4_X_7h2o.yaml`, REJECTED | The rejected record's `MERGED_INTO` history names the active seven-water owner, with transferred occurrences and withdrawn SSSOM rows. This is an existing merge record, not two active owners needing another merge. The proposed balanced seven-water alias belongs only on the active owner. Preserve rejection, prior transfer history and all source holds; do not count or transfer occurrences again. |
| `Niso4_X_6_H2o.yaml`, REJECTED, CHEBI:53437 | `Nickel_II_sulfate_hexahydrate.yaml`, MAPPED | The proposal corrects stale six-water chemistry on the rejected merge record only. The active survivor already carries six-water formula, InChI and SMILES. Preserve the rejected status and zero-publication scope; this proposal neither reactivates the record nor creates another active identity. Its priority is archival consistency, distinct from the active heptahydrate structure defect. |
| `Nh42ni_So42_X_6_H2o.yaml`, MAPPED, CHEBI:86149 | `Nh42ni_So42.yaml`, MAPPED | This is an unresolved active-owner form conflict already tracked by [#1050](https://github.com/CultureBotAI/MediaIngredientMech/issues/1050). The bare label omits hydration, and its conflicting CAS evidence is not independently settled. The new explicitly balanced six-water aliases do not prove the bare cohort is anhydrous or hexahydrate. Keep #1050 suppression/merge holds, retain the rejected bare-formula synonym on the explicit owner, and do not merge by shared CURIE or rewrite CAS 56110-30-6. |

The exact-path dependency scan read all 10 immutable shards, containing 1,879 cases, independently of gitignore. All matches for these six owner paths occur within worker 02; no other worker shard contains an exact reference to them. This is a dependency enumeration, not review of any other worker's scientific cases, and not a claim that source-only cases elsewhere cannot concern the same substances.

| Frozen owner path suffix | Exact reference count | Distinct cases | Worker slots |
|---|---:|---:|---|
| `Feso4_X_7_H2o.yaml` | 0 | 0 | none |
| `Feso4_X_7h2o.yaml` | 3 | 1 | 02 |
| `Niso4_X_6_H2o.yaml` | 6 | 2 | 02 |
| `Nickel_II_sulfate_hexahydrate.yaml` | 7 | 1 | 02 |
| `Nh42ni_So42.yaml` | 5 | 1 | 02 |
| `Nh42ni_So42_X_6_H2o.yaml` | 8 | 2 | 02 |

Reference counts include repeated fields inside a case; they are not ingredient occurrence counts. Exact source identities, case IDs and baseline owner hashes are in the JSON companion. No reference was reassigned to a different worker or owner.

The recorded strict-schema and canonical-label results do not settle these boundaries. In particular, unchanged MICRO:0000520 adapter unavailability remains a separate gate for clarified rumen fluid, and the explicit source-alias review does not supply that missing native grounding result. All changed-owner support-withdrawal, full-payload, duplicate-owner and publication obligations remain.

Issue triage is in `finding-triage.json`. O-carbamyl-D-serine warrants a new bounded finding after the recorded name/ID searches found no matching issue. Nickel chemistry is an existing #321/history and SEM residual, so its draft updates that tracker rather than claiming a new defect class. Both foreign alum fragments are already explicitly listed in #811; the draft updates #811 and preserves SEM:15761b556078b9a904a8. No issue or comment was posted by this follow-up.
