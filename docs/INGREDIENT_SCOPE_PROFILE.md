# Ingredient scope profile v1

Profile identifier: `https://w3id.org/mediaingredientmech/sssom/ingredient-scope/v1`.
The machine-readable contract is packaged at
`src/mediaingredientmech/profiles/ingredient_scope_v1.yaml`; validation and
metadata construction live in `mediaingredientmech.mapping_scope`.
The same module provides `read_profile_table` and `write_profile_table`,
which preserve extensions and reject input that has lost the required profile.

This contract separates the entity described by a source, its canonical
identifier, and registry/product claims. MICRO/NCIT/ChEBI preference is applied
after scope review. A CAS RN denotes a registered substance or material and a
catalog identifier denotes a commercial product specification; neither
namespace chooses entity scope or establishes equivalence.

## Scope and composition

`mimscope:` expands to `https://w3id.org/mediaingredientmech/scope/`.
Subject and object scope each use one of `chemical_family`,
`defined_substance`, `material`, `preparation`, `catalog_product` or
`unknown`. Composition is a separate axis: `single_component`, `mixture`
or `unknown`. Thus a product can be a mixture without becoming a generic
mixture ingredient. Existing `ingredient_type` and OWL logical types retain
their own meanings; this does not migrate the corpus under issue #478.

## Mapping authorization

SSSOM `extension_definitions` declare all eight profile columns, their
property IRIs and datatypes. `ext_scope_profile` may appear as a mapping-set
default or on individual rows in a mixed set. Conflicting declarations and
unknown profile versions are errors. Each profiled row supplies both scopes,
both composition values, `ext_scope_review_status`, `ext_scope_evidence`
and `ext_identity_authorized` (`true` or `false`).

SSSOM/TSV declarations use CURIEs, such as
`mimprofile:subjectScope` for a property and
`mimprofile:ingredient-scope/v1` for the profile. The validator expands
compact and full-IRI declarations before comparison; identical identifiers
must not conflict solely because their surface syntax differs.

Canonicalization requires all of:

- A SUPPORTED, complete-row and owner-bound review with resolvable evidence.
- `skos:exactMatch` and explicit `ext_identity_authorized=true`.
- Equal, established subject/object scope and compatible reviewed composition
  (v1 requires equal composition values).

Matching vocabulary values are necessary but do not themselves prove chemical
identity. Unknown composition can match unknown composition when independent
review establishes the same material. Unknown entity scope cannot authorize
canonicalization. WITHHOLD/UNREVIEWED rows and all broader, narrower, close and
related mappings must set authorization to false. A review outcome in TSV is
not proof by itself: the bundle consumer also verifies its review inputs,
owner, evidence and content digests.

SKOS exactMatch is not OWL sameAs. Broader mappings are exported as broader
mappings; independently supported native ontology classification is separate.
A comment, confidence value, shared CAS or supplier name cannot override this
policy.

## Source context and examples

Resolve an occurrence to a stable scoped concept before using its mapping:

| Source concept | Target | Scope | Registry/product handling |
| --- | --- | --- | --- |
| MIM:Rifamycin | CHEBI:26580 | chemical_family | No single CAS; no all-members activity inference. |
| MIM:Rifamycin_Sv | CHEBI:29673 | defined_substance | Verified cas:6998-60-3 belongs to SV. |
| MIM:Bovine_Serum_Albumin | NCIT:C85253 | material | Verified cas:9048-46-8; each source retains its supplied preparation. |
| MIM:Xanthine | CHEBI:17712 | defined_substance | Reviewed ingredient representation with cas:69-89-6. |
| Generic xanthine trait concept | CHEBI:15318 | chemical_family | Keep the source's generic scope and native ontology relationship. |

The example generic trait concept is not a second exact mapping from
`MIM:Xanthine`. Its source identifier must denote its own reviewed meaning.
The ingredient mapping does not prove a tautomer-pure physical reagent.
Sigma A7030 is source-specific. CultureMech:015191's A9647 **or** A7409 is an
occurrence alternative, not a conditional exact mapping or two confirmed uses.

Registry claims join by owning entity and annotation ID; each registry/source/
status tuple retains its own evidence. Their producer/export contract is
#769. Supplied forms and occurrence alternatives are #770. They do not become
generic ingredient identity xrefs.

## Legacy compatibility and review

An unprofiled row has legacy semantics only when no nonempty scope fields
claim otherwise. A mixed release must declare which legacy sources/cohorts it
retains in its manifest; it cannot silently infer scope for them. A profiled
record with unknown scope remains noncanonicalizable, with its local/source
identity and explicit disposition preserved.

Scope changes require fresh complete-row/owner-bound decisions through the
existing receipt and reviewed-release infrastructure. Existing published
releases stay immutable. Activating the new producer/consumer contract is
gated by the cross-repository acceptance suite in KG-Microbe #1136.

## Tool compatibility

The installed `sssom-py 0.4.21` parser reconstructs mappings through a
standard-slot-only datamodel and drops these extension values, including the
profile declaration. Its strict mode also rejects valid metadata because of
an inverted validity check. Do not use that conversion path for profiled
artifacts. The lossless profile TSV reader/writer and explicit CURIE/extension
checks implement this contract; the release manifest must require the scope
capability so stripped files cannot revert to legacy identity behavior.
These findings and regression coverage are tracked in MIM #771.

References: [SSSOM extensions](https://github.com/mapping-commons/sssom/blob/master/examples/schema/extension-slots.sssom.tsv),
[SKOS semantics](https://www.w3.org/TR/skos-reference/#mapping),
[CAS REGISTRY](https://www.cas.org/cas-data/cas-registry).
