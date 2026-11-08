"""Prepare a native review from independently assessed campaign outcomes.

The native inspect/validate/save commands remain authoritative. This creates an
input document, not a saved review or scientific approval of an owner/export.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import subprocess
import yaml

R = Path('reports/all_unmatched_20261107/worker-02')
T = Path('.temp/all-unmatched-worker-02')
PY = str(T/'venv/bin/python')


class PlainDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def load(path):
    return json.loads(path.read_text())


def utc(value):
    return datetime.fromisoformat(value.replace('Z','+00:00')).astimezone(timezone.utc).isoformat().replace('+00:00','Z')


def main():
    ds = load(R/'decisions.json')['decisions']
    es = load(R/'evidence.json')['evidence']
    ps = load(R/'proposals.json')['proposals']
    assert len(ds) == 188 and all(d['independent_review']['status'] == 'complete' for d in ds)
    targets = yaml.safe_load((T/'final-native-targets.yaml').read_text())['targets']
    inputs = {str(R / p) for p in ['decisions.json','evidence.json','proposals.json','integration/independent-review-coverage.json','subagent-scopes.json','validation/structural-final.json','validation/proposal-schema-final.json','validation/proposal-labels-final.json','validation/helpers-final.log','cross-shard-dependencies.json','validation/proposed-identity-collisions-final.json']}
    inputs |= {'MAPPING_SEMANTICS.md','schema/record_review.yaml','conf/record_review.yaml','docs/record-review-profile.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','uv.lock'}
    inputs |= {o['path'] for d in ds for o in d['owner_records']}
    inputs |= {str(R / e['capture']['path']) for e in es if e['capture']['root'] == 'artifact'}
    inputs |= {str(R / p['after_capture']['path']) for p in ps}
    cmd = [PY,'-B','scripts/record_review.py','inspect','--targets',str(T/'final-native-targets.yaml')]
    for path in sorted(inputs): cmd += ['--input',path]
    s = subprocess.run(cmd,capture_output=True,text=True)
    (R/'validation/native-inspect-final.log').write_text(s.stderr)
    if s.returncode: raise RuntimeError(s.stderr)
    inspection = json.loads(s.stdout)
    (R/'validation/native-inspection-final.json').write_text(json.dumps(inspection,indent=2)+'\n')
    now = datetime.now(timezone.utc)
    finish = now.isoformat().replace('+00:00','Z')
    evidence = []
    kinds = {'primary_source':'primary_source','source_snapshot':'record_content','ontology':'authority','native_record_review':'prior_review','independent_review':'prior_review','unsuccessful_search':'search','local_validation':'validation'}
    for e in es:
        c = e['capture']
        reference = str(R / c['path']) if c['root']=='artifact' else 'Frozen queue preliminary-v5/' + c['path']
        item = {'evidence_id':e['evidence_id'],'kind':kinds[e['kind']],'reference':e.get('url') or reference,
                'locator':reference+'; '+e['locator'],'accessed_at':utc(e['accessed_at']) if e.get('accessed_at') else finish,
                'support':'context_only' if e['kind']=='unsuccessful_search' else 'partial',
                'summary':e['supports_or_contradicts'],'snapshot_sha256':c['sha256']}
        if item['kind']=='search': item['search_scope']=e['locator']+'; '+e['supports_or_contradicts']
        evidence.append(item)
    check_evidence = []
    for name,path in [('structural','validation/structural-final.json'),('schema','validation/proposal-schema-final.json'),('labels','validation/proposal-labels-final.json'),('helpers','validation/helpers-final.log')]:
        eid='w02-native-check-'+name; check_evidence.append(eid)
        evidence.append({'evidence_id':eid,'kind':'validation','reference':str(R/path),'accessed_at':finish,'support':'context_only','summary':'Actual bounded validator receipt; structural checks do not establish scientific approval.','snapshot_sha256':hashlib.sha256((R/path).read_bytes()).hexdigest()})
    ids=[d['case_id'] for d in ds]
    checks=[
        {'check_id':'whole-shard','name':'Whole-shard source accounting and capture integrity','status':'passed','required':True,'summary':'188/188 exact cases; all independent-review statuses complete; all required references and hashes verified. Scientific adequacy is explicitly outside the auditor.','target_ids':ids,'command':'audit_worker_outcomes_v1.py --shard shard-02.json --decisions decisions.json --evidence evidence.json --proposals proposals.json --artifact-root worker-02 --source-root preliminary-v5 --mim-root . --output validation/structural-final.json (full resolved inputs recorded in receipt)','exit_code':0,'evidence_ids':[check_evidence[0]]},
        {'check_id':'proposal-shape','name':'Exact active proposal strict LinkML validation','status':'passed','required':True,'summary':'25 explicit active after-payloads; zero errors. Withdrawn payloads excluded.','target_ids':[d['case_id'] for d in ds if d['proposal_ids']],'command':'scripts/validate_strict.py <25 explicit active payload paths> --workers 2 --out validation/proposal-schema-final.tsv; exact argv in receipt','exit_code':0,'evidence_ids':[check_evidence[1]]},
        {'check_id':'proposal-labels','name':'Canonical labels and deprecation check','status':'failed','required':False,'summary':'24 canonical labels confirmed; unchanged MICRO:0000520 has no available adapter. Actual exit 1 retained; no universal label-validation pass claimed.','target_ids':[d['case_id'] for d in ds if d['proposal_ids']],'command':'validate_proposal_labels.py validation/proposal-labels-final.json proposals.json','exit_code':1,'evidence_ids':[check_evidence[2]]},
        {'check_id':'helper-negative-tests','name':'Integration helper failure-case tests','status':'passed','required':True,'summary':'16 tests passed, including changed decision/hash, unapproved review, destructive composition and duplicate case rejection.','target_ids':ids,'command':PY+' -B -m unittest discover -s '+str(R)+" -p 'test_*.py'",'exit_code':0,'evidence_ids':[check_evidence[3]]},
        {'check_id':'maintained-export-gates','name':'Maintained data synchronization and export gates','status':'not_applicable','required':False,'summary':'Proposal-only worker assignment; no maintained input changes or downstream generation authorized. Coordinator must run the native gates after guarded integration.','target_ids':ids},
    ]
    assessments=[]; findings=[]; actions=[]
    for i,d in enumerate(ds):
        refs=list(dict.fromkeys(d['evidence_ids']+d['independent_review']['evidence_ids']))
        assessments.append({'assessment_id':f'case-{i:03d}','area':'identity','topic':d['source']['source_label'],'outcome':'unknown' if d['disposition']=='unresolved' else ('concern' if d['disposition'] in ('supplied_form_correction','malformed_or_nonchemical_token') else 'supported'),'summary':d['reasoning'],'details':d['applicability']+' Next requirement: '+(d['missing_requirement'] or 'No additional source identity requirement recorded; all declared integration and release obligations remain.'),'target_ids':[d['case_id']],'evidence_ids':refs,'dimensions':[{'name':'source-disposition','value':d['disposition'],'definition':'Bounded frozen-source assessment; not a mapping/export approval.','evidence_ids':refs}]})
        if d['missing_requirement']:
            findings.append({'finding_id':f'source-requirement-{i:03d}','issue_key':f'w02-source-{d["case_id"].split(":")[1][:24]}','category':'identity','severity':'informational','status':'deferred','certainty':'confirmed','title':'Retained case-specific source or integration requirement','description':d['missing_requirement'],'target_ids':[d['case_id']],'evidence_ids':refs,'ownership_note':'Scope is this exact frozen source case; actual baseline comparison owners are listed on its target. No owner/export status is changed.','external_issues':d['issue_refs']})
    for finding in findings:
        finding['disposition_reason'] = 'Retained after complete source-case research and independent skeptical review. The precise unmet evidence or integration condition is stated in this finding; no unsupported identity or release is inferred.'
    for i,p in enumerate(ps):
        fid=f'proposal-{i:02d}'
        findings.append({'finding_id':fid,'issue_key':'w02-'+p['proposal_id'],'category':'grounding','severity':'major','status':'open','certainty':'confirmed','title':p['proposal_id'],'description':p['description']+' Exact isolated proposed payload: '+p['after_capture']['path']+' SHA256 '+p['after_capture']['sha256']+'. This is a proposed remedy, not an applied fix.','target_ids':p['case_ids'],'evidence_ids':p['evidence_ids'],'ownership_note':'Proposed maintained owner: '+p['owner_path']+'. Recheck original before hash and cross-worker conflicts.','rule_id':'MAPPING_SEMANTICS supplied-form and publication contract','native_severity':'P2','normalization_reason':'An unintegrated identity/alias/property proposal requires curation; this review gives no complete owner or export approval.'})
        actions.append({'action_id':f'integrate-{i:02d}','description':'Coordinator to review and integrate '+p['proposal_id']+' through guarded native writers after conflict resolution.','finding_ids':[fid],'target_ids':p['case_ids'],'ownership_note':'Intended owner '+p['owner_path']+'; never overwrite a different current before hash.','acceptance_checks':['Reconcile all same-owner proposals against the original baseline and retain source-specific holds.','Withdraw inherited positive support when owner bytes change; independently review the full resulting owner payload.','Synchronize native YAML/SSSOM/generated surfaces and run applicable native release gates in the coordinator integration.']})
    review={'schema_version':'1.0.0','review_id':now.strftime('%Y%m%dT%H%M%SZ')+'-w02-all-unmatched-source-review','kind':'batch','repository':'CultureBotAI/MediaIngredientMech','title':'Worker 02 complete frozen source-case review','started_at':utc(load(R/'acceptance.json')['accepted_at']),'finished_at':finish,'reviewer':{'identity':'codex_worker02_root; scientific authors/reviewers identified per case in campaign bundle','kind':'agent','independence':'self_review','independence_basis':'Root compiled the native bundle. Separate in-process reviewers assessed every final source decision and proposal; exact authorship, scopes, digests and exceptions are preserved in integration/independent-review-coverage.json. This document does not claim root independence from integration.'},'skill':'review-ingredients','completion':'completed','verdict':'needs_curation','scientific_review':True,'summary':'All 188 assigned frozen source cases were researched and independently reviewed; 25 active isolated proposals remain. Precise unresolved requirements and source/owner/publication holds survive. No maintained data was changed. This is source-case review, not whole-owner, role, or export approval.','source':inspection['source'],'targets':targets,'scope':{'description':'Exact worker02 frozen shard, all complete recipe/source contexts and actual candidate owners; no other shard assessed.','selection':'Immutable shard-02.json SHA256 993e393b8a50e6061e4a9863bd60b3ab2a48ee584907a97e3066c1cbc03d6db0; all cases in original order.','coverage':'full','population_size':188,'reviewed_target_ids':ids,'exclusions':[{'target':'Other worker shards, complete owners, roles, publication and downstream rebuild','reason':'Outside this source-review shard and worker integration authority.'}]},'checks':checks,'evidence':evidence,'assessments':assessments,'findings':findings,'actions':actions,'limitations':['Source cases are the review targets; actual comparison/target owners are listed without inventing owners for source-only cases.','Frozen source snapshots outside this worktree remain bound by their original queue paths and SHA256 in evidence.json. Captured primary artifacts retain actual retrieval timestamps; no shared cache reuse confers approval.','24 proposal mappings have canonical-label confirmation; MICRO:0000520 adapter unavailable. MeSH concept terms pass the current local label/schema checks; downstream consumer compatibility remains a coordinator obligation.','No maintained YAML, canonical SSSOM, unified snapshot, semantic review, companion selectors or publication inputs were edited. No merges, extra external sessions or downstream builds were performed.','All changed owner bytes withdraw inherited positive approval. Existing REJECTED/WITHHOLD/source-material restrictions and unresolved supplied-form/version/quantity boundaries remain.'],'links':['https://github.com/CultureBotAI/MediaIngredientMech/pull/1158','https://github.com/CultureBotAI/MediaIngredientMech/issues/1181','https://github.com/CultureBotAI/CultureMech/issues/675','https://github.com/CultureBotAI/CultureMech/issues/408','https://github.com/CultureBotAI/CultureMech/issues/150']}
    destination=T/'native-review-final.yaml'
    if destination.exists(): raise FileExistsError(destination)
    destination.write_text(yaml.dump(review,Dumper=PlainDumper,allow_unicode=True,sort_keys=False))
    (R/'validation/native-preparation.json').write_text(json.dumps({'command':cmd,'exit_code':s.returncode,'prepared_at':finish,'review_id':review['review_id'],'targets':len(targets),'hashed_inputs':len(inspection['source']['inputs']),'assessments':len(assessments),'findings':len(findings),'saved':False},indent=2)+'\n')
    print({'review_id':review['review_id'],'targets':len(targets),'inputs':len(inputs),'prepared_document':str(destination)})


if __name__=='__main__': main()
