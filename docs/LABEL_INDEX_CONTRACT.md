# `docs/data/label_index.csv` — consumption contract

The published answer to *"a recipe says this string; which ingredient is it?"*

MediaIngredientMech is the source of truth for ingredient→ontology mappings, and
this file is how a sibling repo consumes them. It exists because the
record-shaped exports cannot express the question: a record has one
`preferred_term` and many synonyms, so the ambiguity is **per label**, not per
record (#232).

## Columns

| column | meaning |
|---|---|
| `label` | the raw string a recipe might contain |
| `match_type` | how the label reached the record — `preferred_term`, `synonym`, or `ontology_label` |
| `identifier` | **the value to trust.** The record's primary key, and in MIM that IS the ontology CURIE for mapped records |
| `preferred_term` | the record's own name, for display and debugging |
| `ontology_id` | the mapped term; empty for unmapped records |
| `mapping_status` | see below — do **not** filter on this naively |
| `ambiguity` | whether the first row can be trusted for this label — see below |

## Precedence: take the FIRST row for a label

Rows for one label are contiguous and ordered most-significant-first. A consumer
takes the first and stops. The order is:

0. **Ownership.** A row whose `match_type` is `preferred_term` — i.e. a record
   whose own name IS this label — outranks everything, including status.
1. `MAPPED` before any other status
2. `preferred_term`, then `synonym`, then `ontology_label`
3. `identifier`, then `preferred_term` — a deterministic tie-break, because
   `identifier` is not unique across records (tombstones share the winner's)
4. `label` (the raw, case-preserving string) — final tie-break only

Note (1) outranks (2): a live record's `ontology_label` beats a tombstone's
`synonym`. That is deliberate.

**Why (0) sits above (1).** A record that owns the label makes a claim about
exactly that string; a synonym or term-label on a *different* record is a weaker
claim about something else. A tombstone still resolves — see the next section —
so preferring it over an unrelated live record loses nothing. Without rule (0),
`FeSO4 x 7H2O` resolved to `CHEBI:75832` *FeSO4 x 5 H2O*: a heptahydrate label
answered with the pentahydrate. `MnSO4 x 1 H2O` and `NiCl2 x 6 H2O` failed the
same way.

Rule (0) is narrower than "match_type beats status" on purpose. Promoting
`match_type` wholesale would also let a tombstone's `synonym` beat a live
record's `ontology_label`, which sent `EDTA disodium salt (anhydrous)` back to
the rejected dihydrate. Only rank 0 jumps the queue.

**Why (4) sits last.** It used to sort second, above every semantic key, so
among case variants of one label plain ASCII picked the winner and uppercase
won: `FRUCTOSE` (a synonym on *Fructooligosaccharides (FOS)*) outranked
`Fructose`, the owning record, and `ASPARAGINE`/`CYSTEINE` returned the
L-enantiomer for a stereo-unspecified label. 16 labels resolved to the wrong
record. Grouping is by lowercased label, so contiguity never depended on
sorting the raw string early.

These rules are pinned by `tests/test_label_index_precedence.py`, which builds
records in memory — asserting against the published CSV would pass trivially
after any regeneration.

## `ambiguity` — when *take the first row* does not hold

Precedence answers every label a record **owns**. It cannot answer a label no
record claims, where the first row is a deterministic but arbitrary pick among
competitors. This column says which case you are in, so the 2% that are
genuinely undecided can be refused rather than trusted like the rest.

| value | labels | meaning |
|---|---:|---|
| `unique` | 8,052 | one identifier. Nothing to choose. |
| `resolved:owned` | 97 | several identifiers, but a record's own `preferred_term` **is** this label, and it sorts first. Trust it. |
| `agree:same_substance` | 12 | competitors have the **same molecular formula** — one substance, modelled twice (e.g. `L-Cysteine` and `L-cysteine zwitterion`, both C3H7NO2S). Either pick is right. |
| `conflict:different_substances` | **167** | competitors have **different formulas**. The first row may be the wrong compound. |
| `unresolved:partial_chemistry` | 32 | only one competitor has a formula, so it could not be decided. |
| `unresolved:no_chemistry` | 8 | no competitor has a formula (mixtures, environmental terms, registry mints). |

**Treat `conflict:different_substances` as "this label does not identify one
substance".** It is the salt-inheritance pattern: a free acid's systematic name
is carried as a synonym by its salts, so asking for the acid can hand you a
salt.

```
(2S)-2-aminobutanedioic acid   CHEBI:17053      C4H7NO4     L-Aspartic acid
                               cas:1115-63-5    C4H6KNO4    L-Aspartic acid potassium salt
                               cas:323194-76-9  C4H8NNaO5   L-Aspartic acid sodium salt monohydrate
```

Nothing is suppressed and no curation was deleted — the ambiguity is published
rather than resolved by guess. Which of the competitors a given recipe means is
a curation question, tracked in #232.

Note the verdict is per **label**, so every row sharing a label carries the same
value. `unresolved:*` means *we could not check*, not *they agree* — a third of
records carry no formula, and defaulting those to agreement would have blessed
exactly the collisions this column exists to expose.

### Residual ambiguity this does NOT resolve

336 labels still map to more than one identifier. Precedence now answers every
one where a record *owns* the label (96 of them, previously 80). The other 240
are labels no record claims as its `preferred_term` — typically a systematic
name carried as a synonym by several salts or hydrates of one parent, e.g.
`(2R)-2,3-dihydroxypropyl dihydrogen phosphate` on both the lithium and
bis(cyclohexylammonium) salts of sn-glycerol 3-phosphate. For those the first
row is a deterministic but arbitrary pick among near-equivalent answers.
Tracked in #232; do not read a first row as "unambiguous".

## `mapping_status: REJECTED` does not mean "no answer"

It means the record is a tombstone — merged away, or retired as invalid. For a
**merged** record the `identifier` already points at the merge target, so the row
still resolves correctly and should be followed.

Dropping REJECTED rows is a mistake that has been made: it is what published
`Glucose` (2,120 occurrences) as unresolvable in culturebotai-claw#67.

The exception is a record retired as *invalid* rather than merged — those carry
an `UNMAPPED_NNNN` identifier, which resolves to nothing by design.

## `match_type: ontology_label`

The mapped term's own label, added in #365. Many records are named by formula
(`KOH`, `KI`, `NaH2PO4•H2O`) while consumers write the chemical name, and that
name appears nowhere else on the record — neither preferred_term nor synonym.
754 rows; 623 labels became resolvable that were not before.

It ranks last because it is the ontology's name for the concept, not a name the
record claims.

## Freshness

Regenerated by `just export-lists` on every export and gated in CI by
`scripts/check_flat_export_coverage.py`, which regenerates into a temp directory
and diffs. A stale index cannot land.

## Known limits

* **Normalising the label discards information.** Stripping non-alphanumerics
  collapses `Na2MoO4·2H2O` and `Na2MoO4 x 2 H2O` to one key, which are different
  hydration states in general. Match on the exact string first; normalise only
  as a fallback, and treat a normalised hit as weaker evidence.
* **Not every MIM record is here.** Records with no label cannot be indexed, and
  a handful of names a consumer knows may simply be absent from MIM — see
  CultureBotAI/CultureMech#260 for the coverage gaps found when this contract was
  agreed.
