# MediaIngredientMech justfile
# Run `just` to see all available commands

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
