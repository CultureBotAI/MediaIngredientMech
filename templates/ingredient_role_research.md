# Media Ingredient Role Research Template

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
- **Notes:** {notes}

## Existing role assignments on this record
{existing_role_assignments}

## CHEBI has_role axioms already asserted
{chebi_role_axioms}

## Research Objective

Research the **functional roles** the ingredient **{ingredient_label}** plays across three
orthogonal facets, and update
`data/ingredients/{ingredient_status}/{ingredient_slug}.yaml` with evidence-bearing
role assignments. Facets are independent — a single ingredient often fills multiple
(e.g. L-cysteine → `AMINO_ACID_SOURCE` + `SULFUR_SOURCE` nutritionally, `REDUCING_AGENT`
physicochemically, `SUBSTRATE` cellular-metabolically).

Prefer confirming or refining the existing assignments above rather than replacing them.
Where CHEBI's own `has_role` axioms already assert a role, cite them alongside the
literature — an agreement between CHEBI and a primary source is stronger than either alone.

## Required Findings

### 1. Nutritional facet (`NutritionalRoleEnum`)

What element or macronutrient does this ingredient supply to a culture medium?

Candidate values (pick zero or more; use ONLY these tokens): **{candidate_nutritional_roles}**

For each proposed value, cite the strongest primary source (DOI or PMID) that shows the
ingredient supplies that element in a defined medium. Concentration ranges, media
categories (marine, soil, human-gut, …), and organism scope belong in `metabolic_context`.

### 2. Physicochemical facet (`PhysicochemicalRoleEnum`)

What chemical or physical job does the ingredient perform in the medium, INDEPENDENT of
what element it supplies? (Buffering, chelation, indicator, surfactant, gelling, etc.)

Candidate values: **{candidate_physicochemical_roles}**

Recipe-conditional roles (e.g. `BUFFER` only when paired with a conjugate) should still
be reported with a `metabolic_context` note explaining the condition; the mechanistic
lane already handles unconditional CHEBI has_role → role hits.

### 3. Cellular-metabolic facet (`CellularMetabolicRoleEnum`)

What does the ingredient do INSIDE or ON the cultured microbe? These are OFTEN
**organism-conditional** — methanol is `ELECTRON_DONOR` only for methylotrophs; sulfide
is only for sulfide-oxidising chemolithotrophs.

Candidate values: **{candidate_cellular_metabolic_roles}**

Always populate `metabolic_context` when a value applies only to a subset of organisms
or growth modes.

### 4. Cross-facet conflicts / synonymy

Flag any observed cross-facet double-mapping (e.g. `OSMOTIC_AGENT` + `OSMOPROTECTANT`
both point at CHEBI:25728 — they are legitimately distinct facets that share an
ontology anchor). Do not silently propose the same role in two facets unless the
literature genuinely supports both interpretations for this specific ingredient.

## Output Format

Return a curation-focused report followed by a **machine-readable fenced YAML block**
with the exact shape below. The block will be parsed by
`scripts/extract_roles_from_edison.py` on the CultureMech side and applied via the
MIM `apply_role_research_results.py` script.

Example (edit fields to reflect your findings — this shape is required):

```yaml
role_research:
  ingredient: {ingredient_slug}
  ingredient_identifier: {ingredient_identifier}
  nutritional_roles:
    - role: SULFUR_SOURCE
      confidence: 0.9
      metabolic_context: "canonical sulfur source in defined media"
      evidence:
        - reference_type: PEER_REVIEWED_PUBLICATION
          doi: 10.1128/jb.00456-20
          reference_text: "Smith et al. 2020, J. Bacteriol."
          excerpt: "L-cysteine supplied at 0.5 g/L served as the sole sulfur source..."
    - role: AMINO_ACID_SOURCE
      confidence: 0.95
      evidence: []
  physicochemical_roles:
    - role: REDUCING_AGENT
      confidence: 0.85
      metabolic_context: "at ~0.5 g/L in anaerobic media"
      evidence:
        - reference_type: PEER_REVIEWED_PUBLICATION
          pmid: "12345678"
          excerpt: "..."
  cellular_metabolic_roles:
    - role: SUBSTRATE
      confidence: 0.9
      metabolic_context: "assimilatory sulfate reduction pathway; NOT for organisms lacking cys biosynthesis"
      evidence: []
  warnings:
    - "Do not confuse with cystine (oxidised dimer) — different CHEBI id, different roles."
```

Rules for the fenced block:

- Every `role:` value MUST be from the candidate menus above (case-sensitive tokens).
  Do NOT invent tokens; if none fit, omit the entry rather than guess.
- `confidence` is a 0.0-1.0 float. Use 0.9-1.0 only when a primary source explicitly
  asserts the role for this specific ingredient in a culture-media context.
- `evidence[]` list order matches citation strength — put the strongest source first.
- `metabolic_context` is required for organism-conditional or concentration-conditional
  values; optional for unconditional supply roles.
- Leave a facet's list EMPTY (`[]`) if the literature doesn't support any value there —
  never fabricate to fill a gap.
- The curation-focused prose report above is for human review; the fenced YAML block
  is what actually applies to the record. Both are required.

Also include:

- Scope summary (2-3 sentences).
- Source-backed evidence table (one row per citation).
- DOI-first bibliography (PMID only when DOI unavailable).
- Warnings for claims not yet ripe for curation.
