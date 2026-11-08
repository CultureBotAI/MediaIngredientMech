from pathlib import Path
import datetime,hashlib,json,re,subprocess,shutil
M=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech');C=M/'.temp/all-unmatched-20261107';D=C/'preflight/polypeptone-final-grounding-decision-v1';W5=C/'workers/w05/worktree';W6=C/'workers/w06/worktree';A5=W5/'reports/all_unmatched_20261107/worker-05';A6=W6/'reports/all_unmatched_20261107/worker-06';S=A5/'tellurium-polypeptone-v1/polypeptone';T=M/'.temp/kgm-unmapped-20261107/worktree'
def sha(b):return hashlib.sha256(b).hexdigest()
def put(p,x):
 p=D/p;p.parent.mkdir(parents=True,exist_ok=True)
 if p.exists():raise RuntimeError('exclusive output exists: '+str(p))
 p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
def git(root,*a):return subprocess.check_output(['git','-C',str(root),*a])
inputs=[]
def capture(p,dest=None,root=None,head=None):
 b=p.read_bytes();r={'path':str(p),'sha256':sha(b),'bytes':len(b)}
 if root:
  rel=p.relative_to(root).as_posix();g=git(root,'show',f'{head}:{rel}');assert g==b;r.update(git_root=str(root),git_revision=head,git_path=rel,git_blob_matches=True)
 if dest:
  out=D/dest;out.parent.mkdir(parents=True,exist_ok=True);assert not out.exists();out.write_bytes(b);r['capture']=dest
 inputs.append(r);return r
h5=git(W5,'rev-parse','HEAD').decode().strip();h6=git(W6,'rev-parse','HEAD').decode().strip()
assert h5=='0bac12cabfd1f67f212631d8eef9aa46379f6b41';assert h6=='0d7fde51fb3109b10424dd3bcf4091c05aa900e7'
for n,h in [(5,h5),(6,h6)]:assert (D/f'remote-w0{n}.txt').read_text().split()[0]==h
p5s=json.loads((S.parent/'core/proposals.json').read_text())['proposals'];p5=next(x for x in p5s if x['proposal_id']=='W05-FINAL-MAT-030')
p6s=json.loads((A6/'successor-v5/proposals.json').read_text())['proposals'];p6=next(x for x in p6s if x['proposal_id']=='A-P-POLYPEPTONE-BOUNDARY')
for n,p,a,w,h in [(5,p5,A5,W5,h5),(6,p6,A6,W6,h6)]:
 put(f'snapshot/w0{n}-selected-proposal.json',p);assert sha((a/p['after_capture']['path']).read_bytes())==p['after_capture']['sha256'];capture(a/p['after_capture']['path'],f'snapshot/w0{n}-Polypeptone.yaml',w,h)
 assert p['before_sha256']=='5ecabcf8a37d4c2218e12fb3112f17b79d103abfa5f0a6a64322d7bf19c56baa'
 for k in ['decisions','evidence','proposals']:
  f=S.parent/'core'/f'{k}.json' if n==5 else A6/'successor-v5'/f'{k}.json';capture(f,root=w,head=h)
 for k in ['decisions','evidence']:
  f=S.parent/'core'/f'{k}.json' if n==5 else A6/'successor-v5'/f'{k}.json';obj=json.loads(f.read_text());items=obj[k];ids=set(p['case_ids'] if k=='decisions' else p['evidence_ids']);key='case_id' if k=='decisions' else 'evidence_id';selected=[x for x in items if x[key] in ids];assert len(selected)==len(ids);put(f'snapshot/w0{n}-selected-{k}.json',selected)
capture(A6/'successor-v5/selection.json','snapshot/w06-selection.json',W6,h6)
for f in ['README.md','selected-origin-bindings.json','MANIFEST.json','review/main-review.json']:
 capture(S.parent/f,'snapshot/w05-'+f.replace('/','-'),W5,h5)
