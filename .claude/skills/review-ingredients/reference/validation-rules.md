# Validation Rule Definitions

*Reference for the **review-ingredients** skill — see [`../skill.md`](../skill.md) for the overview, workflows, and rule summary.*

---

### Rule Definitions

#### P1 - Critical Errors

**Rule P1.1: Ontology Term Existence**
```yaml
id: P1.1
description: Ontology term does not exist (404 from OAK/OLS)
check: OAK lookup returns None for ontology_id
impact: Broken link in knowledge graph
fix: Re-map to correct term or mark unmappable
```

**Rule P1.2: Invalid CURIE Format**
```yaml
id: P1.2
description: Ontology ID not valid CURIE (e.g., "CHEBI:123" vs "CHEBI123")
check: Regex ^[A-Z]+:\d+$
impact: Parser failures in downstream systems
fix: Auto-correct to valid CURIE format
```

**Rule P1.3: Dual Identifier Mismatch**
```yaml
id: P1.3
description: Sequential ID (id field) doesn't match ontology ID (identifier field)
check: For mapped ingredients, identifier should be ontology_id (not UNMAPPED_X)
impact: Confusion between persistent ID and semantic ID
fix: Update identifier field to match ontology_id
```

**Rule P1.4: Missing Required Fields**
```yaml
id: P1.4
description: Required fields missing (ontology_id, preferred_term)
check: Schema validation via LinkML
impact: Invalid YAML structure
fix: Add missing required fields
```

#### P2 - High-Priority Warnings

**Rule P2.1: Label Mismatch**
```yaml
id: P2.1
description: Ontology label differs significantly from preferred_term
check: Normalized string comparison (ontology label vs preferred_term)
threshold: Edit distance > 5 or token overlap < 0.8
impact: Potential incorrect mapping
fix: Manual review - update preferred_term or re-map
```

**Rule P2.2: Definition Mismatch**
```yaml
id: P2.2
description: Ontology definition semantically different from expected
check: LLM-assisted semantic comparison
impact: Conceptual misalignment
fix: Manual review with domain expert
```

**Rule P2.3: Deprecated Term**
```yaml
id: P2.3
description: Ontology term marked as obsolete/deprecated
check: OWL obsolete annotation or OLS deprecated flag
impact: Future-proofing issues
fix: Map to replacement term (check owl:replacedBy)
```

**Rule P2.4: Purity Merge Violation**
```yaml
id: P2.4
description: Pure and impure variants merged incorrectly
check: Cross-reference merge history with purity annotations
impact: Loss of purity information critical for media design
fix: Unmerge and create separate records
```

**Rule P2.5: KG-Microbe Dictionary Disagreement**
```yaml
id: P2.5
description: MIM ontology_id disagrees with kg-microbe's unified chemical dictionary
             for the same preferred_term or synonym
check: |
  For each MIM record, look up preferred_term (and each synonym_text) in
  kg-microbe's unified_chemical_mappings.tsv.gz synonym→chebi_id index.
  Flag if kg-microbe maps the same surface form to a different CHEBI ID.
impact: Cross-repo semantic drift. MIM and kg-microbe knowledge graphs will
        disagree on the same chemical, breaking joins on CHEBI ID at KG ingest.
fix: |
  Both sides must be verified — kg-microbe's dict has known TSV-parse bugs
  producing false synonyms (e.g., merged-row pollution attaching "MnCl2"
  synonym to CHEBI:30200 kaempferol glucoside). Reviewer must:
    1. Lookup MIM's ontology_id via OAK/OLS → get canonical label
    2. Lookup kg-microbe's proposed CHEBI via OAK/OLS → get canonical label
    3. Compare both labels against MIM's preferred_term
    4. Pick the winner; update MIM or log an issue upstream against kg-microbe
severity: P2 (possible wrong mapping, needs expert review)
data_source: |
  /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/
    mappings/unified_chemical_mappings.tsv.gz
  Columns: chebi_id, canonical_name, formula, synonyms (pipe-separated),
           xrefs, sources
  Rows: ~164,597
known_false_positive_patterns:
  - Merged-row pollution: when a synonym field contains embedded quotes,
    csv.DictReader may merge the next row, attaching the following row's
    synonyms to the wrong CHEBI ID.
  - Common-cation contamination: short synonyms like "Na+", "K+", "Cl-"
    appear under many CHEBI IDs and never indicate a real equivalence.
  - Ambiguous ion/salt names: "calcium", "magnesium", "iron" without
    anion qualifier.
```

