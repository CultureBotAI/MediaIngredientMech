#!/usr/bin/env python3
"""
Batch validate all ingredients and generate comprehensive reports.

Usage:
    python scripts/batch_review.py --output reports/validation_20260315
    python scripts/batch_review.py --priority P1,P2
    python scripts/batch_review.py --source CHEBI --threads 8
    python scripts/batch_review.py --limit 10 --dry-run
"""

import argparse
import json
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List

import yaml
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TimeElapsedColumn

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mediaingredientmech.curation.ingredient_curator import IngredientCurator
from mediaingredientmech.validation.ingredient_reviewer import IngredientReviewer

console = Console()


def load_mapped_ingredients() -> List[Dict]:
    """Load mapped ingredients from YAML file."""
    mapped_file = Path("data/curated/mapped_ingredients.yaml")
    with open(mapped_file) as f:
        data = yaml.safe_load(f)
    return data.get("ingredients", [])


def generate_markdown_report(result, output_path: Path):
    """Generate Markdown validation report."""
    report_lines = [
        "# Ingredient Validation Report",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "## Summary Statistics",
        f"- Total ingredients reviewed: {sum(result.summary.values())}",
        f"- P1 Critical errors: {result.summary['P1']}",
        f"- P2 High-priority warnings: {result.summary['P2']} ({result.summary['P2'] / max(sum(result.summary.values()), 1) * 100:.1f}%)",
        f"- P3 Medium-priority warnings: {result.summary['P3']} ({result.summary['P3'] / max(sum(result.summary.values()), 1) * 100:.1f}%)",
        f"- P4 Low-priority info: {result.summary['P4']} ({result.summary['P4'] / max(sum(result.summary.values()), 1) * 100:.1f}%)",
        "",
    ]

    # Group issues by priority and category
    priority_groups = {"P1": {}, "P2": {}, "P3": {}, "P4": {}}
    for issue in result.all_issues:
        priority = issue.priority
        category = issue.category
        if category not in priority_groups[priority]:
            priority_groups[priority][category] = []
        priority_groups[priority][category].append(issue)

    # P1 Critical Errors
    report_lines.append("## P1 Critical Errors ({})".format(result.summary["P1"]))
    report_lines.append("")
    if result.summary["P1"] == 0:
        report_lines.append("*No critical errors found*")
        report_lines.append("")
    else:
        for category, issues in priority_groups["P1"].items():
            report_lines.append(f"### {category.replace('_', ' ').title()} ({len(issues)})")
            report_lines.append("")
            for i, issue in enumerate(issues, 1):
                report_lines.append(f"{i}. **{issue.ingredient_id}**")
                report_lines.append(f"   - {issue.message}")
                report_lines.append(f"   - Evidence: {issue.evidence}")
                report_lines.append("")

    # P2 High-Priority Warnings
    report_lines.append("## P2 High-Priority Warnings ({})".format(result.summary["P2"]))
    report_lines.append("")
    if result.summary["P2"] == 0:
        report_lines.append("*No high-priority warnings*")
        report_lines.append("")
    else:
        for category, issues in priority_groups["P2"].items():
            report_lines.append(f"### {category.replace('_', ' ').title()} ({len(issues)})")
            report_lines.append("")
            for i, issue in enumerate(issues[:10], 1):  # Limit to first 10
                report_lines.append(f"{i}. **{issue.ingredient_id}**")
                report_lines.append(f"   - {issue.message}")
                report_lines.append("")
            if len(issues) > 10:
                report_lines.append(f"   *...and {len(issues) - 10} more*")
                report_lines.append("")

    # P3 Medium-Priority Warnings (summary only)
    report_lines.append("## P3 Medium-Priority Warnings ({})".format(result.summary["P3"]))
    report_lines.append("")
    if result.summary["P3"] > 0:
        for category, issues in priority_groups["P3"].items():
            report_lines.append(f"- **{category.replace('_', ' ').title()}**: {len(issues)} ingredients")
        report_lines.append("")
        report_lines.append("*See JSON report for full details*")
        report_lines.append("")

    # P4 Low-Priority Info (summary only)
    report_lines.append("## P4 Low-Priority Info ({})".format(result.summary["P4"]))
    report_lines.append("")
    if result.summary["P4"] > 0:
        for category, issues in priority_groups["P4"].items():
            report_lines.append(f"- **{category.replace('_', ' ').title()}**: {len(issues)} ingredients")
        report_lines.append("")

    # Failed validations
    if result.failed:
        report_lines.append("## Failed Validations ({})".format(len(result.failed)))
        report_lines.append("")
        for failure in result.failed:
            report_lines.append(f"- **{failure['ingredient']}**: {failure['error']}")
        report_lines.append("")

    # Write report
    output_path.write_text("\n".join(report_lines))
    console.print(f"[green]✓ Markdown report written to {output_path}[/green]")


