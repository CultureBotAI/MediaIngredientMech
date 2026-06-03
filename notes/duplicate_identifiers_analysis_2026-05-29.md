# Duplicate `identifier` analysis — 2026-05-29

## Resolution status (updated 2026-06-02)
- **Stereoisomer mis-maps — RESOLVED (PR #37)** via `scripts/fix_stereoisomer_remaps.py`:
  `(R)-3-hydroxybutyrate`→CHEBI:10983, `(S)-3-hydroxybutyrate`→CHEBI:11047 (off achiral
  CHEBI:37054), `L-Carnitine`→CHEBI:16347 (off racemate CHEBI:17126).
- **Remaining category-3 candidates — reviewed, left as-is (no clean fix):**
  - *Shared-CAS source variants* — `cas:84082-64-4` (porcine mucin Type II vs III) is the
    **same chemical substance** at different purity grades → sharing the CAS is correct.
    `cas:9036-88-8` (carob vs yeast mannan) and `cas:39280-21-2` (soy vs potato
    rhamnogalacturonan) are genuinely different source materials, but assigning distinct
    registry IDs needs per-source CAS research (these natural-polymer CAS numbers are
    themselves ambiguous) — deferred to manual curation.
  - *Coarse FOODON/MICRO solution terms* — `NCIT:C896` (3 trace-element solutions),
    `MICRO:0000455`/`MICRO:0001363` (trace-element / liver-extract recipes),
    `ENVO:00001998` (CR1 Soil vs Soil): distinct products/recipes sharing a deliberately-
    coarse parent term. No distinct ontology term exists for most (e.g. "Zeikus trace
    element solution"), so the coarse mapping is the best available — documented variant
    collisions, not errors.
  - *Casein-peptone trio* — PARTIALLY RESOLVED (PR for 2026-06-03) via
    `scripts/remap_peptones_to_micro.py`: `FOODON:03315719` (mammalian milk protein,
    hydrolyzed) was shared by Casein peptone / Trypticase / Tryptone. Tryptone →
    `MICRO:0000182` (tryptone) and Trypticase → `MICRO:0000175` (Trypticase peptone) were
    re-pointed to their precise MICRO terms (each now legitimately co-located with its
    same-substance trade variant — Bacto-tryptone / "Trypticase peptone"). Generic "Casein
    peptone" (occ=0) has no exact MICRO term and remains on FOODON:03315719 (now its sole
    holder — the triple collision is resolved).

## TL;DR
`data/curated/mapped_ingredients.yaml` contains **60 ontology identifiers shared by 2+
records (143 records total)**. These are **not data corruption** — they are surface-form
variants (hydrates, casing, naming, and a few stereoisomers/coarse-ontology cases) that
all resolve to the same ontology term. This is the expected consequence of using the
ontology CURIE as the sole primary key after the dual-identifier scheme was rolled back
(see `identifier_correction.md`): CHEBI/FOODON/MICRO often have no separate term per
hydrate or trade-name, so several distinct ingredient records legitimately map to one term.

No action was taken on the data — resolving these is a design decision (see Options).

## Why this is safe today
- **Indexes are not deduped**: `generate_index_files.py` iterates the record list directly,
  so all 143 records appear in every index. The only identifier-keyed structure is
  `records_by_identifier` (line ~177), used solely to resolve `parent_ingredient` /
  `child_ingredients` hierarchy links — a feature that is currently unused. With dups it
  keeps the last record per id, but nothing depends on it.
- **validate_strict passes**: closed-schema validation is per-record; the collection is a
  YAML list, not an identifier-keyed map, so duplicates are never flagged.

## Categories (60 groups)
1. **Pure hydrate variants — 23 groups.** Same base name, differing waters of
   crystallisation, all → anhydrous CHEBI. e.g. `CHEBI:34683` ← Na2HPO4 + ·2/·3/·6/·7/·12 H2O.
   Unambiguously correct.
2. **Hydrate / casing / naming variants of one substance — ~27 groups.** e.g.
   `CHEBI:3312` ← CaCl2 / CaCl2·7H2O / "Calcium Chloride"; `CHEBI:17201` ←
   Glycyl-glycine / Glycylglycine; `CHEBI:17992` ← D-Sucrose / Sucrose;
   `CHEBI:32954` ← Na-acetate / Sodium acetate / ·3H2O. Same substance, fine.
3. **Genuinely-questionable — review candidates (~10 groups).** The shared term is either
   too coarse or arguably wrong:
   - `CHEBI:37054` — (R)-3-hydroxybutyrate **and** (S)-3-hydroxybutyrate (enantiomers; a
     single achiral CHEBI is too coarse — consider distinct stereo CHEBI ids).
   - `CHEBI:17126` — DL-carnitine vs L-Carnitine (racemate vs enantiomer).
   - `cas:9036-88-8` — "b-Mannan ... carob seed" vs "Mannan from S. cerevisiae"
     (different biological sources sharing one CAS — likely a wrong CAS on one).
   - `cas:84082-64-4` — porcine mucin Type II vs Type III (different grades, one CAS).
   - `cas:39280-21-2` — rhamnogalacturonan from soy vs from potato (different sources).
   - `FOODON:03315719` — Casein peptone / Trypticase / Tryptone (3 distinct products).
   - `NCIT:C896` — Trace element solution / SL-10 / Zeikus (3 distinct recipes).
   - `MICRO:0000455` — Algal vs WC Trace Elements Solution (distinct recipes).
   - `MICRO:0001363` — Liver extract / concentrate / infusion.
   - `ENVO:00001998` — "CR1 Soil" vs generic "Soil".

## Options (for the user to decide — not actioned)
- **A. Accept & document** that `identifier` is the *ontology mapping*, not a globally-unique
  surrogate key; variants intentionally share it. (Lowest effort; matches current reality.)
- **B. Populate the variant hierarchy** (`parent_ingredient` / `child_ingredients` /
  `variant_type`, already in the schema) so hydrate/name variants nest under a canonical
  record while keeping per-variant occurrence counts. Resolves categories 1–2 cleanly.
- **C. Re-tighten ontology granularity** for category-3 review candidates (distinct
  stereo/source/recipe → distinct or registry identifiers), leaving only true variants sharing a term.
- **D. Re-introduce a unique surrogate key** — explicitly rejected before (dual-id rollback);
  noted only for completeness.

Recommendation: **A + C** — document the trait, and send the ~10 category-3 groups to
curator review (esp. the enantiomer and shared-CAS cases, which may be genuine mapping errors).
