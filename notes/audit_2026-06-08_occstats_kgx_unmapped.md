# Audit pass 2026-06-08 — occurrence stats / KGX / high-occurrence unmapped

## 1. occurrence_statistics audit — FIXED
New `scripts/audit_occurrence_stats.py` (`--check` CI gate / `--fix`). The corpus was
otherwise consistent (0 REJECTED-with-occurrences, 0 negatives, 0 media_count >
total_occurrences). The one issue: **10 records had `occurrence_statistics: null`** —
all ontology-derived (`AUTO_CREATE_FROM_MICRO` / CHEBI) records that were never tracked
in media counting (peptone variants, MnCl2/borate, two PAHs). Backfilled to `0/0` with a
`CORRECTED` curation event. `tests/test_occurrence_stats.py` now guards this.

(Note: ~1211 MAPPED records legitimately have 0 occurrences — many CultureBotHT compounds
are catalogued but unused in any medium. That is expected, not an inconsistency.)

## 2. KGX export refresh — N/A (no export exists)
There is **no KGX / Biolink edge export in the repo** (grep for biolink/kgx/has_part/
edges.tsv/nodes.tsv finds only a curie_map mention in `validate_sssom_invariants.py`).
The earlier memory note referenced a `kgx_export.py` that is not present here (likely a
CultureMech tool or never committed). "Refresh" is therefore not applicable; building a
KGX exporter is a new feature, out of scope for this audit pass. The SSSOM set
(`mappings/ingredient_mappings.sssom.tsv`) is the current machine-readable export and is
kept current by `reconcile_sssom.py` + its CI gate.

## 3. High-occurrence unmapped mixes — reviewed, correctly unmapped
The highest-occurrence unmapped records are legitimately unmappable and already correctly
classified; no clean action exists:
- **Placeholders** — `Full composition available at source database` (occ 196),
  `See source for composition` (143): media whose recipe wasn't parsed; correctly
  `UNDEFINED_MIXTURE`. Not real ingredients (cf. the removed CHEBI:1 artifact) but they
  carry the "composition unavailable" signal for those media, so retained.
- **Defined stock solutions** — Wolfe's vitamin/mineral mix + ATCC variants (61/60/46/43),
  `Mc_*` salt/vitamin mixes, `P-IV Metal Solution`, `MOPS_2M_pH7` (`STOCK_SOLUTION`): multi-
  component recipes with **no single ontology term** and **no stashed KG source_id**
  (checked — all NONE), so they cannot be mapped to a chemical ontology or promoted to a
  `kgmicrobe.solution:` node. Correctly classified.
- **Defined media** — `ZMB_ALS`, `MoLS4` (`DEFINED_MEDIUM`): complete media, not ingredients.
- **Undefined mixtures** — `Sea salts`, `Vitamin B`: no single term.

Conclusion: these need recipe-level decomposition (out of scope) to become structured, not
an ontology mapping. Classifications verified correct; no changes made.
