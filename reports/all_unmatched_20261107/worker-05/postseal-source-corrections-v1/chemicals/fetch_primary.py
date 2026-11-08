from pathlib import Path
import requests, hashlib, json, datetime, concurrent.futures, re, html
OUT=Path(__file__).parent/'captures'
URLS={
 'wallace-2003-full':'https://www.microbiologyresearch.org/deliver/fulltext/ijsem/53/4/ijs530965.html?itemId=/content/journal/ijsem/10.1099/ijs.0.02110-0&mimeType=html&fmt=ahah',
 'bergey-eubacterium':'https://onlinelibrary.wiley.com/doi/full/10.1002/9781118960608.gbm00629',
 'bergey-treponema':'https://onlinelibrary.wiley.com/doi/full/10.1002/9781118960608.gbm01249',
}
def fetch(item):
 name,url=item
 meta={'url':url,'accessed_at':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=requests.get(url,timeout=40)
  p=OUT/(name+'.body');p.write_bytes(r.content)
  meta.update(status_code=r.status_code,final_url=r.url,sha256=hashlib.sha256(r.content).hexdigest(),bytes=len(r.content),content_type=r.headers.get('content-type'),capture_file=p.name)
  (OUT/(name+'.txt')).write_text(html.unescape(re.sub('<[^>]+>',' ',r.text)))
 except Exception as e:meta['retrieval_error']=str(e)
 (OUT/(name+'.receipt.json')).write_text(json.dumps(meta,indent=2)+'\n')
 return meta
if __name__=='__main__':
 OUT.mkdir(exist_ok=True)
 for m in concurrent.futures.ThreadPoolExecutor(max_workers=3).map(fetch,URLS.items()):print(json.dumps(m))
