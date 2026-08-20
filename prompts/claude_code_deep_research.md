# Claude Code task: one MediaIngredientMech deep-research curation

Work from the MediaIngredientMech repository root. Read `CLAUDE.md`, any
applicable `AGENTS.md`, `history/README.md`, the LinkML schema, and the selected
ingredient record before editing.

## Mission

Select exactly one unresolved culture-media ingredient identity question,
research it with the `claude_code` deep-research provider, and save supported
findings in one schema-compliant `IngredientRecord`.

The deep-research Markdown and citations files are raw audit artifacts. They do
not satisfy the schema requirement by themselves. The accepted result must be
curated into the canonical YAML record and validated.

## Constraints

- Use only the `claude_code` provider; never call or fall back to Falcon/Edison,
  Cyberian, or another provider. Run no more than one new research job.
- Do not repeat a target that already has an equivalent
  `*-deep-research-claude_code.md` report.
- Never expose or alter `.env` or credentials.
- Do not modify the schema, generated datamodel, or validators to accept output.
- Do not guess that a trade name, hydrolysate, extract, peptone, digest, or
  mixture is a pure chemical. Preserve mixture-versus-compound distinctions.
- Require source-backed exact identity before assigning an ontology CURIE. Do
  not choose an identifier merely because its label is lexically similar.
- Keep CAS numbers, stereochemistry, salt/hydrate state, grade, source material,
  and manufacturing process distinct. Preserve ambiguity when the sources do.

## 1. Pick one identity question

Inspect `data/ingredients/unmapped/` and `data/ingredients/mapped/`, prioritizing
records with high `occurrence_statistics`, ambiguous identity, incomplete
synonyms, or weak mapping provenance. Check existing Claude Code reports under
`research/ingredients/` and select one target with no equivalent completed run.

State the status directory, slug, YAML path, selection rationale, and one exact
question before starting research. Use this form:

> What is the precise chemical or material identity of **<ingredient label>** as
> used in culture media, including mixture status, synonyms, source/process,
> stereochemical or salt form, and the most defensible ontology mapping, if any?

Choose one record only. Do not promote or edit it during selection.

## 2. Check provider fit and run one job

Run:

```bash
just deep-research-provider claude_code identity_mapping
```

This checks capability/availability without starting a research task. Stop if
unavailable; do not switch providers. Otherwise run exactly once:

```bash
just research-ingredient claude_code <mapped-or-unmapped> <slug>
```

Capture the report and citations paths, then verify that the report is non-empty
and its conclusions trace to real sources. Do not retry an unsuccessful or
inconclusive job, and do not turn an inconclusive answer into a confident map.

## 3. Curate into IngredientRecord YAML

Use the schema and nearby curated records as the authority. Edit only the chosen
record, plus artifacts required by repository history and consistency policy.

- Update `preferred_term`, synonyms, ingredient type, mapping status, and
  identifier only to the level explicitly supported.
- Treat identity, functional role in a medium, and occurrence as separate
  claims. This run is for identity/mapping; do not add unsupported biological
  roles from generic chemical knowledge.
- Cite stable primary or authoritative sources. Evidence snippets must be
  verbatim and attached to the assertion they support.
- If no exact ontology class exists, retain an unmapped/local identifier and
  record what was ruled out. A null result is valid research.
- Follow repository tooling for any required mapping/index synchronization; do
  not hand-edit generated collections or indexes unless the repo instructions
  say they are canonical.
- Append the appropriate LLM-assisted `curation_history` entry in the ingredient
  record and create the required append-only `history/` record with
  `just new-history` as documented in `history/README.md`. Reference the raw
  Claude Code report. Do not edit past history.

## 4. Validate

Run the focused gates first:

```bash
just validate-strict <target-yaml-path>
just validate-individual
just qc-evidence
just validate-history <new-history-path>
```

If a mapping or published surface changed, also run the applicable repository
consistency gates, including `just qc-sssom`, `just qc-flat-coverage`, and
`just qc-duplicate-ids`. Fix data, not validation policy. Do not launch another
research job. Finish with `git diff --check` and inspect the focused diff.

## Completion report

Report the question and target-selection rationale, provider check, one research
command, report/citations paths, canonical YAML and history paths, the mapping
decision and rejected alternatives, validation results, and unresolved identity
uncertainty.

