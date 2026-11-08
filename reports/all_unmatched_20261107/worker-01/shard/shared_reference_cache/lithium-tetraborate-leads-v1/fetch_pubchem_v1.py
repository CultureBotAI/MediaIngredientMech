"""2026-11-08 bounded PubChem lookup leads for worker01 allocation159.

Exactly four CID property requests and one exact CAS-name CID query, one attempt
each, using the free official REST API. No authentication, retries, source edits,
case decisions, chemical-form selection or mapping approval.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIELDS = "MolecularFormula,InChI,InChIKey,IUPACName"
CIDS = [15764247, 9815330, 21895667, 90478374]


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def main():
    requests = [
        {"key": f"cid-{cid}-properties", "requested_cid": cid,
         "url": f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/property/{FIELDS}/JSON"}
        for cid in CIDS
    ]
    requests.append({"key": "cas-12007-60-2-cids", "requested_cas": "12007-60-2",
                     "url": "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/12007-60-2/cids/JSON"})
    assert len(requests) == 5
    (HERE / "captures").mkdir()
    with (HERE / "requests.json").open("x") as stream:
        json.dump(requests, stream, indent=2)
        stream.write("\n")
    results = []
    for item in requests:
        receipt = {**item, "requested_at": now(), "attempt": 1}
        payload = b""
        try:
            request = urllib.request.Request(item["url"], headers={"User-Agent": "MediaIngredientMech-readonly-evidence-cache/1.0", "Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=25) as response:
                receipt.update(status=response.status, final_url=response.url, headers=dict(response.headers))
                payload = response.read(2_000_001)
                if len(payload) > 2_000_000:
                    raise ValueError("Response exceeds the bounded lookup cache")
        except urllib.error.HTTPError as exc:
            receipt.update(status=exc.code, final_url=exc.url, headers=dict(exc.headers), error=str(exc))
            payload = exc.read(2_000_000)
        except (OSError, ValueError, urllib.error.URLError) as exc:
            receipt.update(status=None, error=repr(exc))
        receipt["completed_at"] = now()
        path = HERE / "captures" / (item["key"] + ".json")
        with path.open("xb") as stream:
            stream.write(payload)
        receipt.update(capture_path=str(path.relative_to(HERE)), payload_sha256=hashlib.sha256(payload).hexdigest(), bytes=len(payload), scientific_identity_verified=False)
        with (HERE / "captures" / (item["key"] + ".http.json")).open("x") as stream:
            json.dump(receipt, stream, indent=2, sort_keys=True)
            stream.write("\n")
        results.append(receipt)
        time.sleep(0.25)
    with (HERE / "http-results.json").open("x") as stream:
        json.dump(results, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"requests": len(results), "HTTP_200": sum(row.get("status") == 200 for row in results), "failed_keys": [row["key"] for row in results if row.get("status") != 200]}))


if __name__ == "__main__":
    main()
