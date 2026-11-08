from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, shutil

W=Path.cwd(); S4=W/'.temp/w05-buffer-parts-v1'; S=S4/'parents-direct-v1'; OLD=S4/'parents'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
dump=lambda p,x:p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
now=datetime.now(timezone.utc).isoformat()
assert not (S/'MANIFEST.json').exists()
assert load(S/'validation/receipt.json')['status']=='PASS'
assert sha(S/'proposed/Peptone.yaml')=='c083794668a362203de6430eaa2609c34cd8ef78574a1230aa25b4a64fb55fd7'
reviewdir=S/'review'; reviewdir.mkdir(exist_ok=False)
for name in ['direct-parent-independent-review-v1.json','ontology-interpretation-reassessment-v1.json']:
    src=S4/'review'/name; shutil.copyfile(src,reviewdir/name); assert sha(src)==sha(reviewdir/name)
review=load(reviewdir/'direct-parent-independent-review-v1.json')
assert review['after']['sha256']==sha(S/'proposed/Peptone.yaml')
assert review['reviewer']=='/root/final_skeptical'
inputs=[]
for p in sorted((S/'captures').glob('*')):
    if p.is_file(): inputs.append(dict(path=str(p.relative_to(S)),sha256=sha(p),scope='Exact preserved primary capture or original capture receipt. Full NLM descriptor/concept and browser/OLS term inspected; manufacturer PDF relevant printed page7, with previous Soy pages26/33 context. Receipt time is original, not recapture time.'))
for name in ['MAPPING_SEMANTICS.md','.claude/skills/add-media/SKILL.md','.claude/skills/curate-yaml-record/SKILL.md','src/mediaingredientmech/schema/mediaingredientmech.yaml']:
    p=W/name; inputs.append(dict(path=str(p),sha256=sha(p),scope='Current native contract; identity sections1/3 and partonomy6; focused skills and schema shape.'))
for name in ['ASSESSMENT.md','HANDOFF.json','MANIFEST.json','decision.json','captures/web-foodon-nlm-response.json','captures/web-w3c-semantics-response.json','source-extracts/exact-owl-entities.json']:
    p=S/'input/coordinator-reassessment'/name; inputs.append(dict(path=str(p.relative_to(S)),sha256=sha(p),scope='Full selected coordinator interpretation or exact captured primary excerpt read; coordinator scientist attribution retained, independent applicability reassessed. All35 original manifest members separately rehashed; integrity verification does not mean every script/log is scientific primary evidence.'))
for name in ['proposals.json','decisions.json','evidence.json','case-deltas.json','proposed/Peptone.yaml','scientific-plan.json','owner-search.json','validation/receipt.json']:
    p=S/name; inputs.append(dict(path=name,sha256=sha(p),scope='Full parsed successor artifact; complete changed Peptone payload, proposal and changed decision fields scientifically read. Large unchanged source/hold objects compared exactly against sealed full predecessor; no reauthorship or historical approval transfer.'))
