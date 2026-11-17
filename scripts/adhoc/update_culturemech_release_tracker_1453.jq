# Purpose: reconcile CultureMech release tracker #687 after reviewed intake #1453.
# Inputs: gh issue view --json number,body; --rawfile checkpoint with final evidence.
# Output: replacement issue body on stdout; this helper never publishes it.
# Date: 2026-11-17. Preserve the historical campaign evidence below the new checkpoint.
if .number != 687 then error("Expected CultureMech tracker 687") else .body end
| if contains("Variant-only ingredient prose is a separate curation gap (#683).")
  then sub("Variant-only ingredient prose is a separate curation gap \\(#683\\).";
           "The scoped variant-prose gap in #683 is resolved by the reviewed v3 inventory. Its separate MIM intake and remaining integrated-release gates are recorded below.")
  else error("Tracker scope changed; reread before editing") end
| if contains("scientific curation remains open in #683.")
  then sub("scientific curation remains open in #683\\.";
           "this was the historical pre-curation checkpoint. Issue #683 is now closed; the reviewed v3 successor is recorded above.")
  else error("Historical checkpoint changed; reread before editing") end
| if contains("## Source comparison receipt") and ($checkpoint | length) > 0
  then sub("## Source comparison receipt";
           $checkpoint + "\n\n## Source comparison receipt (historical baseline)")
  else error("Missing checkpoint or insertion point") end