#### P3 - Medium-Priority Warnings

**Rule P3.1: Missing Chemical Properties**
```yaml
id: P3.1
description: SMILES, InChI, or molecular_formula missing for CHEBI terms
check: chemical_properties section empty
impact: Reduced utility for cheminformatics
fix: Auto-enrich from EBI OLS v4 API
```

**Rule P3.2: Missing Synonyms**
```yaml
id: P3.2
description: Ontology has synonyms not in ingredient record
check: Compare ontology synonyms (exact, related, narrow) with record synonyms
impact: Reduced search/matching capability
fix: Auto-add ontology synonyms with source attribution
```

**Rule P3.3: Low Confidence Mapping**
```yaml
id: P3.3
description: Mapping quality < 0.7 or quality level is PROVISIONAL
check: ontology_mapping.confidence or quality field
impact: Uncertain mappings may need expert review
fix: Manual review or LLM-assisted re-validation
```

**Rule P3.4: Ambiguous Quality Level**
```yaml
id: P3.4
description: CLOSE_MATCH quality without purity/catalog notes in reasoning
check: quality=CLOSE_MATCH and reasoning doesn't mention purity/catalog/hydrate
impact: Unclear why match is "close" not "exact"
fix: Enhance reasoning field with normalization details
```

#### P4 - Low-Priority Info

**Rule P4.1: Additional Synonyms Available**
```yaml
id: P4.1
description: Ontology has many more synonyms than in record
check: Ontology synonym count > record synonym count + 5
impact: Potential enrichment opportunity
fix: Review and selectively add relevant synonyms
```

**Rule P4.2: Alternative Ontology Matches**
```yaml
id: P4.2
description: High-scoring matches in other ontologies
check: OAK multi-source search finds score > 0.8 in different source
impact: Potential better fit in different ontology
fix: Manual review of alternative
```

**Rule P4.3: Enrichment Opportunities**
```yaml
id: P4.3
description: Additional metadata available (cellular roles, pathways)
check: CHEBI has role annotations, pathway links
impact: Enhanced semantic richness
fix: Optionally add role/pathway links
```

**Rule P4.4: KG-Microbe Synonym Enrichment Candidates**
```yaml
id: P4.4
description: kg-microbe's unified chemical dict has synonyms for this record's
             CHEBI ID that MIM does not yet carry
check: |
  For MIM record with ontology_id=CHEBI:X, fetch the row from
  unified_chemical_mappings.tsv.gz keyed by chebi_id=X. The "synonyms"
  column is pipe-separated. Diff against existing MIM synonym_text values
  (case-insensitive, whitespace-normalized).
impact: Search/matching recall in CultureMech recipe mapping — every missing
        synonym is a potential ingredient that won't resolve to this CHEBI.
fix: |
  Candidates are NOT auto-applied. Each candidate must be round-trip
  verified before adding:
    1. Sanity-check: does the synonym plausibly name this chemical?
       (A synonym like "MnCl2" on kaempferol glucoside fails this check.)
    2. Reverse-lookup: in the kg-microbe TSV, does this synonym also map
       to a DIFFERENT CHEBI? If yes, it's ambiguous — skip or investigate.
    3. If accepted, add with source="kg-microbe/unified_chemical_mappings"
       and synonym_type=EXACT or RELATED per kg-microbe's context.
severity: P4 (enrichment, not correctness)
safety: |
  Do NOT treat kg-microbe synonyms as authoritative. The dict was built
  from multiple upstream sources and has documented parsing bugs.
  Every proposal needs human-in-the-loop review before commit.
```
