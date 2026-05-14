# Task Processing Guide for MediaIngredientMech Claude

**For use in MediaIngredientMech Claude Code session**

---

## Overview

When the orchestration Claude creates a curation task, you (MediaIngredientMech Claude) can process it using your built-in Claude capabilities. No API keys needed!

---

## Quick Start

### Check for Pending Tasks

```
Read ../kg-microbe-orchestration/workspace/tasks/ and show me any pending tasks
```

### Process a Task

```
Process the pending task curation_batch_YYYYMMDD_HHMMSS from ../kg-microbe-orchestration/workspace/tasks/
```

---

## Step-by-Step Instructions

### 1. Find the Task

**User prompt**:
```
Check ../kg-microbe-orchestration/workspace/tasks/ for any pending curation tasks
```

**You should**:
- List all .yaml files in that directory
- Show tasks with status="pending"
- Display the task parameters

### 2. Process Ingredients

**User prompt**:
```
Process task curation_batch_20260320_192217 with the following steps:
1. Load unmapped ingredients from data/curated/unmapped_ingredients.yaml
2. Filter by parameters (min_occurrences, batch_size)
3. For each ingredient, use your Claude capabilities to suggest ontology mappings
4. Auto-accept mappings with confidence >= threshold
5. Save results
```

**You should**:
- Read data/curated/unmapped_ingredients.yaml
- Apply filters from task parameters
- For each ingredient:
  - Consider the ingredient name and context
  - Suggest appropriate CHEBI/FOODON/ENVO ontology ID
  - Estimate confidence (0.0-1.0)
  - If confidence >= auto_accept_threshold: Mark as accepted
  - Otherwise: Mark for manual review
- Write results to ../kg-microbe-orchestration/workspace/results/

### 3. Update Task Status

**After processing**:
- Update task file: status="complete", completed_at=now
- Write result file with summary

---

## Example Session

### Terminal: MediaIngredientMech Claude Code

```
User: "Check for pending tasks in ../kg-microbe-orchestration/workspace/tasks/"

Claude: "I'll check for pending tasks.

Found 1 pending task:
- Task ID: curation_batch_20260320_192217
- Operation: batch_curate
- Parameters:
  - Batch size: 5
  - Auto-accept threshold: 0.9
  - Min occurrences: 10
  - Dry run: false
- Status: pending
- Created: 2026-03-20T19:22:17Z

Would you like me to process this task?"

User: "Yes, process it"

Claude: "I'll process the curation task.

Step 1: Loading unmapped ingredients...
Found 115 unmapped ingredients.

Step 2: Filtering by min_occurrences >= 10...
Filtered to 28 ingredients.

Step 3: Processing first 5 ingredients (batch_size=5)...

[1/5] MgSO4•7H2O (29 occurrences)
  Analyzing: Magnesium sulfate heptahydrate
  Ontology ID: CHEBI:75895
  Label: magnesium sulfate heptahydrate
  Confidence: 0.95 (HIGH)
  ✓ AUTO-ACCEPTED (0.95 >= 0.9)

[2/5] CaCl2•2H2O (22 occurrences)
  Analyzing: Calcium chloride dihydrate
  Ontology ID: CHEBI:86142
  Label: calcium chloride dihydrate
  Confidence: 0.92 (HIGH)
  ✓ AUTO-ACCEPTED (0.92 >= 0.9)

[3/5] NaCl (13 occurrences)
  Analyzing: Sodium chloride
  Ontology ID: CHEBI:26710
  Label: sodium chloride
  Confidence: 0.98 (HIGH)
  ✓ AUTO-ACCEPTED (0.98 >= 0.9)

[4/5] Vitamin B (23 occurrences)
  Analyzing: Vitamin B complex
  Note: 'Vitamin B' is ambiguous (B1, B2, B3, B6, B12, etc.)
  Confidence: 0.30 (LOW)
  ⊘ SKIPPED (0.30 < 0.9) - needs manual review

[5/5] Biotin Vitamin Solution (18 occurrences)
  Analyzing: Biotin (Vitamin B7/H)
  Ontology ID: CHEBI:15956
  Label: biotin
  Confidence: 0.85 (MEDIUM-HIGH)
  ⊘ SKIPPED (0.85 < 0.9) - close but below threshold

Processing complete!

Summary:
- Processed: 5 ingredients
- Auto-accepted: 3 (MgSO4•7H2O, CaCl2•2H2O, NaCl)
- Skipped (low confidence): 2 (Vitamin B, Biotin Vitamin Solution)
- Duration: ~3 minutes

Saving results to ../kg-microbe-orchestration/workspace/results/curation_batch_20260320_192217.yaml

Updating task status to 'complete'...

✓ Task complete!"
```

---

## Task File Format

**Location**: `../kg-microbe-orchestration/workspace/tasks/TASK_ID.yaml`

