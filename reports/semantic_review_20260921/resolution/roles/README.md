# Role evidence review for #710

Eight cellular metabolic roles now have inspected primary-publication support and
explicit organism/condition context. The old computational provenance and numeric
confidence remain intact. The evidence concerns the named cultures only; it does
not establish universal microbial utilization. The two hydrated-salt extensions
are explicitly marked as chemical inferences about the dissolved oxyanion rather
than claims that the publication tested that exact solid form.

The applied, hash-bound before/after changes are in `cellular-role-plan.json`.
`apply_cellular_evidence.py` uses the repository's closed-schema validated writer,
checks all inputs before writing, and refuses replay against changed records.
`summary.json` records the validation and ledger digests.

## Primary evidence used for the eight corrections

| Ingredient records | Scoped source support |
| --- | --- |
| K2S4O6 | Potassium tetrathionate supplies electrons during the studied aerobic *Acidithiobacillus caldus* cultures. [Aston et al.](https://doi.org/10.1007/s11274-010-0441-4) |
| Na2S2O3 | Sodium thiosulfate is supplied with nitrate in the *Thiobacillus denitrificans* culture method. [Kato et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC3382511/) |
| Thiosulfate; Na2S2O3 x 5 H2O | Thiosulfate-fed, illuminated anoxic *Chlorobaculum tepidum* WT2321 cultures are studied directly. The pentahydrate extension is limited to its dissolved thiosulfate supply. [Levy et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC5066360/) |
| Nitrous oxide | Acetate-fed growth and N2O reduction are measured for four named isolates under anoxic conditions. [Yoon et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC4907195/) |
| Sodium perchlorate; sodium perchlorate monohydrate | Sodium perchlorate is used in anoxic cultures of *Dechlorosoma suillum* PS and *Dechloromonas agitata* CKB. The monohydrate extension concerns dissolved perchlorate supply. [Chaudhuri et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC124121/) |
| Tetrachloroethene | Respiratory reductive dechlorination in strain 195 is supported with hydrogen as donor. [Maymo-Gatell et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC91463/) |

## Complete affected-role inventory and remaining work

`original-flagged-assertions.json` preserves all 681 affected assertions from the
identity-corrected snapshot: 670 prediction-only plus 11 empty-evidence assertions.
The eight cellular claims are included in the 670, not eight additional claims.
`role-dispositions.tsv` binds every one to the original record SHA256, assertion
SHA256, and exported edge ID. After these edits, **662 prediction-only and 11
empty-evidence role assertions remain unapproved**; all eight cellular roles have
context. No other role has been withdrawn or promoted by this batch.

The provenance inventory is exhaustive for those 681 assertions: 367 name-pattern
inferences, 157 ontology-ancestry inferences, 70 generic energy-substrate inferences,
76 in-session LLM predictions, and 11 empty evidence lists. The ledger records an
appropriate source requirement for each assertion; this classification is not a
claim that all 673 remaining roles are false or that each has received a complete
literature review.

The schema intentionally permits `COMPUTATIONAL_PREDICTION` and describes it as
computational inference or prediction. This is useful provenance, but neither the
enum nor a confidence number demonstrates the biological claim. A shared citation,
chemical ancestry, or name match cannot substitute for ingredient-specific support.

Concrete inspected counterexamples to automatic approval include:

- The *T. saccharolyticum* study uses 2-deoxyglucose in catabolite-repression
  experiments. It does not establish the asserted growth-carbon role.
  [Primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3526391/)
- The original *Neurospora* experiment distinguishes uptake of 3-O-methyl-D-glucose
  from its metabolism. Neither uptake nor a glucose-like name establishes carbon
  nutrition. This does not prove nonutilization by every organism, and the separately
  registered cyclic form is not equated to another registry identity.
  [Primary study](https://doi.org/10.1016/S0021-9258(19)77148-8)
- A human primary study describes 4-pyridoxic acid as a B6 catabolite. That supplies
  no evidence of microbial vitamin salvage or vitamin replacement.
  [Primary study](https://pubmed.ncbi.nlm.nih.gov/11756060/)
- ChEBI identifies para-aminosalicylic acid's antitubercular role. Its chemical
  amino-acid ancestry does not establish nutritional building-block use.
  [ChEBI entry](https://www.ebi.ac.uk/chebi/CHEBI:27565)

The inference scripts themselves call their output provisional. Their descriptions
of carbohydrate-to-carbon-source and amino-acid-to-nutrient rules as unambiguous
are not scientific evidence and are contradicted by the examples above. The ledger
keeps those claims open rather than treating script comments as authority.

**Full-graph semantic approval remains FAIL.** This batch is evidence-backed
progress on eight roles and does not clear identity, component, or historical
record-review findings elsewhere in the graph.
