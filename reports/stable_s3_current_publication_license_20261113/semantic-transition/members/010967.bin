Question: # Media Ingredient Mapping Research Template

## Target Ingredient
- **Ingredient label:** Modified Cooked Meat Medium
- **Ingredient identifier:** UNMAPPED_0763
- **Ingredient status:** unmapped
- **Ingredient slug:** Modified_Cooked_Meat_Medium
- **Ingredient type:** None recorded
- **Mapping status:** NEEDS_EXPERT
- **Ontology mapping:** None recorded
- **Chemical properties:** None recorded
- **Synonyms:** Modified Cooked Meat Medium (type=RAW_TEXT, source=microbedecoder)
- **Occurrence summary:** total_occurrences=0; media_count=0; source_occurrences=[{'source': 'microbedecoder', 'count': 1, 'source_columns': 'bergey:substrates'}]
- **Existing evidence:** None recorded
- **Curation history:** CREATED_AS_UNMAPPED; timestamp=2026-08-04T02:54:09.684805+00:00; changes=Imported from microbedecoder (source_id=kgmicrobe.compound:modified_cooked_meat_medium); no CAS-RN or CHEBI/NCIT match. Curator review needed.; FLAGGED_NEEDS_EXPERT; timestamp=2026-08-05T00:01:30.894952+00:00; changes=Not a single-compound grounding target: multi-component blend or named medium; no single ontology term grounds it -- needs decomposition into constituents.
- **Notes:** Imported from microbedecoder (source_id=kgmicrobe.compound:modified_cooked_meat_medium); no CAS-RN or CHEBI/NCIT match. Curator review needed.

## Research Objective

Research the media ingredient **Modified Cooked Meat Medium** as a candidate MediaIngredientMech
curation target. Focus on source-backed identity, composition, formulation, and ontology
grounding that can be used to update `data/ingredients/unmapped/Modified_Cooked_Meat_Medium.yaml`.

## Required Findings

### 1. Identity And Scope
- Determine whether the term is a single chemical, hydrate/salt form, mixture, commercial
  formulation, buffer, extract, medium component family, or ambiguous label.
- Identify boundary cases where the label should not be treated as equivalent to a generic parent.
- Call out spelling variants, supplier terms, abbreviations, or legacy culture-medium names.

### 2. Chemical Or Formulation Evidence
- For single chemicals, report formula, hydrate state, charge/salt form, CAS Registry Number,
  and common synonyms when source-backed.
- For mixtures or named formulations, summarize composition and distinguish required from
  variable ingredients.
- Mark source conflicts, ambiguous stoichiometry, and formulation-specific evidence as warnings.

### 3. Ontology Grounding
- Suggest CURIEs where available from CHEBI, NCIT, MESH, FOODON, UBERON, ENVO, NCBITaxon,
  or other stable resources relevant to media ingredients.
- Explain whether any suggested ontology term is an exact identity match, close match, broader
  parent, narrower child, or unsuitable generic parent.
- Do not invent identifiers. Label-only candidate mappings are acceptable when grounding is unclear.

### 4. Curation Recommendation
- Recommend `MAPPED`, `UNMAPPED`, or a non-identity mapping status when applicable.
- State whether `skos:exactMatch`, `skos:closeMatch`, `skos:narrowMatch`, or no SSSOM row is
  appropriate, and why.
- Provide concise YAML-oriented update notes for synonyms, chemical properties, ontology mapping,
  and curation history.

## Output Format

Return a curation-focused report with:
- Scope summary.
- Candidate ontology mappings with match type and confidence.
- Source-backed chemical/formulation facts.
- Recommended record updates.
- DOI-first bibliography, using PMID only when DOI is unavailable.
- Warnings for claims that should not yet be curated into MediaIngredientMech.


# Curation report: Modified Cooked Meat Medium (UNMAPPED_0763)

## Scope summary

**Modified Cooked Meat Medium is a named, multi-component microbiological culture medium, not a single chemical, hydrate, salt, buffer, or chemically defined substance.** The strongest retrieved source is *Handbook of Media for Clinical Microbiology*, whose purpose is to compile medium compositions, preparation methods, commercial sources, and intended uses. Its contents list **“Cooked Meat Medium, Modified”** as an entry distinct from **“Cooked Meat Medium”** and from two explicitly supplemented cooked-meat media. This supports interpreting the imported phrase “Modified Cooked Meat Medium” as the natural-order form of that named formulation. (atlas2006handbookofmedia pages 1-5, atlas2006handbookofmedia media 7d265ef5)

The label is nevertheless **underspecified without its originating recipe**: “modified” denotes a formulation-level change but does not itself identify which ingredients or concentrations differ. It must not be normalized to generic Cooked Meat Medium as an exact identity. The handbook separately lists:

