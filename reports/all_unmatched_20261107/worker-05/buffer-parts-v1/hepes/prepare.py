from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
import copy, hashlib, json, shutil, subprocess
import yaml

W = Path.cwd()
C = W.parents[2]
B = W/'reports/all_unmatched_20261107/worker-05'
O = B/'tellurium-polypeptone-v1/core'
S = W/'.temp/w05-buffer-parts-v1/hepes'
T = C/'preflight/buffer-source-parts-triage-v1'
Q = C/'queue/preliminary-v5'
CID = 'CM_NAME:6bb791d024e4025f398cd7b81fa3a943646581daf6079a42d779d6efa87ec78f'
PIDS = ['CHEM-C1193-HEPES-1221', 'CHEM-C1193-HEPES-1474']
HEAD = '0bac12cabfd1f67f212631d8eef9aa46379f6b41'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
objsha = lambda x: hashlib.sha256(json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()
j = lambda p: json.loads(p.read_text())
at = datetime.now(timezone.utc).isoformat()
def put(path, value):
    assert not path.exists(), path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False)+'\n')
reads=[]
def capture(src, rel, purpose):
    dst=S/rel
    assert not dst.exists(), dst
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src,dst)
    assert src.read_bytes()==dst.read_bytes()
    reads.append(dict(source_path=str(src), local_path=str(dst.relative_to(S)), sha256=sha(src), purpose=purpose, read_scope='complete', assessed_by='/root/buffer_hepes', assessed_at=at))
    return dst

assert subprocess.check_output(['git','rev-parse','HEAD'], text=True).strip()==HEAD
assert sha(T/'ASSESSMENT.json')=='53e137bc1f567a810258a1d552fa001b5dd10ebffd83f3654695a5053a7b07b0'
triage=j(T/'ASSESSMENT.json')
for name,h in triage['files'].items(): assert sha(T/name)==h,(name,'triage integrity')
for name in ['ASSESSMENT.json','new-hepes-components-finding-v1.json','verified-payloads.json','primary-capture-index.json','issue1237-comment.md']:
    capture(T/name,'input/triage/'+name,'Exact coordinator triage and authentic before-fix finding; retained original timestamp where declared.')
for name in ['MAPPING_SEMANTICS.md','.claude/skills/add-media/SKILL.md','.claude/skills/curate-yaml-record/SKILL.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/validation/component_partonomy.py']:
    p=W/name
    reads.append(dict(source_path=str(p),sha256=sha(p),purpose='Native contract or validator read for declared component/whole-stock scope',read_scope='Complete skill and MAPPING_SEMANTICS sections3/6; schema/validator relevant component and evidence shapes',assessed_by='/root/buffer_hepes',assessed_at=at))
ps=j(O/'proposals.json')['proposals'];ds=j(O/'decisions.json')['decisions'];es=j(O/'evidence.json')['evidence']
proposals=[copy.deepcopy(next(x for x in ps if x['proposal_id']==pid)) for pid in PIDS]
decision=copy.deepcopy(next(x for x in ds if x['case_id']==CID))
put(S/'input/selected-proposals.json',{'proposals':proposals})
put(S/'input/selected-decision.json',decision)
put(S/'input/selected-input-bindings.json',dict(base_head=HEAD,source_files=[dict(path=str(p.relative_to(W)),sha256=sha(p)) for p in [O/'proposals.json',O/'decisions.json',O/'evidence.json']],selected_proposal_object_sha256s={p['proposal_id']:objsha(p) for p in proposals},selected_decision_object_sha256=objsha(decision)))
frozen=next(x for x in j(Q/'shards/shard-05.json')['cases'] if x['case_id']==CID)
put(S/'input/frozen-case.json',frozen)
for occurrence in frozen['occurrences']:
    src=Q/occurrence['full_recipe_snapshot'];assert sha(src)==occurrence['source_file_sha256']
    capture(src,'input/recipes/'+src.name,'Full frozen recipe; raw stock label and corrupt flattened mass unit preserved as historical source data, not scientifically reused as stock constituent amount.')

primary=[]
class Visible(HTMLParser):
    def __init__(self): super().__init__();self.hidden=0;self.parts=[]
    def handle_starttag(self,tag,attrs):
        if tag in ['script','style']: self.hidden+=1
    def handle_endtag(self,tag):
        if tag in ['script','style']: self.hidden-=1
    def handle_data(self,data):
        if self.hidden==0:self.parts.append(data)
