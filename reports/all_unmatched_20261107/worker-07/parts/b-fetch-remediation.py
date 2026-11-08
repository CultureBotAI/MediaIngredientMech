import json,pathlib,subprocess,hashlib,datetime,concurrent.futures,urllib.parse
R=pathlib.Path(__file__).resolve().parents[1]
targets=[]
for i,ns in [(108,['M2256']),(109,['M3175']),(111,['M3057','M3221']),(128,['M2577'])]:
 for n in ns:targets.append((i,n,'https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id='+n))
targets += [(118,'JCM825','https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=825'),(118,'MediaDive4784','https://mediadive.dsmz.de/rest/solution/4784')]
pmids={90:['15459799','14673546','15781419','12603321','16698295','17234153'],116:['13611202','21513516','11135197','233720','7961411']}
for i,ids in pmids.items():
 for p in ids:targets.append((i,'PMID'+p,'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query='+urllib.parse.quote('EXT_ID:'+p+' AND SRC:MED')+'&format=json&resultType=core'))
for i,doi in [(90,'10.1007/s00253-004-1743-y'),(90,'10.1007/s00253-003-1499-9'),(90,'10.1016/j.ymben.2004.10.004'),(90,'10.1046/j.1432-1033.2003.03448.x'),(116,'10.1099/00221287-19-3-592'),(116,'10.1186/1475-2859-10-25'),(116,'10.1128/jb.130.2.805-811.1977'),(116,'10.1128/jb.176.21.6599-6605.1994')]:targets.append((i,'DOI'+doi,'https://doi.org/'+doi))
targets += [(116,'PMC3107774','https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3107774/fullTextXML'),(116,'PMC235284','https://www.ebi.ac.uk/europepmc/webservices/rest/PMC235284/fullTextXML'),(116,'PMC197015','https://www.ebi.ac.uk/europepmc/webservices/rest/PMC197015/fullTextXML')]
def fetch(t):
 i,fam,url=t;p=R/'captures'/('b-remediation-'+hashlib.sha256(url.encode()).hexdigest()[:16]+'.body');at=datetime.datetime.now(datetime.timezone.utc).isoformat();q=subprocess.run(['curl','-L','-sS','--connect-timeout','5','--max-time','18','-o',str(p),'-w','%{http_code}\n%{url_effective}\n%{content_type}',url],capture_output=True);s=q.stdout.decode(errors='replace').splitlines();e={'case_index':i,'family':fam,'url':url,'accessed_at':at,'transport_success':q.returncode==0,'http_status':s[0] if s else None,'final_url':s[1] if len(s)>1 else None,'content_type':s[2] if len(s)>2 else None,'error':q.stderr.decode(errors='replace')}
 if p.exists():
  ext='.pdf' if p.read_bytes().startswith(b'%PDF') else '.json' if 'json' in str(e['content_type']) else '.xml' if 'xml' in str(e['content_type']) else '.html';dest=p.with_suffix(ext);p.rename(dest);e.update(path=dest.relative_to(R).as_posix(),sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),bytes=dest.stat().st_size)
 return e
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:out=list(ex.map(fetch,targets))
(R/'parts/b-remediation-retrievals.json').write_text(json.dumps(out,indent=2))
print([(x['case_index'],x['family'],x['http_status'],x.get('bytes')) for x in out])
