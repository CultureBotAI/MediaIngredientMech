# MIM Mapping Semantics

This document is the authoritative reference for what the predicates in
`mappings/ingredient_mappings.sssom.tsv` actually mean, why MIM uses a
**registry/identity row pattern** alongside ontology mappings, the most common
mistakes a curator can make, and what to do when CI rejects a row.

It is written for a curator who has never read the kg-microbe code. You should
not need to look at any other repository to understand the rules. Where a rule
is enforced by the SSSOM validator (`scripts/validate_sssom_invariants.py`),
the rule's identifier (Rule A, B1, B2, B3, B4) is given inline so you can match
a CI failure to the section that explains it.

> **Status of validator rules**: only **Rule A** is currently implemented in
> `scripts/validate_sssom_invariants.py` and enforced by CI. **Rules B1–B4**
> are *planned/deferred* — described here so curators can write conformant
> mappings and so the next validator PR has a documented contract to satisfy.
> Sections below mark each B-rule's enforcement status explicitly.

The SSSOM file has the following columns; every example below uses these:

```
subject_id  subject_label  predicate_id  object_id  object_label  object_source  mapping_justification  source  mapping_date  confidence  comment  other  validation_method
```

A "row" is one tab-separated line in that file.

---

## 1. Predicate semantics

MIM uses four [SKOS](https://www.w3.org/2004/02/skos/) mapping predicates.
Their meanings are **not interchangeable** — picking the wrong one corrupts
the downstream graph. Each predicate has a precise behavioral contract that
both producers (the claw builder, human curators) and consumers (kg-microbe's
`consolidate_chemical_mappings.py`, KGX exports, CommunityMech joins) rely on.

### `skos:exactMatch`

> **MIM:X and Y denote the SAME entity. Bidirectional substitution is safe in
> any graph context.**

If `MIM:Glucose skos:exactMatch CHEBI:17234` is present, then for any
graph operation, `MIM:Glucose` and `CHEBI:17234` are interchangeable: same
node identity, same incoming edges, same outgoing edges. A consumer is free
to drop one of the two CURIEs and rewrite all triples to the other.

Use `skos:exactMatch` when:

- The MIM ingredient and the ontology term are the same chemical/material at
  the same level of specificity (e.g. `MIM:Glucose` ↔ `CHEBI:17234 "glucose"`,
  `MIM:Sodium_chloride` ↔ `CHEBI:26710 "sodium chloride"`).
- You are emitting a **registry/identity row** (see Section 2), pairing a
  `MIM:<slug>` subject with its `kgmicrobe.{ingredient,compound}:<slug>`
  primary id.

Do **not** use `skos:exactMatch` when:

- The ontology term is a parent/broader category and the MIM ingredient is a
  more specific child (use `skos:narrowMatch`).
- The two terms refer to similar but distinct entities (use `skos:closeMatch`).

### `skos:closeMatch`

> **MIM:X and Y are similar but not identical. DO NOT substitute one for the
> other in a graph; the relationship is informational.**

If `MIM:X skos:closeMatch Y` is present, a consumer may surface the link
to a human (e.g. "see also Y") but **must not** merge the two nodes,
re-route edges, or treat them as the same identity.

Use `skos:closeMatch` when:

- Two ingredients are related but not at parent/child level — different
  hydration states, different stereoisomers where stereochemistry matters
  for downstream use, near-synonyms whose biological roles diverge.
- You want to record a related ontology term for human reference without
  asserting any formal subsumption.

Do **not** use `skos:closeMatch` as a "soft exactMatch" when you are unsure.
If you are unsure, the correct action is to leave the row out and flag the
ingredient for review, not to weaken the predicate.

### `skos:narrowMatch`

> **MIM:X is a kind-of Y (Y is the broader/parent term). Used to anchor MIM
> children to OBO parents. Downstream consumers MUST emit this as
> `biolink:subclass_of` (or `rdfs:subClassOf`), NEVER as identity.**

This predicate is **asymmetric**: substitution is only legal in one
direction (specific → general for inference like "Vermont Soil is soil"),
and even that direction is only valid for subclass-of reasoning, not
identity. The MIM child and the ontology parent are **different graph
nodes**.

Use `skos:narrowMatch` when:

- The MIM ingredient is more specific than any available ontology term
  and you want to anchor it to the closest parent. Example: there is no
  CHEBI/ENVO term for "Vermont Soil" specifically, so `MIM:Vermont_Soil`
  narrowMatches `ENVO:00001998 "soil"`.
- You are asserting subclass-of, not identity. The parent term retains
  its own identity; the MIM subject does not collapse into it.

Do **not** use `skos:narrowMatch` when:

- A more specific ontology term exists. Find that term and use
  `skos:exactMatch` instead.
- The MIM ingredient is a sibling of the ontology term, not a child.
- You omit the registry row (Section 2). Every `narrowMatch` from a
  `MIM:<slug>` subject **must** be accompanied by a registry exactMatch
  row. This is enforced by **Rule B1**.

### `skos:broadMatch`

> **Inverse of narrowMatch. MIM:X is broader than Y; Y is a kind-of MIM:X.**

Used rarely in MIM, since the typical pattern is "MIM ingredient → OBO
parent" (i.e. narrowMatch). The semantic guarantee is symmetric to
narrowMatch: asymmetric, subclass-of only, not identity. If you find
yourself reaching for `broadMatch`, double-check that the relationship
is actually broad-to-narrow in the direction the row claims, and not a
mislabeled `narrowMatch`.

---

## 2. Registry/identity row pattern

MIM uses two **independent kinds of mapping rows** for any ingredient that
also asserts a `narrowMatch` to an OBO term:

1. **Ontology row** — `MIM:<slug> skos:narrowMatch <ENVO|CHEBI|FOODON|…>:<id>`
   anchors the MIM child to its OBO parent. The object_id is an external
   ontology term.
2. **Registry/identity row** — `MIM:<slug> skos:exactMatch
   kgmicrobe.{ingredient,compound}:<slug>` declares that the MIM subject
   has its own primary id in the kg-microbe namespace. The object_id is a
   first-class kg-microbe CURIE.

The registry row is **mandatory** whenever the same MIM subject also
asserts any narrowMatch. This will be enforced by **Rule B1** of the
SSSOM validator (planned — the current validator implements Rule A
only; Rule B1 lands in the Group B follow-up PR). Until Rule B1 is
in place curators are asked to follow this convention by hand. The
registry row is also the **single channel** by which downstream
consumers resolve a MIM subject to its kg-microbe primary id without
conflating it with the OBO parent.

### Worked example: `MIM:Vermont_Soil`

`MIM:Vermont_Soil` is one of many soil-source ingredients in the MIM
data set. There is no ENVO term for Vermont soil specifically; the
closest parent is `ENVO:00001998 "soil"`. Vermont_Soil is mapped using
**two rows** in `mappings/ingredient_mappings.sssom.tsv`:

```tsv
subject_id      subject_label  predicate_id      object_id                          object_label  object_source  mapping_justification        source                                                                                                          mapping_date  confidence  comment
MIM:Vermont_Soil  Vermont Soil  skos:narrowMatch  ENVO:00001998                       soil          obo:envo.owl   semapv:ManualMappingCuration  MIM:cbclaw_envo_promotion|MIM:specificity-loss-review (mint_kgm_ingredient)|MIM:curator=auto_classify_ingredient_type  2026-05-02    0.9
MIM:Vermont_Soil  Vermont Soil  skos:exactMatch   kgmicrobe.ingredient:vermont_soil  Vermont Soil  kgm:ingredient  semapv:ManualMappingCuration  MIM:cbclaw_envo_promotion|MIM:specificity-loss-review (mint_kgm_ingredient)|MIM:curator=auto_classify_ingredient_type  2026-05-02    0.99        Registry/identity row preserving kgmicrobe.ingredient:vermont_soil alongside parent ENVO:00001998.
```

What the two rows together say:

- "Vermont Soil **is a kind of** soil" — the narrowMatch row.
- "Vermont Soil **also has a kg-microbe primary id**, namely
  `kgmicrobe.ingredient:vermont_soil`, distinct from the parent
  `ENVO:00001998`" — the registry row.

### Why both rows are required

Imagine the registry row were missing — only the narrowMatch row exists.
A downstream consumer that calls `find_chebi_by_name("Vermont Soil")`
walks the SSSOM by `subject_label`, finds the narrowMatch row, and
returns its `object_id`: **`ENVO:00001998`** (the parent "soil"). The
consumer has now silently substituted the parent for the child. Every
recipe that uses Vermont Soil will be indexed against the generic
"soil" node, the Vermont-specific identity is lost, and any downstream
graph join treats Vermont Soil and (say) Cape Cod Soil and Amazon
Rainforest Soil as the same node. This is exactly the bug Codex
adversarial review #558 round 3 flagged.

With the registry row present, the same consumer call resolves to the
exactMatch row first and returns `kgmicrobe.ingredient:vermont_soil` —
the child's own primary id. The narrowMatch row is then available
separately for subclass-of inference, but it is no longer the only path
from the MIM subject to a CURIE.

### Naming convention

The registry CURIE always uses the same slug as the MIM subject:

- `MIM:Vermont_Soil` → `kgmicrobe.ingredient:vermont_soil`
- `MIM:Glucose` → `kgmicrobe.compound:glucose`
- `MIM:KH2PO4` → `kgmicrobe.compound:kh2po4`

Slug normalization: lowercase, underscore-separated, no special
characters. The `ingredient` vs `compound` namespace split mirrors the
type assigned by the auto-classifier (`scripts/classify_ingredient_type.py`
in claw): pure compounds use `kgmicrobe.compound:`, complex/biological
materials use `kgmicrobe.ingredient:`.

---

## 3. Common mistakes

Each of the four most common mistakes a curator (or an automated
pipeline) makes is below, with a worked TSV example, the rule that
catches it, and the antidote. When CI rejects a row, the reject_reason
column names the rule that fired; this section explains each rule by
id.

Today only **Rule A** rejects produce entries in
`mappings/needs_curator_review.tsv` — that's the only rule the current
validator implements. The B-series rule ids referenced below (B1, B2,
B3, B4) describe planned enforcement that will land with the Group B
follow-up PR. The TSV examples and antidotes still apply now (they
describe correct curation regardless of validator coverage); only the
"CI rejects this" claim is deferred for the B-series.

### Mistake 1 — Auto-classifier label drift (Rule A)

The auto-classifier scripts in claw
(`scripts/classify_ingredient_type.py`,
`scripts/categorize_residual_p25.py`) sometimes propose mappings where
the subject and object share **zero token overlap**, indicating the
proposed object is not actually related to the subject. The most
notorious example: a row that maps `MIM:KH2PO4` (potassium phosphate
monobasic) to `CHEBI:31346 "calcium sulfate dihydrate"`:

```tsv
subject_id     subject_label                     predicate_id      object_id     object_label              object_source  mapping_justification        source                                          mapping_date  confidence
MIM:KH2PO4     potassium phosphate monobasic     skos:narrowMatch  CHEBI:31346   calcium sulfate dihydrate  obo:chebi.owl  semapv:ManualMappingCuration  MIM:curator=auto_classify_ingredient_type  2026-05-02    0.85
```

`subject_label` = "potassium phosphate monobasic"; `object_label` =
"calcium sulfate dihydrate". After lowercasing and stop-word removal,
the token sets are `{potassium, phosphate, monobasic}` and
`{calcium, sulfate, dihydrate}`. Intersection: empty. The `source`
column carries `MIM:curator=auto_classify_ingredient_type`, so this is
a machine-generated proposal with no human review.

**Rule A** rejects the row. The validator demands at least one of:

- `confidence` ≥ 0.95, OR
- token overlap ≥ 1 between `subject_label` and `object_label`, OR
- a non-auto curator tag in `source` (a human touched the row), OR
- an independent CAS-RN or PubChem CID xref in the subject's MIM YAML
  (`chemical_properties.cas_rn` or `chemical_properties.pubchem`)
  that corroborates the chemistry from a registry other than the
  ontology.

None of those is satisfied here, so the row goes to
`mappings/needs_curator_review.tsv` with
`reject_reason = "Rule A: zero token overlap, no human curator, no CAS/PubChem corroboration"`.

**Antidote**: do not merge the row. Either (a) re-curate the mapping
(KH2PO4 should map to CHEBI:63036 "potassium dihydrogen phosphate" or
its parent), (b) add `chemical_properties.cas_rn` to the YAML if a
registry confirms the chemistry, or (c) leave the row in
`needs_curator_review.tsv` and reject the proposal.

### Mistake 2 — Double-typed pair (Rule B2)

A pair of rows for the same `(subject_id, object_id)` under two
different predicates says contradictory things. Most commonly,
the same MIM subject is asserted to be **both** identical to and a
child of the same ontology term:

```tsv
subject_id          subject_label  predicate_id      object_id      object_label  object_source  mapping_justification        source                                  mapping_date  confidence
MIM:Vermont_Soil    Vermont Soil   skos:exactMatch   ENVO:00001998  soil          obo:envo.owl   semapv:ManualMappingCuration  MIM:cbclaw_envo_promotion           2026-05-02    0.9
MIM:Vermont_Soil    Vermont Soil   skos:narrowMatch  ENVO:00001998  soil          obo:envo.owl   semapv:ManualMappingCuration  MIM:specificity-loss-review        2026-05-02    0.9
```

Both rows have the same `(subject_id, object_id) = (MIM:Vermont_Soil,
ENVO:00001998)`. The first row asserts identity; the second asserts
parent/child. They cannot both be true.

**Rule B2** rejects this: at most one row per `(subject_id, object_id)`
pair. **Rule B3** also rejects this specific shape: for any subject
`MIM:<slug>` and any OBO-parent target `Y`, if `narrowMatch Y` is
asserted, then `exactMatch Y` must NOT be.

**Antidote**: pick `narrowMatch` (the parent IS broader; Vermont Soil
is not literally identical to all soil) and remove the `exactMatch`
row. Then add the registry row to
`kgmicrobe.ingredient:vermont_soil` per Section 2.

### Mistake 3 — Missing registry row (Rule B1)

A `narrowMatch` row is present, but no registry exactMatch row
accompanies it:

```tsv
subject_id          subject_label  predicate_id      object_id      object_label  object_source  mapping_justification        source                       mapping_date  confidence
MIM:Vermont_Soil    Vermont Soil   skos:narrowMatch  ENVO:00001998  soil          obo:envo.owl   semapv:ManualMappingCuration  MIM:cbclaw_envo_promotion  2026-05-02    0.9
```

That's the only row for `MIM:Vermont_Soil`. There is no second row
mapping `MIM:Vermont_Soil` to a `kgmicrobe.{ingredient,compound}:`
CURIE. As described in Section 2, this means downstream consumers
that resolve "Vermont Soil" by `subject_label` get back the parent
`ENVO:00001998` instead of a Vermont-specific child id.

**Rule B1** rejects this: every `MIM:<slug>` subject that has any row
must have exactly one row of the form `MIM:<slug> skos:exactMatch
kgmicrobe.{ingredient,compound}:<slug>`.

**Antidote**: mint the registry CURIE first, then add the registry row.
For Vermont_Soil, mint `kgmicrobe.ingredient:vermont_soil` (lowercased,
underscored slug) and add:

```tsv
MIM:Vermont_Soil    Vermont Soil   skos:exactMatch   kgmicrobe.ingredient:vermont_soil    Vermont Soil    kgm:ingredient   semapv:ManualMappingCuration  MIM:cbclaw_envo_promotion|MIM:specificity-loss-review (mint_kgm_ingredient)  2026-05-02    0.99    Registry/identity row preserving kgmicrobe.ingredient:vermont_soil alongside parent ENVO:00001998.
```

Both rows now coexist for the same MIM subject and play complementary
roles per Section 2.

### Mistake 4 — Locally-edited object_label (Rule B4)

A curator hand-edits the `object_label` to a non-canonical synonym, or
the ontology has updated its primary label and MIM still carries the
old one:

```tsv
subject_id          subject_label  predicate_id      object_id      object_label  object_source  mapping_justification        source                       mapping_date  confidence
MIM:Vermont_Soil    Vermont Soil   skos:narrowMatch  ENVO:00001998  soils         obo:envo.owl   semapv:ManualMappingCuration  MIM:cbclaw_envo_promotion  2026-05-02    0.9
```

`object_label = "soils"` instead of the canonical ENVO label `"soil"`.

**Rule B4** *will* flag this once it lands in the Group B follow-up
PR. The planned design: when the local kg-microbe ontology transforms
are present (`../kg-microbe/data/transformed/ontologies/envo_nodes.tsv`
in this case), the validator will look up the canonical label and
exact-synonym set for `ENVO:00001998` and reject rows where
`object_label` matches neither. In CI environments without those
transforms (the typical case on PR CI), Rule B4 will emit a warning
and skip, so the rule will not block PRs that don't have access to
the canonical label source. The current validator implements Rule A
only; Rule B4 is not yet enforced.

This rule prevents the "stale child label leaking onto parent"
pollution that kg-microbe's `purge_asymmetric_pollution()` exists to
clean up: if a curator typed in "Vermont soil" as the `object_label`
of a `narrowMatch ENVO:00001998` row, downstream consumers might index
"Vermont soil" against the ENVO parent — exactly the kind of identity
collapse Section 2 describes.

**Antidote**: use the canonical OBO-published label
(`object_label = "soil"`). Do not hand-edit the label to match the
subject; use a synonym already registered in the ontology, or update
`subject_label` if the ingredient really should be more general.

### Why this list is short on purpose

Other mistakes exist (wrong predicate direction, malformed CURIE
prefixes, missing required columns), but they are caught by the
SSSOM toolchain before they reach this validator. The four mistakes
above are the ones that pass syntactic checks and break **graph
semantics** downstream. Rule A through Rule B4 exist specifically to
catch those.

---

## 4. Curator workflow

When CI rejects a row, the validator writes the row plus a
`reject_reason` column to `mappings/needs_curator_review.tsv` and exits
with code 2 (CI-blocking). The PR will not merge until the row is
resolved. You have three options.

### Option A — Fix the YAML and let claw regenerate

This is the right option when the row reflects genuinely incorrect data.

1. Locate the underlying ingredient YAML in
   `data/ingredients/mapped/<Slug>.yaml` (or
   `data/ingredients/unmapped/<Slug>.yaml` for in-progress entries).
   The MIM subject id maps directly to the file stem:
   `MIM:Vermont_Soil` → `data/ingredients/mapped/Vermont_Soil.yaml`.
   Note that filenames preserve the slug case from the subject id
   (`Vermont_Soil`, not `vermont_soil`).
2. Fix the field that produced the bad row. Examples by rule:
   - **Rule A**: re-curate the `ontology_mappings` entry for the
     ingredient — remove the wrong CHEBI/ENVO id and set the correct
     one. If an external CAS-RN or PubChem CID corroborates the
     chemistry, add it under `chemical_properties.cas_rn` /
     `chemical_properties.pubchem` so future reruns of Rule A grant
     benefit-of-the-doubt automatically.
   - **Rule B1**: ensure the YAML's `kgmicrobe_curie` field is set to
     `kgmicrobe.ingredient:<slug>` or `kgmicrobe.compound:<slug>`.
     The claw builder uses that field to emit the registry row.
   - **Rule B2/B3**: pick one predicate. If the ontology term is a
     proper parent, keep the narrowMatch and drop the exactMatch.
   - **Rule B4**: update `object_label` in the YAML's
     `ontology_mappings` entry to the canonical OBO label.
3. Regenerate `mappings/ingredient_mappings.sssom.tsv` from the
   updated YAMLs. The SSSOM build lives in the sibling
   `culturebotai-claw` repository — run from that checkout:
   `cd ../culturebotai-claw && just build-sssom && just publish-sssom`.
   (MIM does not host the builder; only the published TSV.)
4. Re-run the validator: `cd MediaIngredientMech && just qc-sssom`
   (or equivalently, `python3 scripts/validate_sssom_invariants.py`,
   which is what CI invokes). The row should now pass. Commit the
   regenerated SSSOM along with the YAML change.

This is the **default option** and the one the audit trail rewards: the
fix is durable because future regenerations of the SSSOM will produce
the same correct row.

### Option B — Park the row in `needs_curator_review.tsv` for triage

This is the right option when the row may eventually be valid but you
don't have time / context to resolve it now, and you want CI to merge
the rest of the change set without waiting.

1. The validator already wrote the row to
   `mappings/needs_curator_review.tsv` with a `reject_reason` column.
   Leave it there; do not move it back to the main SSSOM.
2. Open a curation issue describing what is needed to resolve the row
   (e.g. "Need a domain-expert review of MIM:Wood_Ash → CHEBI parent
   selection — current auto-classifier proposed wrong target").
3. Reference the issue in your PR description so reviewers know the row
   is parked deliberately, not lost.

The CI gate fails on rows in the **main** SSSOM that violate any rule;
rows that live in `needs_curator_review.tsv` are explicitly exempt.
That is the entire reason the file exists.

### Option C — Reject the proposal entirely

This is the right option when the row should never have been proposed
and there is no underlying ingredient that needs the mapping at all.

1. Delete the offending row from the source YAML's `ontology_mappings`
   list. If the entire ingredient was created in error, also delete the
   YAML file.
2. Regenerate the SSSOM as in Option A.
3. Confirm the row no longer appears in either the main TSV or
   `needs_curator_review.tsv` after regeneration.

This option is more invasive than B (it deletes data, not just parks
it) so reach for it only when you are sure. If in doubt, use Option B
and let the curation issue surface the question.

### Reading the validator output

`just qc-sssom` (and the equivalent direct invocation
`python3 scripts/validate_sssom_invariants.py`) print a per-row
report to stderr. The current implementation emits a single FAIL
header followed by one line per rejected row:

```
FAIL: 1 row(s) in ingredient_mappings.sssom.tsv fail Rule A (auto-classifier token-overlap gate).
  row 47: MIM:KH2PO4 'potassium phosphate monobasic' -> CHEBI:31346 'calcium sulfate dihydrate' — zero token overlap; no human curator; no CAS/PubChem corroboration
```

Exit codes:
- **0** — all rows pass.
- **1** — input file not found (configuration error).
- **2** — one or more rows reject; the violating rows are written
  to `mappings/needs_curator_review.tsv` with a `reject_reason`
  column and CI fails.

There is currently no exit-code 1 "warnings only" mode; the planned
Rule B4 warn-and-skip behaviour will introduce it when Group B
lands. Match each `row N` line to its rule id (currently always
Rule A) to find the antidote.

### Where the rules live

- **Validator implementation**: `scripts/validate_sssom_invariants.py`
  (Rule A only today; Rules B1–B4 deferred to the Group B PR).
- **Justfile recipe**: `just qc-sssom` runs the validator; `just qc`
  runs it as part of the full quality-check composite.
- **CI workflow**: `.github/workflows/qc-sssom.yaml` invokes
  `python3 scripts/validate_sssom_invariants.py` directly (it does
  not call `just`) on every PR that modifies
  `mappings/ingredient_mappings.sssom.tsv`,
  `mappings/needs_curator_review.tsv`, or
  `scripts/validate_sssom_invariants.py`, and on every push to `main`.

If you need to add a new rule (e.g. enforcement of a new mapping
convention introduced by a future curation pass), follow the existing
Rule A / Rule B-series pattern: name the rule, define what it catches
in plain terms here, implement it in
`scripts/validate_sssom_invariants.py`, and update the CI workflow only
if the rule needs additional inputs (it usually does not).

---

## See also

- `scripts/validate_sssom_invariants.py` — the validator that enforces
  every rule named here.
- `mappings/ingredient_mappings.sssom.tsv` — the published SSSOM.
- `mappings/needs_curator_review.tsv` — triage queue for rejected rows.
- `docs/CURATION_GUIDE.md` — broader curation workflow (this file is
  scoped to mapping semantics specifically).
