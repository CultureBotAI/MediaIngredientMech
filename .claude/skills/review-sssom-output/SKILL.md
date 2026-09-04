---
name: review-sssom-output
description: "Review final MediaIngredientMech SSSOM output for GAP/ORPHAN/STALE drift, predicate and registry-row invariant failures, id-label drift, unresolved MIM subjects, and unsafe synonyms in `other` before KG-Microbe publication."
category: validation
requires_database: false
requires_internet: false
version: 1.0.0
tags: [sssom, validation, kg-microbe, mappings, synonyms, quality-assurance]
---

# Review SSSOM Output

## Core Scope

Audit `mappings/ingredient_mappings.sssom.tsv` as the final published
MediaIngredientMech SSSOM product. Every row must agree with
`data/curated/mapped_ingredients.yaml`, obey the predicate contract in
`MAPPING_SEMANTICS.md`, carry canonical-or-synonym labels in product columns,
and avoid republishing rejected or noisy text through the `other` column.

Use this skill for the published TSV and downstream products:

- `mappings/ingredient_mappings.sssom.tsv`
- `mappings/needs_curator_review.tsv`
- `docs/data/mapped_ingredients.csv`
- `UNIFIED_INGREDIENT_MAPPING.tsv`, when a cross-repo snapshot is part of the
  review

Do not use this as the primary workflow for new ontology mapping, duplicate
merging, or deep identity research. Escalate those root-cause fixes to
`map-media-ingredients`, `merge-ingredients`, or
`mediaingredientmech-agentic-curation`.

## Read-Only Audit First

Start with commands that report the TSV's current state before editing anything.

```bash
python scripts/reconcile_sssom.py
just qc-sssom
just curie-validate
python scripts/check_sssom_subject_files.py
just validate-products
```

Read the generated reports and validator stderr:

- `scripts/reconcile_sssom.py` reports `GAP`, `ORPHAN`, and `STALE` drift
  between mapped curated YAML records and the SSSOM.
- `just qc-sssom` runs `scripts/validate_sssom_invariants.py` and writes
  rejected rows to `mappings/needs_curator_review.tsv`.
- `just curie-validate` asserts the published SSSOM uses valid CURIE syntax.
- `scripts/check_sssom_subject_files.py` reports `MIM:` subjects whose slug no
  longer resolves to a per-record YAML file. This is reported, not gated, while
  issue #236 keeps `MIM:` subject semantics undecided.
- `just validate-products` enforces id-label correspondence across the final
  SSSOM and docs CSV product columns under the canonical-or-synonym policy from
  `conf/id_label_targets.yaml`.

## Review Questions

Check each questionable row against these questions:

- **Subject currency:** is every `subject_label` present as a mapped ingredient
  in `data/curated/mapped_ingredients.yaml`?
- **Subject slug:** does the `MIM:<slug>` still identify the intended record,
  even if `scripts/check_sssom_subject_files.py` says the slug no longer
  matches a file stem?
- **Object identity:** does `object_id` match the record's current
  `ontology_mapping.ontology_id` for the ontology row?
- **Predicate semantics:** does `mapping_quality` map to the right SSSOM
  predicate: `EXACT_MATCH` and `SYNONYM_MATCH` to `skos:exactMatch`,
  `CLOSE_MATCH` to `skos:closeMatch`, `NARROW_MATCH` to `skos:narrowMatch`, and
  `BROAD_MATCH` to `skos:broadMatch`?
- **Registry sibling:** does every `skos:narrowMatch` or `skos:broadMatch` row
  have a sibling `MIM:<slug> skos:exactMatch
  kgmicrobe.{ingredient,compound}:<slug_lc>` row for the same subject?
- **Identity rows:** is a row that maps to the record's own `identifier` always
  an `skos:exactMatch` row, regardless of the ontology mapping quality?
- **Object source:** does every row name the ontology or registry behind its
  target in `object_source`?
- **Object label:** is every OBO `object_label` either the canonical ontology
  label or an exact/related ontology synonym for that exact `object_id`?
- **Published synonyms:** is every pipe-delimited token in `other` a real
  resolving synonym for the subject, not a `REJECTED_LABEL`, assay role,
  concentration note, non-resolving catalog label, or bare CAS value copied from
  structured chemistry metadata?
- **Duplicate pairs:** does each `(subject_id, object_id)` pair appear once and
  under only one predicate?

## Fix Patterns

Fix the source of truth whenever the final SSSOM reflects bad curation data:

- Edit `data/ingredients/mapped/<Slug>.yaml` or
  `data/curated/mapped_ingredients.yaml`, depending on where the drift came
  from.
- Keep `REJECTED_LABEL` entries as provenance-only typed synonyms. They may stay
  in YAML, but they must not be emitted in SSSOM `other`.
- Put assay-only, role-only, concentration-only, and non-resolving catalog labels
  in provenance or `notes`, not active resolving synonyms.
- Preserve raw aliases as typed synonyms only when they genuinely resolve the
  same ingredient surface.
- Use `kgmicrobe.compound:` for distinct simple chemicals that lack an ontology
  term; use `kgmicrobe.ingredient:` for distinct non-chemical ingredients.
- Regenerate the final SSSOM from the sibling CultureBotAI builder after YAML
  repairs so the committed TSV remains a product of curated records.

Use the reconcile script only for mechanical drift where curated YAML is already
authoritative:

```bash
python scripts/reconcile_sssom.py --apply --date YYYY-MM-DD
```

`reconcile_sssom.py --apply` can rewrite `STALE` ontology rows and drop
`ORPHAN` subjects. It deliberately reports `GAP` rows without inventing new SSSOM
provenance, so add those rows through the normal builder or a purpose-built
apply script.

## Validation

Re-run the narrow gates after every SSSOM repair:

```bash
python scripts/reconcile_sssom.py
just qc-sssom
just curie-validate
just validate-products
```

For PR-ready changes, run the repository composite:

```bash
just qc
```

If `just validate-products` writes `reports/label_drift.tsv`, triage rows as
wrong label vs wrong id with `id-label-correspondence`. A mismatched label in the
SSSOM is often a stale generated product; a mismatched id is a mapping bug.

## Escalation

- Use `map-media-ingredients` when a row points at the wrong CHEBI, FOODON,
  ENVO, NCIT, MICRO, BTO, PATO, MeSH, CAS, or KG-Microbe target.
- Use `merge-ingredients` when a GAP/ORPHAN/STALE cluster is caused by duplicate
  MIM records for one ingredient identity.
- Use `id-label-correspondence` when the same id-label mismatch appears across
  YAML inputs, SSSOM, docs CSV, or review TSVs.
- Use `build-unified-mapping` when the audit must compare the final SSSOM to the
  cross-repo CultureMech coverage snapshot.
- Use `mediaingredientmech-agentic-curation` when the correct identity, formula,
  CAS-RN, synonym, or parent term needs source-backed evidence.

## Final Summary

Report:

- SSSOM row count before and after
- `GAP`, `ORPHAN`, and `STALE` counts before and after
- invariant failures fixed, grouped by validator rule
- `other` synonym decisions, especially removed `REJECTED_LABEL` or noisy
  tokens
- YAML records, generated TSVs, and review TSVs changed
- validation commands and results
