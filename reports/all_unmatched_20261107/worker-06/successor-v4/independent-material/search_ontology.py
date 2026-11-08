from pathlib import Path
import datetime,hashlib,json,subprocess,urllib.parse
O=Path(__file__).resolve().parent;D=O/'live-ontology';D.mkdir(exist_ok=False)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(name,x):
 with (D/name).open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
requests=[('apple-pectin-exact',{'q':'apple pectin','exact':'true','type':'class','obsoletes':'false','rows':100}),('pectin-apple-exact',{'q':'pectin (apple)','exact':'true','type':'class','obsoletes':'false','rows':100}),('apple-pectin-label-synonym',{'q':'apple pectin','queryFields':'label,synonym','type':'class','obsoletes':'false','rows':100})]
rows=[]
for name,params in requests:
 url='https://www.ebi.ac.uk/ols4/api/search?'+urllib.parse.urlencode(params);body=D/(name+'.body');headers=D/(name+'.headers')
 at=datetime.datetime.now(datetime.timezone.utc).isoformat();cmd=['curl','--fail','--location','--retry','2','--connect-timeout','15','--max-time','45','--silent','--show-error','--dump-header',str(headers),'--output',str(body),url]
 r=subprocess.run(cmd,capture_output=True,text=True);(D/(name+'.stderr')).write_text(r.stderr)
 row={'name':name,'url':url,'accessed_at':at,'completed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'command':cmd,'exit_code':r.returncode,'body_path':str(body),'body_sha256':sha(body) if body.exists() else None,'header_sha256':sha(headers) if headers.exists() else None,'stderr_sha256':sha(D/(name+'.stderr'))}
 if r.returncode==0:
  x=json.loads(body.read_text());row['numFound']=x.get('response',{}).get('numFound');row['response_documents']=x.get('response',{}).get('docs',[])
 rows.append(row)
save('queries.json',{'scope':'Bounded official OLS search at real query times. Search hits are leads, not exact-identity evidence; full term scope inspected separately. No global ontology absence claim.','queries':rows})
print(json.dumps([{'name':x['name'],'exit':x['exit_code'],'numFound':x.get('numFound'),'hits':x.get('response_documents')} for x in rows],indent=2))
