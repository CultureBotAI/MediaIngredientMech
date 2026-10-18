# Semantic review decisions — 2026-09-21

This review consolidates the existing scientific adjudications, verifies their
applicability to the current records, reviews every changed SSSOM field, and adds
the evidence and scope findings below. Coverage completion is distinct from a
passing semantic release verdict. **The current full graph fails semantic review.**

## Applicability of previous reviews

All 2,679 files in the mapped directory are byte-identical to the snapshot that
accompanied the mapped-record ledger at commit
`44093d6e5275b7965e55f8bc01457c3a7a736692`. All 272 remaining files in the unmapped
directory are byte-identical to the September 1 unmapped-review snapshot at
`60c4c8eea4eec613a4b5396dd12ce94d6032455e`. Git paths are Unicode-normalized before
comparison; the contents are compared as bytes, without normalization.

Their existing adjudications can therefore be carried forward as existing
reviews, with the original report links and content hashes. This is not a claim
that a new reviewer independently researched all 2,951 records. The existing
mapped ledger includes 14 identity blockers, and its findings are still live.
The unmapped review explicitly rejects false equivalences involving salts,
hydrates, metal complexes, cobamides, families, and incompletely specified recipes.
Reviewed retention as UNMAPPED does not mean the substance has been identified.

## SSSOM changes

All 3,024 subject/object pairs are unchanged from the mapped-review snapshot.
The changed fields are 294 comments and 166 predicate/date/validation-method
updates. All 166 predicate changes convert the former narrowMatch convention to
SKOS broadMatch, correctly pointing from the specific ingredient to its broader
target. No exact target identity or synonym was changed by that correction.

Each current row receives a content hash and source-review link. Record findings
conservatively block certification of the associated rows; this does not mean
every mapping on a problematic record is false. In particular, an exact registry
row does not certify the biological correctness of a separate ontology grounding.

## Historical exporter correction, superseded by #734

The #245 ruling supersedes the conversion recorded in this dated review.
Current export and review validation use `biolink:broad_match` with
`relation=skos:broadMatch`; narrow mappings reverse endpoints and preserve their
original row in `assertion_json`. A broadMatch is not evidence of ontological
subsumption. Rebuilt current bundles follow that rule; the historical release
is immutable and uses the validator preserved at its release tag.

The first standalone KGX exporter retained `biolink:broad_match` for the 166
parent mappings. MIM's own `MAPPING_SEMANTICS.md` Section 1 then required
these curated kind-of relationships to become `biolink:subclass_of` downstream.
The historical exporter followed that dataset-specific contract, retaining the original
SSSOM row and SKOS relation. An inverse-mapping regression test verifies that a
future narrowMatch points from its child object to its broader subject in KGX.
This corrects the projection; it does not approve an unsupported source mapping.

## Roles

The 989 role assertions contain **671 prediction-only assertions** and **11 with
empty evidence lists**. All eight cellular metabolic roles are provisional
in-session predictions without metabolic context. A lower confidence value and
the COMPUTATIONAL_PREDICTION label preserve uncertainty but do not independently
verify a biological role. These assertions require inspected supporting sources
before semantic approval. No organism utilization is inferred from chemical
ancestry, a name pattern, or membership in an ingredient class.

The previous ledger marked 26 prediction-only assertions' source records `pass`.
This review does not carry those passes into approval of the unsupported roles.
Other externally cited assertions retain the earlier record review and any
unresolved findings; a URL's presence alone is not counted as a fresh validation.

## Components

All 505 part assertions are covered. Source scope and completeness remain distinct
from the truth of the asserted membership. The 46 abbreviation-expansion parts
and five curated-interpretation parts require original source-preparation checks
before certification. UNKNOWN or PARTIAL completeness does not establish that a
guessed constituent is present.

Two concrete counterexamples warrant reopening the prior disposition:

* `GYPS` asserts starch, while its cited decomposition explicitly permits “Salts
  (or Starch)”. No source-specific evidence chooses starch.
* `PYGS` likewise states that S can denote salts or soluble starch. An acronym
  alone does not choose between them.

The 362 recipe-transcription and 92 label-enumeration edges retain their original
record reviews and evidence. They have not been independently re-transcribed from
every remote recipe in this pass. Ingredient names, identifiers, quantities,
units, evidence, and declared completeness remain bound to the source record.

## Recipe references

The stored BHI EXACT_FORMULATION evidence names constituent materials but does
not identify and compare the original MicrobeDecoder BHI formulation and amounts
with CultureMech:015492. The generic name and common ingredients cannot certify
exact formulation identity. This is an evidence insufficiency finding, not a
claim that the two preparations necessarily differ.

The GYPS link remains SIMILAR_COMPOSITION. It must not be promoted to exact
formulation identity; its unresolved abbreviation is separately recorded above.

## Unmapped candidates

Eight unmapped records have retained parent proposals in their annotations.
These proposals are not published SSSOM/KGX edges. Four preserve reasonable
non-identity category/source annotations: calf brains → brain, shrimp-shell
chitin → chitin, monobasic sodium phosphate → sodium phosphate, and vitamin B →
vitamin. Retaining these annotations does not support an exact identity.

Four require curation before any promotion:

* Inorganic salts-starch agar → inorganic salt confuses a mixture with a component.
* Iron as FeCl3 in EDTA → iron confuses a preparation with its element.
* Khayasin C → KHAYASIN is a name-derived proposal without demonstrated subsumption.
* Xyloglucan hepta/octa/nona-saccharides → xyloglucan confuses polymer fragments
  with a kind of the source polymer.

## Independently corroborated identity blockers

Fresh primary-authority checks corroborate representative failures in the unchanged
ledger. These have not been silently changed in the corpus:

* Sodium phosphate dibasic is the disodium salt, while its MIM record points to
  trisodium phosphate and also carries a monosodium synonym. ChEBI identifies
  [disodium hydrogenphosphate as CHEBI:34683](https://www.ebi.ac.uk/chebi/CHEBI:34683).
* The `Nano` record preserves NaNO3 source labels, but targets the NCIT nano unit
  prefix. ChEBI identifies [sodium nitrate as CHEBI:63005](https://www.ebi.ac.uk/chebi/CHEBI:63005).
* Atrazin's stored CAS differs from the CAS of
  [atrazine, CHEBI:15930](https://www.ebi.ac.uk/chebi/CHEBI:15930).
* The benzylhydrazine hydrochloride record contains benzylamine hydrochloride
  chemistry; supplier documentation identifies the mono-hydrochloride as
  [CAS 1073-62-7](https://www.sigmaaldrich.com/DE/en/search/Benzylhydrazine?focus=products&page=1&perpage=30&sort=relevance&term=Benzylhydrazine&type=product).
  Mono- and dihydrochloride forms must not be substituted for one another.

The complete correction backlog includes these and all unresolved prior findings,
with source-record and assertion references. Resolving that backlog is a separate
curation operation; a successful schema validator must not close these findings.
