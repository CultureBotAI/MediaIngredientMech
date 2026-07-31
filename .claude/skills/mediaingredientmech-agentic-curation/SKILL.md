---
name: mediaingredientmech-agentic-curation
description: Use FutureHouse Falcon deep research for source-backed MediaIngredientMech ingredient curation, ontology mapping review, SSSOM predicate decisions, validation, and generated sharing artifacts.
version: 1.0.0
tags: [curation, futurehouse, falcon, deep-research, ingredients, sssom, chebi, foodon, envo]
author: MediaIngredientMech Team
created: 2026-05-09
---

# MediaIngredientMech Agentic Curation

## Core Rule

Use Falcon as a source-finding and evidence-triage tool, not as an automatic YAML or SSSOM editor. Curate only claims that can be traced to source-backed evidence. Prefer DOI-backed sources; use PMID when DOI is unavailable.

Never print, commit, or persist API keys outside the repo-local gitignored `.env`. Do not stage `.env`, generated research reports, caches, embeddings, lockfile noise, or unrelated local changes unless explicitly requested.

## Setup Checks

From the MediaIngredientMech repo:

```bash
git check-ignore .env
just research-provider falcon
```

Falcon should report available when `EDISON_API_KEY` is set. The research wrapper also maps `FUTUREHOUSE_API_KEY` to `EDISON_API_KEY` in the subprocess environment when `EDISON_API_KEY` is not already set.

Confirm the dry-run command shape before a live research call:

```bash
just research-ingredient falcon <mapped|unmapped> <slug> --dry-run
```

Reports are written to:

```text
research/ingredients/<mapped|unmapped>/<slug>-deep-research-falcon.md
research/ingredients/<mapped|unmapped>/<slug>-deep-research-falcon.citations.md
```

## Workflow

1. Pick a focused batch of 5-15 records from `data/ingredients/mapped/<slug>.yaml` or `data/ingredients/unmapped/<slug>.yaml`.
2. Prioritize high-impact records: `UNKNOWN_TERM` review rows, high-frequency unmapped records, suspected wrong exact mappings, hydrate/salt ambiguity, and complex mixtures or named formulations that may need non-identity mapping semantics.
3. Run Falcon for each candidate:

```bash
just research-ingredient falcon <mapped|unmapped> <slug>
```

4. Read the report and citation file. Treat Falcon output as leads; verify identity, formula, hydrate state, composition, and ontology grounding against cited source metadata/snippets before editing.
5. Curate only locally supported fields:
   `mapping_status`, `ontology_mapping`, `chemical_properties`, `synonyms`, `notes`, `kg_microbe_node_id`, `ingredient_type`, and `curation_history`.
6. Keep edits narrow and schema-consistent. Preserve filenames and existing identifiers unless the task is explicitly an identifier repair.
7. Do not identity-map complex mixtures, media formulations, vitamin/trace solutions, buffers, extracts, seawater preparations, or catalog preparations to generic parents. Use non-identity semantics or leave them unmapped for curator review.

## Mapping Semantics

Use `MAPPING_SEMANTICS.md` as the authority for SSSOM predicate decisions:

- `skos:exactMatch`: true identity only; bidirectional substitution is safe.
- `skos:closeMatch`: related but not substitutable.
- `skos:narrowMatch`: MIM ingredient is more specific than the ontology parent; must have a registry exact row for the same `MIM:<slug>`.
- Registry rows use `MIM:<slug> skos:exactMatch kgmicrobe.{ingredient,compound}:<slug_lc>`.

When SSSOM rows change, update `mappings/ingredient_mappings.sssom.tsv` consistently with the YAML and run:

```bash
python3 scripts/validate_sssom_invariants.py
```

If a `narrowMatch` is added manually, verify the required `kgmicrobe.compound:` or `kgmicrobe.ingredient:` registry row is present.

## Editing Pattern

For each curated record:

- Add a `curation_history` event with timestamp, curator/process, action, concise change summary, `new_status` when applicable, and whether the step was LLM assisted.
- For mapped exact identities, ensure `ontology_mapping.ontology_id`, `ontology_label`, `ontology_source`, `mapping_quality`, and evidence agree with the curated identity.
- For non-identity or uncertain mappings, record the related term in notes/SSSOM semantics without implying substitution.
- Add chemical properties only when source-backed and form-specific: formula, hydrate state, CAS-RN, SMILES/InChI, data source, and retrieval date.
- Preserve raw source names as synonyms when useful, but avoid importing Falcon prose as synonyms or notes.
- If individual YAML records changed, regenerate aggregate outputs and inspect diffs:

```bash
python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir data/curated
```

## Validation

After curation edits, run targeted checks first:

```bash
python scripts/validate_all.py --mode individual
python3 scripts/validate_sssom_invariants.py
```

Then run the broader checks when practical:

```bash
just validate-all
PYTHONPATH=src pytest -o addopts='' tests/
```

Run lint when code or scripts changed:

```bash
just lint
```

If broad validation or tests fail on pre-existing schema, merge, or data-shape issues, document the failing commands and separate those failures from the curated ingredient changes.

## Final Summary

Report:

- records reviewed and curated
- Falcon reports and citation files used
- identity, formula, hydrate/salt, formulation, or ontology decisions made
- YAML fields and SSSOM rows changed
- DOI citations added, and any PMID fallbacks
- generated aggregate or sharing artifacts updated
- validation, SSSOM invariant, test, and lint results
- commits pushed and any untouched local files
