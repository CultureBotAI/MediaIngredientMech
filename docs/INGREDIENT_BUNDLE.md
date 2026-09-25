# Reviewed ingredient bundles, version 1

This opt-in export carries a reviewed scoped cohort, registry claims and source
occurrences together. It does not replace the complete legacy SSSOM release or
promote its withheld rows. The initial cohort contains the 20 reviewed
KG-Microbe cases under issues #769 and #770.

```bash
python -m mediaingredientmech.export.ingredient_bundle export \
  --review reports/ingredient_bundle_20260924/review.json \
  --output output/ingredient-bundle-v1
python -m mediaingredientmech.export.ingredient_bundle validate \
  output/ingredient-bundle-v1 --manifest-sha256 <exported-manifest-sha256>
```

The output directory must be new. Export validates the current complete mapping
review, snapshots every input, stages and validates the resulting bundle, checks
for concurrent source changes, and publishes by renaming the staged directory.
Identical input bytes and exporter code produce identical output bytes. A release
consumer must obtain the manifest digest from its reviewed activation policy;
hashes inside a downloaded manifest are integrity checks, not independent trust.

## Files and capabilities

`manifest.json` binds every member by SHA-256 and byte count, declares its cohort,
records exporter/review provenance, and names required capabilities. Unsupported
versions, missing required capabilities, changed contract files, undeclared files,
escaping paths, and missing/mismatched members fail validation before consumption.
The schema and scope profile are bundled and must match the consumer's packaged
versions; nothing downloads a newer schema automatically.

| Artifact | Representation and meaning |
| --- | --- |
| `ingredient_mappings.sssom.tsv` | Complete original supported rows plus the eight declared scope extensions. Source-specific name resolution must precede application of these mappings. |
| `ingredient_identifier_annotations.tsv` | One complete owner/identifier/source/status/version claim per row. Evidence is a structured JSON cell; associated values are never parallel pipe lists. |
| `ingredient_products.json` | Supplier/catalog specifications, original supplied-form payload, evidence and review status. No lot identity is inferred. |
| `ingredient_occurrences.json` | Individual recipe/observation occurrences, quantities, preparation notes, original payloads and explicit product alternatives. |
| `review.json`, `sources/` | Complete companion decisions, existing mapping review, selected owning records, original SSSOM and evidence bytes needed to reconstruct every output artifact. |

Mappings and the annotation table are required. Products and occurrences have
explicit file names or JSON `null` in `manifest.artifacts`; a present file cannot
silently become optional. Presence requires `catalog-products-v1` or
`ingredient-occurrences-v1`. Every consumer also needs `ingredient-scope-v1`,
`owner-bound-review-v1` and `identifier-annotations-v1`. Legacy input is a separate,
explicit mode; a failed profiled bundle must not fall back to legacy consumption.

## Reviews and registry history

Companion decisions use the same complete-payload and owning-record evidence
verifier as the reviewed SSSOM export. The reviewed payload includes the claim
kind, stable ID, owner and all attributes. Review evidence additionally names the
owner path and its exact hash. Changing a claim, source record, status, qualifier,
alternative or scientific reason requires renewed matching evidence. Rehashing
an output file or its manifest cannot approve that change. Existing mapping
reviews must support the unchanged original row before scope extensions are added.

`identifier_validity`, `source_status`, `source_currentness`, `review_status` and
`xref_eligible` answer different questions. A supported FDA `SUPERSEDED` claim is
historical evidence and cannot be an active xref. A different source's `REPORTED`
claim remains separate; this does not turn an FDA status into a global CAS ruling.
Invalid raw CAS strings have an empty normalized identifier, `INVALID` validity
and false eligibility. The exporter validates active CAS syntax and check digits
and never guesses a replacement.

Claims are owned by stable MIM ingredient or product IDs. A consumer may project
an ingredient claim to a canonical target only through that owner's explicitly
authorized, matching-scope mapping. A broader target cannot inherit a specific
owner's CAS. Product CAS references describe supplied material; they do not make
two catalog products identical. Registry annotations never authorize identity
collapse, supply exact synonyms, or imply a subclass relation.

Annotation IDs hash the owner, normalized/raw identifier, source, source status,
source version and retrieval date. Evidence or eligibility corrections preserve
that natural-key ID but invalidate its complete-payload approval. Multiple sources
or versions remain independent claims.

## Occurrences, products and alternatives

An occurrence ID hashes its source ID and an explicitly reviewed stable source
occurrence key. The key is not a label-to-global-ID inference; repeated source
components need distinct keys. A product ID hashes the normalized supplier name
and exact catalog number. It denotes a specification, not an individual vial,
batch, stock solution or immutable composition. A materially changed catalog
specification requires a new versioned catalog key and review.

Occurrence qualifiers suffice when only that source's amount, treatment or notes
need preservation. A product node is warranted when a supplier/catalog identity
has independent properties or must be queried as an alternative. Do not move
supplier, catalog or preparation fields into generic ingredient synonyms or xrefs.
Missing information is JSON `null`, not an inferred grade, quantity or CAS.

CultureMech:015191 contains a `one_of` group with A9647 and A7409 and
`selection_status: UNSPECIFIED`. It cannot also assert a selected product. Each
option retains its reported details; the original recipe's 350 g/L component
value is not a measured or inferred A7409 solution concentration. The group ID
hashes the occurrence ID and its explicit group key. A7030 is linked only to its
original CultureBotHT occurrence. All seven BSA recipe memberships and their own
quantities/preparations remain independent.

Sorbitan occurrences retain the complete archived payload, including historical
grounding diagnostics, while their reviewed ingredient mapping selects the local
material. Raw source payload values are evidence, never input to identity indexes.
No Tween 80 or replacement CAS is inferred. Generic rifamycin has family scope
and no CAS; explicit SV retains its own CAS. The reviewed MIM xanthine ingredient
retains CHEBI:17712 without changing generic trait CHEBI:15318 or the ontology's
native relation between them.

The JSON Schema and portable validator are packaged for reuse by KG-Microbe.
KGX projection and activation acceptance are tracked by KG-Microbe #1134–#1136.
