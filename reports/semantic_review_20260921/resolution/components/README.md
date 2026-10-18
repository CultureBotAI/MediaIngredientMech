# Source-context review of components and recipe links (#710)

The 51 flagged component assertions were traced to their original MicrobeDecoder
source contexts. Three GYPS parts are verified, one GYPS part is corrected, four
false CMC mixture parts are withdrawn, and **43 component assertions remain open**.
The separate GYPS abbreviation finding is resolved; PYGS remains open. BHI's
unsupported exact recipe link is withdrawn. This bounded review does not approve
the full ingredient graph.

The ignored raw `microbedecoder_database.zip` contains the species and Bergey
citation lost by the label-only worksheet. The exact-match extraction in
[source-contexts.json](source-contexts.json) preserves all 133 source rows for
16 labels with archive/member/row hashes. Searches included ignored files and
16 prior ignored literature reports. Their existence was not treated as source
verification. The Fastidious Anaerobe Broth report contains no answer.

## Changes supported by original context

- **GYPS** belongs to *Caminicella sporogenes*. [Alain et al. 2002,
  p.1622](https://doi.org/10.1099/00207713-52-5-1621) explicitly identifies sulfur
  with glucose, peptone and yeast extract. Starch was wrong. The current four
  parts are a **partial** transcription; documented buffer, salts, indicator and
  reducing agent are not asserted absent. The author-institution PDF was read;
  its SHA256 is recorded in the manifest. [ChEBI confirms
  CHEBI:33403](https://www.ebi.ac.uk/chebi/CHEBI:33403) is elemental sulfur.
- **CMC + PY + Horse Serum** belongs to *Filifactor villosus*. [Love et al.
  1979](https://doi.org/10.1099/00207713-29-3-241) describes separate cooked
  meat-carbohydrate and peptone-yeast cultures with horse serum. CMC was wrongly
  expanded to carboxymethylcellulose and separate contexts flattened into one
  mixture. The raw expression is preserved as `UNMAPPED_0740`, `AMBIGUOUS`; its
  four components and unsupported registry mapping are withdrawn.
- **BHI** belongs to *Hespellia porcina*. Its original recipe was not compared
  with the CultureBotHT/FEBA preparation in `CultureMech:015492`. The old
  `EXACT_FORMULATION` link is now `CANDIDATE_UNVERIFIED`, not an approved
  composition relationship.

## Adversarial correction

A tentative TYGVS change used a tryptone-containing *T. denticola* protocol to
replace the Trypticase component in the *T. medium* source preparation. The
independent reviewer found a [primary *T. medium* study](https://pmc.ncbi.nlm.nih.gov/articles/PMC145376/)
using the Trypticase name, while [Ito et al. 2010](https://academic.oup.com/femspd/article/60/3/251/530699)
uses tryptone in *T. denticola*. Shared oral context and acronym do not prove
identical recipe identity. The tentative constituent change and evidence
promotion were reverted. TYGVS now records the recovered species context and
explicit uncertainty; all four original component claims remain **open**, with
their original method and completeness. Validation checks that these fields and
components have not been strengthened.

## Audit files

- `dispositions.tsv`: one disposition per original edge/finding (54 rows).
- `before-records.json`: complete unchanged input snapshots of all 16 records.
- `applied-changes.json`: complete before/after states and exact path/hash changes.
- `related-record-findings.tsv`: older component-related record findings retained
  for the broader review. They are not silently closed by this subtask.
- `manifest.json`: counts and content hashes, explicit **FAIL** release verdict.
- `validation.json`: schema validation of edited records, whole live component
  invariant check, and the targeted adversarial no-strengthening check.

Rebuild the bounded ledger with `python reports/semantic_review_20260921/resolution/components/build_ledger.py`.

Validate the current bounded review with `.venv/bin/python reports/semantic_review_20260921/resolution/components/validate_components.py`.