for number,eid in [('1221','CHEM-CAP-b4a1db85c19c42e5'),('1474','CHEM-CAP-c801a5637573d5ae')]:
    meta=next(x for x in j(T/'primary-capture-index.json') if x['name']=='nbrc'+number)
    legacy=next(x for x in es if x['evidence_id']==eid)
    html=capture(T/meta['path'],'captures/'+meta['path'],'Complete NBRC original primary HTML, no stock material inputs enumerated; source and receiving-medium context read.')
    text=capture(T/('nbrc'+number+'.txt'),'captures/nbrc'+number+'.txt','Exact coordinator source extraction, checked against full HTML using a separate stdlib parser.')
    assert sha(B/legacy['capture']['path'])==sha(html)==meta['sha256']==legacy['capture']['sha256']
    parser=Visible();parser.feed(html.read_text());parsed=' '.join(' '.join(parser.parts).split())
    assert parsed==text.read_text().strip()
    primary.append(dict(source_number=number,url=meta['url'],html=dict(path=str(html.relative_to(S)),sha256=sha(html)),extraction=dict(path=str(text.relative_to(S)),sha256=sha(text)),coordinator_capture=meta,legacy_worker_capture=legacy,byte_identical_independent_retrievals=True,source_name='1M HEPES-KOH',source_receiving_quantity='20 ml',source_nominal_whole_stock_strength='1 M',receiving_medium_pH='7.14' if number=='1221' else '9.0',stock_pH=None,stock_solvent=None,enumerated_stock_material_inputs=[],neutralization_ratio=None,interpretation='The complete source names a whole stock additive, not material constituents. Receiving-medium pH/water cannot be borrowed as stock properties. Missing stock details do not prove equality or difference between accession-qualified proposals.',assessed_by='/root/buffer_hepes',assessed_at=at))

payloads=[]
for p in proposals:
    src=B/p['after_capture']['path'];assert sha(src)==p['after_capture']['sha256']
    dst=capture(src,'input/current/'+src.name,'Complete currently selected payload, all fields/history inspected; retained unchanged.')
    old=B/p['predecessor_after_capture']['path'];assert sha(old)==p['predecessor_after_capture']['sha256']
    before=capture(old,'input/original/'+old.name,'Complete authentic original payload cited by NEW-02; inferred component objects preserved.')
    rec=yaml.safe_load(dst.read_text());orig=yaml.safe_load(before.read_text())
    assert 'components' not in rec and 'component_assertion' not in rec
    assert orig['components'] and orig['component_assertion']
    assert rec['curation_history'][:len(orig['curation_history'])]==orig['curation_history']
    for k in ['identifier','preferred_term','mapping_status','ingredient_type','solution_type','synonyms','occurrence_statistics','supplied_form','physicochemical_roles','nutritional_roles','cellular_metabolic_roles','chemical_properties']:
        assert rec.get(k)==orig.get(k),(p['proposal_id'],k)
    payloads.append(dict(proposal_id=p['proposal_id'],current_selected_capture=p['after_capture'],authentic_original_capture=p['predecessor_after_capture'],current_proposal_object_sha256=objsha(p),current_payload_unchanged=True,new_history_events=0,components_absent=True,paired_assertion_absent=True,existing_history=rec['curation_history'],withdrawn_original_components=orig['components'],withdrawn_original_assertion=orig['component_assertion'],remaining_whole_stock_unknowns=['stock pH','solvent','preparation inputs','neutralization ratio','individual component concentrations'],applies_to_occurrence_ids=p['applies_to_occurrence_ids']))
git_paths=[p['after_capture']['path'] for p in proposals]+['final-correction-v1/chemicals/new-hepes-components-finding-v1.json']
log=subprocess.check_output(['git','log','--format=%H%x09%aI%x09%cI%x09%s','--']+[str((B/p).relative_to(W)) for p in git_paths],text=True)
put(S/'input/git-publication-history.json',dict(command=['git','log','--format=%H%x09%aI%x09%cI%x09%s','--']+[str((B/p).relative_to(W)) for p in git_paths],stdout=log,scope='Local retained commit metadata; commit time is not a provider push receipt or exact private mutation time.'))
put(S/'primary-assessment.json',dict(author='/root/buffer_hepes',at=at,base_head=HEAD,case_id=CID,occurrence_ids=decision['occurrence_ids'],sources=primary,payloads=payloads,conclusion='The filed component withdrawal is already present in both exact current payloads. Retain them unchanged and independently re-review current complete bytes. Fresh report-only evidence/routing/chronology is warranted; repeated material removal or an invented no-op curation event is not.',family_identity='Two accession-qualified conditional candidates preserve source provenance. The inspected facts support the same bounded nominal description, but neither establish full formulation equivalence nor demonstrate distinct stock preparations. Coordinator owns final owner reconciliation; no arbitrary winning identity is selected.',composition_representation='Unknown composition is retained in notes. No components and no orphan UNKNOWN ComponentAssertion are introduced.',limits=['No new or revised maintained records, family union, source-case ownership, role approval or export admission.','Current stock identity candidates remain conditional. Removing unsupported components does not resolve the separate family reconciliation.','Historical source notes/failed interpretations and all earlier evidence remain intact; original frozen20G_PER_L is not adopted as actual stock quantity.']))
put(S/'source-read-ledger.json',dict(author='/root/buffer_hepes',at=at,scientific_scope=dict(complete_current_payloads=2,complete_original_payloads=2,complete_source_decisions=1,frozen_recipes=2,primary_source_documents=2,case_id=CID,proposal_ids=PIDS),reads=reads,all_source_and_proposal_paths_read_only=True,new_primary_fetches=0,reused_primary_captures='Exact frozen primary bytes independently assessed; original acquisitions and actual retrieving author remain separately attributed.'))
print(json.dumps(dict(status='prepared',current_payloads_changed=0,selected_proposals=2,case_id=CID,primary_documents=2)))
