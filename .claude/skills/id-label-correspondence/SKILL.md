---
name: id-label-correspondence
description: Validate that every ontology ID carries its correct ontology LABEL across MIM data inputs, intermediates, and data products (SSSOM/CSV). Uses LinkML schema bindings + linkml-term-validator for YAML data (canonical label) and a shared OAK validator for products (canonical-or-synonym). Run report-then-enforce; triage drift as wrong-label vs wrong-id.
category: validation
requires_database: false
requires_internet: true
version: 1.0.0
---

# ID↔Label correspondence (MIM)

## The invariant

Every ontology **ID** must carry its **correct ontology label**, everywhere it
appears — data inputs, intermediates, and data products. Checking that an ID
*exists* is not enough; the **label must be the right label for that ID**.

Policy (**Hybrid**):
- **Schema YAML label fields** (`ontology_mapping.ontology_label`,
  `environmental_context.environment_label`) must equal the **canonical OBO
  label** (e.g. `CHEBI:26710` → `sodium chloride`). Abbreviations, formulas,
  and free names (`NaCl`) belong in `preferred_term` / `synonyms`, **not** in
  `ontology_label`.
- **Product `*_label` columns** (SSSOM, CSV) accept the **canonical label OR an
  exact/related ontology synonym** — the conventional surface form.

See `docs/ID_LABEL_CORRESPONDENCE.md` for the cross-repo rationale.

## How it's enforced

**Engine A — LinkML-native (YAML data).** The schema
(`src/mediaingredientmech/schema/mediaingredientmech.yaml`) marks each label
slot `slot_uri: rdfs:label` and gives the term-bearing slot a range-less
`binding` (`binds_value_of: <id_field>`). That makes
`linkml-term-validator validate-data --labels` look up the id's canonical label
via OAK and **fail** when the asserted label differs.

```bash
just validate-terms data/ingredients/mapped/<file>.yaml   # one file
just validate-terms-all                                    # all data
```

**Engine B — shared OAK validator (products).**
`scripts/validate_id_label_correspondence.py` (vendored byte-identical across
the Mech repos) walks the surfaces in `conf/id_label_targets.yaml`, resolves
canonical label + synonyms from OAK, and flags drift.

```bash
just validate-products       # enforce (exit 2 on mismatch / unknown id)
just report-label-drift      # baseline: writes reports/label_drift.tsv, never fails
```

## Rollout: report → baseline → enforce

The gates are **not** in `qc` yet — enforcing them will fail on existing drift
(MIM `ontology_label` often holds formulas/abbreviations instead of the
canonical label). The CI workflow `label-correspondence.yaml` runs
`report-label-drift` **non-blocking** and uploads `reports/label_drift.tsv`.

1. `just report-label-drift` → open `reports/label_drift.tsv`.
2. **Triage each row** (see below).
3. Once drift is cleared, add `validate-terms-all` + `validate-products` to the
   `qc` recipe and flip the CI workflow to blocking (Phase 2).

## Triage: wrong label vs wrong ID

A `MISMATCH` means the label is not a name for that ID. Two root causes:
- **Stale/wrong label, right ID** → replace the label with the canonical OBO
  label (move the old surface form to `preferred_term`/`synonyms`).
- **Wrong ID** → the label describes a *different* term; fix the **ID** (the
  more serious bug). Use `scripts/backfill_ontology_labels.py` (OLS4) and the
  `merge-ingredients` / `map-media-ingredients` skills to re-resolve.

An `ID_NOT_FOUND` means the CURIE is absent/obsolete in the ontology — re-map.

## Surfaces covered (`conf/id_label_targets.yaml`)

- `data/curated/mapped_ingredients.yaml`, `data/ingredients/{mapped,unmapped}/*.yaml`
  (`ontology_id`/`ontology_label`, `environment_term`/`environment_label`) — canonical
- `mappings/ingredient_mappings.sssom.tsv` (`subject_*`/`object_*`) — canonical-or-synonym
- `docs/data/mapped_ingredients.csv` (`ontology_id`/`ontology_label`) — canonical-or-synonym
- `mappings/*review*.tsv` — canonical-or-synonym

Prefixes without a configured OAK adapter (`cas:`, `kgmicrobe.compound:`,
`registry:`, `MIM:`) are reported `SKIPPED_NO_ADAPTER`.

## Related

- `scripts/validate_sssom_invariants.py` (Rule B4 — the SSSOM canonical-or-synonym
  check this generalizes), `scripts/backfill_ontology_labels.py`,
  `src/mediaingredientmech/validation/ontology_validator.py` (`validate_term_via_oak`).
