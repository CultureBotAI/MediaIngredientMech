"""Client for retrieving chemical properties from ChEBI and PubChem APIs."""

from __future__ import annotations

import json
import logging
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from urllib.parse import quote

import requests

logger = logging.getLogger(__name__)

# Cache directory for chemical properties
CACHE_DIR = Path.home() / ".cache" / "mediaingredientmech" / "chemical_properties"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

# API endpoints
CHEBI_OLS_API = "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms"
PUBCHEM_API = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound"

# Rate limiting (5 requests per second)
MIN_REQUEST_INTERVAL = 0.2
_last_request_time = 0.0


@dataclass
class ChemicalProperties:
    """Chemical structure and properties for a chemical entity."""

    molecular_formula: Optional[str] = None
    smiles: Optional[str] = None
    inchi: Optional[str] = None
    molecular_weight: Optional[float] = None
    data_source: Optional[str] = None
    retrieval_date: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert to dictionary for YAML serialization."""
        result = {}
        if self.molecular_formula:
            result["molecular_formula"] = self.molecular_formula
        if self.smiles:
            result["smiles"] = self.smiles
        if self.inchi:
            result["inchi"] = self.inchi
        if self.molecular_weight is not None:
            result["molecular_weight"] = self.molecular_weight
        if self.data_source:
            result["data_source"] = self.data_source
        if self.retrieval_date:
            result["retrieval_date"] = self.retrieval_date
        return result


class ChemicalPropertiesClient:
    """Retrieve chemical properties from ChEBI and PubChem APIs."""

    def __init__(self, cache_enabled: bool = True):
        """Initialize the client.

        Args:
            cache_enabled: Whether to use file-based caching.
        """
        self.cache_enabled = cache_enabled

    def get_properties(
        self,
        ontology_id: str,
        label: str,
        source: str,
    ) -> Optional[ChemicalProperties]:
        """Get chemical properties for an ontology term.

        Args:
            ontology_id: Ontology ID in CURIE format (e.g., CHEBI:26710).
            label: Human-readable label for the term.
            source: Ontology source (CHEBI, FOODON, etc.).

        Returns:
            ChemicalProperties if available, None otherwise.
        """
        # Only process CHEBI terms
        if source != "CHEBI":
            logger.debug("Skipping non-CHEBI term: %s (%s)", ontology_id, source)
            return None

        # Check cache first
        if self.cache_enabled:
            cached = self._get_from_cache(ontology_id)
            if cached is not None:
                return cached

        # Extract CHEBI numeric ID
        chebi_id = ontology_id.split(":")[-1]

        # Try to get properties from ChEBI OLS API
        props = self._get_chebi_properties(chebi_id, ontology_id)

        # If we have ChEBI ID, try to enrich with PubChem SMILES/InChI
        if props and chebi_id:
            pubchem_props = self._get_pubchem_properties(chebi_id)
            if pubchem_props:
                # Merge PubChem data
                if pubchem_props.smiles and not props.smiles:
                    props.smiles = pubchem_props.smiles
                if pubchem_props.inchi and not props.inchi:
                    props.inchi = pubchem_props.inchi
                if pubchem_props.molecular_weight and not props.molecular_weight:
                    props.molecular_weight = pubchem_props.molecular_weight
                # Update source to indicate both
                if props.data_source == "ChEBI":
                    props.data_source = "ChEBI+PubChem"

        # Cache the result
        if props and self.cache_enabled:
            self._save_to_cache(ontology_id, props)

        return props

    def _get_chebi_properties(
        self, chebi_id: str, ontology_id: str
    ) -> Optional[ChemicalProperties]:
        """Retrieve properties from ChEBI OLS API v4.

        Args:
            chebi_id: Numeric ChEBI ID (e.g., 26710).
            ontology_id: Full ontology ID (e.g., CHEBI:26710).

        Returns:
            ChemicalProperties with formula and molecular weight if available.
        """
        try:
            # Construct OLS v4 API URL
            encoded_iri = quote(
                f"http://purl.obolibrary.org/obo/CHEBI_{chebi_id}", safe=""
            )
            url = f"{CHEBI_OLS_API}/{encoded_iri}"

            # Rate limiting
            self._rate_limit()

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            # Extract annotation fields
            annotation = data.get("annotation", {})
            formula = None
            molecular_weight = None

            # Look for formula in annotation
            if "formula" in annotation:
                formula_list = annotation["formula"]
                if formula_list and len(formula_list) > 0:
                    formula = formula_list[0]

            # Look for mass/molecular weight
            if "mass" in annotation:
                mass_list = annotation["mass"]
                if mass_list and len(mass_list) > 0:
                    try:
                        molecular_weight = float(mass_list[0])
                    except (ValueError, TypeError):
                        pass

            if formula or molecular_weight:
                return ChemicalProperties(
                    molecular_formula=formula,
                    molecular_weight=molecular_weight,
                    data_source="ChEBI",
                    retrieval_date=datetime.now(timezone.utc).isoformat(),
                )

            logger.debug("No chemical properties found in ChEBI for %s", ontology_id)
            return None

        except requests.RequestException as e:
            logger.warning("Failed to fetch ChEBI properties for %s: %s", ontology_id, e)
            return None
        except (KeyError, ValueError, TypeError) as e:
            logger.warning("Error parsing ChEBI response for %s: %s", ontology_id, e)
            return None

    def _get_pubchem_properties(self, chebi_id: str) -> Optional[ChemicalProperties]:
        """Retrieve SMILES and InChI from PubChem using ChEBI cross-reference.

        Args:
            chebi_id: Numeric ChEBI ID.

        Returns:
            ChemicalProperties with SMILES and InChI if available.
        """
        try:
            # Search PubChem by ChEBI ID
            search_url = f"{PUBCHEM_API}/name/CHEBI:{chebi_id}/cids/JSON"

            # Rate limiting
            self._rate_limit()

            search_response = requests.get(search_url, timeout=10)

            # PubChem returns 404 if not found - this is normal
            if search_response.status_code == 404:
                logger.debug("No PubChem entry found for CHEBI:%s", chebi_id)
                return None

            search_response.raise_for_status()
            cids_data = search_response.json()

            cids = cids_data.get("IdentifierList", {}).get("CID", [])
            if not cids:
                logger.debug("No PubChem CIDs found for CHEBI:%s", chebi_id)
                return None

            # Use the first CID
            cid = cids[0]

            # Get properties for this CID
            props_url = (
                f"{PUBCHEM_API}/cid/{cid}/property/"
                f"CanonicalSMILES,InChI,MolecularWeight/JSON"
            )

            # Rate limiting
            self._rate_limit()

            props_response = requests.get(props_url, timeout=10)
            props_response.raise_for_status()
            props_data = props_response.json()

            properties = props_data.get("PropertyTable", {}).get("Properties", [])
            if not properties:
                return None

            prop = properties[0]
            smiles = prop.get("CanonicalSMILES")
            inchi = prop.get("InChI")
            mol_weight = prop.get("MolecularWeight")

            if smiles or inchi:
                return ChemicalProperties(
                    smiles=smiles,
                    inchi=inchi,
                    molecular_weight=float(mol_weight) if mol_weight else None,
                    data_source="PubChem",
                    retrieval_date=datetime.now(timezone.utc).isoformat(),
                )

            return None

        except requests.RequestException as e:
            # Don't log 404s as warnings - they're expected for many ChEBI terms
            if not (hasattr(e, "response") and e.response.status_code == 404):
                logger.debug("Failed to fetch PubChem properties for CHEBI:%s: %s", chebi_id, e)
            return None
        except (KeyError, ValueError, TypeError) as e:
            logger.warning("Error parsing PubChem response for CHEBI:%s: %s", chebi_id, e)
            return None

    def _rate_limit(self):
        """Enforce rate limiting (5 requests per second)."""
        global _last_request_time
        now = time.time()
        elapsed = now - _last_request_time
        if elapsed < MIN_REQUEST_INTERVAL:
            time.sleep(MIN_REQUEST_INTERVAL - elapsed)
        _last_request_time = time.time()

    def _get_cache_path(self, ontology_id: str) -> Path:
        """Get cache file path for an ontology ID."""
        # Use sanitized ontology ID as filename
        safe_id = ontology_id.replace(":", "_")
        return CACHE_DIR / f"{safe_id}.json"

    def _get_from_cache(self, ontology_id: str) -> Optional[ChemicalProperties]:
        """Retrieve properties from cache if available."""
        cache_path = self._get_cache_path(ontology_id)
        if not cache_path.exists():
            return None

        try:
            with open(cache_path) as f:
                data = json.load(f)
            return ChemicalProperties(
                molecular_formula=data.get("molecular_formula"),
                smiles=data.get("smiles"),
                inchi=data.get("inchi"),
                molecular_weight=data.get("molecular_weight"),
                data_source=data.get("data_source"),
                retrieval_date=data.get("retrieval_date"),
            )
        except (OSError, json.JSONDecodeError) as e:
            logger.warning("Failed to read cache for %s: %s", ontology_id, e)
            return None

    def _save_to_cache(self, ontology_id: str, props: ChemicalProperties):
        """Save properties to cache."""
        cache_path = self._get_cache_path(ontology_id)
        try:
            with open(cache_path, "w") as f:
                json.dump(props.to_dict(), f, indent=2)
        except OSError as e:
            logger.warning("Failed to save cache for %s: %s", ontology_id, e)
