"""2026-11-08: capture primary recipe sources for worker-07 batch A; no maintained writes."""
import pathlib,json,re,urllib.request,hashlib,datetime,concurrent.futures,subprocess
R=pathlib.Path('reports/all_unmatched_20261107/worker-07'); Q=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
cs=json.loads((R/'parts/a-input.json').read_text())['cases']; urls={}
for i,c in enumerate(cs):
 for o in c['occurrences']:
  t=(Q/o['full_recipe_snapshot']).read_text()
  found=re.findall(r'https?://(?:www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd\?GRMD=\d+|www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet\?NO=\d+|www.atcc.org/~/media/[A-F0-9]+.ashx|www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium\d+.pdf|togomedium.org/medium/M\d+|www.ccap.ac.uk/wp-content/uploads/MR_[A-Za-z0-9_]+.pdf)',t)
  specific=[u for u in found if 'togomedium' not in u]
  for u in dict.fromkeys(specific or found): urls.setdefault(u,[]).append(i)
extra={
'https://www.sigmaaldrich.com/US/en/product/sigma/a9647':[32],
'https://www.sigmaaldrich.com/US/en/product/sigma/d1501':[56],
'https://www.fgsc.net/fgn48/Kaminskyj.htm':[63],
'https://mediadb.systemsbiology.net/defined_media/media/288/':[64],
'https://mediadb.systemsbiology.net/defined_media/media/37/':[68],
'https://mediadb.systemsbiology.net/defined_media/media/479/':[15],
'https://repository.tudelft.nl/file/File_025a63db-3c03-4a9d-b18c-d37a795e6cad':[16],
}
urls.update(extra)
def fetch(item):
 u,indices=item; slug=hashlib.sha256(u.encode()).hexdigest()[:16]; stamp=datetime.datetime.now(datetime.timezone.utc).isoformat(); entry={'url':u,'accessed_at':stamp,'indices':sorted(set(indices))}
 try:
  req=urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 (source review)'}); r=urllib.request.urlopen(req,timeout=35); b=r.read(); typ=r.headers.get('Content-Type',''); ext='pdf' if b.startswith(b'%PDF') else 'html'; p=R/'captures'/f'a-source-{slug}.{ext}'; p.write_bytes(b); entry.update(status=r.status,path=str(p.relative_to(R)),sha256=hashlib.sha256(b).hexdigest(),content_type=typ,final_url=r.url)
  if ext=='pdf':
   out=p.with_suffix('.txt'); proc=subprocess.run(['pdftotext','-layout',str(p),str(out)],capture_output=True); entry['text_path']=str(out.relative_to(R)) if out.exists() else None
 except Exception as e: entry.update(error=str(e))
 return entry
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool: out=list(pool.map(fetch,urls.items()))
(R/'parts/a-fetch-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'requests':len(out),'success':sum('path' in x for x in out),'failures':[x for x in out if 'error' in x]},indent=2))
