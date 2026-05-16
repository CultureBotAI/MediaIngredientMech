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
  primary key on a record today is `identifier` (an ontology CURIE or
  `UNMAPPED_NNNN`).
- File-level cross-references between attic files use the old root-level
  paths; they resolve because every file lives here together, but links
  pointing into `docs/` or `notes/` from inside the attic may be stale.
