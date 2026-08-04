# `/goal` prompt — triage the open issues and ship them

Paste the block below after `/goal`. Invoking it **is** the explicit merge
authorization the global git rules require; without it, stop at "PR open, green".

Optionally scope it by appending e.g. `Limit to issues #182 and #183.` or
`Do not merge — stop at PR open and green.`

---

Review and prioritize this repo's open GitHub issues, then work the top items
end to end: branch, commit, push, open a PR, review it adversarially, file issues
from the review, address them, merge, and delete the branch. Respect dependencies
between PRs. Pause and ask me when a decision is genuinely mine.

## 1. Triage before touching anything

List open issues and PRs. For each issue, verify the claim against the current
tree before ranking it — issues go stale, and at least one in this repo did not
reproduce at all (#164: its glob reasoning was right but aimed at a file that
already used the correct form). Say explicitly which issues you re-verified.

Rank by **silence, not severity**. Anything loud is recoverable; a wrong thing
that reports success is not. In order:

1. Silent, irreversible data loss — especially in a code path something else now
   depends on.
2. Checks that report OK while checking nothing (a filter that narrowed a guard
   until it stopped guarding; a comparison against a stale committed artifact).
3. High-likelihood correctness bugs that are at least noisy.
4. Correctness of published artifacts (`mappings/*.sssom.tsv`,
   `UNIFIED_INGREDIENT_MAPPING.tsv`) that downstream consumers re-sync.
5. Footguns and hygiene.
6. Upstream-blocked or cosmetic — name them so gaps are explained, don't work them.

Present the ranking with a one-line justification each, then start on the top
item. Don't ask permission to begin.

## 2. Reproduce before fixing

Do not fix from the issue text. Reproduce the failure and show the output, or
state plainly that it does not reproduce and close the issue with that evidence.
A fix whose failure you never saw is a guess.

When the fix is a gate or guard, **verify it fails, not just that it passes.**
Revert the data or inject the exact defect and confirm a non-zero exit. A gate
that cannot fail is worthless, and this repo has shipped one before.

## 3. PR discipline

Branch before the first edit; never commit to `main`. One coherent change per PR.
After pushing, review the diff **adversarially as a separate pass** — delegate it
to a fresh agent with no context of your reasoning, since reviewing your own work
from memory reproduces your own blind spots. Every review finding becomes a
GitHub issue, then triage: fix what belongs in this PR, leave the rest filed, and
say which is which and why.

Check that your own claims are true. In this session a commit message asserted
data had been committed when it had not, a PR body cited a schema example
verbatim that differed by one word, and a test asserted `argparse`'s documented
behaviour rather than the code's. Re-read what you wrote against what you did.

## 4. Dependencies between PRs — the expensive lessons

- **Prefer independent branches off `main`.** Check for file overlap before
  claiming independence; two PRs editing the same comment block are not
  independent, however different their subjects.
- **If PRs must stack, retarget the child to `main` BEFORE merging or deleting
  the parent's branch.** Deleting a base branch *closes* the child PR rather than
  retargeting it, and a closed PR cannot be reopened while its base is gone —
  recovering means restoring the branch from its SHA. This cost a full recovery
  cycle here.
- **Merge bottom-up, rebasing each child onto the new `main`** after the parent
  lands. Parents are squash-merged, so the child still carries the pre-squash
  commits and will look conflicted until rebased.
- **Put a shared fix in the PR that owns the file**, then rebase the dependent PR
  on top, rather than duplicating it.

## 5. Verification gates

Before requesting merge: `just qc` exits 0, the full test suite passes (report
the count), and CI is green. State what you ran.

Never trust a status label over content. "PR merged" does not prove the content
landed — squash-merges make commit-level checks lie. Diff the branch's own
changes against `main` before deleting anything.

Watch for changes that are large but content-neutral. If a diff is thousands of
lines, characterise it (records added/removed/modified, field-level) before
accepting or dismissing it. An unreviewable diff is how 55 curation events were
silently reverted here for months.

## 6. When to pause and ask

Use `AskUserQuestion` — do not guess, and do not stall silently — when:

- the choice is a **judgment call with cross-repo blast radius** (renaming a
  shared enum, changing something CultureMech imports, altering a vendored file);
- fixing it means **deciding what the data should say** rather than what the code
  should do (which of two ontology groundings is right, whether two records are
  duplicates or genuinely distinct);
- an issue's premise is wrong and the right action is to **close or re-scope
  someone else's issue**;
- the work needs **credentials, budget, or an external service** (Edison runs, a
  billed sweep) — and when you do spend, canary exactly one unit first and verify
  the artifact is on disk before fanning out;
- proceeding would **delete or overwrite** something you did not create.

Otherwise decide and proceed, saying what you chose and why.

## 7. Done

Every item you took on is either merged with its branch deleted, or closed with
evidence, or filed as a follow-up with a reason. `main` is green, the working
tree is clean, and no branch you created is left on the remote. Report what
shipped, what you deliberately did not do, and what you would pick up next.