for f in ['findings.json','source-assessment.json','conditional-grounding-matrix.json','source-read-ledger.json','context-ledger-v2.json','input/complete-150-context-recipes.json','read/dedup-search.json']:
 capture(S/f,root=W5,head=h5)
for f in ['foodon.json','micro-polypeptone.json','micro-polypeptone-parents.json','mediadive442.json','mediadive2060.json','jcm181.html','jcm130.html','togo-gmdb-retry-M122.json']:
 capture(S/'captures'/f,'cached-primary/'+f,W5,h5);capture(S/'captures'/(f+'.receipt.json'),'cached-primary/'+f+'.receipt.json',W5,h5)
for f in ['thermo.pdf','wako-2001.pdf','wako-2002.pdf','nihon-manufacturing-2007.pdf','wako.pdf']:
 capture(S/'captures'/f,root=W5,head=h5);capture(S/'captures'/(f+'.receipt.json'),'cached-primary/'+f+'.receipt.json',W5,h5)
for f in ['AGENTS.md','MAPPING_SEMANTICS.md','.claude/skills/review-yaml-record/SKILL.md','docs/record-reviews.md']:
 capture(M/f,'contract/'+f.replace('/','-'))
base=capture(T/'data/ingredients/mapped/Polypeptone.yaml','snapshot/authentic-before-Polypeptone.yaml',T,git(T,'rev-parse','HEAD').decode().strip());assert base['sha256']==p5['before_sha256']
recipes=json.loads((S/'input/complete-150-context-recipes.json').read_text())['complete_recipes'];rec=recipes['bacterial/TOGO_M122_Alkaline_Xylan_Medium.yaml'];put('snapshot/frozen-CultureMech007758.json',rec)
current=Path(rec['source_path']);now={'path':str(current),'exists':current.is_file(),'frozen_sha256':rec['sha256']}
if current.is_file():now.update(sha256=sha(current.read_bytes()),matches_frozen=sha(current.read_bytes())==rec['sha256']);capture(current,'snapshot/current-CultureMech007758.yaml')
put('quantity-current-source-comparison.json',now)
q=json.loads((S/'findings.json').read_text())['findings'];q=next(x for x in q if x['finding_id']=='W05-POLY-SOURCE-001');put('quantity-original-finding.json',q)
# bounded saved issue-body search; no Gitignore filtering
rx=re.compile(r'(?i)(?:JCM[ _-]*(?:medium[ _-]*)?130\b|TOGO[ _-]*M122\b|Alkaline[ _-]+Xylan)');dedup=[]
for f in ['root-integration-findings-v1/issues-for-w06-review-0628.json','root-integration-findings-v1/live-issues-0638-v1.json','remote-audit-20261108T0533-v1/all-issues.stdout']:
 p=C/'preflight'/f;b=p.read_bytes();dedup.append({'path':str(p),'sha256':sha(b),'bytes':len(b),'regex':rx.pattern,'hits':[m.group() for m in rx.finditer(b.decode())]})
put('quantity-saved-dedup.json',{'ignored_files_included':True,'method':'Read the three exact saved issue inventories explicitly, plus full fresh1202/118/150/408 and indexed searches; not universal all-comment search','inventories':dedup})
put('source-bindings.json',{'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'author':'/root/next23_context','scope':'Proposed scientific grounding decision preflight; not independent final combined-owner approval','heads':{'w05':h5,'w06':h6},'inputs':inputs,'selected_proposals':{'w05':p5,'w06':p6},'all_input_bytes_rechecked':all(sha(Path(x['path']).read_bytes())==x['sha256'] for x in inputs),'heads_unchanged':git(W5,'rev-parse','HEAD').decode().strip()==h5 and git(W6,'rev-parse','HEAD').decode().strip()==h6})
print(json.dumps({'inputs':len(inputs),'source_bindings_sha256':sha((D/'source-bindings.json').read_bytes()),'current_recipe':now},indent=2))
