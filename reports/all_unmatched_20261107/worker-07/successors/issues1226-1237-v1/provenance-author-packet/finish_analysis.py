"""Append component-specific detail and diagnostic controls; preserve first pass."""
from pathlib import Path
import collections
import copy
import datetime
import hashlib
import json
import rebind

ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(n,d):
    p=ROOT/n
    if p.exists():raise ValueError('Existing output')
    p.write_text(json.dumps(d,indent=2,sort_keys=True,ensure_ascii=False)+'\n')

allow=json.loads((ROOT/'allowlist-v1.json').read_text())
exc=json.loads((ROOT/'exclusions-v1.json').read_text())
comp=[]
for row in exc['component_assertions']:
    for i,e in enumerate(row['complete_object']['evidence']):
        comp.append({'proposal_id':row['proposal_id'],'payload':row['payload'],
                     'pointer':row['pointer']+'/evidence/'+str(i),
                     'enum':'ComponentEvidenceTypeEnum','evidence_type':e['evidence_type'],
                     'full_object':e,'full_object_sha256':rebind.value_sha(e),
                     'disposition':'EXCLUDED_FROM_MAPPING_EVIDENCE_TYPE_REPAIR'})
write('component-evidence-exclusions-v2.json',{
    'author':rebind.AUTHOR,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'supersedes_only':'The convenience enum/evidence_type annotation on the component_assertions section of exclusions-v1.json; complete assertion objects, hashes and exclusion decisions remain valid.',
    'correction':'v1 safely binds and excludes complete ComponentAssertion objects but queried evidence_type at their parent, yielding null. The actual enum slot is ComponentAssertion.evidence[].evidence_type. This supplement binds each exact nested object. No ingredient payload was written or retyped.',
    'preserved_predecessor':{'path':'exclusions-v1.json','sha256':sha(ROOT/'exclusions-v1.json')},
    'component_assertions':len(exc['component_assertions']),
    'component_evidence_objects':len(comp),
    'type_counts':dict(collections.Counter(x['evidence_type'] for x in comp)),
    'rows':comp,'scientific_review':False,'independent_approval':False})

def bound(row,owner_raw,object_value,context,ordinal):
    if hashlib.sha256(owner_raw).hexdigest()!=row['payload']['sha256']:raise ValueError('stale owner')
    if rebind.value_sha(object_value)!=row['full_object_sha256']:raise ValueError('stale object')
    if rebind.value_sha(context)!=row['mapping_context_sha256']:raise ValueError('stale attachment')
    if ordinal!=row['duplicate_ordinal_1based']:raise ValueError('wrong duplicate occurrence')
    if row['enum']!='EvidenceTypeEnum' or not row['type_pointer'].startswith('/ontology_mapping/evidence/'):raise ValueError('wrong enum slot')
    return True
controls=[]
def check(n,fn):
    assert fn(),n
    controls.append({'control':n,'status':'pass'})
def refuses(fn):
    try:fn()
    except ValueError:return True
    return False
