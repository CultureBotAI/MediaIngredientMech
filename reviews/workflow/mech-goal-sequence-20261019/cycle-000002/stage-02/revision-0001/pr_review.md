# Cycle 2 Stage 2 (`causal_graphs`) — Adversarial Review Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Repository:** `CultureBotAI/MediaIngredientMech` (`mediaingredientmech`)
- **Cycle / Stage / Revision:** Cycle `2`, Stage `2` (`causal_graphs`), Revision `1` (`revision-0001`)
- **Pull Request:** `https://github.com/CultureBotAI/MediaIngredientMech/pull/928` (`chore/cycle-02-stage-02-causal-graphs`)
- **Reviewer Conversation ID:** `c04f3217-6f0a-4b61-b294-d6c89b2971de`
- **Review Status:** `complete`
- **Remaining Findings:** `0`

---

## Round 1 Adversarial Findings & Remediations (Commit `6e9f7e048d21d81d8fe44db154750dc4151953bd`)

1. **Finding 1 (P1 — Directory and `mapping_status` counts in `data/ingredients/mapped/*.yaml` and `data/ingredients/unmapped/*.yaml`):**
   - *Finding:* `data/ingredients/mapped/*.yaml` has `2,680` files (`2,611 MAPPED` + `69 REJECTED`), and `data/ingredients/unmapped/*.yaml` has `273` files (`260 UNMAPPED` + `1 AMBIGUOUS` (`data/ingredients/unmapped/CMC_PY_Horse_Serum.yaml`, `UNMAPPED_0740`) + `12 REJECTED`). The mutually exclusive partition in Section 4.1 had double-counted `UNMAPPED` `NAMED_MEDIUM` records across `I1` and `I6`.
   - *Remediation:* Updated both `coverage_report.md` and `validation.md` with exact directory and `mapping_status` counts and a strictly mutually exclusive 12-cohort partition (`I1`–`I8` = `457` ineligible records; `E1`, `E2a`, `E2b`, `E3` = `2,496` `IDENTITY_GATE`-eligible records; total = `2,953`).

2. **Finding 2 (P1 — Schema enum names, slot names, `<facet>#<ROLE>` syntax, `ProteinExample` slots, predicates, and contract diagnostic codes):**
   - *Finding:* `coverage_report.md` and `validation.md` contained paraphrased enum/slot names (`MechanismGraphKindEnum`, `ChemicalBridgeKindEnum`, `basis`, `role_explained`, `entry_name`, `has_active_moiety`) instead of the authoritative definitions in `src/mediaingredientmech/schema/mediaingredientmech.yaml` and `docs/CAUSAL_GRAPH_CONTRACT.md`.
   - *Remediation:* Updated all schema enum names (`IngredientGraphKindEnum`, `BridgeKindEnum`, `AssertionBasisEnum`), slot names (`assertion_basis`, `explains` with `<facet>#<ROLE>` syntax, `ProteinExample` slots `uniprot_id`, `protein_label`, `gene_symbol`, `taxon_id`, `taxon_label`, `entry_status`, `role`), predicates (`BFO:0000051`, `rdfs:subClassOf`, `RO:0018033`/`RO:0018034`, `RO:0018036`, `skos:broadMatch`, `RO:0002020`, `RO:0002233`, `RO:0000056`), and contract diagnostic codes (`IDENTITY_GATE`, `EXPLAINS_UNKNOWN_ROLE`, `SNAPSHOT_INCOMPLETE`, `ONTOLOGY_FACT_MISSING`, `BASIS_UNVERIFIED`, `DELEGATION_TARGET_HAS_NO_MECHANISM`, etc.) across `coverage_report.md` and `validation.md`.

3. **Finding 3 (P1 — `scripts/score_causal_graph_readiness.py` ascending sort order and exact candidate record fields/SHA-256 hashes):**
   - *Finding:* `scripts/score_causal_graph_readiness.py` sorts ascending (`readiness_score` `7.000` at Rank 1 up to `81.500` at Rank `2,611`), and several candidate records in Sections 5 and 6 had drifted readiness ranks, scores, or SHA-256 digests.
   - *Remediation:* Documented both the lowest-scoring mapped records (Ranks `1`–`10` from `--limit 25 --out /tmp/cg_readiness.tsv`, scores `7.000`–`10.000`) and the highest-scoring mapped records (Ranks `2,592`–`2,611` from `--limit 5000 --out /tmp/cg_readiness_all.tsv`, scores `79.500`–`81.500`), and verified every Section 6 candidate record's exact file path, SHA-256 digest, readiness rank/score, `identifier`, `mapping_quality`, role evidence, and `component_associations`.

4. **Finding 4 (P1 — `INFRA_TASKS.md` state and `mappings/duplicate_identifier_baseline.tsv` exemplars):**
   - *Finding:* `INFRA_TASKS.md` currently has `tasks: []` (Steps 3–7 are tracked in the `docs/CAUSAL_GRAPH_CONTRACT.md` Status table), and `CHEBI:26710` (`Nacl.yaml`) is not in `mappings/duplicate_identifier_baseline.tsv`.
   - *Remediation:* Updated all references in `coverage_report.md` and `validation.md` to state that `INFRA_TASKS.md` has `tasks: []` and cite actual `mappings/duplicate_identifier_baseline.tsv` groups (`CHEBI:86345`, `CHEBI:29377`, `cas:39280-21-2`).

---

## Round 2 Adversarial Findings & Remediations (Commit `c4cae75dc3743406fec94cc72d19b0bbf71dd0d0`)

1. **Finding 1 (P1 — Stale rows in `coverage_report.md` Section 5.1 Ranks 9–10 and Section 5.2 Ranks 2592–2601):**
   - *Finding:* In `coverage_report.md`, Section 5.1 Ranks 9–10 (`lines 158–159`) still listed stale rows instead of `Artificial_Sea_Salt.yaml` and `Na2HPO4-NaH2PO4_Buffer.yaml` from `/tmp/cg_readiness.tsv`, and Section 5.2 Ranks 2592–2601 (`lines 167–176`) carried pre-refresh `total_occurrences` counts and `CHEBI:32031` on `K2hpo4.yaml` instead of `CHEBI:131527` (`total_occurrences: 4,555`) from `/tmp/cg_readiness_all.tsv`. (`validation.md` had `0` findings in Round 2.)
   - *Remediation:* Replaced lines `158–159` and `167–176` of `coverage_report.md` with the exact rows from `/tmp/cg_readiness.tsv` and `/tmp/cg_readiness_all.tsv`.

---

## Round 3 Adversarial Re-Verification

- **Reviewer:** `c04f3217-6f0a-4b61-b294-d6c89b2971de`
- **Artifacts Verified:**
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-02/revision-0001/coverage_report.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-02/revision-0001/validation.md`
  - `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-02/revision-0001/pr_review.md`
- **Verdict:** **PASS — 0 actionable findings remain (`remaining_findings = 0`).**
