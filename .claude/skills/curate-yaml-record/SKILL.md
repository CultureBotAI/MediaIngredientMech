---
name: curate-yaml-record
description: Review and curate one MediaIngredientMech ingredient YAML record for exact substance identity, ontology mapping, supplied form, roles, evidence, completeness, and resolvable gaps. Use when asked to audit, improve, complete, correct, map, or add evidence to one ingredient; do not use for bulk mapping, source ingestion, or as permission to contact anyone or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate one MediaIngredientMech YAML record

Produce a defensible ingredient record and an explicit account of what is
supported, corrected, unresolved, and genuinely unknown. Search results and
research reports are leads; only inspected sources can support a mapping or
scientific claim.

## Boundaries

- Resolve one target under `data/ingredients/{mapped,unmapped}/`. If a label
  denotes multiple substances or forms, stop and disambiguate before editing.
- An audit or review request is read-only. Curate, improve, complete, correct,
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
