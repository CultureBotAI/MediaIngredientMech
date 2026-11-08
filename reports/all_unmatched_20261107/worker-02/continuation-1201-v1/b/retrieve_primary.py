import concurrent.futures,datetime,hashlib,json,urllib.request,urllib.parse
from pathlib import Path
B=Path(__file__).resolve().parent; urls={
'bd-oadc':'https://www.bd.com/en-ca/products-and-solutions/products/product-page.212240',
'bd-manual':'https://www.cmp-micro.com/ch/wp-content/uploads/BD_EN_Difco_and_BBL_Manual_web.pdf',
'chromium-hydrate':'https://www.sigmaaldrich.com/US/en/product/aldrich/342432',
'larch':'https://www.sigmaaldrich.com/US/en/product/sigma/10830',
'fe-ammonium-edta':'https://www.canada.ca/en/environment-climate-change/services/evaluating-existing-substances/screening-assessment-edta-salts.html',
'noah-fe-edta':'https://store.noahchemicals.com/products/inorganics/v16122-ammonium-iron-iii-edta-99-pure--80-mesh-nh4fec10h16n2o8',
'verduyn':'https://repository.tudelft.nl/file/File_025a63db-3c03-4a9d-b18c-d37a795e6cad',
'flikweert':'https://repository.tudelft.nl/file/File_980a303e-e5c4-40e9-ae2c-d1efee438339?preview=1',
'jcm997':'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=997',
'jcm1137':'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1137',
'jcm431':'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=431'}
for cid in ['50732','53471','53438','75422','27569','39033','86156','30729']:
 urls['chebi-'+cid]='https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms?iri='+urllib.parse.quote('http://purl.obolibrary.org/obo/CHEBI_'+cid,safe='')
for q in ['ferric ammonium EDTA','21265-50-9','15244-38-9','iron(III) sulfate hexahydrate','adenine sulfate','larch arabinogalactan','resazurin sodium']:
 urls['ols-'+hashlib.sha256(q.encode()).hexdigest()[:10]]='https://www.ebi.ac.uk/ols4/api/search?q='+urllib.parse.quote(q)+'&rows=30'
def get(pair):
 name,url=pair;r={'name':name,'url':url,'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  req=urllib.request.Request(url,headers={'User-Agent':'MIM-source-review/1.0'})
  with urllib.request.urlopen(req,timeout=35) as f:b=f.read();r.update(status=f.status,final_url=f.url,content_type=f.headers.get('Content-Type',''))
  p=B/'captures'/('new-'+name+'.bin');p.write_bytes(b);r.update(path=str(p),sha256=hashlib.sha256(b).hexdigest(),bytes=len(b))
 except Exception as e:r['error']=repr(e)
 return r
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 rs=list(ex.map(get,urls.items()))
(B/'retrievals.json').write_text(json.dumps(rs,indent=2)+'\n');print(json.dumps([{k:v for k,v in r.items() if k in ['name','status','error','bytes','content_type']} for r in rs],indent=2))
