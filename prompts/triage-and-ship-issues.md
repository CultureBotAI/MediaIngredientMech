# `/goal` prompt — triage the open issues and ship them

Paste everything below the rule after `/goal`.

**Merging.** By default the loop stops at "PR open and green" and asks. To
authorize merges, name them in the invocation — e.g. append
`You may merge and delete the branch for #182 and #183.` The global rule
(`~/.claude-work/CLAUDE.md`) is that merging is the user's call and prior
approval of one PR is not approval of the next, so a blanket standing
authorization is not something this file can grant itself.

Other useful scopings: `Limit to issues #182 and #183.` ·
`Triage only — rank and report, change nothing.`

> The incident citations below are illustrative and were true when written
> (2026-08-04). Re-verify any you rely on; this repo has already had a command
> file rot into recommending the exact workflow that caused #148.

---

Review and prioritize this repo's open GitHub issues, then work the top items
end to end: branch, commit, push, open a PR, review it adversarially, file issues
from the review, address them. Merge and delete the branch **only for PRs this
invocation explicitly authorized** — otherwise stop at PR open and green and ask.
Respect dependencies between PRs. Pause and ask when a decision is genuinely
mine.

## 1. Triage before touching anything

Start from `NEXT_TASKS.md` and the `next-tasks` skill, which owns backlog
reconciliation — do not build a parallel backlog in your head. Then list open
issues and PRs.

Verify each claim against the current tree before ranking it. Issues go stale,
and #164 did not reproduce as filed. But note how that ended: the adjacent
surface *was* broken (`data/custom/*.yaml` matched zero files because that
directory holds a `.tsv`), so the right move was to fix what was actually wrong,
record the reasoning in the file so a later "tidy" cannot reintroduce it, and
close the issue with evidence. **"Does not reproduce" is the start of the
investigation, not the end of it.** Say which issues you re-verified.

Rank by **silence, not severity**. Anything loud is recoverable; a wrong thing
that reports success is not. In order:

1. Silent, irreversible data loss — especially in a path something else now
   depends on.
