# MediaIngredientMech justfile
# Run `just` to see all available commands

set dotenv-load := true

research_dir := "research"
templates_dir := "templates"

# Default recipe - list all commands
default:
    @just --list

# Install package and dependencies
install:
    pip install -e ".[dev]"

# Generate LinkML dataclasses from schema
gen-schema:
    gen-linkml --dir src/mediaingredientmech/datamodel src/mediaingredientmech/schema/mediaingredientmech.yaml

# Validate schema syntax
validate-schema:
    linkml-validate --schema src/mediaingredientmech/schema/mediaingredientmech.yaml

# Import data from CultureMech
import-data:
    python scripts/import_from_culturemech.py

# Validate all data against schema (both collection and individual files)
validate-all:
    python scripts/validate_all.py --mode both

# Strict closed-schema validation: in-process LinkML validator with
# JsonschemaValidationPlugin(closed=True) so unknown fields are flagged.
# Walks data/ingredients/{mapped,unmapped} and data/curated by default.
# Emits a categorized TSV (reports/instance_validation_failures.tsv) and
# exits non-zero if any ERROR rows were produced.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# Inventory YAML-writing scripts under scripts/ and the central curation /
# utils packages. Records whether each writer validates before writing
# and whether it appends a curation_history event. Output:
# reports/pipeline_writers_audit.tsv. Useful for tracking adoption of
# write_validated_ingredient + record_curation_event over time.
audit-writers:
    uv run python scripts/audit_writers.py --out reports/pipeline_writers_audit.tsv

# Verify literature snippets in evidence claims appear verbatim in
# cached PubMed abstracts. Anti-hallucination gate. See
# ../culturebotai-claw/.claude/skills/evidence-reference-validation/.
# Exits 2 on SNIPPET_NOT_IN_ABSTRACT (CI blocking).
qc-evidence:
    /opt/homebrew/bin/python3.13 ../culturebotai-claw/scripts/validate_evidence_references.py

# Fetch missing PubMed abstracts referenced by MIM evidence claims.
# Polite (3 req/s, 10 with NCBI_API_KEY env var).
fetch-pubmed *args:
    /opt/homebrew/bin/python3.13 ../culturebotai-claw/scripts/fetch_pubmed_abstracts.py {{args}}

# Validate mappings/ingredient_mappings.sssom.tsv against structural
# invariants (Rule A: auto-classifier token-overlap gate). Rejects are
# written to mappings/needs_curator_review.tsv. Exits 2 on violation
# (CI blocking). See ../culturebotai-claw/.claude/plans/now-focus-on-culturemech-piped-shell.md.
qc-sssom:
    python3 scripts/validate_sssom_invariants.py

# Composite QC: schema validation + strict closed-schema check +
# evidence reference validation + SSSOM invariants.
qc: validate-all validate-strict qc-evidence qc-sssom

# Render per-ingredient HTML detail pages from data/ingredients/*.yaml
# into pages/ingredient/. Idempotent (skips fresh outputs); --force
# regenerates everything. See
# ../culturebotai-claw/docs/proposals/phase5_mkdocs_material_and_browser_parity.md
gen-ingredient-pages *args:
    /opt/homebrew/bin/python3.13 src/mediaingredientmech/render_ingredient_pages.py {{args}}

# Launch interactive curation CLI
curate:
    python scripts/curate_unmapped.py

# Generate curation progress report
report:
    python scripts/generate_report.py

# Generate HTML documentation from schema
gen-docs:
    gen-doc --directory docs src/mediaingredientmech/schema/mediaingredientmech.yaml

# Export ingredients to browser JSON
export-browser:
    python scripts/browser_export.py

# Generate UMAP visualization
generate-umap:
    python scripts/generate_ingredient_umap.py

# Build complete documentation site
build-docs: gen-docs export-browser
    @echo "Documentation built in docs/"
    @echo "Open docs/index.html to view locally"

# Export collection files to individual YAML records
export-individual:
    python scripts/export_individual_records.py

# Aggregate individual files back to collections
aggregate-collections:
    python scripts/aggregate_records.py

# Validate individual ingredient files only
validate-individual:
    python scripts/validate_all.py --mode individual

# Run FutureHouse Falcon / deep-research-client against an ingredient record
research-ingredient provider status slug *args="":
    uv run --extra dev python scripts/research_ingredient.py \
        --provider {{provider}} \
        --status {{status}} \
        --slug {{slug}} \
        --template {{templates_dir}}/ingredient_mapping_research.md \
        --research-dir {{research_dir}} \
        {{args}}

# List available deep-research-client providers
research-providers:
    uv run --extra dev python scripts/research_ingredient.py --list-providers

# Check availability for one deep-research-client provider
research-provider provider:
    uv run --extra dev python scripts/research_ingredient.py --provider-status {{provider}}

# Edison Scientific deep research (PaperQA3) for one ingredient record.
# target = slug (searched across mapped/ + unmapped/) or YAML path.
# Examples:
#   just research-ingredient-edison yeast_extract
#   just research-ingredient-edison soil --job literature-high
#   just research-ingredient-edison peptone --dry-run
research-ingredient-edison target *args="":
    uv run --extra dev python scripts/research_ingredient_edison.py \
        --target {{target}} \
        --template {{templates_dir}}/ingredient_mapping_research.md \
        --out-dir {{research_dir}}/ingredients \
        {{args}}

# Edison deep research for a batch of ingredients (JSON list of slugs/paths).
research-ingredient-edison-batch batch *args="":
    uv run --extra dev python scripts/research_ingredient_edison.py \
        --batch {{batch}} \
        --template {{templates_dir}}/ingredient_mapping_research.md \
        --out-dir {{research_dir}}/ingredients \
        {{args}}

# Retroactively backfill Edison provenance sidecars (no re-billing).
enrich-edison-response *args="":
    uv run --extra dev python scripts/enrich_edison_response.py {{args}}

# Full workflow: export, validate, aggregate
sync-individual:
    just export-individual && just validate-individual && just aggregate-collections

# Create snapshot of current data
snapshot:
    @timestamp=$(date +%Y%m%d_%H%M%S) && \
    mkdir -p data/snapshots/$$timestamp && \
    cp data/curated/*.yaml data/snapshots/$$timestamp/ && \
    echo "Snapshot created: data/snapshots/$$timestamp"

# Run tests
test:
    pytest tests/

# Run tests with coverage report
test-cov:
    pytest tests/ --cov=mediaingredientmech --cov-report=term-missing --cov-report=html

# Format code with black
format:
    black src/ tests/ scripts/

# Lint code with ruff
lint:
    ruff check src/ tests/ scripts/

# Type check with mypy
typecheck:
    mypy src/

# Run all quality checks
check: lint typecheck test

# Clean generated files
clean:
    rm -rf build/ dist/ *.egg-info htmlcov/ .pytest_cache/ .coverage
    find . -type d -name __pycache__ -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete
