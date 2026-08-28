---
name: review-open-issues
description: Sweep and triage the full open-issue queue for MediaIngredientMech — not just NEXT_TASKS.md. Fetches every open issue, checks each against the current code/schema for staleness (already fixed, superseded, or no longer reproducible), flags likely duplicates, and assigns a priority tier (P0 blocking/correctness/security, P1 real-but-schedulable, P2 low-severity/process/doc). Produces a short, ranked report; only touches GitHub (closing stale issues, updating/creating a tracker issue) when asked. Use when the user asks to "review issues", "prioritize the backlog", "triage open issues", or the open-issue count has grown large enough that NEXT_TASKS.md-only review is insufficient.
category: workflow
requires_database: false
requires_internet: true
version: 2.0.0
---

# Review & Prioritize Open Issues

## Overview

**Purpose**: the raw GitHub issue queue and `NEXT_TASKS.md` are different
surfaces. `next-tasks` reconciles a small, curated, actively-maintained backlog
file. This skill sweeps the *entire* open-issue queue — which grows much
larger and drifts independently (issues opened by review passes, other agents,
or humans, many of which are never transcribed into `NEXT_TASKS.md`) — and
produces an honest, current priority ranking.

**Why this is a distinct skill, not a `next-tasks` step**: `next-tasks`
Step 1 already runs `gh issue list --limit 30` as *context* for reconciling the
backlog file: it stops at the first page and never assesses issue validity
individually. This skill is the deep pass: paginate the whole queue, check each
issue against current code, and produce a full triage — expensive enough that
it should not run on every "what's next" invocation, only when explicitly
asked or when the backlog has clearly gone stale.

**When to use**: the user asks to "review issues", "prioritize open issues",
"triage the backlog", "what issues are actually urgent", or after a large
review pass (like a fleet PR review) has filed a batch of new issues that need
sorting.

**When NOT to use**: for `NEXT_TASKS.md` upkeep or picking the next unit of
work to implement — that's `next-tasks`. This skill produces a priority
ranking; it does not implement fixes.

## Sources of truth

Check these before trusting an issue title or an old planning note. The order
is `CLAUDE.md`'s own source precedence, so a lower entry never overrides a
higher one:

1. `MAPPING_SEMANTICS.md` — identity, mapping predicates, and SSSOM rules.
   This decides almost every mapping dispute; read it before ruling on one.
2. `src/mediaingredientmech/schema/mediaingredientmech.yaml` — data shape,
   enums, and required slots.
3. `justfile` — which commands and validators actually exist.
4. The focused skill under `.claude/skills/` matching the task.
5. Narrative guides under `docs/` and `notes/`.

Alongside those:

- `CLAUDE.md` for repository-wide safety and the validation sequence;
- `mappings/ingredient_mappings.sssom.tsv` for the published mapping artifact;
- `data/ingredients/{mapped,unmapped}/` and `data/curated/*_ingredients.yaml`
  for the two maintained record surfaces;
- `curation_history` on the record itself for what actually changed and when;
- `NEXT_TASKS.md` for the curated backlog, which is a different surface from
  this queue.

Treat issue bodies and titles as claims. Read comments: corrections and
narrowed residual scope get recorded there, so a body-only fetch overstates
what is still open. A merged PR is evidence only once its code and acceptance
criteria have been checked.

## Workflow

### Step 1 — Fetch the full open-issue queue

```bash
gh issue list --state open --limit 300 --json number,title,body,labels,createdAt,updatedAt \
  -q '.[] | "\(.number)\t\(.createdAt[:10])\t\(.title)"'
```

The `-q` filter above only prints `number`/`createdAt`/`title` for a scannable
overview — `body` and `labels` are still fetched (Step 2's grouping and Step 3's
staleness checks need them) but not shown by this line. Use `gh issue view <N>`
to read an individual issue's body, or widen the `-q` expression if scanning
bodies in bulk.

