# Deep-research: grounding the microbedecoder residual chemicals

**Date:** 2026-08-04
**Branch:** `research/microbedecoder-residual-chemicals`
**Method:** 10 parallel literature/database subagents (WebSearch + WebFetch against EBI CHEBI,
OLS4, PubChem, DSMZ MediaDive, ATCC, primary literature); the 20 single-compound CHEBI
decisions were each independently adversarially re-verified (all returned CONFIRMED).
**Source of the target list:** the residual triage already produced on
`feat/microbedecoder-residual-grounding` (PR #192 follow-on) — files
`mappings/microbedecoder_residual_deferred_ncit.tsv`,
`mappings/microbedecoder_demoted_antibiotics_triage.tsv`, and
`mappings/microbedecoder_residual_blends.tsv`.

## Scope — why these ~60 labels and not the other 5,000

The upstream file is `kg-microbe/data/transformed/microbedecoder/unmapped_labels.tsv`, staged
here as `data/custom/microbedecoder/unmapped_labels.tsv` (5,224 rows). Most rows are numeric
phenotype measurements, isolation-category environment/host context, enzyme names, or metabolic
pathways — not chemicals (see `notes/microbedecoder_source_assessment_2026-08-03.md`). Of the
~1,023 chemical/ingredient candidates, the existing grounding passes already handled the easy
cases: the #193 import exact-matched labels, and the #192 follow-on recovered 20 more by
normalized/fuzzy matching and re-promoted 11 falsely-demoted antibiotics. Those passes then
**explicitly deferred three buckets to deep research** — that is exactly what this report
covers, so nothing already grounded is re-done here.

## Deliverables

- `mappings/microbedecoder_residual_research_proposed.tsv` — 22 single-term decisions
  (buckets A–C below + parse-artifact singletons), ready for a curator to apply.
- `mappings/microbedecoder_residual_research_decomposition.tsv` — 43 multi-component media /
  co-substrate labels with recommended split/complex-medium strategy and component CURIEs.
- `mappings/microbedecoder_residual_research_proposed.sssom.tsv` — the single-term **ledger**
  (13-column schema matching `ingredient_mappings.sssom.tsv`), with a per-row `validation_method`
  status: `APPLIED` (3), `ALREADY_MAPPED_SYNONYM_MERGE` / `ALREADY_MAPPED_NEEDS_SPLIT` (7),
  `DEFERRED_*` (10). The two NO_GROUNDING items (keratin, Mono-and-Disaccharides) are omitted.

## Applied vs deferred — what actually happened

Working through the 22 single-term proposals against MIM's *existing* records changed the
picture: 7 of the "net-new" labels turned out to already be mapped in MIM under a canonical
label (exactly the "fuzzy matching moves net-new into already-known" caveat the 2026-08-03
assessment flagged). Final disposition:

**APPLIED (3 net-new)** — promoted `unmapped/` → `mapped/` via
`scripts/promote_resolved_unmapped.py --apply` (record moved, canonical CHEBI label set,
`PROMOTED_TO_MAPPED` history entry, SSSOM row added to `ingredient_mappings.sssom.tsv`, docs
regenerated). All gates green: `reconcile_sssom` GAP 0, id-label ✅, SSSOM Rules A/B1/B2/B3,
`validate-strict` 0 errors.

| residual label | → CHEBI | mapped record |
|---|---|---|
| Diacetyl (UNMAPPED_0810) | CHEBI:16583 | `Diacetyl.yaml` |
| Ferric Iron (UNMAPPED_0667) | CHEBI:29034 | `Ferric_Iron.yaml` |
| Sodium(+) (UNMAPPED_0843) | CHEBI:29101 | `Sodium().yaml` — curator may relabel to `sodium(1+)` |

**ALREADY MAPPED → synonym-merge, NOT applied (7)** — the CHEBI term is already a MIM record;
the residual label should be added as a **synonym** to the existing record rather than made a
new mapping. Forcing the promoter here left dangling duplicates and (for RNA) a bad merge, so
these are left for a curator synonym pass:

| residual label | CHEBI | existing MIM record | action |
|---|---|---|---|
| Alpha-hydroxybutyrate | CHEBI:64552 | `2-hydroxybutyrate` | add synonym |
| Beta-hydroxybutyrate | CHEBI:37054 | `3-hydroxybutyrate` | add synonym |
| Achromycin | CHEBI:27902 | `Tetracycline` | add trade-name synonym |
| Neomycin E | CHEBI:7934 | `Paromomycin` | add synonym |
| (+)-D-glycogen | CHEBI:28087 | `Glycogen` | add synonym (parse artifact) |
| (+)-L-lyxitol | CHEBI:18403 | `Arabitol` | confirm enantiomer, add synonym |
| RNA | CHEBI:33697 | `Ribonucleic acid from torula yeast type VI` | **split needed** — generic RNA must not merge onto the specific Torula-yeast product record |

**DEFERRED (10)** — 6 antibiotics absent from the local `chebi.db` (>747618; OLS4-validated,
unblock on the #200 refresh), **filipin** (broadMatch → needs a registry sibling the promoter
won't synthesise), and the 3 non-CHEBI parse/variant items (Peptones, Peptone/Yeast-Extract
`(0.01 %` → merge into existing `MIM:Peptone` / `MIM:Yeast_Extract`).

The `decomposition.tsv` (43 multi-component labels) remains research output for a curator pass —
not applied.

---

## Bucket A — 9 deferred single compounds (NCIT rejected → CHEBI)

All CONFIRMED by independent verification.

| source label | → CHEBI | label | predicate | conf | key point |
|---|---|---|---|---|---|
| alpha-hydroxybutyrate | CHEBI:64552 | 2-hydroxybutyrate | exact | high | racemic anion; exact synonym; α=2-position |
| beta-hydroxybutyrate | CHEBI:37054 | 3-hydroxybutyrate | exact | high | racemic DL anion; β=3-position; rejects NCIT "Measurement" |
| ferric iron | CHEBI:29034 | iron(3+) | exact | high | Fe(III) cation; rejects NCIT "Ferric" adjective |
| diacetyl | CHEBI:16583 | butane-2,3-dione | exact | high | rejects NCIT "Diacetyl Measurement" |
| RNA | CHEBI:33697 | ribonucleic acid | exact | high | "RNA" is a CHEBI synonym; rejects NCIT "RNA Measurement" |
| keratin | **NO_GROUNDING** | — | — | high | ChEBI excludes proteins; route to Protein Ontology (PR) |
| Achromycin | CHEBI:27902 | tetracycline | exact | high | trade name; free base preferred over HCl salt CHEBI:35006 |
| Filipin | CHEBI:83267 | filipin III | **related** | medium | no "filipin complex" term; filipin III = major (~76%) isomer |
| neomycin E | CHEBI:7934 | paromomycin | exact | high | neomycin E is a documented synonym of paromomycin |

**Curator notes.** *Keratin* has no CHEBI grounding at all — it is a structural-protein family
and should be routed to PR/UniProt, not the ingredient pipeline. *Filipin* is deliberately a
`relatedMatch` (narrower single isomer standing in for the complex), not an exact match.

## Bucket B — 6 antibiotics beyond local CHEBI coverage (ID validation)

These already had candidate CHEBI IDs; they were demoted only because the local `chebi.db`
accession ceiling is stale (reaches 747618; these sit above it). All six re-validated as
**current, non-obsolete, exact-label** CHEBI terms in OLS4 — they are blocked on a `chebi.db`
refresh, not on identity. All CONFIRMED.

| label | CHEBI | conf | note |
|---|---|---|---|
| carbomycin | CHEBI:756054 | high | macrolide; no competing canonical entry |
| colistin sulfate | CHEBI:759883 | high | salt term matches salt label; parent colistin = CHEBI:37943. Caveat: ChEMBL entry lacks formula, synonyms contaminated with kanamycin brand names |
| gentamicin | CHEBI:759884 | high | exact-label ChEMBL entry; stable curated alternative CHEBI:17833 "gentamycin" |
| lysostaphin | CHEBI:753395 | medium | valid CHEBI term, but lysostaphin is a ~27 kDa endopeptidase (EC 3.4.24.75) — PR is ontologically more precise |
| netilmicin | CHEBI:748901 | high | correct formula; better than variant-spelling CHEBI:7528 "netilmycin" |
| polymyxin B | CHEBI:759086 | high | clinical-mixture term; better than too-specific B1/B2 components |

## Bucket C — parse-artifact singletons (from the "blends" list)

Labels mangled by upstream CSV parsing that are actually single ingredients:

| source label | → | label | note |
|---|---|---|---|
| Sodium(+) | CHEBI:29101 | sodium(1+) | "(1+)" charge mangled to "(+)" |
| (+)-D-glycogen | CHEBI:28087 | glycogen | stray optical-rotation prefix |
| (+)-L-lyxitol | CHEBI:18403 | L-arabinitol | L-lyxitol is a synonym; confirm enantiomer |
| Peptones | MICRO:0000178 | peptone | plural variant |
| Peptone (0.01 % | MICRO:0000178 | peptone | truncated concentration annotation |
| Yeast Extract (0.01 % | FOODON:03315426 | yeast extract | truncated concentration annotation |
| Mono- And Disaccharides | **NO_GROUNDING** | — | grouping term, not a single entity |

(MICRO:0000178 / FOODON:03315426 verified against existing repo records for Peptone / Yeast
Extract.)

## Bucket D — 43 multi-component labels (decomposition / complex media)

Full component breakdown in `microbedecoder_residual_research_decomposition.tsv`. Two shapes:

1. **Co-substrate pairs** (electron donor + acceptor / two carbon sources joined with "+"):
   the H2+X, Formate+X, alcohol+CO2, and Glucose+X families. Each **decomposes** cleanly into
   two CHEBI terms. Only caveat: 3-methylmercaptopropionate (MMPA) — CHEBI:1438 is the acid
   form, the label is the anion (no distinct anion entry found).
2. **Named complex media** (BHI, PYG/PYGS/GYPS/PYEG, TYGVS, rumen-fluid media, cooked-meat
   media). The PYG family decomposes into peptone + yeast extract + glucose (+ salts/starch);
   BHI and cooked-meat/FAB media are better mapped whole to an existing complex-medium concept
   (MICRO:0000193 BHI, FOODON:03305103 cooked meat). Undefined biologicals (yeast extract,
   peptone, rumen fluid, horse serum, corn steep liquor) are called out with their own terms.

**Gaps flagged for the curator:** rumen fluid has no exact term (nearest MICRO:0000520
"clarified rumen fluid" broadMatch / UBERON:0010228); corn steep liquor has no FOODON/CHEBI
term (use CAS 66071-94-1 or mint a `kgmicrobe.compound:` placeholder); the TYGVS VFA mixture
is an undefined blend with no single CURIE.

---

## Recommended next steps (not done here)

1. Done in this PR: the 3 net-new groundings (Diacetyl, Ferric Iron, Sodium(+)) are applied.
   Remaining single-term work is a curator **synonym pass** for the 7 already-mapped labels
   (add each residual label as a synonym on the existing record; split the RNA/Torula case),
   plus the parse/variant merges. Keep *keratin* and *Mono- and Disaccharides* as NO_GROUNDING
   (or route keratin to PR).
2. For bucket B, these confirmations unblock as soon as `chebi.db` is refreshed past 747618
   (tracked by #200); until then they resolve in OLS4 but not the local adapter.
3. Decompose bucket D per the decomposition TSV; mint placeholders for the three flagged gaps
   (rumen fluid exactness, corn steep liquor, VFA mixture).
4. All CHEBI IDs here were validated in OLS4 on 2026-08-04; re-confirm against the pinned
   ontology release at apply time.
