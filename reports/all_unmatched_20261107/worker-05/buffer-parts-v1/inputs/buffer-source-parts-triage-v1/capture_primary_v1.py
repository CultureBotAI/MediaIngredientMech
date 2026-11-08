"""2026-11-08: source captures for four already-proposed buffers; no source edits."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json,hashlib,datetime,subprocess
O=Path(__file__).resolve().parent
items=[("nbrc1221","https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1221"),("nbrc1474","https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1474"),("dsm394","https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium394.pdf"),("dsm1137","https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1137.pdf"),("jcm1061","https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1061")]
def get(x):
 name,url=x
 try:
  r=requests.get(url,timeout=40);suffix="pdf" if r.content.startswith(b"%PDF") else "html"; p=O/(name+"."+suffix);p.write_bytes(r.content)
  j={"name":name,"url":url,"final_url":r.url,"status":r.status_code,"at":datetime.datetime.now(datetime.UTC).isoformat(),"path":p.name,"sha256":hashlib.sha256(r.content).hexdigest()}
  if suffix=="pdf":
   dest=O/(name+".txt");subprocess.run(["/opt/homebrew/bin/pdftotext",str(p),str(dest)],check=True);j["text_path"]=dest.name;j["text_sha256"]=hashlib.sha256(dest.read_bytes()).hexdigest()
  return j
 except Exception as e: return {"name":name,"url":url,"error":str(e)}
with ThreadPoolExecutor(max_workers=5) as pool: rows=list(pool.map(get,items))
(O/"primary-capture-index.json").write_text(json.dumps(rows,indent=2)+"\n")
for r in rows: print(json.dumps(r))
