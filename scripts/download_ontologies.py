#!/usr/bin/env python3
"""
Download and cache OWL files from OBO Foundry.

Usage:
    python scripts/download_ontologies.py --check-only
    python scripts/download_ontologies.py --sources CHEBI FOODON
    python scripts/download_ontologies.py --all
    python scripts/download_ontologies.py --force --sources CHEBI
    python scripts/download_ontologies.py --verify
"""

import argparse
import hashlib
import json
import sys
from pathlib import Path
from datetime import datetime, timezone

import requests
from rich.console import Console
from rich.progress import Progress, DownloadColumn, TransferSpeedColumn, TimeRemainingColumn

console = Console()

# OBO Foundry URLs
ONTOLOGY_URLS = {
    "CHEBI": "http://purl.obolibrary.org/obo/chebi.owl",
    "FOODON": "http://purl.obolibrary.org/obo/foodon.owl",
    "ENVO": "http://purl.obolibrary.org/obo/envo.owl",
}

CACHE_DIR = Path("ontology/cache")
MANIFEST_FILE = CACHE_DIR / "manifest.json"


def compute_md5(file_path: Path) -> str:
    """Compute MD5 checksum of a file."""
    md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            md5.update(chunk)
    return md5.hexdigest()


def load_manifest() -> dict:
    """Load manifest.json if it exists."""
    if MANIFEST_FILE.exists():
        with open(MANIFEST_FILE) as f:
            return json.load(f)
    return {}


def save_manifest(manifest: dict):
    """Save manifest.json."""
    MANIFEST_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest, f, indent=2)


def download_ontology(source: str, url: str, force: bool = False) -> bool:
    """
    Download an ontology OWL file.

    Args:
        source: Ontology source (e.g., "CHEBI")
        url: Download URL
        force: Re-download even if cached

    Returns:
        True if downloaded successfully
    """
    output_file = CACHE_DIR / f"{source.lower()}.owl"

    # Check if already exists and not forcing
    if output_file.exists() and not force:
        console.print(f"[yellow]{source} already cached at {output_file}[/yellow]")
        return True

    console.print(f"[cyan]Downloading {source} from {url}...[/cyan]")

    try:
        # Stream download with progress
        response = requests.get(url, stream=True, timeout=60)
        response.raise_for_status()

        total_size = int(response.headers.get("content-length", 0))

        with Progress(
            *Progress.get_default_columns(),
            DownloadColumn(),
            TransferSpeedColumn(),
            TimeRemainingColumn(),
            console=console,
        ) as progress:
            task = progress.add_task(f"Downloading {source}", total=total_size)

            CACHE_DIR.mkdir(parents=True, exist_ok=True)

            with open(output_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
                    progress.update(task, advance=len(chunk))

        # Compute MD5
        md5 = compute_md5(output_file)
        size_mb = output_file.stat().st_size / (1024 * 1024)

        console.print(f"[green]✓ Downloaded {source} ({size_mb:.1f} MB)[/green]")

        # Update manifest
        manifest = load_manifest()
        manifest[source.lower()] = {
            "url": url,
            "downloaded": datetime.now(timezone.utc).isoformat(),
            "md5": md5,
            "size_mb": round(size_mb, 1),
            "status": "valid",
        }
        save_manifest(manifest)

        return True

    except Exception as e:
        console.print(f"[red]✗ Failed to download {source}: {e}[/red]")
        return False


def verify_ontology(source: str) -> bool:
    """Verify an ontology file's integrity."""
    manifest = load_manifest()
    source_lower = source.lower()

    if source_lower not in manifest:
        console.print(f"[yellow]{source} not in manifest[/yellow]")
        return False

    file_path = CACHE_DIR / f"{source_lower}.owl"
    if not file_path.exists():
        console.print(f"[red]✗ {source} file not found: {file_path}[/red]")
        return False

    # Verify MD5
    expected_md5 = manifest[source_lower].get("md5")
    actual_md5 = compute_md5(file_path)

    if expected_md5 != actual_md5:
        console.print(f"[red]✗ {source} MD5 mismatch[/red]")
        console.print(f"  Expected: {expected_md5}")
        console.print(f"  Actual: {actual_md5}")
        return False

    # Verify file size
    expected_size = manifest[source_lower].get("size_mb", 0)
    actual_size = file_path.stat().st_size / (1024 * 1024)

    if abs(expected_size - actual_size) > 0.1:  # Allow 0.1 MB difference
        console.print(f"[yellow]⚠ {source} size difference[/yellow]")
        console.print(f"  Expected: {expected_size:.1f} MB")
        console.print(f"  Actual: {actual_size:.1f} MB")

    console.print(f"[green]✓ {source} verified[/green]")
    return True


def check_status():
    """Check current cache status."""
    manifest = load_manifest()

    if not manifest:
        console.print("[yellow]No ontologies cached[/yellow]")
        return

    console.print("[bold]Cached Ontologies:[/bold]\n")

    for source, info in manifest.items():
        console.print(f"[cyan]{source.upper()}[/cyan]")
        console.print(f"  Downloaded: {info.get('downloaded', 'N/A')}")
        console.print(f"  Size: {info.get('size_mb', 0):.1f} MB")
        console.print(f"  MD5: {info.get('md5', 'N/A')[:16]}...")
        console.print(f"  Status: {info.get('status', 'unknown')}")
        console.print()


def main():
    parser = argparse.ArgumentParser(description="Download and manage ontology OWL files")
    parser.add_argument(
        "--sources",
        nargs="+",
        choices=list(ONTOLOGY_URLS.keys()),
        help="Ontology sources to download",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Download all supported ontologies",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force re-download even if cached",
    )
    parser.add_argument(
        "--verify",
        action="store_true",
        help="Verify integrity of cached files",
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Show current cache status without downloading",
    )

    args = parser.parse_args()

    # Check status
    if args.check_only:
        check_status()
        return 0

    # Verify
    if args.verify:
        manifest = load_manifest()
        all_valid = True
        for source in manifest.keys():
            if not verify_ontology(source.upper()):
                all_valid = False
        return 0 if all_valid else 1

    # Determine which sources to download
    sources_to_download = []
    if args.all:
        sources_to_download = list(ONTOLOGY_URLS.keys())
    elif args.sources:
        sources_to_download = args.sources
    else:
        parser.error("Either --sources or --all must be specified")

    # Download
    console.print(f"[cyan]Downloading {len(sources_to_download)} ontologies...[/cyan]\n")

    success_count = 0
    for source in sources_to_download:
        url = ONTOLOGY_URLS[source]
        if download_ontology(source, url, force=args.force):
            success_count += 1

    console.print(f"\n[green]✓ Successfully downloaded {success_count}/{len(sources_to_download)} ontologies[/green]")

    return 0 if success_count == len(sources_to_download) else 1


if __name__ == "__main__":
    sys.exit(main())
