import pathlib,json,subprocess,hashlib
from lxml import html
W=pathlib.Path.cwd();C=W.parents[2];O=W/'.temp/nine-scope-candidates-independent-v1/skeptical';a=json.loads((C/'assignments/w01-nine-scope-candidates-independent-v1.json').read_text());sources={}
ids=['BIO-PRIMARY-supp-8bb907b6a644b834','MATERIALS-CAP-5c0a089f5206be3d','MATERIALS-C1193-JCM117','ROOT-jcm-266','R1193-FLUID-md-161','R1193-FLUID-md-212','b-primary-b80f9ee369','b-targeted-b087f0859f30','M1193-DIRECT-110','sv1-bio-primary-db052c139ff2c422b6a9','sv1-bio-primary-66b327a7bae22ac4602a']
for c in a['candidates']:
 for o in c['origins']:
  for e in o.get('evidence',[]):
   if e['evidence_id'] not in ids or e['evidence_id'] in sources:continue
   p=pathlib.Path(e['guarded_capture_path']);b=p.read_bytes()
   if b.startswith(b'%PDF'): text=subprocess.check_output(['pdftotext','-layout',str(p),'-']).decode();method='pdftotext -layout'
   else:
    text=b.decode(errors='replace');method='utf8'
    if '<html' in text.lower() or '<!doctype' in text.lower(): text=html.fromstring(text).text_content();method='lxml text_content'
   dest=O/(e['evidence_id']+'.txt');dest.write_text(text);sources[e['evidence_id']]={'path':str(p),'sha256':hashlib.sha256(b).hexdigest(),'url':e.get('url'),'extraction':method,'derivative':str(dest),'derivative_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
(O/'source-read-index-v1.json').write_text(json.dumps(sources,indent=2)+'\n')
for k in ids:
 t=(O/(k+'.txt')).read_text(); print('\n===',k,'===')
 if k=='sv1-bio-primary-db052c139ff2c422b6a9':
  pages=t.split('\f'); print('\n'.join('PAGE '+str(i+1)+'\n'+x for i,x in enumerate(pages) if ('Phytone' in x and 'Soytone' in x and len(x)<14000)))
 elif k=='b-targeted-b087f0859f30':print(t.split('\f')[0])
 else: print(t)