dump(S/'read-ledger.json',dict(at=now,scientific_author='/root/buffer_hepes',independent_reviewer='/root/final_skeptical',entries=inputs,explicit_scope=['Direct generic Peptone assessment only; unchanged Soy full proposal/decision carried without byte changes.','Generic complete owner identity is distinct from missing source-assay/supplier details, organism role and release approval.','No new external capture is claimed. Exact old source bytes and original times retained.','NLM descriptor JSON gives active label and preferred concept; explicit singular Peptone entry term is visible in linked complete primary browser capture and OLS object.','Full FoodOn OWL class restriction remains real; the earlier inferred food-use/lot eligibility gate is expressly superseded.','The successful coordinator web captures lack an absolute retrieval timestamp; failed shell receipts are not used to fabricate one.']))
ps=load(S/'proposals.json')['proposals']; ds=load(S/'decisions.json')['decisions']; es=load(S/'evidence.json')['evidence']
dump(S/'selected-files.json',dict(author='/root/buffer_hepes',at=now,selection=[dict(path=n,sha256=sha(S/n)) for n in ['proposals.json','decisions.json','evidence.json','case-deltas.json']],proposal_ids=[p['proposal_id'] for p in ps],case_ids=[d['case_id'] for d in ds],additive_evidence_ids=[e['evidence_id'] for e in es],replacement_scope='Use this full2P2D parent fragment instead of parents/final parent2P2D. Preserve and include all parents/final/evidence-v2.json historical additive evidence plus these8 entries. Separate parents/final/tombstone-*-v2.json files remain selected unchanged. This does not select child/RCM proposals.',peer_review=dict(path='review/direct-parent-independent-review-v1.json',sha256=sha(reviewdir/'direct-parent-independent-review-v1.json'),status=review['status'])))
receipt=load(S/'author-receipt.json')
handoff=f'''# W05 direct generic Peptone successor

Author: `/root/buffer_hepes`. Independent scientist/reviewer: `/root/final_skeptical`.
Sealed at {now}. This is an append-only report proposal; no maintained changes, Git/GitHub writes or export approval.

Select `proposals.json` and `decisions.json` as the complete two-parent fragment. Soy proposal `W05-FINAL-MAT-032` and its full source decision are unchanged. Peptone `W05-FINAL-MAT-039` now uses `mesh:D010461` / `Peptones` / `EXACT_MATCH`; exact after SHA is `{receipt['after_capture']['sha256']}`. The authentic maintained beforeimage remains `{receipt['authentic_before']['sha256']}`, and sealed prior local-plus-broader payload remains `{receipt['predecessor_capture']['sha256']}`. Do not combine this parent fragment with the earlier parent fragment as duplicate selections.

The primary NLM generic sense and independent manufacturer definition support this exact unspecified material identity under native section3. The earlier process/precipitation certificate requirement and FoodOn food-use/lot eligibility inference were overstated. Original interpretations remain as dated evidence/history and are expressly superseded by this successor. No different assigned actual preparation was established. No source-assay, product, enzyme, feedstock, role, owner or release approval follows.

`evidence.json` adds {len(es)} entries to the old complete evidence set; it does not replace the old44 parent entries. All11 prior curation events and5 MappingEvidence objects are intact, with one genuine new event and3 claim-specific `LLM_SUGGESTION` entries. Neither old enum values nor historical authorship are rewritten. Native/closed-schema/guarded checks pass in `validation/receipt.json`; Peptone projection changes two prior rows into one exact MeSH row, and Soy retains its exact MICRO row. Rejected identity tokens remain absent from exported `other`.

The source Peptone case remains unresolved for its specific assays and all frozen hold objects, original labels, two observations and owner bindings are unchanged. Full Soy decision is an exact carry. The201-member old parents manifest was reverified without changes. Its Bacto_Soytone tombstone v2 successor stays selected separately and unchanged. There are no new source cases.

Exact author payload science review passed at {review['at']} in `review/direct-parent-independent-review-v1.json`; full assembled source decisions, final manifest and source-specific dependencies still require root's final composition review. Root will separately use reviewed successors for only the five generic child references plus RCM against the actual final `mesh:D010461` identifier; no global replace or arbitrary owner union.

The coordinator35-member reassessment is copied exactly under `input/coordinator-reassessment/`, HANDOFF SHA `ed4b490104249457bbb557767418eff3d19437aab459a5084cb91a2658c41663`. This receipt supplies scientific context, not blanket final owner approval. Original failed shell receipts and successful web-response evidence remain distinct; no missing retrieval time was invented. The author event at {receipt['at']} follows receipt of the sealed reassessment; no new formal GitHub filing time is claimed. Prior report/private-selection/publication chronology remains in the sealed predecessor packet.

See `selected-files.json`, `read-ledger.json`, `scientific-plan.json`, `case-deltas.json` and `MANIFEST.json` for exact composition bindings. Root owns final integration, final native full-corpus checks, acceptance and publication.
'''
(S/'HANDOFF.md').write_text(handoff)
members=[dict(path=str(p.relative_to(S)),sha256=sha(p),bytes=p.stat().st_size) for p in sorted(S.rglob('*')) if p.is_file() and p.name!='MANIFEST.json']
dump(S/'MANIFEST.json',dict(schema_version=1,author='/root/buffer_hepes',sealed_at=now,files=members,selected_proposals=2,changed_payloads=1,carried_unchanged_payloads=1,source_cases=2,new_source_cases=0,additive_evidence=len(es),independent_review='review/direct-parent-independent-review-v1.json',limitations='Final root composition, whole-source accounting, dependent references and full native checks remain separate.'))
for row in members: assert sha(S/row['path'])==row['sha256']
print(json.dumps(dict(files=len(members),manifest_sha256=sha(S/'MANIFEST.json'),handoff_sha256=sha(S/'HANDOFF.md'),selected={n:sha(S/n) for n in ['proposals.json','decisions.json','evidence.json','case-deltas.json','selected-files.json','validation/receipt.json']})))
