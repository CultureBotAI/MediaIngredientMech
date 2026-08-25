# ATTIC

Historical status reports, completion writeups, and executed plans from past
curation pushes. These files were originally at the repo root; they describe
work that is **done** and snapshots of state that is now **stale**, so they're
preserved here for reference rather than as living docs.

Live docs:

- Repo orientation → top-level `README.md`
- Predicate / mapping semantics → top-level `MAPPING_SEMANTICS.md`
- Curator workflows and operational guides → `docs/`
- Per-batch / per-session curation notes → `notes/`

Caveats when reading anything in this directory:

- Many files reference the brief 2026-03-14 dual-identifier scheme
  (`id: MediaIngredientMech:NNNNNN`) which was **rolled back**. The canonical
  semantic identifier slot today is `identifier` (an ontology CURIE or
  `UNMAPPED_NNNN`), but it is not a guaranteed unique document address.
- File-level cross-references between attic files use the old root-level
  paths; they resolve because every file lives here together, but links
  pointing into `docs/` or `notes/` from inside the attic may be stale.
- `HIERARCHY_GUIDE_RETIRED.md`, `WATER_VARIANT_CURATION_RETIRED.md`,
  `build_water_hierarchy.py`, `analyze_duplicates_and_variants.py`, and
  `duplicates_and_variants.yaml` are the retired #448 ingredient-hierarchy
  prototype and analysis snapshot. They target a rolled-back record shape and
  are non-runnable historical material; do not use them as schema, API,
  curation instructions, or current analysis output.
- `id_utils.py` and `manage_identifiers_sequential_id_reference/` preserve the
  rolled-back `MediaIngredientMech:NNNNNN` utility and instructions. Current MIM
  records use ontology CURIEs or `UNMAPPED_NNNN` in `identifier`; these archived
  examples must not be run against MIM data.
- `apply_corrections.py` and `unmerge_complex_media.py` are retired mutators
  that addressed records through the removed `id` field (and, in the correction
  writer, emitted a stale curation-event shape). They are not safe current APIs.
- `reconcile_unmapped.py` is a retired hard-coded cross-repository report using
  the same old record shape and collision-losing label dictionaries. The #453
  comparator supersedes it.
- `merge_pattern_analysis.{md,yaml}` and the `good_merge_examples.md` /
  `bad_merge_examples.md` catalogs are a retired 211-cluster training snapshot.
  They use rolled-back surrogate IDs and include water/hydrate merge judgments
  that conflict with current identity semantics.
- `merge_identifier_collisions.py` is the completed #414/#417 one-shot merge.
  It is not a reusable current curation command; its pre-baseline uniqueness
  language is retained only as historical context.
