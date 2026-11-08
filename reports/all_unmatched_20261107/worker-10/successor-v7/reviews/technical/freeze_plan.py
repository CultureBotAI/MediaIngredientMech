"""Read-only technical baseline and planned checks; no payload authoring."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess

R=Path.cwd();O=R/'.temp/columbia-controls-successor-v1';P=O/'technical';A=R/'reports/all_unmatched_20261107/worker-10';S=A/'successor-v6'
P.mkdir(parents=True,exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def canon(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def save(name,x):
    with (P/name).open('x') as f:json.dump(x,f,indent=2,ensure_ascii=False);f.write('\n')
def ref(p):return {'path':str(p.relative_to(R)),'sha256':sha(p)}
started=datetime.now(timezone.utc).isoformat()
head=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip();assert head=='c66d6d3665368fe1ae8986fb7c16340a103582c1'
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=no'],text=True);assert not status
sel=read(S/'selection.json');core={}
for n,b in sel['authoritative_core'].items():
    p=A/b['path'];assert sha(p)==b['sha256'];core[n]={'path':str(p.relative_to(R)),'sha256':sha(p),'object':read(p)}
proposals=core['proposals.json']['object']['proposals'];decisions=core['decisions.json']['object']['decisions'];evidence=core['evidence.json']['object']['evidence']
assert (len(proposals),len(decisions),len(evidence))==(127,188,1218)
occ=[x for d in decisions for x in d['occurrence_ids']];assert len(occ)==len(set(occ))==304
payloads=[]
for p in proposals:
    dest=A/p['after_capture']['path'];assert sha(dest)==p['after_capture']['sha256']
    payloads.append({'proposal_id':p['proposal_id'],'proposal_canonical_sha256':canon(p),'owner_path':p['owner_path'],'before_sha256':p.get('before_sha256'),'after_capture':p['after_capture'],'payload_bytes':dest.stat().st_size})
owners={str(p.relative_to(R)):sha(p) for p in sorted((R/'data/ingredients').rglob('*.yaml'))};assert len(owners)==2956
owner=R/'data/ingredients/unmapped/Columbia_Blood_Agar_Base.yaml';assert sha(owner)=='29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324'
contracts=['MAPPING_SEMANTICS.md','docs/record-reviews.md','docs/record-review-profile.md','.claude/skills/review-yaml-category/SKILL.md','.claude/skills/curate-yaml-record/SKILL.md','.claude/skills/add-media/SKILL.md','src/mediaingredientmech/curate/curation_event.py','src/mediaingredientmech/validation/write_validated.py','src/mediaingredientmech/validation/component_partonomy.py','src/mediaingredientmech/synonym_policy.py','src/mediaingredientmech/schema/mediaingredientmech.yaml','scripts/export_lists.py','scripts/validate_sssom_invariants.py','scripts/record_review.py','schema/record_review.yaml']
save('baseline-v1.json',{'at':started,'head':head,'tracked_status':status,'selection':ref(S/'selection.json'),'selected_core':core,'selected_payloads':payloads,'maintained_owner_hashes':owners,'generic_Columbia_before':ref(owner),'contract_hashes':{p:sha(R/p) for p in contracts},'counts':{'proposals':127,'decisions':188,'occurrences':304,'evidence':1218,'maintained_owners':2956},'search_scope':'Direct explicit selected paths and ignored-inclusive Path.rglob; no gitignore filtering.'})
plan={
 'at':datetime.now(timezone.utc).isoformat(),'reviewer':'worker10:/root/buffers_research','author':'worker10:/root','status':'planned_awaiting_exact_author_candidate','scientific_review':False,
 'prior_authorship':'Authored original W10 buffer proposals including these Tris/HEPES named preparations, plus HCl and later serum corrections. This scope independently verifies author-proposed metadata/native behavior and preservation, and is not independent approval of my original source science. Separate scientist owns scientific judgment.',
 'baseline':ref(P/'baseline-v1.json'),
 'inputs':[ref(p) for p in sorted((O/'inputs').glob('*.json'))],
 'allowed_scope':[
  'Authentic same-path generic Columbia UNMAPPED_0118 edit from maintained29ed preimage: preserve generic identity/status/history and both exact vendor labels/sources, switch only reviewed vendor label disposition to REJECTED_LABEL with truthful new partition notes/history.',
  'Supported Difco alias/source-case routing and exact owner-dependency after-hash binding; preserve vendor new-owner kind and null maintained-before origin. Bind real W04 Oxoid authored origin read-only, not an invented W10 maintained preimage.',
  'Two original buffer payloads: component_assertion completeness PARTIAL to UNKNOWN plus bounded current explanation and one truthful history event; no component/name/reference/id/amount/unit/pH/strength/solvent/titrant changes.',
  'Metadata/lineage dependencies and independently completed review pointers only as separately frozen; all other selected science remains byte-exact.'
 ],
 'fresh_native_checks':[
  {'api':'record_curation_event(record, **exact_new_event)','purpose':'Reconstruct each appended event on a private predecessor copy; preserve exact original history prefix and LLM attribution; never mutate selected source.'},
  {'api':'validate_ingredient + write_validated_ingredient','purpose':'Closed-schema validation and exact guarded YAML roundtrip for each changed payload, private fixture only.'},
  {'api':'validate_component_partonomy(full_selected_overlay.values())','purpose':'Relational component/reference/quantity pairing against full maintained catalog plus final selected owner overlays. Preserve known admission holds separately.'},
  {'api':'is_resolving_synonym + export_lists._synonyms / export_label_index','purpose':'Both rejected vendor labels stay available as provenance but do not resolve to generic UNMAPPED_0118. Test actual native label projection in private scratch; Difco routing has exact source subset rather than provider-wide assignment.'},
  {'api':'Actual Claw _row_from_yaml + build_owner_index + _check_producer_bindings','purpose':'Bounded in-memory before/after projections only. Generic UNMAPPED owner produces no mapped identity row; changed mapped identities retain correct own exactMatch. Distinguish honest history date/curator deltas from label routing.'},
  {'api':'validate_sssom_invariants.record_identifier/evaluate_rule_d','purpose':'Read actual private payload fixtures and check real identity rows; reject deliberately degraded own-identity closeMatch.'},
  {'api':'record_review.load_document(raw bytes), validate_review, render_markdown','purpose':'Final native assembly source/hash/target/claim-scope and exact rendered Markdown parity. No saver or bulk review rewrite.'}
 ],
 'focused_controls':[
  'Native writer refuses unknown field and invalid completeness enum before any file write.',
  'Reverting a reviewed REJECTED_LABEL to CATALOG_VARIANT must be detected by actual native resolving-synonym/label projection check.',
  'Dropping either vendor raw label or source, repurposing generic identifier/status or fabricating nonnull before on vendor new-owner proposal fails full lineage invariant.',
  'Invented buffer component, altered concentration/unit, changed identity/alias or dropped old history fails exact authorized-field delta guard, even when schema-valid.',
  'Native partonomy rejects deliberate mismatched amount/unit or missing active component reference.',
  'Native Rule D rejects own-identity closeMatch using exact fixture; schema alone is not scientific provenance verification.'
 ],
 'lineage':{'old_core_and127payloads':'Compare against independent baseline; changed subset explicit, no forced new count.','case_occurrences':'All original188case304occurrence membership preserved, with separate admitted/held subset routing metadata; do not equate whole-case membership to permission for every occurrence.','difco':'Retain nominal seven-input COMPLETE/CURATED_INTERPRETATION scope from S6; this task does not impose blanket UNKNOWN.','oxoid':'Real W04 origin and actual source300/921 association bound read-only; four older prepared-base CM331 occurrences stay held, no dry-powder dose substitution.','protected_examples':'Prior carbonate/calf and serum/HCl science stays unchanged; old sealed reports remain immutable.'},
 'finding_policy':'Report any real defect with exact bytes and reproducible negative before author remediation; retain reviewer harness failures separately.',
 'limits':['No primary scientific self-approval, owner admission, merge, role or export release.','No maintained data, other-worker sources, shared source, Git or GitHub mutation; no paid provider or additional external session.','Do not run unrelated broad test suites or weaken native gates.'],
 'writes_only':str(P)}
save('plan-v1.json',plan)
print(json.dumps({'baseline':ref(P/'baseline-v1.json'),'plan':ref(P/'plan-v1.json'),'counts':read(P/'baseline-v1.json')['counts']},indent=2))
