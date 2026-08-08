# Ingredient Record Verification (Claude deep research lane)

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

## Why this lane exists

This ingredient is also researched by a literature-mining lane (PaperQA3), which
reads primary literature well but repeatedly cannot answer the one question that
decides the record: *does the cited ontology term actually exist, and does it
denote this exact substance?* Its reports say so in as many words — "no ChEBI
CURIE was verified in the retrieved evidence", "retain provisionally, but
directly verify the current ChEBI record".

**You can open the ontology and chemistry databases directly. That is your job
here.** Do not try to reproduce a literature review. Resolve the identifiers.

## Required Findings

### 1. Resolve the cited term (do this first)

If the record cites an ontology term, fetch it and report, each as a separate
line with the URL you read it from:

- **Exists?** Does the CURIE resolve at all?
- **Label.** The term's current primary label, verbatim. Compare with the
  recorded `ontology_label` — report any difference exactly, including case.
- **Obsolete / merged / replaced?** Report `owl:deprecated`, `IAO:0100001`
  (term replaced by), and any `hasAlternativeId` / merge notice.
- **Definition.** Quote it, then state plainly whether it denotes *this*
  substance or something broader, narrower, or simply different.
- **Structure discriminators.** For chemicals: charge/protonation state,
  stereochemistry, hydrate/solvate, salt counterion. These are where a mapping
  is usually wrong — `X(2-)` vs `X` vs `X acid` vs `sodium X` are four different
  ChEBI terms and only one is right.

Useful resources: the EBI OLS4 term page, the ChEBI entry page, the ChEBI/OLS4
REST APIs, PubChem, CAS Common Chemistry, and DSMZ MediaDive for the
growth-medium sense of a label.

### 2. Identity and scope of the raw label

State whether the label denotes a single chemical, a specific hydrate/salt, a
mixture, a commercial formulation, a buffer, an extract, or an ambiguous family
name. Say explicitly when the label is **under-specified** — an under-specified
label mapped to a specific term is a defect even when the term is real.

### 3. Chemical facts

Formula, hydrate state, charge/salt form, molecular weight, and CAS-RN, each
with the URL it came from.

**CAS-RN discipline.** A CAS number found on a page that merely mentions this
compound is wrong roughly half the time — it usually belongs to the anhydrous
parent or a neighbouring hydrate. Quote the sentence, state which exact form
that sentence assigns it to, and verify the check digit. Report no CAS-RN rather
than an unverified one.

### 4. Better candidates

If the cited term is wrong or the record is unmapped, propose the CURIEs that
*are* right — resolved, not guessed, each with its label and the URL you
verified it at. If nothing in CHEBI / FOODON / NCIT / MESH / ENVO / UBERON
denotes this substance, say so explicitly; "no ontology term exists" is a
finding, and in this repo it is recorded as a `kgmicrobe.compound:` registry
term rather than forced into a bad match.

**Never write a CURIE you have not resolved.** A plausible-looking invented
identifier is the single most damaging thing you can put in this report.

## Output Format

Begin with exactly these two things, in this order:

1. A line reading `Overall verdict: CONFIRMED` or `Overall verdict:
   NEEDS_CORRECTION` or `Overall verdict: INSUFFICIENT_EVIDENCE`.
2. A table `| field | verdict | recorded | corrected |` with one row per
   populated field above, where `verdict` is `CONFIRMS`, `REFUTES`, or
   `INSUFFICIENT`, and `corrected` gives the corrected value when you refute.

Then the sections above, then a `## Sources` list of every URL you actually
opened.

Saying `CONFIRMS` for a field you did not verify is worse than saying
`INSUFFICIENT` — it converts an open question into a false record. Do not pad
the table.
