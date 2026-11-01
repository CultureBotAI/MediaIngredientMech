Fresh bounded audit of main `4625afd492b6cf43e3b499d1425d2453d490009d` (before this run’s narrowly scoped curation): **2,987 canonical rows, 45 Rule K collision pairs, 45 baseline entries, 0 unbaselined failures and 0 unused baseline entries**. Baseline dispositions are 25 `HYDRATE_FAMILY_UNREVIEWED` and 20 `UNREVIEWED`. All current owners were resolved with native merge/tombstone semantics; none of these 45 pairs requires retired-owner credit. Historical #699/#763 counts are not being carried forward.

**Seven YAML-backed cases remain unchanged.** Current official ChEBI confirms these common labels, with an important scope distinction:

| Specific record | Colliding label | Current ChEBI assertion |
| --- | --- | --- |
| `MIM:Beta-lactose` | `lactose` | hasRelatedSynonym on [CHEBI:36218](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:36218) |
| `MIM:D-mannitol` | `Mannitol` | hasExactSynonym, hasRelatedSynonym on [CHEBI:16899](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16899) |
| `MIM:L-asparagine` | `ASPARAGINE` | hasExactSynonym, hasRelatedSynonym on [CHEBI:17196](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17196) |
| `MIM:L-cysteine` | `CYSTEINE` | hasExactSynonym, hasRelatedSynonym on [CHEBI:17561](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17561) |
| `MIM:L-glutamic_Acid` | `GLUTAMIC ACID` | hasExactSynonym, hasRelatedSynonym on [CHEBI:16015](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16015) |
| `MIM:L-proline` | `PROLINE` | hasExactSynonym, hasRelatedSynonym on [CHEBI:17203](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:17203) |
| `MIM:L-tryptophan` | `Tryptophan` | hasExactSynonym, hasRelatedSynonym on [CHEBI:16828](https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:16828) |

All seven generic preferred-name owners already come first in the current native `label_index.csv`, with `resolved:owned`; the older claim that uppercase aliases necessarily select L-specific records is stale for that consumer. This does **not** settle unqualified aliases in SSSOM `other`, or make the specific and generic substances identical. Beta-lactose’s current ChEBI `lactose` assertion is **related**, while its MIM synonym is typed exact; that discrepancy must remain visible instead of claiming all seven are ChEBI exact synonyms.

**Policy options requiring an explicit decision:**

1. Retain shared common names as resolving aliases, with explicit accepted collision obligations and generic-owner precedence at every consumer. This preserves ontology vocabulary but requires consumers to carry the scope/ambiguity instead of interpreting `other` as unqualified exact names.
2. Retain sourced typed aliases in YAML but suppress ambiguous generic-owned tokens from unqualified SSSOM alias publication through an explicit, reviewed export policy. A simple `EXACT_SYNONYM`→`RELATED_SYNONYM` edit is insufficient because the current exporter publishes both.
3. Retire a name as a wrong-substance alias only when claim-level evidence supports that record-specific decision; never infer this solely from a collision, stereochemical prefix, or absent dictionary entry.

**Recommendation:** preserve all seven now; choose option 2 as a separate consumer/export-contract change, with generic-name ownership and source synonym scope retained. Do not silently turn this recommendation into seven `REJECTED_LABEL` edits, identity merges, or scientific approval.

**The other 38 aliases are absent from current subject YAML.** Only 6 are recoverable from today’s KG target-alias loader; absence from that dictionary is not evidence of chemical falsity. Per-pair assessment separates:

- **23 pairs** whose subject or preferred-name owner is in open #912: preserve and coordinate the hydrate/solution-family adjudication.
- **8 pairs** requiring identity or name-scope decisions: Vibriostat/phosphate, the two Carnitine hydrochloride records, the shared-ID magnesium and ammonium-nickel hydrate pairs, Na2glycerophosphate5h2o, lithium glycerol phosphate, and sodium succinate dibasic. In particular, CAS 150-90-3 and CHEBI:63675 denote the same anhydrous sodium succinate; deleting that alias as chemically false would be unsupported.
- **7 bounded alias-removal candidates** are supported by distinct primary-source chemistry or explicit maintained stock identity, independently of KG availability:
  - `MIM:4-Methyl-2-oxopentanoic_Acid_Sodium_Salt` / `4-Methyl-2-oxovaleric acid`: PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430 is the acid C6H10O3. The parent preferred name cannot assert exact substance identity for this sodium salt.
  - `MIM:84_GL_NaHCO3_Solution` / `NaHCO3`: The maintained identity is explicitly a stock solution kgmicrobe.ingredient:84_gl_nahco3_solution, with concentration and solution curation; the owner NaHCO3 is neat sodium hydrogencarbonate CHEBI:32139. This is a mixture/concentration boundary, not merely spelling.
  - `MIM:Betaine_Hydrochloride` / `Betaine x H2O`: PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242 is glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate identities differ.
  - `MIM:D-Mannose_6-phosphate_Sodium_Salt` / `Mannose-6-Phosphate`: PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369 is D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material.
  - `MIM:MES_Hydrat` / `MES [2-(N-morpholino) ethane sulfonic acid]`: PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S. This evidence supports a form boundary independent of KG alias availability.
  - `MIM:Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt` / `Glycerol 3-phosphate`: PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P; ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias does not require guessing the salt identity.
  - `MIM:Sodium_Perchlorate` / `Sodium perchlorate monohydrate`: PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate ClH2NaO5. ChEBI:132103 confirms the anhydrous subject.

These seven are recommendations, **not applied**. Any refresh requires the native producer, exact row selectors, preserved source provenance, mapping-change receipts, and review holds. Full regeneration is not promoted: its wider row-class/payload changes must not be mistaken for an alias-only correction. #912 touches canonical SSSOM and shared aggregates/exports; #914 touches shared aggregates/exports. No broad refresh may supersede those PRs.

Separate genuine defects are now tracked before edits:

- #1003: residual **carnitinamide** IUPAC name on `Carnitine_Hydrochloride`, despite the July correction removing the wrong amide identity. Its bounded correction retains the name/source as `REJECTED_LABEL`; this is not one of the 45 baseline tokens.
- #1004: `Carnitine_Dl_Hydrochloride` primary CAS461-06-3/structure is DL-carnitine without chloride.
- #1005: `Sn-Glycerol_3-phosphate_Lithium_Salt` primary CAS17989-41-2/structure is the free acid.

The latter two were explicitly untracked in #887. Their new issues retain source-backed alternatives and prohibit guessed replacement CAS IDs or automatic merges. Original-source identity evidence is needed before treating the parent-name aliases as settled wrong-substance labels.

The exact 45-row inventory, complete #912/#914 file snapshots, source responses with timestamps and hashes, historical ignored-inclusive search scope, and per-pair dispositions are saved in `reports/sssom_scientific_curation_20261101/audit669/` for the forthcoming curation PR. This diagnostic audit does not grant whole-record or release approval.
