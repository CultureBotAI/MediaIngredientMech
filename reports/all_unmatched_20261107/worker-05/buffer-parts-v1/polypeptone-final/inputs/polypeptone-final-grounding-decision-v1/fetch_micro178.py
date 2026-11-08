from pathlib import Path
import datetime,hashlib,json,urllib.request
D=Path(__file__).parent
u="https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?iri=http%3A%2F%2Fpurl.obolibrary.org%2Fobo%2FMICRO_0000178"
r={"url":u,"started_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"method":"GET","no_authentication":True}
try:
 with urllib.request.urlopen(u,timeout=30) as x:b=x.read();r.update(status=x.status,headers=dict(x.headers),final_url=x.url)
except Exception as e:
 b=str(e).encode();r.update(error=repr(e))
p=D/"fresh-primary/micro-peptone.json";p.write_bytes(b);r.update(finished_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b),path=str(p.relative_to(D)));(D/"fresh-primary/micro-peptone.receipt.json").write_text(json.dumps(r,indent=2)+"\n");print(json.dumps(r))
