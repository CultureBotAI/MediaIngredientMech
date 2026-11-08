from pathlib import Path
import concurrent.futures,datetime,hashlib,json,urllib.request,urllib.parse
R=Path('reports/all_unmatched_20261107/worker-02/continuation-1201-v1/a');C=R/'captures';C.mkdir(exist_ok=True)
jobs=[
('sigma-manganese-variable','https://www.sigmaaldrich.com/US/en/product/aldrich/229784'),
('sigma-manganese-mono','https://www.sigmaaldrich.com/US/en/product/sigald/221287'),
('cytiva-product-guide','https://info.cytivalifesciences.com/rs/614-VFU-334/images/Whatman-filtration-product-guide.pdf'),
('ols-mn-parent','https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86360'),
('ols-mn-monohydrate','https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?obo_id=CHEBI:86364')]
names=['manganese sulfate hydrate','15244-36-7','Whatman grade 1 filter paper','JCM 1182 sulfuric acid solution','JCM 378 basal solution','JCM 149 standard mineral base','DSMZ 110a meat filtrate','Asahi Ebios tablets','ultrapure water','2 M sulfuric acid solution','0.1 M sulfuric acid solution','1 N sulfuric acid solution','0.01 M manganese sulfate solution','filter sterilized methanol ATCC 2883','JCM 525 chalcopyrite suspension','JCM 382 ferrous sulfate solution','JCM 414 calcium magnesium solution','MRSsi medium','JCM 1483 concentrated sulfuric acid','JCM 636 50% methanol','DSMZ 718 ferrous ammonium sulfate solution','NBRC 1627 4.98% ferrous sulfate','JCM 54 peeled cut carrot']
jobs += [(f'ols-search-{i:02}', 'https://www.ebi.ac.uk/ols4/api/search?'+urllib.parse.urlencode({'q':name,'rows':10,'exact':'true'})) for i,name in enumerate(names)]
def one(job):
 name,url=job;now=datetime.datetime.now(datetime.timezone.utc).isoformat();rec={'key':name,'url':url,'accessed_at':now}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (source review)'});res=urllib.request.urlopen(req,timeout=35);b=res.read();rec.update(status=res.status,content_type=res.headers.get('Content-Type'),final_url=res.url)
 except Exception as ex:
  rec.update(status=getattr(ex,'code',None),error=str(ex));b=ex.read() if hasattr(ex,'read') else str(ex).encode()
 out=C/(name+'.bin');out.write_bytes(b);rec.update(path=str(out.relative_to(R.parent.parent)),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b));return rec
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:rows=list(pool.map(one,jobs))
(R/'retrievals.json').write_text(json.dumps({'requests':rows,'ols_queries':names},indent=2)+'\n')
print(json.dumps([{'key':x['key'],'status':x['status'],'bytes':x['bytes']} for x in rows]))
