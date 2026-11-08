"""2026-11-08: primary_b read-only primary evidence capture for frozen w07 subset.
Inputs: exact b-input.json and frozen CultureMech recipes. Output: b-* captures.
No maintained data edits. Network errors are recorded rather than treated as evidence.
"""
import json, pathlib, re, datetime, hashlib, urllib.request, concurrent.futures, subprocess
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
QUEUE=pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
cases=json.loads((ROOT/'parts/b-input.json').read_text())['cases']
requests={}
contexts=[]
def add(url,cid):
    requests.setdefault(url,[])
    if cid not in requests[url]: requests[url].append(cid)
for index,case in enumerate(cases,70):
    context={'index':index,'case_id':case['case_id'],'label':case['source_label'],'occurrences':[]}
    for occurrence in case['occurrences']:
        path=QUEUE/occurrence['full_recipe_snapshot']; raw=path.read_bytes(); doc=yaml.safe_load(raw)
        context['occurrences'].append({'source_file':occurrence['full_recipe_snapshot'],'sha256':hashlib.sha256(raw).hexdigest(),'raw_component':occurrence['raw_component'],'complete_recipe':doc})
        urls=re.findall(r'https?://[^\s<>\]\)]+',str(doc.get('notes','')))
        urls += [s.get('url','') for s in doc.get('sources',[])]
        urls += [s.get('reference','') for s in doc.get('references',[])]
        for url in urls:
            if 'togomedium.org/medium/' in url:
                mid=re.search(r'/medium/(M\d+)',url)
                if mid:add('https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id='+mid[1],case['case_id'])
            elif ('jcm.riken.jp/cgi-bin/' in url or 'DSMZ_Medium' in url or '/MR_' in url or 'mediadive.dsmz.de/rest/' in url or 'sagdb.uni-goettingen.de/culture_media/' in url or 'utex.org/products/' in url):
                add(url.replace(' ','%20').replace('http://sagdb','https://sagdb'),case['case_id'])
        for ident in occurrence.get('source_identifiers',[]):
            if ident['value'].startswith('mediadive.compound:'):
                add('https://mediadive.dsmz.de/rest/compound/'+ident['value'].split(':')[1],case['case_id'])
    contexts.append(context)
(ROOT/'parts/b-contexts.json').write_text(json.dumps(contexts,indent=2,ensure_ascii=False)+'\n')
def fetch(item):
    url,cids=item; timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(); key=hashlib.sha256(url.encode()).hexdigest()[:16]
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 scientific-source-review/1.0'})
        with urllib.request.urlopen(req,timeout=40) as response:
            content=response.read(); mime=response.headers.get('Content-Type',''); final=response.url
        ext='pdf' if content.startswith(b'%PDF') else 'json' if content.lstrip()[:1] in (b'{',b'[') else 'html'
        rel='captures/b-primary-'+key+'.'+ext; (ROOT/rel).write_bytes(content)
        result={'url':url,'final_url':final,'accessed_at':timestamp,'case_ids':cids,'path':rel,'sha256':hashlib.sha256(content).hexdigest(),'content_type':mime,'bytes':len(content),'success':True}
        if ext=='pdf':
            txt=ROOT/rel.replace('.pdf','.txt')
            proc=subprocess.run(['pdftotext','-layout',str(ROOT/rel),str(txt)],capture_output=True,text=True)
            result['text_path']=str(txt.relative_to(ROOT));result['pdftotext_returncode']=proc.returncode
        return result
    except Exception as exc:return {'url':url,'accessed_at':timestamp,'case_ids':cids,'success':False,'error':str(exc)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
    results=list(pool.map(fetch,requests.items()))
(ROOT/'parts/b-retrievals.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'requested':len(results),'success':sum(r['success'] for r in results),'failed':[r['url'] for r in results if not r['success']]}))
