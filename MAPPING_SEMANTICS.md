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

> **Status of validator rules**: Rules A, B1, B2, B3, and B4 are all
> implemented in `scripts/validate_sssom_invariants.py` and enforced by
> CI. Rule B1 is strict-by-default (a missing registry row contributes
> to exit-2). Rule B4 silently skips per-prefix when the kg-microbe
> ontology transform file isn't checked out locally — typical in CI —
> and is therefore best-effort there. Sections below describe each
> rule's contract.

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

- Two ingredients are related but not at parent/child level — near-synonyms
  whose biological roles diverge, or a record retaining a related term for
  human reference.
  **Not** for hydration states or stereoisomers where a specific term exists:
  Section 3 requires those to take their own identifier rather than a weakened
  predicate against the parent.
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
asserts any narrowMatch. This is enforced by **Rule B1** of the SSSOM
validator (strict-by-default — a missing registry row makes CI
fail). The claw SSSOM builder
(`culturebotai-claw/scripts/build_mim_ingredient_sssom.py`,
`_row_from_yaml`) emits the registry row automatically whenever it
emits a narrow/broad parent row, so a curator who lets the builder
generate the SSSOM does not need to write the registry row by hand.
The registry row is also the **single channel** by which downstream
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

## 3. Identity granularity — one record per substance

Section 2 says how to express "MIM's thing is more specific than the ontology's
thing". This section says **when** that applies, and settles a cluster of
questions that were being answered case by case: hydrates, salts, stereoisomers,
two records sharing an id, and one substance under two ids.

### The rule

> **One MIM record per distinct substance. A record's `identifier` is the most
> specific stable id that denotes *that* substance. Never express a more
> specific thing by sharing a broader term's identifier.**

### What counts as "a distinct substance": orderability

MIM is a **practically oriented** resource. Its consumers are building growth
media, so a record should denote **a specific chemical someone can order** —
and where the sources disagree about which form that is, **pick one by
convention** rather than splitting the record or retreating to a generic term.

**The operative test is the CAS a lab would buy.** When two ontology terms
describe the same purchasable substance at different granularity, prefer the one
carrying the commercial CAS.

