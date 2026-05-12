# Media Ingredient Mapping Research Template

## Target Ingredient
- **Ingredient label:** {ingredient_label}
- **Ingredient identifier:** {ingredient_identifier}
- **Ingredient status:** {ingredient_status}
- **Ingredient slug:** {ingredient_slug}
- **Ingredient type:** {ingredient_type}
- **Mapping status:** {mapping_status}
- **Ontology mapping:** {ontology_mapping}
- **Chemical properties:** {chemical_properties}
- **Synonyms:** {synonyms}
- **Occurrence summary:** {occurrence_summary}
- **Existing evidence:** {evidence_summary}
- **Curation history:** {curation_summary}
- **Notes:** {notes}

## Research Objective

Research the media ingredient **{ingredient_label}** as a candidate MediaIngredientMech
curation target. Focus on source-backed identity, composition, formulation, and ontology
grounding that can be used to update `data/ingredients/{ingredient_status}/{ingredient_slug}.yaml`.

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