- Cooked Meat Medium;
- Cooked Meat Medium with Glucose, Hemin, and Vitamin K;
- Cooked Meat Medium, Modified; and
- Cooked Meat Medium with Peptone and Yeast Extract. (atlas2006handbookofmedia media 7d265ef5)

These are boundary cases, not interchangeable synonyms. “Chopped Meat Medium” is likewise a separately named family in the handbook and should not be merged solely because both names describe meat-containing anaerobic media. (atlas2006handbookofmedia media 7d265ef5)

Recommended type: **named culture-medium formulation / multi-component mixture**. If the local schema permits only a broad type, use `mixture` rather than `chemical`.

## Candidate ontology mappings

No source-verified CHEBI, NCIT, MESH, FOODON, UBERON, ENVO, NCBITaxon, or other stable CURIE was found for the exact formulation. The evidence supports the following disposition:

| Candidate/interpretation | Relationship to target | Confidence | Disposition |
|---|---|---|---|
| Modified Cooked Meat Medium (raw label) | Exact source label for the unmapped record; treat as a named culture-medium formulation/mixture rather than a single chemical (atlas2006handbookofmedia media 7d265ef5) | High | Keep as primary label; retain UNMAPPED pending source-level formulation confirmation |
| Cooked Meat Medium, Modified | Normalized inverted-name variant of the same named medium listed in the handbook table of contents (atlas2006handbookofmedia media 7d265ef5) | High | Add as synonym/label variant only; acceptable textual normalization |
| Cooked Meat Medium | Broader or ambiguous parent label; handbook lists it separately from the modified medium, so it is not identity-equivalent (atlas2006handbookofmedia media 7d265ef5) | High | Do not assert exact match; at most broader/related concept in notes |
| Cooked Meat Medium with Glucose, Hemin, and Vitamin K | Separate supplemented formulation explicitly listed apart from the modified medium (atlas2006handbookofmedia media 7d265ef5) | High | Do not merge; curate as distinct formulation if needed |
| Cooked Meat Medium with Peptone and Yeast Extract | Separate supplemented formulation explicitly listed apart from the modified medium (atlas2006handbookofmedia media 7d265ef5) | High | Do not merge; curate as distinct formulation if needed |
| Generic chemical ontology parent (e.g., CHEBI chemical entity or single-compound food/meat term) | Unsuitable: target is a whole culture medium/mixture, not a single substance; no exact ontology identity established from available evidence (atlas2006handbookofmedia media 7d265ef5) | High | No exact chemical grounding |
| Verified stable exact CURIE / SSSOM row | No verified exact ontology identifier was found in available evidence; accessible source only supports named-medium status and distinctions among variants (atlas2006handbookofmedia media 7d265ef5, atlas2006handbookofmedia pages 1-5) | High | No SSSOM row; leave ontology_mapping empty and status UNMAPPED/NEEDS_EXPERT |


*Table: This table summarizes the recommended interpretation and mapping disposition for Modified Cooked Meat Medium. It is useful for deciding which labels can be kept as synonyms, which related media must stay separate, and why no exact ontology grounding should be asserted yet.*

### Mapping assessment

- **Exact match:** none verified; do not create `skos:exactMatch`.
- **Close match:** generic Cooked Meat Medium is not safe as `skos:closeMatch`, because the reference handbook explicitly maintains it as a separate entry from the modified medium. (atlas2006handbookofmedia media 7d265ef5)
- **Narrow/broad relation:** generic Cooked Meat Medium may be a conceptual parent or formulation family, but no stable identifier or formal hierarchy was verified. Do not emit `skos:narrowMatch` merely from the labels.
- **Chemical ontology terms:** unsuitable for whole-record identity. Individual constituents could later receive CHEBI mappings after the exact recipe is recovered, but those would be component mappings rather than mappings for this named medium.
- **SSSOM:** **no row at present**. A label-only candidate note—“Cooked Meat Medium, Modified”—is appropriate internally, but not as an asserted ontology mapping.

## Source-backed formulation facts

1. The target belongs to a family of named cooked-meat culture media. The handbook lists the modified medium independently, demonstrating that modification status is identity-relevant. (atlas2006handbookofmedia media 7d265ef5)
2. Glucose, hemin, and vitamin K occur in the title of one **separate supplemented formulation**; they cannot be inferred to be constituents of “Cooked Meat Medium, Modified.” (atlas2006handbookofmedia media 7d265ef5)
3. Peptone and yeast extract similarly define another separately listed formulation and cannot be assigned to the target without the target entry’s recipe. (atlas2006handbookofmedia media 7d265ef5)
4. The retrieved handbook states that its entries provide composition, preparation, commercial sources, and applications, but the accessible extract ended before the recipes on pp. 160–162. Therefore no exact quantities, required constituents, pH, preparation procedure, supplier equivalence, or variable ingredients for the modified entry were verified in this search. (atlas2006handbookofmedia pages 1-5, atlas2006handbookofmedia media 7d265ef5)
5. Because this is a mixture, a molecular formula, formal charge, hydrate state, single CAS Registry Number, and single-compound stoichiometry are **not applicable** to the whole medium.

