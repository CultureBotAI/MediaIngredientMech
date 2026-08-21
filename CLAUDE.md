# Repository instructions for coding agents

These instructions apply to the whole repository. Keep changes narrow, preserve
provenance, and do not treat generated or research output as curated truth.

## Source precedence

When instructions disagree, use this order:

1. `MAPPING_SEMANTICS.md` for identity, mapping predicates, and SSSOM rules.
2. The LinkML schema rooted at
   `src/mediaingredientmech/schema/mediaingredientmech.yaml` for data shape.
3. `justfile` for supported commands and workflow behavior.
4. The focused skill under `.claude/skills/` that matches the task.
5. Narrative guides under `docs/` and `notes/`.

Do not copy an older example when it conflicts with a higher-authority source.

## Identity and mapping safety

One ingredient record denotes one distinct substance. Its `identifier` must be
the most specific stable identifier for that substance. Hydrates, anhydrous
forms, salts, and stereoisomers are not interchangeable: never map a hydrate to
the anhydrous or generic parent as an exact identity. Follow the decision
procedure in `MAPPING_SEMANTICS.md`: use a form-specific ontology term when one
exists; otherwise preserve the distinct identity with the documented CAS or
`kgmicrobe.*` pattern and an asymmetric parent mapping.

Research reports and LLM suggestions are proposals, not authorization to edit
YAML or SSSOM automatically. Verify the proposed identity, form, ontology term,
predicate, and evidence before applying it.

## Keep both data surfaces synchronized

The same records exist in two maintained surfaces:

- Per-record files: `data/ingredients/{mapped,unmapped}/*.yaml`
- Aggregate collections: `data/curated/{mapped,unmapped}_ingredients.yaml`

Choose one surface to edit, then synchronize in the correct direction:

- After per-record edits, run `just sync-curated`.
- After aggregate-collection edits, run `just sync-individual`.

`just sync-individual` exports collections first and will overwrite unsynced
per-record edits. Inspect the diff before and after synchronization; do not use
either command to erase unrelated work.

## Audit trail and SSSOM

Every material curation change must append a `curation_history` event with the
timestamp, curator or process, action, concise change summary, status transition
when applicable, and whether an LLM assisted the decision. Preserve raw source
labels as synonyms when required by the mapping semantics.

When an identifier, ontology mapping, label, or predicate changes, keep
`mappings/ingredient_mappings.sssom.tsv` consistent with the YAML. Follow the
SSSOM generation and registry-row rules in `MAPPING_SEMANTICS.md`; do not
hand-wave a failing invariant or invent an identity row.

## Safe validation sequence

1. Run `git status --short` before editing and preserve unrelated changes.
2. Run the narrowest relevant test or validator while iterating.
3. Synchronize the two data surfaces in the correct direction and inspect the
   resulting diff for unexpected bulk rewrites.
4. For data changes, run `just validate-all`, `just qc-sssom`, and
   `just qc-roundtrip`.
5. For code changes, run focused tests, then the applicable broader recipes in
   `justfile`. Run `just qc` when the full data/dependency environment is
   available.

Never discard, reformat, or include unrelated dirty-worktree changes. Report
which checks ran and any failures or unavailable external dependencies.
