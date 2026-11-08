"""2026-11-08: bounded free official-source capture for existing lexical owner hints.

Input is requests-v1.json in this private cache. Output is new raw payloads and
HTTP provenance here only. No scientific decision, worker/record write or paid API.
"""

from __future__ import annotations

import concurrent.futures
import datetime
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALLOWED = {"www.ebi.ac.uk", "pubchem.ncbi.nlm.nih.gov"}


def now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def capture(item):
    assert urllib.parse.urlsplit(item["url"]).hostname in ALLOWED
    prefix = HERE / "captures" / item["key"]
    assert not prefix.with_suffix(".json").exists()
    attempts = []
    payload = b""
    for attempt in range(1, 3):
        observation = {"attempt": attempt, "requested_at": now(), "url": item["url"]}
        try:
            request = urllib.request.Request(item["url"], headers={"User-Agent": "MediaIngredientMech-readonly-evidence-cache/1.0", "Accept": "application/json"})
            with urllib.request.urlopen(request, timeout=25) as response:
                observation.update(status=response.status, final_url=response.url, headers=dict(response.headers))
                payload = response.read(2_000_001)
                if len(payload) > 2_000_000:
                    raise ValueError("Response exceeds this bounded evidence cache")
        except urllib.error.HTTPError as exc:
            observation.update(status=exc.code, final_url=exc.url, headers=dict(exc.headers), error=str(exc))
            payload = exc.read(2_000_000)
        except (OSError, ValueError, urllib.error.URLError) as exc:
            observation.update(status=None, error=repr(exc))
        observation["completed_at"] = now()
        attempts.append(observation)
        if observation.get("status") not in {None, 429, 500, 502, 503, 504} or attempt == 2:
            break
        time.sleep(1)
    path = prefix.with_suffix(".json")
    with path.open("xb") as stream:
        stream.write(payload)
    result = {**item, "capture_path": str(path.relative_to(HERE)), "payload_sha256": hashlib.sha256(payload).hexdigest(), "bytes": len(payload), "attempts": attempts, "retrieval_succeeded": attempts[-1].get("status") == 200, "semantic_content_verified": False}
    with prefix.with_suffix(".http.json").open("x") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    return result


def main():
    requests = json.loads((HERE / "requests-v1.json").read_text())
    (HERE / "captures").mkdir(exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(capture, requests))
    with (HERE / "http-results-v1.json").open("x") as stream:
        json.dump(results, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"requests": len(results), "HTTP_200": sum(row["retrieval_succeeded"] for row in results), "failures": [row["key"] for row in results if not row["retrieval_succeeded"]]}))


if __name__ == "__main__":
    main()