## Recommended record updates

**Status:** retain `UNMAPPED` and `NEEDS_EXPERT`. This is not a failed chemical lookup; it is a named-medium record requiring source-level recipe identification and eventual decomposition.

Suggested YAML-oriented update:

```yaml
ingredient_label: Modified Cooked Meat Medium
ingredient_identifier: UNMAPPED_0763
ingredient_slug: Modified_Cooked_Meat_Medium
ingredient_type: named culture medium formulation
mapping_status: NEEDS_EXPERT
ingredient_status: unmapped

synonyms:
  - value: Modified Cooked Meat Medium
    type: RAW_TEXT
    source: microbedecoder
  - value: Cooked Meat Medium, Modified
    type: NORMALIZED_LABEL
    source: Atlas and Snyder 2006

chemical_properties:
  molecular_formula: null
  formal_charge: null
  hydrate_state: null
  cas_rn: null
  note: >-
    Not applicable to the whole record: named multi-component culture
    medium. Exact recipe and component concentrations remain unverified.

ontology_mapping: null

curation_notes:
  - >-
    Treat as a named culture-medium formulation/mixture, not as a single
    chemical grounding target.
  - >-
    Do not merge with generic Cooked Meat Medium; the reference handbook
    lists Cooked Meat Medium, Cooked Meat Medium Modified, and supplemented
    variants as distinct entries.
  - >-
    Do not infer glucose, hemin, vitamin K, peptone, or yeast extract as
    constituents of this target from neighboring formulation names.
  - >-
    Retrieve the full Cooked Meat Medium Modified recipe (handbook p. 162)
    and the exact originating Bergey substrate definition before decomposing
    the record into constituent ingredients.

curation_history:
  - action: REVIEWED_AS_NAMED_MEDIUM_MIXTURE
    changes: >-
      Source review confirmed a separately named Cooked Meat Medium,
      Modified entry. No verified exact ontology CURIE or exact formulation
      was recovered. Retained UNMAPPED/NEEDS_EXPERT; no SSSOM identity row.
```

If `ingredient_type` is controlled and does not include `named culture medium formulation`, use the closest allowed value such as `mixture` and preserve the more precise classification in `curation_notes`.

## Curation recommendation

**Final recommendation: `UNMAPPED` + `NEEDS_EXPERT`; no identity mapping and no SSSOM row.** The record should remain intact as a named-medium placeholder until the exact source recipe is retrieved. After that, preserve the formulation record for provenance while representing its constituents as separate mapped ingredients where possible. Mapping the whole medium to one constituent, to generic meat, or to generic Cooked Meat Medium would conflate formulation membership with identity.

## Warnings

- Do **not** curate any molecular formula, charge, hydrate, or CAS-RN for the whole medium.
- Do **not** infer a recipe from generic Robertson’s Cooked Meat Medium, commercial cooked-meat products, or similarly named “chopped meat” media.
- Do **not** treat “modified” as semantically ignorable.
- Do **not** add glucose, hemin, vitamin K, peptone, or yeast extract to this record solely because separately titled variants contain those words. (atlas2006handbookofmedia media 7d265ef5)
- Do **not** create fabricated or label-guessed ontology CURIEs.
- Supplier formulations and historical recipes may differ; any later composition should carry source, edition, supplier/product number where applicable, quantities, final volume, pH, and preparation conditions.

## DOI-first bibliography

1. Atlas RM, Snyder JW. *Handbook of Media for Clinical Microbiology*. 2nd ed. CRC Press; 2006. **doi:10.1201/9781420005462**. The handbook describes its scope as medium composition, preparation, sources, and applications, and its contents distinguish the target from generic and supplemented cooked-meat media. (atlas2006handbookofmedia pages 1-5, atlas2006handbookofmedia media 7d265ef5)

No additional publication with an accessible, source-verifiable exact recipe for **Cooked Meat Medium, Modified** was recovered. Accordingly, composition beyond the formulation names above should not yet be curated.

References

1. (atlas2006handbookofmedia pages 1-5): Ronald M. Atlas and James W. Snyder. Handbook Of Media for Clinical Microbiology. CRC Press, May 2006. URL: https://doi.org/10.1201/9781420005462, doi:10.1201/9781420005462. This article has 136 citations.

2. (atlas2006handbookofmedia media 7d265ef5): Ronald M. Atlas and James W. Snyder. Handbook Of Media for Clinical Microbiology. CRC Press, May 2006. URL: https://doi.org/10.1201/9781420005462, doi:10.1201/9781420005462. This article has 136 citations.