def generate_json_report(result, output_path: Path):
    """Generate JSON validation report."""
    report_data = {
        "metadata": {
            "generated": datetime.now(timezone.utc).isoformat(),
            "total_reviewed": sum(result.summary.values()),
            "summary": result.summary,
        },
        "issues": [
            {
                "ingredient": issue.ingredient_id,
                "priority": issue.priority,
                "rule_id": issue.rule_id,
                "category": issue.category,
                "message": issue.message,
                "evidence": issue.evidence,
            }
            for issue in result.all_issues
        ],
        "suggestions": [
            {
                "action": sugg.action,
                "field_path": sugg.field_path,
                "current_value": str(sugg.current_value),
                "suggested_value": str(sugg.suggested_value),
                "auto_correctable": sugg.auto_correctable,
                "confidence": sugg.confidence,
                "rationale": sugg.rationale,
            }
            for sugg in result.all_suggestions
        ],
        "failed": result.failed,
    }

    output_path.write_text(json.dumps(report_data, indent=2))
    console.print(f"[green]✓ JSON report written to {output_path}[/green]")


def generate_html_dashboard(result, output_path: Path):
    """Generate HTML interactive dashboard."""
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ingredient Validation Dashboard</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.datatables.net/1.11.5/css/dataTables.bootstrap5.min.css" rel="stylesheet">
    <style>
        body {{ padding: 20px; }}
        .priority-P1 {{ color: #dc3545; font-weight: bold; }}
        .priority-P2 {{ color: #ffc107; font-weight: bold; }}
        .priority-P3 {{ color: #0dcaf0; }}
        .priority-P4 {{ color: #198754; }}
    </style>
</head>
<body>
    <div class="container-fluid">
        <h1>Ingredient Validation Dashboard</h1>
        <p class="text-muted">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>

        <div class="row mb-4">
            <div class="col-md-3">
                <div class="card text-white bg-danger">
                    <div class="card-body">
                        <h5 class="card-title">P1 Critical</h5>
                        <p class="card-text display-4">{result.summary['P1']}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card text-white bg-warning">
                    <div class="card-body">
                        <h5 class="card-title">P2 High Priority</h5>
                        <p class="card-text display-4">{result.summary['P2']}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card text-white bg-info">
                    <div class="card-body">
                        <h5 class="card-title">P3 Medium Priority</h5>
                        <p class="card-text display-4">{result.summary['P3']}</p>
                    </div>
                </div>
            </div>
            <div class="col-md-3">
                <div class="card text-white bg-success">
                    <div class="card-body">
                        <h5 class="card-title">P4 Low Priority</h5>
                        <p class="card-text display-4">{result.summary['P4']}</p>
                    </div>
                </div>
            </div>
        </div>

        <h2>Issues</h2>
        <table id="issuesTable" class="table table-striped table-hover">
            <thead>
                <tr>
                    <th>Priority</th>
                    <th>Ingredient</th>
                    <th>Rule</th>
                    <th>Category</th>
                    <th>Message</th>
                </tr>
            </thead>
            <tbody>
"""

    for issue in result.all_issues:
        html_content += f"""                <tr class="priority-{issue.priority}">
                    <td>{issue.priority}</td>
                    <td>{issue.ingredient_id}</td>
                    <td>{issue.rule_id}</td>
                    <td>{issue.category}</td>
                    <td>{issue.message}</td>
                </tr>
"""

    html_content += """            </tbody>
        </table>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/dataTables.bootstrap5.min.js"></script>
    <script>
        $(document).ready(function() {
            $('#issuesTable').DataTable({
                order: [[0, 'asc']],
                pageLength: 25
            });
        });
    </script>
</body>
</html>
"""

    output_path.write_text(html_content)
    console.print(f"[green]✓ HTML dashboard written to {output_path}[/green]")


def main():
    parser = argparse.ArgumentParser(description="Batch review ingredients")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output directory for reports",
    )
    parser.add_argument(
        "--format",
        default="md,json",
        help="Report formats (comma-separated): md,json,html (default: md,json)",
    )
    parser.add_argument(
        "--priority",
        help="Filter by priority (comma-separated): P1,P2,P3,P4",
    )
    parser.add_argument(
        "--source",
        help="Filter by ontology source: CHEBI,FOODON,ENVO",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=4,
        help="Number of parallel workers (default: 4)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Process only first N ingredients (for testing)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview without writing files",
    )
    parser.add_argument(
        "--use-local-owl",
        action="store_true",
        help="Use local OWL files instead of remote OAK",
    )

    args = parser.parse_args()

    # Initialize
    reviewer = IngredientReviewer(use_local_owl=args.use_local_owl)

    # Load ingredients
    console.print("[cyan]Loading mapped ingredients...[/cyan]")
    ingredients = load_mapped_ingredients()

    # Filter by source if specified
    if args.source:
        sources = args.source.split(",")
        ingredients = [
            ing
            for ing in ingredients
            if ing.get("ontology_mapping", {}).get("ontology_id", "").split(":")[0]
            in sources
        ]
        console.print(f"Filtered to {len(ingredients)} ingredients from {args.source}")

    # Limit if specified
    if args.limit:
        ingredients = ingredients[: args.limit]
        console.print(f"Limited to {args.limit} ingredients")

    # Parse priority filter
    priority_filter = None
    if args.priority:
        priority_filter = args.priority.split(",")

    # Run validation
    console.print(f"\n[cyan]Validating {len(ingredients)} ingredients...[/cyan]")

    with Progress(
        SpinnerColumn(),
        *Progress.get_default_columns(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("Validating...", total=len(ingredients))

        result = reviewer.batch_review(
            ingredients,
            priority_filter=priority_filter,
            parallel=True,
            max_workers=args.threads,
        )

        progress.update(task, completed=len(ingredients))

    # Display summary
    console.print("\n[bold]Validation Summary:[/bold]")
    console.print(f"  Total reviewed: {len(ingredients)}")
    console.print(f"  [red]P1 Critical errors: {result.summary['P1']}[/red]")
    console.print(f"  [yellow]P2 High-priority warnings: {result.summary['P2']}[/yellow]")
    console.print(f"  [blue]P3 Medium-priority warnings: {result.summary['P3']}[/blue]")
    console.print(f"  [green]P4 Low-priority info: {result.summary['P4']}[/green]")

    if result.failed:
        console.print(f"  [red]Failed validations: {len(result.failed)}[/red]")

    # Generate reports
    if not args.dry_run:
        if not args.output:
            args.output = Path(f"reports/validation_{datetime.now().strftime('%Y%m%d_%H%M%S')}")

        args.output.mkdir(parents=True, exist_ok=True)
        console.print(f"\n[cyan]Generating reports in {args.output}...[/cyan]")

        formats = args.format.split(",")

        if "md" in formats:
            generate_markdown_report(result, args.output / "validation_report.md")

        if "json" in formats:
            generate_json_report(result, args.output / "validation_data.json")

        if "html" in formats:
            generate_html_dashboard(result, args.output / "dashboard.html")

        console.print(f"\n[green]✓ Reports generated in {args.output}[/green]")
    else:
        console.print("\n[yellow]Dry-run mode - no files written[/yellow]")

    # Exit code
    return 0 if result.summary["P1"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