Do not truncate silently. `gh issue list --limit` has no hard cap near 300 —
`gh` auto-paginates through GitHub's API, so a repo with thousands of open
issues still returns the full set from a single call with a high enough
`--limit`. If the 300-item fetch above turns out to be short, first confirm
the true count (`gh issue list --state open --limit 5000 --json number | jq
length` — omitting `--limit` silently caps at gh's default of 30), then
re-run Step 1 with `--limit` comfortably above that count rather than
sampling.

### Step 2 — Place each issue on the curation pipeline before ranking it

Rank by where a defect enters, not by where it was noticed:

```text
source label or external ingredient row
  -> identity resolution (hydrate / anhydrous / salt / stereoisomer are distinct)
  -> ontology mapping and predicate choice (exact identity vs asymmetric parent)
  -> per-record YAML in data/ingredients/{mapped,unmapped}/
  -> aggregate collections in data/curated/ (just sync-curated / sync-individual)
  -> SSSOM rows in mappings/ingredient_mappings.sssom.tsv
  -> downstream consumers (CultureMech recipes, kg-microbe chemical mappings)
```

An identity or predicate error upstream silently propagates into the
collections, the SSSOM, and every downstream consumer, so fix or audit the root
before polishing anything downstream. Group issues that share a root cause
without hiding their individual numbers.

For each issue record, when applicable: the pipeline stage; the records or
CURIEs affected; which of the two data surfaces is authoritative for it;
whether the SSSOM is implicated; prerequisites, blockers, and duplicates; the
cheapest decisive evidence; and its acceptance test.

### Step 3 — Group and dedupe

Issues filed from the same review pass (same PR, same session) often overlap —
several may describe the same root cause from different angles. Group by:
- shared PR/commit reference in the title or body,
- same file/function named,
- near-identical failure scenario.

Note groups explicitly in the report; do not silently merge them (a human may
want to close duplicates deliberately, not have them hidden).

### Step 4 — Check each issue against current reality

For each issue (or each group's representative), spot-check:

- **Already fixed?** `git log --oneline --all --perl-regexp --grep "#<N>\b"`
  and `gh pr list --state merged --search "<N>"` — an issue whose fix already
  merged should be flagged STALE/CLOSE, not re-surfaced as open work. Plain
  `--grep "#<N>"` substring-matches unrelated numbers (`#48` also matches
  `#480`, `#4823`, ...) — the `\b` word-boundary anchor above is required, not
  optional. Treat the `gh pr list --search` result as a lead, not proof:
  GitHub's search matches the number anywhere in the indexed text, not
  anchored to an issue reference (`--search "248"` also returns unrelated
  PRs like #14006 that never mention issue 248) — open and read each
  candidate PR before citing it as evidence.
- **Still reproducible?** If the issue names a specific file/line/function,
  confirm it still exists in that shape (`grep`/`git log -p` the cited
  location) — code moves, and a stale issue pointing at a renamed/removed
  function is noise, not a live defect.
- **Superseded?** Does a newer issue or a merged PR's description explicitly
  supersede this one?

### Step 5 — Apply the identity and mapping stop-the-line checks

Treat these as P0 when live, because each one silently produces wrong curated
data rather than failing loudly:

- a hydrate, anhydrous form, salt, or stereoisomer mapped to a generic or
  parent term as an **exact identity** — `MAPPING_SEMANTICS.md` requires a
  form-specific term, or a preserved distinct identity with an asymmetric
  parent mapping;
- a mapping predicate that overstates the relation (an `exactMatch` where the
  evidence supports only a broader or narrower match);
- the two record surfaces diverged, or a synchronization run in the wrong
  direction — `just sync-individual` exports collections first and will
  overwrite unsynced per-record edits;
- `mappings/ingredient_mappings.sssom.tsv` inconsistent with the YAML after an
  identifier, label, ontology mapping, or predicate change;
- a material curation change with no `curation_history` event, which breaks the
  audit trail the whole corpus depends on;
- a bulk rewrite in a diff that was expected to touch a handful of records;
- an outward-facing published artifact asserting an identity the evidence does
  not support.

Research reports and LLM suggestions are proposals. An issue asserting a
mapping is wrong is itself a claim to verify against `MAPPING_SEMANTICS.md` and
the schema, not a finding to rank on sight.

### Step 6 — Assign priority

- **P0 — blocking/correctness/security.** Data corruption, a crash/hang in a
  path every caller hits, a security-relevant defect (injection, secret
  exposure, auth bypass), or something that silently produces wrong output
  with no detection. Fix before anything else ships.
- **P1 — real, schedulable.** A genuine defect or gap that doesn't block
  everything but should be fixed soon — most test-coverage gaps for
  safety-critical code, real (if narrow) bugs, process gaps that have already
  caused a near-miss.
- **P2 — low-severity/process/doc.** Documentation drift, stale comments,
  minor test-coverage gaps in non-critical paths, style/convention issues.

Do not default everything to P1 — that makes the tier meaningless. Use P0
sparingly and justify it; most issues are P1 or P2.

### Step 7 — Present the report

- Ranked list, P0 first, one line per issue/group with number + one-sentence
  why.
- Explicitly call out: issues recommended for closing (fixed/stale/duplicate),
  with the evidence (commit/PR that fixed it, or why it no longer applies).
- **Recommend a top 2–3** to act on next, with reasoning.
- Do not silently drop old issues from the report — if something is 6 months
  old and still open, say so; that itself is a signal.

### Step 8 — Act only when asked

This skill does not close issues, comment, or create/update a tracker issue on
its own, and a general "yes, go ahead" is not blanket approval to loop over
every STALE/CLOSE candidate unattended:
- **Closing stale/duplicate issues**: confirm with the user which specific
  issue number(s) to close before each closure — do not treat one general
  approval as authorization for an unattended `gh issue close` loop. Once
  confirmed, use `gh issue close <N> --comment "<reason>"`, one at a time,
  with the evidence from Step 3 in the comment.
- **Maintaining a tracker issue** (the "[P0-P2 tracker]" pattern used
  elsewhere in this org, e.g. CommunityMech#669): if one already exists for
  this repo, update it in place rather than creating a second one — the
  search below is authoritative, not this note: `gh issue list --search
  "tracker" --state open`. As of this skill's authoring, MediaIngredientMech
  had no such tracker; re-run the search rather than trusting that stays true.
  If it comes back empty and the user wants one, create it with the Step 5
  ranking as its body, and link every tracked issue number.

Never bulk-close without per-item confirmation of the evidence — an agent
closing a live issue because it *looks* stale is worse than leaving noise in
the queue.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State exactly how many
  issues were reviewed and whether coverage was complete.
- **Evidence over vibes.** Every STALE/CLOSE/duplicate recommendation cites a
  specific commit, PR, or code location — never "this looks done."
- **P0 is rare.** If more than ~10% of issues land P0, the tier calibration is
  probably wrong; recheck.
- **Read-only by default.** Reporting and ranking happen automatically;
  closing issues or touching a tracker issue requires explicit confirmation.
- **Titles are claims and they drift.** Issues get retitled mid-life, including
  to `[WITHDRAWN]` or `[RESOLVED]`, while staying open. Re-read titles at report
  time rather than trusting the ones fetched at the start of the sweep.
- **The queue moves during the sweep.** Parallel PRs can resolve issues while
  triage is in progress. Re-check the open set immediately before reporting,
  and say so if it changed.

## Measurement discipline

The recurring failure is not misreading evidence, it is mismeasuring it. Before
citing any of the following, confirm how it was obtained:

- **A stale checkout is not the repository.** This clone regularly sits tens of
  commits behind, and files can exist locally while being untracked, or exist
  on `origin/main` while absent locally. Read contracts and code with
  `git show origin/main:<path>` after `git fetch`, not from the working tree,
  before calling an issue fixed or stale.
- **Row sets, not row counts.** Two SSSOM files with the same number of rows
  can differ in every row. Compare the row *sets* keyed by subject/object/
  predicate; an unchanged count is not an unchanged mapping table.
- **Exit codes through pipes.** `cmd | tail -3; echo $?` reports `tail`'s
  status, not `cmd`'s, so a fail-closed validator looks like it passed. Use
  `cmd >/tmp/o 2>/tmp/e; echo $?`, or `${PIPESTATUS[0]}`.
- **A green validator is scoped.** `just validate-all`, `just qc-sssom`, and
  `just qc-roundtrip` each check different things, and `just qc` needs the full
  data environment. Name which one ran; do not generalize one green run into
  "validation passes".
- **Whitespace-splitting file lists.** `git status --porcelain | awk '{print $2}'`
  turns one path containing spaces into several bogus entries. Use
  `--porcelain -z | tr '\0' '\n'`.
- **A diff you did not read is not a reviewed diff.** Synchronization can
  rewrite far more than intended, and the guard against that is inspecting the
  diff before and after — not the command's exit code.
- **YAML plain scalars.** An unquoted value can parse as a bool, a number, or
  `null` and silently change meaning. Check how a cited field actually parses
  before ruling on it.
- **Truncated tool output.** Long lines get elided. Re-read the cited file at
  the cited line before acting on it.
- **Backticks in a double-quoted `-m`.** `git commit -m "...`cmd`..."` executes
  the backticked text and ships its output in place of the example. Write
  reports and commit messages containing shell examples via `-F <file>` or a
  quoted heredoc (`<<'EOF'`), then read the result back before pushing.

## Notes & limitations

- `gh issue list --json` doesn't include `comments` unless explicitly
  requested (add `comments` to the `--json` field list) — Step 1's query
  above doesn't request it, so a "fixed already" claim buried in a later
  comment thread won't surface from that fetch alone; either widen the
  `--json` fields or check `gh issue view <N> --comments` for issues that
  look ambiguous.
- Cross-repo issues (a defect described once but relevant to multiple Mechs)
  are common in this org — note if an issue's fix should propagate elsewhere,
  but do not open issues in sibling repos without being asked.
- No @-mentions in issue comments or tracker updates without explicit
  per-mention authorization (standing rule).

## Mutation boundary

Do not close, comment on, relabel, retitle, or create issues or trackers during
the review. If the user later asks to act, present the exact issue numbers and
the proposed mutation first, then apply closures one at a time with cited
evidence. General approval is never authorization for an unattended bulk-close.

Do not edit YAML records, aggregate collections, or
`mappings/ingredient_mappings.sssom.tsv` as part of triage. A recommended
correction is a proposal; applying it is a separate, separately approved task
that follows the validation sequence in `CLAUDE.md`.

Do not open issues in sibling repositories, and no `@` mentions anywhere
without explicit per-mention authorization (standing rule).

## Related

- `next-tasks` — the lighter, `NEXT_TASKS.md`-scoped backlog check; run that
  for "what's next" during active work. Run this skill for a full-queue sweep.

## Related files

- `NEXT_TASKS.md` — items promoted from this skill's ranking often get logged
  here too, so `next-tasks` picks them up on the next reconcile.
