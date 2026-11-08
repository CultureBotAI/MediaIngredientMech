"""2026-11-08 worker02: capture public primary follow-up sources; no decisions.

Inputs are the explicit URLs below. Outputs are response bytes and timestamped
HTTP metadata inside this worker's evidence tree. Errors are not source evidence.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
from concurrent.futures import ThreadPoolExecutor

ROOT = Path(__file__).resolve().parent / "metatraits-primary"
URLS = {
    "bacdive-chaninin.html": "https://bacdive.dsmz.de/strain/16463",
    "jcm-17027.html": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17027",
    "jcm-reference-8326.html": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_ref?REF=8326",
    "bacdive-butamine.html": "https://bacdive.dsmz.de/strain/168456",
    "phragmitis-original.html": "https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.003763",
    "mesh-ocarbamylserine.json": "https://id.nlm.nih.gov/mesh/C000366.json",
    "congocidine-pubmed.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=19389628&retmode=xml",
    "chainin-pubmed.xml": "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=5036646&retmode=xml",
    "ocarbamyl-d-serine.pdf": "https://www.jstage.jst.go.jp/article/antibiotics1968/21/3/21_3_170/_pdf",
    "taro-butamine.html": "https://www.taro.com/node/352",
}

def fetch(item):
    filename, url = item
    started = datetime.now(timezone.utc).isoformat()
    result = subprocess.run([
        "curl", "--location", "--retry", "2", "--connect-timeout", "15",
        "--max-time", "45", "--silent", "--show-error",
        "--output", str(ROOT / filename), "--write-out", "%{http_code}", url,
    ], capture_output=True, text=True)
    path = ROOT / filename
    return {
        "filename": filename, "url": url, "started_at": started,
        "accessed_at": datetime.now(timezone.utc).isoformat(),
        "curl_exit_code": result.returncode, "http_status": result.stdout,
        "stderr": result.stderr,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.exists() else None,
        "bytes": path.stat().st_size if path.exists() else 0,
    }

if __name__ == "__main__":
    ROOT.mkdir(exist_ok=True)
    with ThreadPoolExecutor(max_workers=3) as pool:
        observations = list(pool.map(fetch, URLS.items()))
    (ROOT / "retrieval-log.json").write_text(json.dumps(observations, indent=2) + "\n")
    print(json.dumps(observations, indent=2))
