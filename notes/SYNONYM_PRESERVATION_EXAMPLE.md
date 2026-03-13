# Synonym Preservation Example

This document shows how the batch curation system preserves original chemical forms as synonyms when normalization is applied.

## Example 1: Hydrate Form

**Original unmapped ingredient:**
```yaml
identifier: UNMAPPED_0003
preferred_term: MgSO4•7H2O
synonyms:
  - synonym_text: MgSO4•7H2O (Sigma 230391)
    synonym_type: RAW_TEXT
    source: CultureMech
mapping_status: UNMAPPED
```

**After batch curation with normalization:**

1. **Normalization applied:**
   - Original: `MgSO4•7H2O`
   - Normalized: `MgSO4` (stripped hydrate notation)
   - Search variants: `MgSO4•7H2O`, `MgSO4`, `magnesium sulfate`

2. **Ontology match found:**
   - CHEBI:32599 - magnesium sulfate (score: 0.95)

3. **Mapping accepted:**
   - Identifier updated to CHEBI:32599
   - Status changed to MAPPED
   - **Original form `MgSO4•7H2O` added as synonym with type `HYDRATE_FORM`**

**Resulting mapped ingredient:**
```yaml
identifier: CHEBI:32599
preferred_term: MgSO4•7H2O  # Original preferred term preserved
synonyms:
  - synonym_text: MgSO4•7H2O (Sigma 230391)
    synonym_type: RAW_TEXT
    source: CultureMech
  - synonym_text: MgSO4•7H2O
    synonym_type: HYDRATE_FORM
    source: batch_curation_normalization
    notes: "Original form before normalization: stripped_hydrate"
mapping_status: MAPPED
ontology_mapping:
  ontology_id: CHEBI:32599
  ontology_label: magnesium sulfate
  ontology_source: CHEBI
  mapping_quality: EXACT_MATCH
  evidence:
    - evidence_type: CURATOR_JUDGMENT
      source: batch_curator
      confidence_score: 0.95
      notes: "Batch curated with normalization: stripped_hydrate"
curation_history:
  - timestamp: "2026-03-09T..."
    curator: batch_curator
    action: MAPPED
    changes: "Mapped to CHEBI:32599 (magnesium sulfate)"
    previous_status: UNMAPPED
    new_status: MAPPED
    llm_assisted: false
    notes: "Batch curated with normalization: stripped_hydrate"
```

## Example 2: Catalog Variant

**Original:**
```yaml
identifier: UNMAPPED_0015
preferred_term: NaCl (Fisher S271-500)
mapping_status: UNMAPPED
```

**After curation:**
```yaml
identifier: CHEBI:26710
preferred_term: NaCl (Fisher S271-500)
synonyms:
  - synonym_text: NaCl (Fisher S271-500)
    synonym_type: CATALOG_VARIANT
    source: batch_curation_normalization
    notes: "Original form before normalization: stripped_catalog"
mapping_status: MAPPED
ontology_mapping:
  ontology_id: CHEBI:26710
  ontology_label: sodium chloride
  ontology_source: CHEBI
  mapping_quality: EXACT_MATCH
```

## Example 3: Incomplete Formula

**Original:**
```yaml
identifier: UNMAPPED_0010
preferred_term: K2HPO
mapping_status: UNMAPPED
```

**After curation:**
```yaml
identifier: CHEBI:63036
preferred_term: K2HPO
synonyms:
  - synonym_text: K2HPO
    synonym_type: INCOMPLETE_FORMULA
    source: batch_curation_normalization
    notes: "Original form before normalization: fixed_incomplete_formula"
mapping_status: MAPPED
ontology_mapping:
  ontology_id: CHEBI:63036
  ontology_label: dipotassium phosphate
  ontology_source: CHEBI
  mapping_quality: SYNONYM_MATCH
```

## Why This Matters

### Searchability

Users can search for ingredients using **any form**:
- Original unmapped form: `MgSO4•7H2O`
- Normalized form: `MgSO4`
- Common name: `magnesium sulfate`
- Ontology ID: `CHEBI:32599`

All searches will find the same mapped ingredient.

### Traceability

The complete curation trail is preserved:
- What was the original form?
- What normalization was applied?
- Why was the mapping made?
- Who made the decision?

### Data Quality

No information is lost during normalization:
- Original notation preserved
- Catalog/supplier codes retained
- All variant forms searchable
- Complete audit trail

## Synonym Types

The system uses specific synonym types for different normalization scenarios:

| Synonym Type | Description | Example |
|--------------|-------------|---------|
| `HYDRATE_FORM` | Hydrate notation | `MgSO4•7H2O`, `CaCl2.2H2O` |
| `CATALOG_VARIANT` | Catalog/supplier code | `NaCl (Fisher S271-500)` |
| `INCOMPLETE_FORMULA` | Incomplete chemical formula | `K2HPO`, `NaNO` |
| `ALTERNATE_FORM` | Other chemical forms | Salt forms, esters, etc. |

These types are defined in the schema and can be used for:
- Filtering searches
- Analyzing curation patterns
- Generating reports
- Quality control

## Benefits

1. **Preserves original notation** - Nothing is lost
2. **Improves searchability** - Multiple ways to find ingredients
3. **Maintains traceability** - Clear audit trail
4. **Enables analysis** - Can study notation patterns
5. **Supports validation** - Can verify normalization decisions

## Schema Compliance

All synonym types are defined in the LinkML schema:
```yaml
SynonymTypeEnum:
  permissible_values:
    HYDRATE_FORM:
      description: Chemical with hydrate notation (e.g., MgSO4•7H2O)
    CATALOG_VARIANT:
      description: Name with catalog/supplier code (e.g., NaCl Fisher S271-500)
    INCOMPLETE_FORMULA:
      description: Incomplete chemical formula (e.g., K2HPO instead of K2HPO4)
    ALTERNATE_FORM:
      description: Alternative chemical form (salt, ester, etc.)
```

All curated data validates against the schema with `linkml-validate`.
