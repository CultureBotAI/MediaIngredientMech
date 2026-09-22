# Bounded adversarial review of #710

This review challenged scientific source scope and the release machinery. It is
not a literature review of the 662 remaining prediction-only and 11 empty-evidence
roles, and it does not approve the full graph. The user authorized a supported
assertion subset with the remaining claims preserved in a separate backlog.

## Findings and repairs

| Issue | Severity | Concrete defect | Required disposition |
| --- | --- | --- | --- |
| [#711](https://github.com/CultureBotAI/MediaIngredientMech/issues/711) | High | Unchanged assertion JSON could conceal altered graph subject, predicate, or object. | Independently reconstruct graph endpoints, direction, context, and metadata; reject tampering even after ordinary edge hashes are recomputed. |
| [#713](https://github.com/CultureBotAI/MediaIngredientMech/issues/713) | High | A newly added role with a citation-type marker could evade old finding coverage and evidence-gap heuristics. | Require an explicit current disposition for every assertion, bound to source bytes and assertion payload. |
| [#714](https://github.com/CultureBotAI/MediaIngredientMech/issues/714) | High | Implicit ignored ledgers could influence exports; unbound old positive statuses could appear current. | Require an explicit hashed ledger and an exact record hash for positive status. Reviewed repair satisfies this boundary. |
| [#715](https://github.com/CultureBotAI/MediaIngredientMech/issues/715) | High | A T. denticola TYGVS recipe was used to strengthen constituent identity for the T. medium source preparation. | Revert Trypticase-to-tryptone promotion and transcription status; keep all four claims open. Implemented and checked by the component reviewer. |
| [#716](https://github.com/CultureBotAI/MediaIngredientMech/issues/716) | High | Identical role payloads could inherit approval across records; explicit role evidence was not bound to complete ingredient identity or source position. | Bind inherited reviews to original record, bytes, claim and position; bind eight role plans to complete reviewed records and exact positions. Archive exact prior review texts, refusing missing or changed receipts. |
| [#717](https://github.com/CultureBotAI/MediaIngredientMech/issues/717) | High | A reviewed subject label could approve arbitrary new mapping targets or relation strengths. | Permit only the exact target, label and predicate established by the identity plan. |

The independent gate tests in `tests/test_semantic_release_adversarial.py` passed
20 cases, including recomputed edge hashes after malicious triple changes. The
builder regression tests in `tests/test_semantic_review_builder.py` passed 24
cases, including cross-record approval, changed ingredient identity, duplicate
role position, exact/close relation promotion, and altered or missing historical
review receipts. Whole-corpus explicit-plan validation passed. The portable
archive captured 1,455 exact prior review reports supporting 2,108 eligible
historical assertion rows; eligibility still does not override explicit current
evidence gaps.

## Scientific scope checks

The eight cellular-role repairs were self-reviewed against the inspected primary
evidence and all are bounded to named organisms and conditions. Two hydrate
extensions are explicitly dissolved-oxyanion inferences, not claims that the
paper tested the exact hydrated solid. Their normalized receipts were independently
checked against commit `463297b4`: each original file hash matches the captured
input, and only the planned cellular assertion and one documented curation event
differ. Other role assertions remain unapproved.

The independent component challenge found a real source conflict:
[a primary T. medium study](https://pmc.ncbi.nlm.nih.gov/articles/PMC145376/)
describes Trypticase-containing TYGVS, while
[Ito et al. 2010](https://academic.oup.com/femspd/article/60/3/251/530699)
uses tryptone in a T. denticola protocol. An acronym and related organisms do not
establish identical preparations. The corrected component report keeps this
uncertainty explicit. GYPS is instead bound to its original C. sporogenes source
and retains PARTIAL completeness. The original
[Love et al. 1979 description](https://doi.org/10.1099/00207713-29-3-241)
distinguishes cooked meat-carbohydrate and peptone-yeast cultures with horse serum,
supporting withdrawal of the invented single CMC/PY mixture. BHI's unverified
recipe candidate remains excluded from supported-assertion approval.

The three identity repairs are scoped to recovered source identity. Two recover
complete source locants and explicit BacDive ChEBI targets. Artepaulin restores
the original CAS fallback, with corroborating name/CAS and complete InChI
agreement; it does not add a ChEBI equivalence or new structure. The inconsistent
KNApSAcK InChIKey is explicitly not imported. These decisions do not transfer
approval to unrelated nutritional or component claims.

The supported exporter and its final generated artifact require their own
independent validation. A PASS for a selected subset cannot be reported as a
PASS for the full corpus or as fresh experimental verification of all historical
claims.
