from pathlib import Path
from urllib.request import Request,urlopen
from datetime import datetime,timezone
import hashlib,json
R=Path(__file__).parent
urls={"atcc1252":"https://www.atcc.org/~/media/CCB197296D624B1DA0BBFA3C2EB8632B.ashx","togo_m2613":"https://togomedium.org/medium/M2613"}
rows=[]
for name,url in urls.items():
 row={"name":name,"url":url,"started_at":datetime.now(timezone.utc).isoformat()}
 try:
  with urlopen(Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=45) as x:
   data=x.read();(R/(name+".body")).write_bytes(data);row.update(status=x.status,final_url=x.url,headers=dict(x.headers),sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),capture=name+".body")
 except Exception as exc:row.update(error=str(exc))
 row["finished_at"]=datetime.now(timezone.utc).isoformat();rows.append(row)
(R/"primary-fetch-results.json").write_text(json.dumps(rows,indent=2)+"\n")
print(json.dumps(rows,indent=2))
