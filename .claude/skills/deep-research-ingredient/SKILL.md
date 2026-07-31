---
name: deep-research-ingredient
description: Run Edison Scientific deep research (PaperQA3) for a MediaIngredientMech ingredient record to gather source-backed identity, composition, CAS-RN, and ontology-grounding (CHEBI/FOODON/NCIT) evidence. Captures a full provenance bundle and produces a curation-focused report for a curator to review and apply.
category: research
requires_database: false
requires_internet: true
version: 1.0.0
---

# Deep Research for an Ingredient (Edison API)

## Overview

**Purpose**: For one MediaIngredientMech ingredient record, run an
Edison Scientific `LITERATURE` (PaperQA3) deep-research job that mines
primary literature, supplier pages, and chemical/ontology resources
for: identity & scope, composition/CAS-RN/formula, candidate ontology
grounding (CHEBI / FOODON / NCIT / MESH / ENVO), and a curation
recommendation (`MAPPED` / `UNMAPPED` / non-identity match).

This is the MIM port of CultureMech's `deep-research-medium`. It ships
the **phase-1 single-record** flow (medium-level search has no
ingredient analog yet); the per-entity follow-up ("phase 2") is
deferred. The response-capture plumbing (`_edison_capture.py`) is
vendored verbatim from CultureMech and is byte-identical across the
Mech repos.

**When NOT to use**: skip if a recent research output already exists
for the target ingredient — re-running spends API credits. For a quick
non-Edison pass, `just research-ingredient <provider> <status> <slug>`
uses `deep-research-client` instead.

## Prerequisites

- `EDISON_PLATFORM_API_KEY` (or the legacy `EDISON_API_KEY` already in
  this repo's `.env`) set in repo-root `.env` or environment.
- `edison-client` SDK installed: `uv sync --extra dev`.
- Template: `templates/ingredient_mapping_research.md` (shared with the
  DRC wrapper — same `{placeholder}` variables).

## Inputs

The skill expects one of:
- An ingredient **slug** (YAML stem, e.g. `yeast_extract`), resolved
  across `data/ingredients/mapped/` and `data/ingredients/unmapped/`.
- A **YAML path** under `data/ingredients/<status>/`.
- `--status <status> --slug <slug>` when a bare slug is ambiguous.

Optional:
- `--job` (default `literature`; alternatives: `literature-high`,
  `precedent`, `phoenix`).
- `--dry-run` to render the query + write meta yaml without spending
  credits.

## Workflow

### Step 1 — Resolve the ingredient

Resolve the user's input to a single YAML file. A bare slug is searched
across the status dirs; if it matches more than one, surface the
candidates and ask which one (or pass a full path / `--status`).

```bash
uv run --extra dev python -c "
import sys; sys.path.insert(0, 'scripts')
import research_ingredient_edison as rie
print(rie.resolve_target('<TARGET>'))
"
```

### Step 2 — Check for existing research output

```bash
ls research/ingredients/<slug>-edison-*.md 2>/dev/null
```

If a recent output exists (`meta.yaml` shows a real `task_id` and
`submitted_at`), tell the user and ask whether to re-run. **Do not
silently re-spend credits.**

### Step 3 — Run the deep-research job

Dry-run first so the rendered query is auditable before spending:

```bash
just research-ingredient-edison <slug> --dry-run
```

Then for real:

```bash
just research-ingredient-edison <slug>
# or with overrides:
uv run --extra dev python scripts/research_ingredient_edison.py \
    --target <slug-or-path> \
    --job literature \
    --template templates/ingredient_mapping_research.md \
    --out-dir research/ingredients
```

Outputs (per task; `<stem>` is `<slug>-edison-literature`):
- `<stem>.md` — primary Markdown answer (`formatted_answer` preferred).
- `<stem>-meta.yaml` — task_id, cost, status, `query_sha256`, full
  rendered query, template_vars, char counts, sidecar inventory.
- `<stem>-response.json` — full `response.model_dump(mode="json")`.
- `<stem>-citations.md` — parsed reference list (DOI/PMID/URL).
- `<stem>-agent-state.json` — PaperQA tool-call trace + env frame.
- `<stem>-files.json` — inventory of any artifacts Edison produced.

In `--dry-run` mode only the meta yaml is written; the `query_sha256`
still lets you diff a planned prompt against prior runs.

**Retroactive enrichment**: if a meta yaml has a `task_id` but is
missing sidecars (e.g. captured by an older script), run
`just enrich-edison-response` to pull verbose + files + parse citations
without re-billing.

### Step 4 — Hand off to the curator

Read `<stem>.md` and summarize for the user:
- Candidate ontology mappings with match type (exact / close / broader)
  and confidence.
- Source-backed chemical/formulation facts (formula, CAS-RN, hydrate).
- Recommended record updates (mapping_status, synonyms,
  chemical_properties, ontology_mapping, curation_history note).
- The total reported cost.

Do **not** mutate `data/ingredients/` files in this skill — that is the
curator's call after reading the report. The per-task markdown + meta
files are the audit trail and source of truth for citations.

## File outputs at a glance

```
research/ingredients/
├── <slug>-edison-literature.md             # answer
├── <slug>-edison-literature-meta.yaml      # audit (task_id, cost, query, ...)
├── <slug>-edison-literature-response.json  # full SDK response
├── <slug>-edison-literature-citations.md   # parsed refs
├── <slug>-edison-literature-agent-state.json
└── <slug>-edison-literature-files.json
```

## Cost & safety

- `LITERATURE` typically costs a few cents per ingredient;
  `LITERATURE_HIGH` is several times more expensive.
- Run `--dry-run` first on new ingredients to audit the rendered query.
- Use `research-ingredient-edison-batch <queue.json>` to go *wide*
  across many ingredients (JSON list of slugs/paths); use this skill to
  go *deep* on one.

## Error handling

- **`edison-client` not installed**: run `uv sync --extra dev`.
- **Missing API key**: add `EDISON_PLATFORM_API_KEY=...` (or
  `EDISON_API_KEY=...`) to repo-root `.env`.
- **Ambiguous target**: list candidate paths and ask the user to pick
  (or pass `--status`).
- **API failure**: surface the error; do not auto-retry (avoids
  accidental double-billing).

## Related skills

- `map-media-ingredients`, `ingredient-roles`, `review-ingredients` —
  apply and validate the curation the report recommends.
- `manage-identifiers` — minting `kgmicrobe.compound:` IDs when no
  ontology term fits.

## Related scripts

- `scripts/research_ingredient_edison.py` — this skill's runner.
- `scripts/_edison_capture.py` — shared response-capture helpers
  (vendored from CultureMech, byte-identical across Mech repos).
- `scripts/enrich_edison_response.py` — retroactive sidecar backfill
  (no re-billing).
- `scripts/research_ingredient.py` — the non-Edison `deep-research-client`
  wrapper (provider-based).

## Quick reference

```bash
# Single ingredient (dry-run to audit the query first):
just research-ingredient-edison <slug> --dry-run
just research-ingredient-edison <slug>

# Deeper job:
just research-ingredient-edison <slug> --job literature-high

# Batch (JSON list of slugs/paths):
just research-ingredient-edison-batch queue.json --limit 5

# Backfill provenance for older runs (no re-billing):
just enrich-edison-response
```
