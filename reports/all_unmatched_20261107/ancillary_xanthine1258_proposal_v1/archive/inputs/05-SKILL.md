---
name: curate-yaml-record
description: Review and curate one MediaIngredientMech ingredient YAML record for exact substance identity, ontology mapping, supplied form, roles, evidence, completeness, and resolvable gaps. Use when asked to audit, improve, complete, correct, map, or add evidence to one ingredient; do not use for bulk mapping, source ingestion, or as permission to contact anyone or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Curate one MediaIngredientMech YAML record

## Structured Review Output

For every new review or audit, follow
[docs/record-reviews.md](../../../docs/record-reviews.md) and
[the local profile](../../../docs/record-review-profile.md).
Capture exact targets and input hashes before judging, preserve this skill's
native rubric, rule IDs, scores and evidence requirements, then author the
structured assessment and run:

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
uv run python scripts/record_review.py validate /tmp/completed-review.yaml
uv run python scripts/record_review.py save --content /tmp/completed-review.yaml
```

Choose session-unique temporary paths. Save authoritative YAML and derived
Markdown under `reviews/structured/<timestamp>-<slug>/`; link both in the
final response. This output contract supersedes prose-only report examples.
A single record uses `kind: record`; batches declare exact selection,
population, reviewed targets and limits. Categories also state boundary decisions.
Every reviewed target must have an assessment. Keep P1-P4 and other native
severity/rule information with a justified common severity, and metric definitions,
scales and denominators. Do not infer scientific approval from a native score.

Raw provider drafts and deterministic validator/scan reports are diagnostic
inputs, not completed scientific reviews. Use `scientific_review: false`
for deterministic-only or provenance-only assessments; mark required unavailable
checks and incomplete coverage explicitly. A valid bundle does not change native
status, clear release holds, authorize edits, or append curation history.
For audit-only requests, stop after assessment and persistence; any application
steps below require curation intent.

Produce a defensible ingredient record and an explicit account of what is
supported, corrected, unresolved, and genuinely unknown. Search results and
research reports are leads; only inspected sources can support a mapping or
scientific claim.

## Shared Contract

<!-- canonical:begin the-contract -->
Produce a defensible record and an explicit account of four things: what is
**supported**, what was **corrected**, what is **still unresolved**, and what is
**genuinely unknown**. The last two are different — a gap you searched for and
could not close is a finding; a gap you did not look at is not.

**One target.** Resolve exactly one record before touching anything. If a label
matches several, or a request names a family rather than a member, stop and
disambiguate. Silently substituting a similar record is the error that no later
check catches, because everything downstream is then correct about the wrong
thing.

**Audit preserves scientific inputs. Curation authorises edits to the named
record only.** A review or audit request changes no scientific record, status,
or curation history. It does save a new timestamped structured review through
`docs/record-reviews.md` and the native rubric in `docs/record-review-profile.md`.
A curate, improve, complete, correct or add-evidence request authorises local edits to that record and the smallest
maintained path its provenance requires — not to neighbours, not to whatever
else looked wrong on the way.

**Search results are leads. Only an inspected source supports a claim.** A
search hit, a deep-research report, a rendered page, and a generated artifact are
each somewhere to look, and none is evidence. Evidence is text you read in the
source, attached to the narrowest assertion it actually supports.
<!-- canonical:end the-contract -->

## Shared Boundaries

<!-- canonical:begin boundaries -->
- **A generated artifact is never the fix.** Pages, merged products, exports and
  derived indexes are outputs. Correct the input or rule that owns the value and
  regenerate; patching the output makes it look right once and diverge on the
  next build.
- **No outbound action without explicit authorisation for that action.** Do not
  launch paid research, contact an author, or create or edit a GitHub issue, PR
  or comment because curation seemed to call for it. Authorisation to curate a
  record is not authorisation to spend or to speak.
- **Absence is not evidence of falsity, and coverage is not a goal.** Never
  infer that an unstated optional property is false. Never fill an optional
  slot to make the record look more complete. An empty field the source does
  not address is correct.
- **Search before declaring anything absent — and search past `.gitignore`.**
  Before treating a record, evidence source, decision row or overlay as missing,
  search for its identifier, label and slug with an ignore-independent tool
  (`rg --no-ignore --hidden`, `grep -r`, or `find`). Ordinary search skips
  ignored files, so an ordinary miss is a search over a subset, not a result.
- **Preserve unrelated work.** Use a branch, and a separate worktree when the
  checkout is dirty or occupied by something else.
<!-- canonical:end boundaries -->

## Shared Evidence Standard

<!-- canonical:begin evidence-standard -->
- Each claim is its own object. A definition, an example, a relation and a
  mechanism edge are separate assertions; attach a source to the narrowest one
  it supports, never to the record as a whole.
- Resolve every DOI, PMID and CURIE, and read enough of the source to establish
  support for the *exact* claim and scope. A matching string from the wrong
  paper, or an unrelated sentence from the right one, is not support.
- A snippet is short verbatim text from the source. Interpretation belongs in a
  notes field, never inside the quotation.
- **The kind of source is part of the citation.** A database assertion, a
  primary experiment, a review, a prediction and a search snippet are different
  strengths of support. Cite each as what it is; never present a database row
  or a review as if it were the primary study.
- Association and prediction do not establish mechanism or causality. Do not
  let a co-occurrence or a computed score become a mechanism edge.
- **A near-miss is not a match.** Never ground to a CURIE or canonical label
  because it looks plausible, and never use a broader or related term as an
  exact identity. Unresolved stays unresolved, recorded as such, until a source
  resolves it.
- **Evidence about one thing supports a claim about that thing.** Do not
  generalise one organism, strain, protein instance, construct or experiment
  into a family-wide, universal or "optimal" claim. Scope inflation is the most
  common way a true observation becomes a false record.
- Keep conflicts. When sources disagree, record both and the disagreement; do
  not resolve it by omission.
- A bounded search that found nothing is a result. Report it as "not found,
  searched X" rather than leaving the field silently empty.
<!-- canonical:end evidence-standard -->

## Shared Write Contract

<!-- canonical:begin writing-back -->
**Write only through the path that preserves formatting and records history.**
Never hand-edit a curated YAML with a text editor or a generic dump: canonical
key order, quoting and derived metadata are what make the corpus diffable, and a
dump destroys them in one save.

Repositories in this fleet do this in three different, equally correct ways, and
which one applies is a property of the corpus:

- **Direct guarded write** — a narrowly scoped mutator loads the record, asserts
  its identity, changes only the reviewed nodes, appends a curation event, and
  writes through the repository's validated writer.
- **Registered editor** — no generic writer exists on purpose; in-place changes
  use text-preserving operations through an editor that is registered and
  behaviourally tested, and the writer audit rejects anything else.
- **Regenerate from inputs** — the record is a build product. The fix goes into
  the decision row, term request, overlay or source inventory that owns the
  value, and the record is regenerated; the YAML is never edited directly.

The section below says which one this repository uses and names the exact
functions or files. Do not guess from a sibling.

Inspect the diff before committing. Whole-file presentation churn — reordered
keys, requoted strings, a hundred lines changed to alter one value — means the
write path was bypassed; abandon and repair rather than commit it.
<!-- canonical:end writing-back -->

## Shared History And Attribution

<!-- canonical:begin history-and-attribution -->
- Use `curator="claude"` when no curator identity was supplied. **Never
  attribute an agent's judgement to the user.** The history entry is a record
  of who decided, and it will be read when the decision is questioned.
- Mark LLM assistance where the schema records it.
- **Do not append a history event when nothing substantive changed.** A
  no-op event is noise that makes real events harder to find.
- The history entry describes the actual diff. If the corpus derives status or
  history from inputs, never set them directly — change the input.
- A REVIEWED status means a human reviewed it. Do not invent one, and do not
  promote to it on the strength of an agent pass.
<!-- canonical:end history-and-attribution -->

## Boundaries

- Resolve one target under `data/ingredients/{mapped,unmapped}/`. If a label
  denotes multiple substances or forms, stop and disambiguate before editing.
- Audit/review preserves scientific inputs and saves a new structured review.
  Curate, improve, complete, correct,
  map, or add-evidence requests authorize local changes to the named record and
  the smallest necessary synchronized mapping/provenance surfaces.
- Never treat a hydrate, salt, stereoisomer, mixture, extract, or generic class
  as exact identity with another substance merely because their names overlap.
- Never create or edit a GitHub issue, PR, comment, email, form, or message
  without explicit authorization for that exact outbound action.
- Preserve unrelated work and inspect `git status` before editing.
- Never fill an optional field only to improve coverage or interpret absence as
  false.

## Read before judging the record

Read the complete target plus:

- `CLAUDE.md`;
- `MAPPING_SEMANTICS.md`;
- the `IngredientRecord`, ontology-mapping, synonym, component, evidence,
  discussion, and curation-event classes in
  `src/mediaingredientmech/schema/mediaingredientmech.yaml`;
- [references/review-checklist.md](references/review-checklist.md).

Inspect the corresponding entry in `data/curated/`, the SSSOM mapping row, and
source occurrences. Neither a research report nor generated documentation is
independent evidence.

## Workflow

### 1. Establish the baseline

Read the entire YAML. Record its identifier, preferred term, exact supplied
form, mapping status and quality, source occurrences, components, roles,
chemical properties, discussions, datasets, and curation history. Run:

```bash
just validate-strict <record-path>
just validate-terms <record-path>
```

Check the matching row in `mappings/ingredient_mappings.sssom.tsv` and whether
the aggregate and per-record copies already agree. A green validator does not
prove that two chemical forms are equivalent.

### 2. Verify identity and mapping first

Determine exactly what substance the source label denotes. Verify identifier,
preferred term, synonyms and synonym types, formula, charge, stereochemistry,
hydration, salt/parent boundaries, components, and supplied form.

Follow `MAPPING_SEMANTICS.md` for predicate direction and identity loss. Use a
form-specific ontology term when available. Otherwise retain a distinct
identity and record an asymmetric broader/narrower relation as specified by the
mapping contract. A close lexical hit is not an exact mapping.

Validate every ontology ID and canonical label. `mapping_status: MAPPED` means
a valid ontology mapping exists; it is not a generic “record reviewed” flag.

### 3. Review every existing claim

For each mapping, xref-like assertion, synonym, component, chemical property,
role, environmental context, dataset, and discussion, verify that its source
supports this exact substance and relation. Distinguish source database
assertions, primary literature, reviews, and search snippets.

Do not infer nutritional, physicochemical, cellular/metabolic, or community
roles solely from a name or chemical class. Keep role context and organism/
medium scope. Exact snippets must be short and verbatim; interpretation belongs
in notes.

### 4. Assess completeness and resolve supported gaps

Apply the checklist and use bounded searches for consequential gaps. Prioritize:

1. conflated or underspecified chemical identity;
2. wrong ontology term, canonical label, or mapping predicate;
3. inconsistent supplied form, structure/property, or component partonomy;
4. unsupported synonyms or roles;
5. missing source occurrence and claim-level evidence needed to understand the
   decision.

Do not force an ambiguous mapping. Use the repository's review status and
queueing semantics when expert judgement is required. A discussion must name a
specific unresolved conflict, what was checked, and what would resolve it.

### 5. Write and synchronize through maintained paths

Use a narrowly scoped mutator that asserts the target ID, calls
`mediaingredientmech.curate.curation_event.record_curation_event` with
`llm_assisted=True`, and writes using
`mediaingredientmech.validation.write_validated.write_validated_ingredient`.
Use `curator="claude"` when no curator identity was supplied; never attribute
an agent decision to the user.

After a per-record edit, run `just sync-curated`. Keep the aggregate collection,
individual record, SSSOM row, path (`mapped` versus `unmapped`), and any
registry entry consistent. Do not run `just sync-individual` over an unsynced
per-record edit: it exports the aggregate and can overwrite the work.

Do not append a history event when the record is otherwise unchanged.

### 6. Verify and report

```bash
just validate-all
just qc-sssom
just qc-roundtrip
just audit-writers
git diff --check
git diff -- data/ingredients data/curated mappings src scripts history
```

Run `just qc-evidence` when evidence changed and `just qc` when the full
dependency environment is available. Re-read both synchronized representations
and confirm the event and SSSOM predicate describe the actual diff.

Report corrections/additions and sources, claims retained after checking,
remaining gaps and bounded searches that failed, the final mapping status and
why, every synchronized surface changed, and validation results.
