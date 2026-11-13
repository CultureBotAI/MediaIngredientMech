"""2026-11-12: bounded read-only primary ontology refresh for four owner notes.

Inputs: five exact public ChEBI/NLM URLs. Outputs: fresh response bodies and
metadata in this private note packet. No paid provider, corpus edit or approval.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
SOURCES = {
    "chebi32138": "https://www.ebi.ac.uk/chebi/backend/api/public/compound/32138/",
    "chebi17712": "https://www.ebi.ac.uk/chebi/backend/api/public/compound/17712/",
    "chebi48517": "https://www.ebi.ac.uk/chebi/backend/api/public/compound/48517/",
    "chebi22590": "https://www.ebi.ac.uk/chebi/backend/api/public/compound/22590/",
    "meshM0319657": "https://id.nlm.nih.gov/mesh/M0319657.json",
}


def fetch(item):
    key, url = item
    result = {"url": url, "started_at": datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(url, timeout=25) as response:
            body = response.read(2_000_001)
            if len(body) > 2_000_000:
                raise ValueError("Response exceeded bounded size")
            result.update(status=response.status, final_url=response.url,
                          bytes=len(body), sha256=hashlib.sha256(body).hexdigest())
        with (ROOT / (key + ".body")).open("xb") as stream:
            stream.write(body)
    except Exception as error:
        result.update(error_type=type(error).__name__, error=str(error))
    result["finished_at"] = datetime.now(timezone.utc).isoformat()
    with (ROOT / (key + ".receipt.json")).open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    return key, result


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=5) as pool:
        results = dict(pool.map(fetch, SOURCES.items()))
    with (ROOT / "PUBLIC-REFRESH.json").open("x") as stream:
        json.dump(results, stream, indent=2)
        stream.write("\n")
    print(json.dumps(results))
