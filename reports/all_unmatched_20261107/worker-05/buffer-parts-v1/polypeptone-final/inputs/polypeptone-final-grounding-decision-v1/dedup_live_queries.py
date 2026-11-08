from pathlib import Path
import json,subprocess,datetime,hashlib
D=Path(__file__).parent
queries=["repo:CultureBotAI/CultureMech is:issue M122", "repo:CultureBotAI/CultureMech is:issue \"alkaline xylan\"", "repo:CultureBotAI/CultureMech is:issue JCM130"]
rs=[]
for i,q in enumerate(queries):
 a=["gh","api","-X","GET","search/issues","-f", "q="+q,"-f","per_page=100"]
 r=subprocess.run(a,capture_output=True);p=D/f"quantity-dedup-live-{i+1}.json";p.write_bytes(r.stdout);(D/f"quantity-dedup-live-{i+1}.stderr").write_bytes(r.stderr);rs.append({"argv":a,"at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"exit":r.returncode,"response":p.name,"sha256":hashlib.sha256(r.stdout).hexdigest()})
(D/"quantity-dedup-live-receipts.json").write_text(json.dumps(rs,indent=2)+"\n")
print(json.dumps(rs))