a={'evidence_type':'MANUAL_CURATION','source':'older','notes':'old'}
b={'evidence_type':'MANUAL_CURATION','source':'new','notes':'new'}
check('reordering preserves complete inherited objects',lambda:rebind.multiset_delta([a,b],[b,a])=={0:1,1:0})
check('duplicate addition inherits only available baseline multiplicity',lambda:rebind.multiset_delta([a],[a,a])=={0:0})
check('modified notes are a new complete object, not inherited by same source',lambda:rebind.multiset_delta([a],[{**a,'notes':'changed'}])=={})
check('duplicate removal keeps same-index match',lambda:rebind.multiset_delta([a,a],[a])=={0:0})
row=allow['rows'][0]; raw=Path(row['payload']['path']).read_bytes(); value=row['full_object']; ctx=row['mapping_context']; ordn=row['duplicate_ordinal_1based']
check('actual exact current owner/object/context accepts binding',lambda:bound(row,raw,value,ctx,ordn))
check('stale owner bytes refused',lambda:refuses(lambda:bound(row,raw+b'\n',value,ctx,ordn)))
check('same-source changed complete claim refused',lambda:refuses(lambda:bound(row,raw,{**value,'notes':value['notes']+' changed'},ctx,ordn)))
check('changed parent mapping context refused',lambda:refuses(lambda:bound(row,raw,value,{**ctx,'ontology_id':'CHEBI:0'},ordn)))
check('wrong duplicate occurrence refused',lambda:refuses(lambda:bound(row,raw,value,ctx,ordn+1)))
wrong=copy.deepcopy(row); wrong['enum']='ComponentEvidenceTypeEnum'; wrong['type_pointer']='/component_assertion/evidence/0/evidence_type'
check('component enum path refused',lambda:refuses(lambda:bound(wrong,raw,value,ctx,ordn)))
check('historical manual object excluded from actual allowlist',lambda:all((x['proposal_id'],x['index'])!=(exc['inherited_manual'][0]['proposal_id'],exc['inherited_manual'][0]['index']) for x in allow['rows']))
write('diagnostic-controls-v1.json',{'author':rebind.AUTHOR,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
      'scope':'Private author-side diagnostic checks of exact-object multiset matching and declared allowlist binding semantics. No production/writer gate tests are claimed.',
      'controls':controls,'passed':len(controls),'failed':0,'independent_review':False})

files=[p for p in sorted(ROOT.iterdir()) if p.is_file()]
write('HANDOFF.json',{
    'author':rebind.AUTHOR,'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'status':'author_analysis_complete_pending_independent_review',
    'inputs_head':rebind.HEAD,'scientific_base':rebind.BASE,
    'scope':'Author-side #1226 exact current MappingEvidence scalar correction allowlist; all100 selected payloads inspected for exact before/after evidence and added history; all79 frozen confirmed W07 objects rebound. No independent scientific or publication approval.',
    'counts':allow['counts'], 'component_evidence_objects':len(comp),
    'selected_type':'All79 complete new agent assertions warrant LLM_SUGGESTION. Eleven distinct full-note patterns include identity/preparation/source applicability judgments; CHEBI190300 includes exact-form/absence inference beyond a direct database fact, so remains LLM_SUGGESTION.',
    'historical_exclusion':'Sodium_phosphate_monobasic_monohydrate mapping evidence[1] is exact baseline #312 evidence; do not retype. No claim of newly authenticated human authorship.',
    'other_exclusions':'All41 other mapping evidence objects and all nested component evidence are outside this scalar repair; scientific fields and old history excluded.',
    'source_scope':'Original capture content and dates are unchanged; source URLs and complete claim notes remain bound, without independent renewal of their scientific truth.',
    'correction_lineage':'ComponentAssertion-level v1 convenience evidence_type field was null; component-evidence-exclusions-v2.json adds correct nested ComponentEvidence locators with all original objects preserved. No payload mutation occurred.',
    'files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in files],
    'next_requirements':['Parent must use native guarded writer and append truthful history for real scalar changes.',
                         'Rebind allowlist immediately before applying; independent reviewer must assess exact complete changed payloads after science corrections.',
                         'Do not decide Hutner union or use metadata changes as owner, role, export or release approval.'],
    'scientific_review':False,'independent_approval':False})
write('MANIFEST.json',{'author':rebind.AUTHOR,'files':[{'path':str(p.relative_to(ROOT)),'sha256':sha(p)} for p in sorted(ROOT.iterdir()) if p.is_file()]})
print(json.dumps({'controls':len(controls),'component_types':dict(collections.Counter(x['evidence_type'] for x in comp)),
                  'handoff_sha256':sha(ROOT/'HANDOFF.json'),'manifest_sha256':sha(ROOT/'MANIFEST.json'),
                  'allowlist_sha256':sha(ROOT/'allowlist-v1.json')},indent=2))
