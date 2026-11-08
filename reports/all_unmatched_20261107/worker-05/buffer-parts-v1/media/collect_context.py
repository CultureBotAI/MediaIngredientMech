from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,shutil,yaml,subprocess
W=Path.cwd();S=W/'.temp/w05-buffer-parts-v1';O=S/'media';C=W.parents[2];B=W/'reports/all_unmatched_20261107/worker-05';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();j=lambda p:json.loads(p.read_text())
for n in ['inputs','captures','read','proposed']: (O/n).mkdir(exist_ok=True)
PS=j(B/'tellurium-polypeptone-v1/core/proposals.json')['proposals']; selected=[p for p in PS if p['proposal_id'] in ['M1193-P-MARINE2216','M1193-P-RCM-182']];names=set();bindings=[]
for p in selected:
    f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];shutil.copy2(f,O/'inputs'/f.name);r=yaml.safe_load(f.read_text());names|={c['component_name'].lower() for c in r['components']};bindings.append(p)
owners=[]
for f in (W/'data/ingredients').rglob('*.yaml'):
    r=yaml.safe_load(f.read_text()); labels=[r.get('preferred_term',''),r.get('ontology_mapping',{}).get('ontology_label','')]+[x.get('synonym_text','') for x in r.get('synonyms',[]) if x.get('synonym_type')!='REJECTED_LABEL'];hits=names&{x.lower() for x in labels}
    if hits:
        q=O/'inputs/owners'/f.name;q.parent.mkdir(exist_ok=True);shutil.copy2(f,q);owners.append(dict(path=str(f.relative_to(W)),sha256=sha(f),capture=str(q.relative_to(O)),matches=sorted(hits),identifier=r['identifier'],ontology_mapping=r.get('ontology_mapping')))
for name,data in [('current-proposals.json',bindings),('component-owner-search.json',dict(at=datetime.now(timezone.utc).isoformat(),includes_ignored_files=True,scope='Complete2956 current ingredient YAML paths, accepted preferred/ontology/synonym strings, exact case-insensitive literal component-name comparison; parent/related searches recorded separately.',rows=owners))]:
    q=O/'inputs'/name;assert not q.exists();q.write_text(json.dumps(data,indent=2)+'\n')
for dirname in ['combined37-v3-independent-v1','w05-final-completion-findings-publication-v1','w05-review-followups-triage-v1']:
    root=C/'preflight'/dirname
    wanted={'combined37-v3-independent-v1':['finding-component-grounding-001.json','component-grounding-followup.md','component-grounding-probe.json'],'w05-final-completion-findings-publication-v1':['review-finding-index-at-read.json','component-grounding-comment.md','caption-comment.md','verified-manifest.json'],'w05-review-followups-triage-v1':['comment.md','readback-00.json','publication-00.json','verified-manifest.json']}[dirname]
    for name in wanted:
        q=S/'inputs'/dirname/name;q.parent.mkdir(exist_ok=True,parents=True);assert not q.exists();shutil.copy2(root/name,q)
print(json.dumps({'owner_candidates':len(owners),'selected_proposals':len(bindings)}))
