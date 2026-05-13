"""DOI resolution and citation metadata retrieval.

This module provides infrastructure for resolving DOIs to citation metadata
using the Crossref and DataCite APIs. It follows the same caching and rate
limiting patterns as chemical_properties_client.py.

Note: This infrastructure is built for future use. Initial role curation
uses CultureMech DATABASE_ENTRY citations.
"""

import json
import time
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import requests


@dataclass
class DOIMetadata:
    """Metadata for a single DOI citation."""

    doi: str
    title: Optional[str] = None
    authors: list[str] = field(default_factory=list)
    year: Optional[int] = None
    journal: Optional[str] = None
    citation_text: Optional[str] = None  # Auto-generated APA citation
    url: Optional[str] = None
    raw_response: Optional[dict] = None  # Full API response for debugging

    def to_citation_dict(self) -> dict:
        """Convert to RoleCitation format for IngredientCurator.

        Returns:
            Dictionary compatible with RoleCitation schema
        """
        return {
            "doi": self.doi,
            "reference_text": self.citation_text or f"DOI: {self.doi}",
            "reference_type": "PUBLICATION",
            "url": self.url or f"https://doi.org/{self.doi}",
        }

    def to_json(self) -> str:
        """Serialize to JSON for caching."""
        # Exclude raw_response from cache to save space
        data = asdict(self)
        data.pop("raw_response", None)
        return json.dumps(data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> "DOIMetadata":
        """Deserialize from JSON cache."""
        data = json.loads(json_str)
        return cls(**data)


class DOIResolver:
    """Client for resolving DOIs to citation metadata.

    Uses Crossref API (primary) with caching and rate limiting.
    """

    def __init__(
        self,
        cache_dir: Optional[Path] = None,
        rate_limit: float = 5.0,  # Max requests per second
        timeout: int = 10,
    ):
        """Initialize DOI resolver.

        Args:
            cache_dir: Directory for caching metadata (default: ~/.cache/mediaingredientmech/doi_metadata)
            rate_limit: Maximum requests per second
            timeout: Request timeout in seconds
        """
        self.cache_dir = (
            cache_dir
            or Path.home() / ".cache" / "mediaingredientmech" / "doi_metadata"
        )
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.rate_limit = rate_limit
        self.timeout = timeout
        self.last_request_time = 0.0

        # Crossref API endpoint (polite pool - requires mailto in User-Agent)
        self.crossref_base = "https://api.crossref.org/works"
        self.user_agent = (
            "MediaIngredientMech/1.0 (mailto:support@example.com) Python/requests"
        )

    def _get_cache_path(self, doi: str) -> Path:
        """Get cache file path for a DOI.

        Args:
            doi: DOI string (e.g., "10.1038/nature12345")

        Returns:
            Path to cache file
        """
        # Sanitize DOI for filename (replace / with _)
        safe_doi = doi.replace("/", "_").replace(":", "_")
        return self.cache_dir / f"{safe_doi}.json"

    def _load_from_cache(self, doi: str) -> Optional[DOIMetadata]:
        """Load metadata from cache.

        Args:
            doi: DOI string

        Returns:
            DOIMetadata if cached, None otherwise
        """
        cache_path = self._get_cache_path(doi)
        if cache_path.exists():
            try:
                with open(cache_path) as f:
                    return DOIMetadata.from_json(f.read())
            except Exception as e:
                print(f"⚠️  Cache read error for {doi}: {e}")
                return None
        return None

    def _save_to_cache(self, metadata: DOIMetadata):
        """Save metadata to cache.

        Args:
            metadata: DOIMetadata to cache
        """
        cache_path = self._get_cache_path(metadata.doi)
        try:
            with open(cache_path, "w") as f:
                f.write(metadata.to_json())
        except Exception as e:
            print(f"⚠️  Cache write error for {metadata.doi}: {e}")

    def _rate_limit_wait(self):
        """Enforce rate limiting between requests."""
        if self.rate_limit <= 0:
            return

        elapsed = time.time() - self.last_request_time
        min_interval = 1.0 / self.rate_limit

        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

        self.last_request_time = time.time()

    def _format_apa_citation(
        self,
        authors: list[str],
        year: Optional[int],
        title: Optional[str],
        journal: Optional[str],
        doi: str,
    ) -> str:
        """Format citation in APA style.

        Args:
            authors: List of author names
            year: Publication year
            title: Article title
            journal: Journal name
            doi: DOI

        Returns:
            APA-formatted citation string
        """
        # Format authors (max 3, then "et al.")
        if not authors:
            author_str = "Unknown authors"
        elif len(authors) <= 3:
            author_str = ", ".join(authors)
        else:
            author_str = f"{', '.join(authors[:3])}, et al."

        year_str = f"({year})" if year else "(n.d.)"
        title_str = f"{title}." if title else "Untitled."
        journal_str = f" {journal}." if journal else ""

        return f"{author_str} {year_str}. {title_str}{journal_str} https://doi.org/{doi}"

    def _parse_crossref_response(self, doi: str, data: dict) -> DOIMetadata:
        """Parse Crossref API response to DOIMetadata.

        Args:
            doi: DOI string
            data: Crossref API response JSON

        Returns:
            DOIMetadata object
        """
        message = data.get("message", {})

        # Extract authors
        authors = []
        for author in message.get("author", []):
            given = author.get("given", "")
            family = author.get("family", "")
            if given and family:
                authors.append(f"{family}, {given[0]}.")
            elif family:
                authors.append(family)

        # Extract year from published date
        year = None
        published = message.get("published-print") or message.get("published-online")
        if published and "date-parts" in published:
            date_parts = published["date-parts"][0]
            if date_parts:
                year = date_parts[0]

        # Extract other fields
        title_list = message.get("title", [])
        title = title_list[0] if title_list else None

        journal_list = message.get("container-title", [])
        journal = journal_list[0] if journal_list else None

        url = message.get("URL") or f"https://doi.org/{doi}"

        # Format citation
        citation_text = self._format_apa_citation(authors, year, title, journal, doi)

        return DOIMetadata(
            doi=doi,
            title=title,
            authors=authors,
            year=year,
            journal=journal,
            citation_text=citation_text,
            url=url,
            raw_response=message,
        )

    def resolve(self, doi: str, use_cache: bool = True) -> Optional[DOIMetadata]:
        """Resolve a single DOI to metadata.

        Args:
            doi: DOI string (e.g., "10.1038/nature12345")
            use_cache: Whether to use cached results

        Returns:
            DOIMetadata if successful, None if resolution fails
        """
        # Check cache first
        if use_cache:
            cached = self._load_from_cache(doi)
            if cached:
                return cached

        # Rate limit
        self._rate_limit_wait()

        # Query Crossref API
        try:
            url = f"{self.crossref_base}/{quote(doi)}"
            headers = {"User-Agent": self.user_agent}

            response = requests.get(url, headers=headers, timeout=self.timeout)

            if response.status_code == 200:
                data = response.json()
                metadata = self._parse_crossref_response(doi, data)

                # Cache result
                if use_cache:
                    self._save_to_cache(metadata)

                return metadata

            elif response.status_code == 404:
                print(f"⚠️  DOI not found: {doi}")
                return None

            else:
                print(
                    f"⚠️  Crossref API error for {doi}: {response.status_code} {response.text}"
                )
                return None

        except requests.exceptions.Timeout:
            print(f"⚠️  Request timeout for {doi}")
            return None

        except Exception as e:
            print(f"⚠️  Error resolving {doi}: {e}")
            return None

    def resolve_batch(
        self, dois: list[str], use_cache: bool = True, progress: bool = True
    ) -> dict[str, Optional[DOIMetadata]]:
        """Resolve multiple DOIs with progress tracking.

        Args:
            dois: List of DOI strings
            use_cache: Whether to use cached results
            progress: Whether to print progress updates

        Returns:
            Dictionary mapping DOI → DOIMetadata (or None if resolution failed)
        """
        results = {}
        total = len(dois)

        for i, doi in enumerate(dois, 1):
            if progress and i % 10 == 0:
                print(f"  Resolved {i}/{total} DOIs...")

            results[doi] = self.resolve(doi, use_cache=use_cache)

        if progress:
            successful = sum(1 for v in results.values() if v is not None)
            print(
                f"\n✅ Resolved {successful}/{total} DOIs ({successful/total*100:.1f}%)"
            )

        return results

    def clear_cache(self, doi: Optional[str] = None):
        """Clear DOI metadata cache.

        Args:
            doi: If provided, clear only this DOI. Otherwise, clear all.
        """
        if doi:
            cache_path = self._get_cache_path(doi)
            if cache_path.exists():
                cache_path.unlink()
                print(f"✅ Cleared cache for {doi}")
            else:
                print(f"ℹ️  No cache found for {doi}")
        else:
            cache_files = list(self.cache_dir.glob("*.json"))
            for cache_file in cache_files:
                cache_file.unlink()
            print(f"✅ Cleared {len(cache_files)} cached DOIs")


# Example usage
if __name__ == "__main__":
    # Test DOI resolution
    resolver = DOIResolver()

    # Test with a well-known DOI
    test_doi = "10.1038/nature12345"
    print(f"Testing DOI resolution for: {test_doi}\n")

    metadata = resolver.resolve(test_doi)

    if metadata:
        print("✅ Resolution successful!")
        print(f"Title: {metadata.title}")
        print(f"Authors: {', '.join(metadata.authors[:3])}")
        print(f"Year: {metadata.year}")
        print(f"Journal: {metadata.journal}")
        print(f"\nAPA Citation:\n{metadata.citation_text}")
        print(f"\nRoleCitation format:\n{metadata.to_citation_dict()}")
    else:
        print("❌ Resolution failed")