Worked example (#394). `Carboxymethyl cellulose` has four source occurrences and
they do not agree: two write it plain (KOMODO 1111, DSMZ 1111) and two write
"sodium salt" (JCM 1052, DSMZ 1684) — and DSMZ 1111's own preparation note
specifies the sodium salt anyway. Upstream, CultureBotHT's `compounds_to_cas.csv`
already maps both the plain and the sodium name to the same CAS. The record
resolves to **CHEBI:234035** because it carries `cas:9004-32-4`, the product on
the shelf; the plain term `CHEBI:85146` carries `cas:9000-11-7`, which is a
different purchase.

**This does not license collapsing genuinely different products.** A hydrate and
its anhydrous form have different CAS numbers, different formula weights, and are
ordered separately — they stay separate records, and the rest of this section
governs them. Orderability breaks ties about *which term names one purchasable
thing*; it does not merge two things a curator would buy from different catalogue
lines.

**The counterweight is mandatory: keep the detail.** Conflating is about the
record's *identity*, never about discarding information. Every raw form stays a
synonym, so `label_index` still answers for the plain string and the salt string
alike, and the SSSOM keeps its asymmetric rows to the broader terms. A record
that conflates without preserving its synonyms has lost data, not simplified it.

Sharing the parent's id is the identity-collapse bug of Section 2, arriving by a
different route. `MgSO4·7H2O` mapped to `CHEBI:32599 magnesium sulfate` does not
say "a hydrate of magnesium sulfate"; it says "this **is** magnesium sulfate",
and every downstream join then treats 246.47 g/mol and 120.37 g/mol as one node.
Formula weight is exactly what a medium recipe depends on.

The contrast is in the data: `MgSO4 x 7 H2O` sits on `CHEBI:31795 magnesium
sulfate heptahydrate` and is **correct** — a specific term existed and was used.
`MgSO4·7H2O` is the same substance on the generic term, and is the defect.

### Decision procedure

Work down the list and stop at the first that applies.

1. **An ontology term denotes exactly this substance** — including its
   hydration, salt and stereochemical state. Use it: `identifier` = that term,
   `skos:exactMatch`, one row.
   `Sodium glutamate monohydrate` → `CHEBI:232425 monosodium L-glutamate hydrate`.

2. **No exact term, but the substance has its own CAS.** `identifier` =
   `cas:<its own CAS>`, `skos:narrowMatch` to the nearest ontology parent, plus
   the mandatory registry row (Section 2, Rule B1).
   `Sodium hypophosphite monohydrate` → `cas:10039-56-2`, narrowMatch
   `sodium hypophosphite`.

   The registry row's `kgmicrobe.*` CURIE is **not a competing identifier** — it
   is the kg-microbe-namespace handle for the same MIM subject, required by
   Rule B1 and emitted by the claw builder. "One substance under two
   identifiers" in the table below means two *ontology/registry-of-record* ids,
   not the subject's own registry handle.

   **This is already the established pattern**: 34 hydrate-labelled subjects
   carry `cas:` exactMatch plus a parent narrowMatch plus the Rule B1 registry
   row. Note that a further **22** `cas:`-identified hydrate records have no
   parent row and no registry row, and become non-compliant with this step the
   moment it lands — they are a backlog, not counter-examples.

3. **No exact term and no CAS.** Mint `kgmicrobe.compound:<slug>` (pure
   compounds) or `kgmicrobe.ingredient:<slug>` (complex/biological materials),
   `narrowMatch` to the nearest parent, plus the registry row.

4. **The label is genuinely under-specified and an unspecified-sense parent term
   exists** — *and the record carries no independent evidence of which specific
   sense it is*. Then the label denotes the unspecified sense: use that term
   with `exactMatch`, and do not reach for a specific child. A bare `arabitol`
   with no locant is `CHEBI:22605 arabinitol`.

   **The evidence escape hatch is the point, not an exception.** MIM's existing
   `Arabitol` record is grounded to `CHEBI:18403 L-arabinitol` and that is
   correct: it carries `cas 7643-75-6` (ChEBI's own xref for the L-term, present
   from the record's `CREATED` event, so not derived from the mapping) plus five
   independently-swept L-form synonyms. It uses `closeMatch`, which asserts no
   identity. A short label does not override record-level evidence — that is why
   #230 closed as premise-disproven. Apply this rule to a label with *nothing
   else attached*.

5. **The label is under-specified and only specific terms exist.** Emit **no
   mapping row** and set `mapping_status: AMBIGUOUS`. Section 1 is explicit that
   `closeMatch` is not a soft `exactMatch` for when you are unsure — if you
   cannot tell which term is meant, the row must be left out and the record
   flagged, not weakened.
   `2-tetrachloroethane` reaches both `CHEBI:34024` and `CHEBI:36026` and gets
   neither.

### Protonation state (bare anion labels)

Steps 1–5 decide *sense*: hydration, salt form, stereochemistry, locants. They do
not decide **protonation**, and a bare anion label (`Fumarate`, `Aspartate`,
`Succinate`) forces that choice. The rule:

> **Read the parent term's definition.** If it says the anion is obtained by
> deprotonation of **"at least one"** carboxy group, the term is *deliberately*
> protonation-agnostic — it already covers the mono- and di-anion, so a bare
> label belongs on it. **Stay.** If the parent carries no such definition and has
> `X(n-)` children, it is merely unspecified — **descend** to the species present
> at growth-medium pH, following the sibling precedent.

The distinction is not visible offline: the local `chebi.db` carries **no
definitions**, so this test requires the live ChEBI/OLS4 entry.

Worked both ways:

| record | parent | definition | outcome |
|---|---|---|---|
| `Malate` | CHEBI:25115 | "…deprotonation of **at least one**…" | stay |
| `Succinate` | CHEBI:26806 | same | stay |
| `Azelaate`, `Glutarate`, `Oxalate` | — | same | stay |
| `Aspartate` | CHEBI:132943 | **none** | descend → `CHEBI:29995 aspartate(2-)` |
| `Ascorbate` | CHEBI:22651 | — | stay: no `X(n-)` child exists at all |
| `Protocatechuate` | CHEBI:36241 | — | stay: already the −1 anion, nothing below |

`Aspartate` descends on the same evidence its sibling `Glutamate` did — the
family precedent is `CHEBI:29987 glutamate(2-)` — and because 30 bare `-ate`
labels in this corpus sit on charged terms while only the "at least one" group
does not.

**For a salt, the `narrowMatch` parent follows the label**: where the label says
"…Acid sodium salt" the parent is that acid, where it names a neutral compound,
that compound. This avoids the acid-vs-anion choice entirely. Only reach for the
anion when ChEBI has no acid term (`2-oxobutyric acid sodium salt` →
`CHEBI:16763 2-oxobutanoate`).

### What this decides

| Symptom | What it means | Action |
|---|---|---|
| Two records share one identifier | Same substance, or one is more specific | Same → merge. More specific → give it its own id per 1–3. |
| One substance under two identifiers | One of them is wrong | Pick by the precedence in 1–3; re-ground the other. |
| A hydrate/salt sits on the anhydrous/free term | Specificity collapsed into the parent | Step 1 if a specific term exists, else step 2. |
| One label resolves to several identifiers | Legitimate shared synonym, or a real duplicate | If the records are the same substance it is a duplicate — merge. If not, resolve via `docs/data/label_index.csv`: **take the first row for that label** and use its `identifier`. Rows are ordered MAPPED before non-MAPPED, then `preferred_term` before `synonym`, so the first row is the best available answer. That settles 18 of the 87; the rest are synonym-vs-synonym and need a curation decision (#232). |

## What the predicate does downstream (kg-microbe, priority 11)

Read this before choosing a predicate. It is not only a statement about meaning
— it decides what happens to the ontology term in the knowledge graph.

kg-microbe consumes this file as the **authoritative** ingredient-mapping source
(`.claude/skills/chemical-mapping/SKILL.md`, priority 11), syncing it straight
from this repo as a sibling checkout. Its rule:

> symmetric matches (`skos:exactMatch`, `skos:closeMatch`) **overwrite the
> canonical name** with MIM's `subject_label`; asymmetric (`narrowMatch`,
> `broadMatch`) keep the ontology label canonical and add the MIM term as a
> synonym.

So:

| predicate | effect on the ontology term in kg-microbe |
|---|---|
| `skos:exactMatch` / `skos:closeMatch` | **renamed** to MIM's `subject_label` |
| `skos:narrowMatch` / `skos:broadMatch` | keeps its label; MIM's term added as a synonym, and a parent/child edge is emitted |

**2,805 of 2,946 rows are symmetric, and 835 carry a label that differs from the
ontology's** — every one renames a node. That is deliberate: a recipe says `KOH`,
not "potassium hydroxide", and MIM is the naming authority for media
ingredients. But it makes `preferred_term` quality load-bearing in a way it was
not before. A typo in a MIM label becomes the KG's name for that term.

**Consequence for grading.** Over-grading is no longer a private inaccuracy. A
record graded `EXACT_MATCH` against a class term both asserts a false identity
*and* renames the class — the doubled harm behind #322 and #317.

That cuts both ways, so check before regrading in bulk: an `EXACT_MATCH` to a
class term is correct when the MIM record **is** that class. `Aromatic
hydrocarbon` → `CHEBI:33658 "arene"` is one such row, and it does rename the
ChEBI class downstream — deliberately, since MIM is the naming authority and
`aromatic hydrocarbon` is the more recognisable name for `arene`.

### The asymmetric predicates do not follow SKOS, and downstream compensates

This document defines `skos:narrowMatch` as *"MIM:X is a kind-of Y (Y is the
broader/parent term)"*. **SKOS says the opposite**: `skos:narrowMatch` is a
sub-property of `skos:narrower`, so `A narrowMatch B` asserts that **B is
narrower than A**. Under the spec, "MIM:X is a kind-of Y" is `skos:broadMatch`.

Nothing is currently broken, because kg-microbe reads MIM's intent rather than
the spec — its consolidator treats **both** asymmetric predicates identically as
*"the MIM subject is a NARROWER concept than the ontology object"*. The 141
`narrowMatch` rows therefore land correctly.

**Do not "fix" this by flipping the predicates.** That would invert 141 edges in
kg-microbe, which compensates for the current direction. It needs a coordinated
change on both sides, tracked as an issue. The one row that *did* disagree —
the corpus's only `broadMatch` — was regrounded rather than flipped, because the
term it should have used all along made the mapping symmetric and the question
moot.

### What *not* to do

**Do not rename a record so its name matches a term it does not denote.** If
`Sodium glutamate monohydrate` is grounded to the anhydrous term, the fix is to
re-ground the record (step 1 or 2), not to rename it "monosodium L-glutamate".
Renaming destroys the raw label a medium actually used, removes it as an SSSOM
`subject_label` — which is how downstream consumers resolve raw strings — and
converts a visible mapping error into an invisible one.

> **Carve-out: correcting a DAMAGED or foreign-language label.** Since MIM
> became kg-microbe's naming authority, `subject_label` is the KG's canonical
> name for the term a symmetric row points at, so a misspelling or a
> source-language label is published as that ontology term's name. Those may be
> corrected — **and the original kept as a `RAW_TEXT` synonym**, which is what
> makes this compatible with the rule above: the raw string still resolves
> through `label_index`, so nothing a medium used is lost.
>
> The distinction is *what the label denotes*. `1-Naphtylacetic Acid` ->
> `1-Naphthylacetic acid` and `1,3-Butandiol` -> `1,3-Butanediol` name the same
> substance either way; only the spelling changes, and the record does not move.
> Renaming `Sodium glutamate monohydrate` to match an anhydrous term changes
> what is claimed. Correct spelling, never identity.
>
> Keep the SSSOM `subject_id`. Per-record filenames are not renamed
> (`collect_existing_filenames` keeps the existing stem), so a corrected record
> keeps subjects like `MIM:13-Butandiol`. A stable subject matters more than a
> tidy one — re-deriving it from the new label is the #293/#307 mistake and
> silently matches nothing.

**Do not treat a record's auto-derived chemistry as evidence of its identity.**
`AUTO_BACKFILL_CHEBI_CHEMISTRY` copies formula, InChI and SMILES *from the
current mapping*, so they agree with it by construction.

Check `chemical_properties.data_source` before trusting a CAS, too — a
`data_source` of the form `PubChem (via CHEBI:…)` was also derived from the
mapping under test. `MgSO4·H2O` carries `cas_rn 10034-99-8` sourced
`PubChem (via CHEBI:31795)` **and** external-sweep synonyms that are all
*heptahydrate* spellings, so a curator reading both as corroboration would
confirm the wrong term twice. Evidence counts only when its provenance is
independent of the mapping being tested — e.g. a CAS present from the record's
`CREATED` event, or a name lookup on the record's own label.

**Do not conclude a term does not exist without quoting the full search.** The
32 hydrate families exist partly because specific terms were not found; at least
one (`CHEBI:232425`) was in the local build the whole time.

---

## 4. Common mistakes

Each of the four most common mistakes a curator (or an automated
pipeline) makes is below, with a worked TSV example, the rule that
catches it, and the antidote. When CI rejects a row, the reject_reason
column names the rule that fired; this section explains each rule by
id.

Rules A, B1, B2, B3, and B4 are all enforced today; rejects from any
of them produce entries in `mappings/needs_curator_review.tsv` and
make CI fail. The TSV examples and antidotes below apply equally to
each rule.

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

**Rule B4** flags this whenever the local kg-microbe ontology
transforms are present
(`../kg-microbe/data/transformed/ontologies/envo_nodes.tsv` in this
case): the validator looks up the canonical label and exact-synonym
set for `ENVO:00001998` and rejects rows where `object_label`
matches neither. In CI environments without those transforms (the
typical case on PR CI), Rule B4 emits a warning and skips per-prefix,
so the rule does not block PRs that don't have access to the
canonical label source.

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

## 5. Curator workflow

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
   - **Rule B1**: regenerate the SSSOM via the claw builder — its
     `_row_from_yaml` synthesizes the
     `kgmicrobe.{ingredient,compound}:<slug_lc>` registry row
     automatically whenever the subject has a narrow/broad parent
     row, choosing the namespace from the parent ontology prefix
     (chemistry registries → `compound`, food / environmental /
     anatomical / tissue ontologies → `ingredient`). A B1 reject
     after a fresh build means either the YAML's `ontology_mapping`
     was hand-edited away from a narrow/broad relationship or the
     SSSOM was edited directly — re-run `just build-sssom` from
     claw and the reject should clear.
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
report to stderr. On a failing run the validator emits a single FAIL
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

Rule B1 is **strict by default**: every narrow/broadMatch subject
must carry a sibling
`MIM:<slug> skos:exactMatch kgmicrobe.{ingredient,compound}:<slug_lc>`
registry row, and a missing registry row contributes to exit-2 just
like Rules A, B2, and B3. The original 162-subject backlog (that
PR #4 shipped warn-only to accommodate) was cleared by the claw
SSSOM builder change in
`culturebotai-claw/scripts/build_mim_ingredient_sssom.py`
(`_row_from_yaml` now synthesizes the registry row whenever a
narrow/broad parent row is emitted), so every fresh build of
`mappings/ingredient_mappings.sssom.tsv` is B1-clean by
construction.

For one-off diagnostic use (e.g. while bisecting which subjects
regressed after a builder-side schema change) you can pass
`--lenient-b1` to downgrade B1 back to warn-only. Do **not** use it
in CI: the strict default is what protects downstream consumers
from the identity-collapse class of bug Section 2 describes. The
legacy `--strict-b1` opt-in flag from the warn-only stage is
accepted as a no-op so any tooling that still passes it keeps
working.

### Where the rules live

- **Validator implementation**: `scripts/validate_sssom_invariants.py`
  enforces Rules A, B1 (strict-by-default), B2, B3, and B4 (best-effort,
  silently skips per-prefix when the kg-microbe transforms are absent).
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