```yaml
task_id: curation_batch_20260320_192217
target_repo: mediaingredientmech
operation: batch_curate
status: pending  # Update to: in_progress, complete, failed
created_at: '2026-03-20T19:22:17Z'
started_at: null  # Update when you start
completed_at: null  # Update when you finish
parameters:
  batch_size: 5
  auto_accept_threshold: 0.9
  min_occurrences: 10
  dry_run: false
assigned_to: mediaingredientmech_claude
result_file: null  # Update with result filename
error: null  # If failed, add error message
instructions: |
  Process 5 unmapped ingredients with:
  - Auto-accept threshold: 0.9
  - Min occurrences: 10
  - Dry run: False

  Use your built-in Claude capabilities to suggest ontology mappings.
  Save results to workspace/results/ when complete.
```

---

## Result File Format

**Location**: `../kg-microbe-orchestration/workspace/results/TASK_ID.yaml`

```yaml
task_id: curation_batch_20260320_192217
status: complete
started_at: '2026-03-20T19:25:00Z'
completed_at: '2026-03-20T19:28:30Z'
duration_seconds: 210
results:
  processed: 5
  auto_accepted: 3
  skipped_low_confidence: 2
  skipped_no_suggestion: 0
  failed: 0
  suggestions:
    - ingredient: MgSO4•7H2O
      ontology_id: CHEBI:75895
      label: magnesium sulfate heptahydrate
      source: CHEBI
      confidence: 0.95
      reasoning: Clear chemical formula matching CHEBI entry
      action: auto_accepted
    - ingredient: CaCl2•2H2O
      ontology_id: CHEBI:86142
      label: calcium chloride dihydrate
      source: CHEBI
      confidence: 0.92
      reasoning: Exact match for hydrated calcium chloride
      action: auto_accepted
    # ... etc
```

---

## Tips for High-Quality Mappings

### 1. Chemical Compounds
- Look for exact chemical formula matches
- Consider hydration states (MgSO4 vs MgSO4•7H2O)
- Check CAS numbers if available
- Confidence: 0.90-0.98 for exact matches

### 2. Complex Media Components
- Commercial products (e.g., "Bacto Soytone") may not have CHEBI IDs
- Consider FOODON for food-derived ingredients
- Confidence: 0.30-0.70 (often need manual review)

### 3. Biological Materials
- Serums, extracts, tissue → may need NCIT or UBERON
- Not usually in CHEBI
- Confidence: 0.40-0.75

### 4. Ambiguous Terms
- "Vitamin B" → could be B1, B2, B3, B6, B12
- "Salt" → could be NaCl, KCl, many others
- Confidence: 0.20-0.50 (always manual review)

### 5. Solutions
- "1.0 M NaOH" → map to NaOH (CHEBI:32145), note concentration
- "100 mg/ml azlocillin" → map to azlocillin, note concentration
- Confidence: 0.85-0.95

---

## Common Issues

### Issue: Can't find ontology ID

**Solution**:
- Try alternative names/synonyms
- Check chemical formula
- Consider if it's a commercial product (no CHEBI ID)
- Lower confidence and mark for manual review

### Issue: Multiple possible matches

**Solution**:
- Choose most specific match
- Document reasoning
- Lower confidence to 0.70-0.85
- May need manual review

### Issue: Incomplete chemical formula

**Example**: "NaNO" (missing subscript)
- Could be NaNO2 (sodium nitrite) or NaNO3 (sodium nitrate)
- Lower confidence to 0.50-0.70
- Note ambiguity in reasoning
- Manual review needed

---

## Updating Files

### Update Task Status

```python
# Read task
with open('../kg-microbe-orchestration/workspace/tasks/TASK_ID.yaml') as f:
    task = yaml.safe_load(f)

# Update status
task['status'] = 'complete'
task['completed_at'] = datetime.utcnow().isoformat() + 'Z'

# Write back
with open('../kg-microbe-orchestration/workspace/tasks/TASK_ID.yaml', 'w') as f:
    yaml.dump(task, f)
```

### Write Results

```python
results = {
    'task_id': 'curation_batch_20260320_192217',
    'status': 'complete',
    'started_at': '2026-03-20T19:25:00Z',
    'completed_at': '2026-03-20T19:28:30Z',
    'duration_seconds': 210,
    'results': {
        'processed': 5,
        'auto_accepted': 3,
        # ... etc
    }
}

with open('../kg-microbe-orchestration/workspace/results/TASK_ID.yaml', 'w') as f:
    yaml.dump(results, f)
```

---

## Full Process Checklist

- [ ] Check for pending tasks
- [ ] Read task parameters
- [ ] Update task status to "in_progress"
- [ ] Load unmapped ingredients
- [ ] Filter by min_occurrences
- [ ] Limit to batch_size
- [ ] For each ingredient:
  - [ ] Analyze name and context
  - [ ] Suggest ontology mapping
  - [ ] Estimate confidence
  - [ ] Decide: auto-accept or skip
- [ ] Write results file
- [ ] Update task status to "complete"
- [ ] Report summary to user

---

## Ready!

You're now ready to process curation tasks using your built-in Claude capabilities. No API keys required!

**Next**: Wait for orchestration Claude to create a task, then process it!
