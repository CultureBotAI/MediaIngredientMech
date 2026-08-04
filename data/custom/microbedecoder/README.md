# microbedecoder unmapped labels (external source)

Staged from `kg-microbe/data/transformed/microbedecoder/unmapped_labels.tsv` on 2026-08-03.

- `unmapped_labels.tsv` — verbatim copy of the kg-microbe microbedecoder residual (labels the
  transform could not ontology-map). Columns:
  `placeholder_curie | category | label | source_columns | occurrences`.
- `ingredient_candidates.tsv` — derived: the 1,023 rows whose source column is a chemical/
  substrate/metabolite/antibiotic assay, sorted by occurrence, flagged `already_in_mim`.

See `notes/microbedecoder_source_assessment_2026-08-03.md` for the full assessment. Short
version: ~1,023 distinct chemical/ingredient labels (676 net-new to MIM); the remaining ~4,200
rows are numeric phenotype measurements, isolation-category environment/host/food context, or
metabolic-function pathways — not media ingredients.
