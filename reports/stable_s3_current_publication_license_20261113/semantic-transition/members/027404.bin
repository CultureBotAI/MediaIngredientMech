"""2026-11-12: bounded free primary-source captures for issue1397.

Inputs: exact existing chromium capture, PubChem endpoints, the already cited
primary phosphite paper and current issue1121. Outputs: raw immutable responses,
URLs/status/date/hashes and original-copy provenance. No decisions or data edits.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import time

C = Path(__file__).resolve().parents[1]
M = C.parents[1]
OUT = C / 'preflight/four-cas-primary-captures-v1'
sha = lambda raw: hashlib.sha256(raw).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat()
OUT.mkdir()
requests = []
for name, cas in [('kh2po3','13977-65-6'), ('tapso','68399-81-5'), ('ticl3','7705-07-9')]:
    requests.append((name+'-properties', 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+cas+'/property/Title,MolecularFormula,MolecularWeight,InChI,InChIKey,IUPACName/JSON'))
    requests.append((name+'-synonyms', 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/'+cas+'/synonyms/JSON'))
requests.append(('kh2po3-primary-paper', 'https://www.ebi.ac.uk/europepmc/webservices/rest/PMC7346359/fullTextXML'))
def fetch(pair):
    name,url = pair
    command = ['curl','--silent','--show-error','--location','--proto','=https','--connect-timeout','10','--max-time','40',
               '--dump-header',str(OUT/(name+'.headers')),'--output',str(OUT/(name+'.raw')),
               '--write-out','%{http_code}\n%{url_effective}\n',url]
    start = now(); process = subprocess.run(command, capture_output=True, timeout=45)
    with (OUT/(name+'.stderr')).open('xb') as stream: stream.write(process.stderr)
    body = OUT/(name+'.raw'); raw = body.read_bytes() if body.exists() else b''
    time.sleep(0.5)
    return {'name':name,'kind':'primary_http_response','url':url,'started_at':start,'finished_at':now(),
            'argv':command,'exit_code':process.returncode,'http_result':process.stdout.decode(),
            'path':str(body),'sha256':sha(raw),'bytes':len(raw),'scientific_approval':False}
result = {'at':now(),'actor':'/root','purpose':'Issue1397 bounded raw evidence acquisition, no paid provider',
          'state':'INCOMPLETE','responses':[],'copies':[],'scientific_approval_added':False}
with (OUT/'RESULT.json').open('x') as receipt:
    try:
        with ThreadPoolExecutor(max_workers=2) as pool: result['responses'] = list(pool.map(fetch, requests))
        for number,endpoint in [(1121,'issues/1121'),(11210,'issues/1121/comments?per_page=100'),(1397,'issues/1397')]:
            argv=['gh','api','repos/CultureBotAI/MediaIngredientMech/'+endpoint]
            process=subprocess.run(argv,capture_output=True,timeout=45)
            name='github-'+str(number)
            with (OUT/(name+'.json')).open('xb') as stream:stream.write(process.stdout)
            with (OUT/(name+'.stderr')).open('xb') as stream:stream.write(process.stderr)
            result['responses'].append({'name':name,'kind':'current_governance_response','at':now(),'argv':argv,
                'exit_code':process.returncode,'path':str(OUT/(name+'.json')),'sha256':sha(process.stdout),'bytes':len(process.stdout)})
        original=M/'output/approved-plan-20261101T031134Z/step7d-execution-20261103/science-a/captures'
        for name in ['pubchem-cas-7788-99-0.json','pubchem-cas-7788-99-0.receipt.json']:
            path=original/name;raw=path.read_bytes();dest=OUT/('historical-'+name)
            with dest.open('xb') as stream:stream.write(raw)
            assert path.read_bytes()==raw
            result['copies'].append({'original_path':str(path),'copied_path':str(dest),'sha256':sha(raw),'bytes':len(raw),
                                     'acquisition':'Original historical acquisition retained; copied now without authority upgrade.'})
        result['state']='ACQUISITION_FINISHED_REVIEW_HTTP_RESULTS_AND_CONTENT'
    except BaseException as error:
        result.update(state='FAILED_PRESERVE_ALL_OUTPUTS',error=repr(error));raise
    finally:
        result['finished_at']=now();json.dump(result,receipt,indent=2);receipt.write('\n')
print(json.dumps({'path':str(OUT/'RESULT.json'),'sha256':sha((OUT/'RESULT.json').read_bytes()),
                  'state':result['state'],'responses':[{'name':x['name'],'exit_code':x['exit_code'],'bytes':x['bytes'],'http_result':x.get('http_result')} for x in result['responses']]}))