2. Checks that report OK while checking nothing: a filter that narrowed a guard
   until it stopped guarding (`paths:` in #160/#166, `branches:` in #174/#175);
   a guard that verifies nothing when a dependency is missing (`justfile`'s
   `_require-claw` exists because a skip-when-missing vendored-sync job passed
   while checking nothing); a self-referential pin that compared a copy to a hash
   from the same repo, so all four Mech repos could pass while diverged
   (retired in #156/#157).
3. High-likelihood correctness bugs that are at least noisy.
4. Correctness of the published artifacts — `mappings/ingredient_mappings.sssom.tsv`
   and `UNIFIED_INGREDIENT_MAPPING.tsv` — which kg-microbe re-syncs on every
   consolidation run.
5. Footguns and hygiene.
6. Upstream-blocked or cosmetic — name them so gaps are explained, don't work them.

Present the ranking with a one-line justification each, then start on the top
item. Don't ask permission to begin.

## 2. Reproduce before fixing

Do not fix from the issue text. Reproduce the failure and show the output.

When the fix is a gate or guard, ask two questions, in this order:

1. **Is it wired to anything?** `scripts/verify_roundtrip.py` existed and was
   correct from 2026-03-07, but nothing executable referenced it until #167 — no
   justfile recipe, no workflow. It was not a gate that could not fail; it was a
   gate nobody ran. Grep the justfile and `.github/workflows/` for it.
2. **Can it fail?** Revert the data or inject the exact defect and confirm a
   non-zero exit. A gate that only ever passes is worthless.

## 3. PR discipline

Branch before the first edit; never commit to `main`. One coherent change per PR.
After pushing, review the diff **adversarially as a separate pass**, delegated to
a fresh agent with no context of your reasoning — reviewing your own work from
memory reproduces your own blind spots. Per the global rules that review is
**read-only**: it must not edit, push, or overwrite anything. Every finding
becomes a GitHub issue; then triage — fix what belongs in this PR, leave the rest
filed, and say which is which and why.

Check that your own claims are true. In one session a commit message asserted
data had been committed when it had not, a PR body quoted a schema example
"verbatim" that differed by a word, and a test asserted `argparse`'s documented
behaviour rather than the code's. Re-read what you wrote against what you did.

## 4. Dependencies between PRs

- **Prefer independent branches off `main`.** Verify independence, don't assume
  it: `git merge-tree $(git merge-base A B) A B` is what caught #178 and #179
  editing the same justfile comment block while both PR bodies claimed no
  overlap.
- **If PRs must stack, retarget the child to `main` BEFORE merging or deleting
  the parent's branch.** Deleting a base branch *closes* the child PR rather than
  retargeting it, and GitHub will not reopen it while its base is gone — you must
  restore the branch from its SHA first. Doing it in the right order costs
  nothing; #178 was retargeted first and merged without incident.
- **Merge bottom-up, rebasing each child onto the new `main`** after the parent
  lands. Parents are squash-merged, so the child still carries the pre-squash
  commits and will look conflicted until rebased.
- **Put a shared fix in the PR that owns the file**, then rebase the dependent PR
  on top, rather than duplicating it.

## 5. Repo-specific constraints that will bite you

- **`just qc` is not the whole local gate.** It is
  `validate-all validate-strict qc-evidence qc-sssom qc-roundtrip`. The
  **blocking** id↔label gate deliberately sits *outside* it because it needs a
  multi-GB OAK download — run `just validate-products` too, or CI will find what
  you didn't.
- **Vendored files are a procedure, not a judgment call.**
  `scripts/validate_id_label_correspondence.py`, `scripts/chem_formula.py`,
  `tests/test_id_label_*.py`, and `src/*/schema/mech_shared.yaml` are
  byte-identical across four Mech repos. Editing one locally fails
  `vendored-sync`. The path is: PR into `CultureBotAI/CultureMech` → merge → copy
  byte-exact → bump `scripts/.vendored_canon_ref` in the same PR.
- **Data changes need a provenance record.** Anything touching
  `data/ingredients/**`, `data/curated/**`, `data/custom/**`, or `mappings/**`
  gets a `just new-history` record. CI treats its *presence* as advisory by
  design, so nothing will stop you forgetting — that is exactly why it belongs
  in your checklist.
- **A published artifact is done when it is rebuilt, not when the YAMLs change.**

## 6. Verification

Report what you ran and its result: `just qc`, `just validate-products`, the full
test suite with its count, and CI.

Never trust a status label over content. "PR merged" does not prove the content
landed — squash-merges make commit-level checks lie. Diff a branch's own changes
against `main` before deleting it.

Characterise large diffs before accepting **or** dismissing them: records added,
removed, modified, and field-level changes. A one-role apply once produced a
9,513-line diff of which ~9,500 was pure reordering (#178/#179). Nothing was
wrong with the data — the hazard is that a real change hides in that volume, and
the tooling had a comment telling reviewers not to read such diffs by line count.

## 7. When to pause and ask

Use `AskUserQuestion` — don't guess, don't stall silently — when:

- the choice has **cross-repo blast radius** (renaming an enum CultureMech
  imports, changing a shared schema);
- fixing it means **deciding what the data should say** rather than what the code
  should do (which of two ontology groundings is right; whether two records are
  duplicates or genuinely distinct compounds);
- an issue's premise is wrong and the right action is to **close or re-scope
  someone else's issue**;
- the work needs **credentials, budget, or an external service** — and see the
  canary rule in `~/.claude-work/CLAUDE.md` before any billed fan-out: free
  dry-runs first, then exactly one real unit **by the same path the batch will
  take**, verify the artifact is on disk and non-empty, re-canary rather than
  fix-and-fan-out, and say what the canary proved;
- proceeding would **delete or overwrite** something you did not create;
- a PR is ready to merge and **this invocation did not authorize merging it**.

Otherwise decide and proceed, saying what you chose and why.

## 8. Done

Every item is merged (where authorized), or left as a green PR awaiting my call,
or closed with evidence, or filed as a follow-up with a reason. `NEXT_TASKS.md`
is updated per the `next-tasks` skill — shipped items marked
`DONE (YYYY-MM-DD, PR #NNN)`, reconcile date bumped — because a loop that merges
and never touches the backlog leaves it stale by exactly what it shipped.
`main` is green, the working tree is clean, and every branch you created is
deleted **both remote and local**. Report what shipped, what you deliberately did
not do, and what you would pick up next.
