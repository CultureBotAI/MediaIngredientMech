# kg-microbe integration follow-up, 2026-09-22

This is a new mapping-specific review of the 17 fallback blockers in
[kg-microbe #1123](https://github.com/Knowledge-Graph-Hub/kg-microbe/issues/1123),
tracked upstream in [#752](https://github.com/CultureBotAI/MediaIngredientMech/issues/752).
The historical review reports and immutable `mim-sssom-2026-09-21` assets remain
available as originally published.

`kgmicrobe-followup.json` binds every decision to the entire current SSSOM row,
its owner bytes and inspected evidence. `kgmicrobe-ontology-evidence.json`
records the selected statements from local SemanticSQL ontology snapshots.
The dated assembler refuses changed evidence, missing aliases, changed prior
negative findings, and attempts to override relation, grounding-grade or
preparation safeguards. The standalone exporter verifies the evidence hashes
independently. These decisions approve mappings only; they confer no role or
biological trait approval.

| Current mapping | Decision and evidence |
| --- | --- |
| Abyssomicin D → mesh:C512805 | SUPPORT: archived identity review and MeSH agree on the specific D congener; no exported aliases. Provisional role and stale historical UNKNOWN_TERM annotation are separate findings. |
| Butyricin 7423 → mesh:C010427 | SUPPORT: archived identity review and MeSH agree on the specific bacteriocin; no aliases. Old placeholder notes do not describe the current mapping. |
| beta-Lipomycin → mesh:C000601869 | SUPPORT: specific beta substance; the complete alias set is the independently reviewed spacing/case variant “Beta Lipomycin”. Explicitly resolves the earlier alias-review objection. |
| Alanosine → CHEBI:221124 | SUPPORT: archived structure review establishes the L compound and its remaining exact IUPAC synonym. This is a review of the defined MIM record, not an inference that every bare source use denotes the L form. |
| Ferroverdin → CHEBI:219729 | SUPPORT: archived identity/structure review and exact ChEBI synonym for the same complex. |
| Kijanimicin → CHEBI:220048 | SUPPORT: archived formula/structure review and the single retained exact ChEBI IUPAC synonym. |
| Miharamycin A → CHEBI:216282 | SUPPORT: archived structure and explicit A/B distinction; retained IUPAC synonym is exact on the A target. |
| Monazomycin → CHEBI:201539 | SUPPORT: archived ChEBI/PubChem identity and formula agree; the retained IUPAC synonym is exact. |
| Nocamycin → CHEBI:219652 | SUPPORT: archived formula/structure review and exact retained ChEBI synonym. |
| Stallimycin → CHEBI:41958 | SUPPORT: archived PubChem CID 3115 review confirms distamycin A, same formula and identity; no remaining aliases. Hydrochloride-related ChEBI synonyms are not used as free-base equivalence evidence. |
| Hydrogen gas → CHEBI:18276 | WITHHOLD: current aliases still include H2_CO2, H2_methanol and Diydrogen. Pure dihydrogen identity does not approve mixture aliases. |
| Angustmycin → CHEBI:8612 | WITHHOLD: A/C specificity remains unresolved (#741); the old process phrase is already removed. |
| Rubradirin → CHEBI:223718 | WITHHOLD: generic source name does not establish Rubradirin B; the old process phrase is already removed. |
| Etamycin → mesh:C004910 | WITHHOLD: Viridogrisein is only a related MeSH synonym in the inspected evidence; complete alias equivalence needs independent support. |
| Rhodomycin A / Pluramycin A / Racemomycin E → MeSH parent | WITHHOLD: the precise broader relation remains unreviewed. Each specific local registry identity is separately supported; downstream can use that identity without strengthening the parent into exactMatch. |

Nine stale process-phrase explanations are replaced with current row-specific
reasoning. Seven cleaned identities above are supported after complete review;
Angustmycin and Rubradirin remain withheld for substantive identity reasons.

The disagreement audit also found three invalid supported CAS identifiers
([#753](https://github.com/CultureBotAI/MediaIngredientMech/issues/753)):
Izalpinin `cas:480-14-4`, Lysozyme `cas:2650-88-3`, and
Methyl-2-Hydroxy-Phenylproprionate `cas:89471-28-0`.
`cas-check-digit-evidence.json` records the reproducible calculation and its CAS
authority source. These exact assertions are withheld, without guessing
replacement identifiers. A permanent supported-release check now rejects
malformed CAS RNs; valid arithmetic still requires scientific identity review.

Relative to main `5019d687`, the result is ten new supported decisions and
three withdrawals: 1,758 supported / 1,269 withheld / 3,027 source rows.
The seven remaining decisions in the original 17-row cohort stay withheld.
No source YAML or canonical mapping payload changes in this follow-up.
The full graph remains unreleasable while unrelated scientific findings stay
open; supported-subset export remains independently validated.

A new reviewed release is required before downstream consumes these changed
approvals. The old KGM pin remains candidate-only. This review does not clear
coverage losses, remaining identifier disagreements, or the downstream
producer/merge review in #1123.
