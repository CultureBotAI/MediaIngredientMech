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

### 0. Verdict On The Existing Record

The fields under **Target Ingredient** above are the *current, possibly wrong*
contents of the record. Treat them as claims to be tested, not as context to agree
with. For each field that is populated, state explicitly whether the evidence
**CONFIRMS**, **REFUTES**, or is **INSUFFICIENT** to judge it, and give the corrected
value when you refute one:

- The **ontology mapping** — does the cited CURIE denote this exact substance, and is
  the recorded `mapping_quality` right? Flag a term that is a broader parent, a
  different hydrate/salt/stereoisomer, an obsolete or merged term, or a label that
  does not match the CURIE.
- The **chemical properties** — formula, hydrate state, molecular weight, CAS-RN.
- The **synonyms** — flag any that denote a *different* substance rather than this one.
- The **ingredient type** and **mapping status**.

Begin the report with a one-line `Overall verdict:` of `CONFIRMED`, `NEEDS_CORRECTION`,
or `INSUFFICIENT_EVIDENCE`, followed by a `| field | verdict | recorded | corrected |`
table covering the populated fields. Saying "confirmed" for a field you did not find a
source for is worse than saying `INSUFFICIENT` — do not pad the table.

### 1. Identity And Scope
- Determine whether the term is a single chemical, hydrate/salt form, mixture, commercial
  formulation, buffer, extract, medium component family, or ambiguous label.
- Identify boundary cases where the label should not be treated as equivalent to a generic parent.
- Call out spelling variants, supplier terms, abbreviations, or legacy culture-medium names.

### 2. Chemical Or Formulation Evidence
- For single chemicals, report formula, hydrate state, charge/salt form, CAS Registry Number,
  and common synonyms when source-backed.
- **CAS-RN discipline.** A CAS number lifted from a page that happens to mention this
  compound is wrong roughly half the time — usually because it belongs to a neighbouring
  hydrate, the anhydrous parent, or a different salt. Quote the sentence the number came
  from, state which exact form that sentence assigns it to, and verify the check digit.
  Report no CAS-RN rather than an unverified one.
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
- The `Overall verdict:` line and the per-field verdict table from section 0, first.
- Scope summary.
- Candidate ontology mappings with match type and confidence.
- Source-backed chemical/formulation facts.
- Recommended record updates.
- DOI-first bibliography, using PMID only when DOI is unavailable.
- Warnings for claims that should not yet be curated into MediaIngredientMech.
