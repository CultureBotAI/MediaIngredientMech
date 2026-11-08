"""Prepare explicit shared-owner successors against original before bytes.

Original published payloads and new author fragments remain immutable inputs.
Exact compositions and every affected case backlink require independent review.
"""
from copy import deepcopy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys
import yaml
from compose_owner_versions import compose

sys.path.insert(0,str(Path.cwd()/'src'))
from mediaingredientmech.validation.write_validated import write_validated_ingredient

S=Path(__file__).resolve().parent
R=S.parent


def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    out=S/'integration';out.mkdir(exist_ok=True)
    dest=out/'shared-owner-composition.json'
    if dest.exists():raise FileExistsError(dest)
    oldps={p['proposal_id']:p for p in load(R/'proposals.json')['proposals']}
    oldds={d['case_id']:d for d in load(R/'decisions.json')['decisions']}
    newps={};newds={}
    for agent in ('a','c'):
        newps.update({p['proposal_id']:p for p in load(S/agent/'proposals.json')['proposals']})
        newds.update({d['case_id']:d for d in load(S/agent/'decisions.json')['decisions']})
    pairs=[('b-proposal-ferric_variable','a2-proposal-ferric-variable-hydrate','w02-v2-ferric-variable-composed'),('w02-proposal-mohr-hexahydrate','c2-proposal-mohr-stock-aliases','w02-v2-mohr-hexahydrate-composed')]
    composed=[];updates=[];receipts=[]
    now=datetime.now(timezone.utc).isoformat()
    for previous_id,revision_id,pid in pairs:
        previous=oldps[previous_id];revision=newps[revision_id]
        owner=previous['owner_path']
        assert owner==revision['owner_path']
        before=Path(owner)
        assert sha(before)==previous['before_sha256']==revision['before_sha256']
        for p in (previous,revision):
            assert sha(R/p['after_capture']['path'])==p['after_capture']['sha256']
        baseline=yaml.safe_load(before.read_text())
        earlier=yaml.safe_load((R/previous['after_capture']['path']).read_text())
        later=yaml.safe_load((R/revision['after_capture']['path']).read_text())
        result=compose(baseline,earlier,later)
        result['curation_history'].append({'timestamp':now,'curator':'codex_worker02_root_issue1201','action':'PROPOSED_CURATION','changes':'Explicitly compose preserved predecessor alias/evidence/history additions with the separately authored successor correction. All source-specific, duplicate-owner, role and publication holds remain; no maintained payload was applied.','previous_status':baseline['mapping_status'],'new_status':result['mapping_status'],'llm_assisted':True})
        target=out/'after'/Path(owner).name
        target.parent.mkdir(exist_ok=True)
        if target.exists():raise FileExistsError(target)
        write_validated_ingredient(result,target)
        p={'proposal_id':pid,'case_ids':list(dict.fromkeys(previous['case_ids']+revision['case_ids'])),'description':'Explicit successor composition: '+revision['description']+' Preserve all previously proposed valid aliases, evidence and history from '+previous_id+'. No source/form alternative is selected and no complete-owner or release approval is granted.','evidence_ids':list(dict.fromkeys(previous['evidence_ids']+revision['evidence_ids']+['w02-v2-shared-composition'])),'owner_path':owner,'kind':'edit_existing_owner','before_sha256':sha(before),'after_capture':{'root':'artifact','path':str(target.relative_to(R)),'sha256':sha(target)},'supersedes_proposals':[deepcopy(previous),deepcopy(revision)],'authors':['/root'],'contributing_revision_author':'/root/research_a' if 'ferric' in pid else '/root/research_c','integration_obligations':['Reconcile cross-shard same-owner edits against this original baseline; select no winner mechanically.','Preserve all unchanged and newly rejected source labels as provenance, and retain full-owner/release holds.','Withdraw inherited approval for changed bytes; coordinator alone performs guarded maintained integration and downstream gates.']}
        composed.append(p)
        for cid in p['case_ids']:
            original=newds.get(cid,oldds[cid]);d=deepcopy(original)
            d['proposal_ids']=[pid if x in (previous_id,revision_id) else x for x in d['proposal_ids']]
            assert pid in d['proposal_ids']
            d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+['w02-v2-shared-composition']))
            d['independent_review']={'status':'pending','evidence_ids':[]}
            updates.append({'case_id':cid,'previous_decision':original,'successor_decision':d,'changed_fields':[k for k in original if original[k]!=d[k]],'reason':'Exact proposal backlink and composition evidence successor; scientific source conclusion retained. Independent review of the final exact decision is required.'})
        receipts.append({'proposal_id':pid,'baseline_owner_sha256':sha(before),'preserved_previous_capture':previous['after_capture'],'revision_capture':revision['after_capture'],'composed_capture':p['after_capture'],'original_history_preserved':result['curation_history'][:len(baseline.get('curation_history',[]))]==baseline.get('curation_history',[]),'previous_added_synonyms_retained':all(x in result['synonyms'] for x in earlier['synonyms'][len(baseline['synonyms']):]),'changed_baseline_synonyms':[{ 'before':a,'after':b} for a,b in zip(baseline['synonyms'],result['synonyms']) if a!=b]})
    (out/'composed-proposals.json').write_text(json.dumps({'schema_version':1,'proposals':composed},ensure_ascii=False,indent=2)+'\n')
    (out/'composed-case-updates.json').write_text(json.dumps({'created_at':now,'updates':updates},ensure_ascii=False,indent=2)+'\n')
    dest.write_text(json.dumps({'created_at':now,'scope':'Two exact isolated owner compositions; original baseline and all fragment bytes retained. No maintained data changed.','compositions':receipts,'scientific_or_release_approval':False},indent=2)+'\n')
    evidence={'evidence_id':'w02-v2-shared-composition','kind':'local_validation','capture':{'root':'artifact','path':str(dest.relative_to(R)),'sha256':sha(dest)},'url':None,'accessed_at':now,'locator':'Original baseline, preserved predecessor/revision capture hashes, exact composed after bytes and changed baseline synonym rows.','supports_or_contradicts':'Shows explicit preservation of previous proposal additions while correcting newly reviewed source aliases. Independent review remains mandatory; composition confers no scientific or release approval.'}
    (out/'composition-evidence.json').write_text(json.dumps({'schema_version':1,'evidence':[evidence]},indent=2)+'\n')
    print(json.dumps({'composed_payloads':len(composed),'case_backlinks_requiring_review':len(updates)}))


if __name__=='__main__':main()
