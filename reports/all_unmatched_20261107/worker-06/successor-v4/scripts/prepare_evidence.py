from pathlib import Path
import json,shutil,hashlib,datetime
W=Path.cwd();R=W/'reports/all_unmatched_20261107/worker-06';S=R/'successor-v4';T=W/'.temp/residual1217-correction-v1';M=T/'independent-material'
def read(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,o):p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(o,indent=2,ensure_ascii=False)+'\n')
def cp(a,b):b.parent.mkdir(parents=True,exist_ok=True);assert not b.exists();shutil.copyfile(a,b);return {'source':str(a.relative_to(W)),'public':str(b.relative_to(W)),'sha256':sha(b)}
bindings=[]
# Bounded review receipts, searches and exact capture bytes; no fixture or owner tree copied.
for row in read(M/'preauthor-MANIFEST.json')['files'] if isinstance(read(M/'preauthor-MANIFEST.json'),dict) and 'files' in read(M/'preauthor-MANIFEST.json') else []:pass
for a in sorted(M.rglob('*')):
 if a.is_file() and a.name not in ['.DS_Store'] and not a.name.startswith('final-science'):
  bindings.append(cp(a,S/'independent-material'/a.relative_to(M)))
for name in ['author_successor.py','author_successor_v2.py','preflight.py','initial-primary-extractor-failure.json','path-correction-receipt.json','path-restoration-final.json','catalog-before.json']:
 bindings.append(cp(T/name,S/'author-provenance'/name))
bindings.append(cp(T/'author-primary-read/index.json',S/'author-provenance/primary-read-index.json'))
E=read(R/'successor-v3/evidence.json'); now=datetime.datetime.now(datetime.timezone.utc).isoformat()
def add(eid,kind,p,locator,summary,url=None,access=None):
 e={'evidence_id':eid,'kind':kind,'capture':{'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p)},'locator':locator,'supports_or_contradicts':summary,'url':url}
 if url:e['accessed_at']=access
 E['evidence'].append(e)
add('V4-E-AUTHOR-ASSESSMENT','local_validation',S/'author-assessment.json','/changed_payloads and /changed_case_indices','LLM-assisted author assessment of bounded residuals, exact changed payload hashes, genuine unknowns and source scope. Independent review is separate.')
for name,eid in [('nci-evs-C84042','V4-E-NCIT-EVS'),('ols-ncit-C84042','V4-E-NCIT-OLS')]:
 row=next(x for x in read(M/'live-specific-terms/receipts.json') if x['name']==name)
 add(eid,'ontology',S/'independent-material/live-specific-terms'/f'{name}.body','Complete exact term response','Active apple-specific NCIT:C84042 and canonical Pectin, Apple label. Generic CHEBI/CAS/formula annotations are not sample identity evidence.',row['url'],row['accessed_at'])
add('V4-E-CURRENT-DEDUP','local_validation',S/'independent-material/current-selector-dedup.json','Full selected payload bindings and catalogue search','Independent ignored-inclusive duplicate check: 985 explicitly selected payloads plus both current native catalogues. No apple-pectin/C84042 owner found in these verified scopes. Later pending heads are not accepted by this search.')
add('V4-E-FILED-ISSUE','source_snapshot',S/'triage-provenance/filed-issue-comment-attempt2.json','GitHub comment 6718920127','Filed coordinator residuals precede this correction. Historical findings and prior 12 dispositions remain unchanged.')
save(S/'author-draft/evidence.json',E);save(S/'public-copy-bindings.json',bindings)
print('Added evidence',len(E['evidence']),'public provenance copies',len(bindings))
