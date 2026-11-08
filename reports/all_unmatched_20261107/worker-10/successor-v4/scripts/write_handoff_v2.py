"""Select timing-clarified native review without rewriting the first handoff."""
from pathlib import Path
import copy, datetime, hashlib, json
R=Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v4'
load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def bind(p):return {'path':str(p.relative_to(R)),'sha256':sha(p)}
def save(p,value):
 with p.open('x') as f:json.dump(value,f,indent=2,ensure_ascii=False);f.write('\n')
check=load(S/'native-check-v2-command.json');assert check['exit_code']==0
old=load(S/'HANDOFF.json');new=copy.deepcopy(old)
new['at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
new['native_review']=load(S/'native-v2/saved-pair.json')
new['native_complete_review_check']=load(S/'native-check-v2.stdout')
new['native_complete_review_check_receipt']=bind(S/'native-check-v2-command.json')
new['prior_handoff']=bind(S/'HANDOFF.json')
new['native_timing_correction']={'finding':bind(S/'reviews/retention/native-timing-finding-v1.json'),'correction':bind(S/'native-v2/timing-correction.json'),'initial_native_pair':old['native_review'],'old_pair_and_handoff_preserved':True,'science_core_payload_unchanged':True}
new['status']='Authoritative assembled selection after native timing clarification; exact-byte final review and sealing precede ordinary publication, with final receipts included in SHA256SUMS'
new['final_assembly_review_scope']='Both actual independent reviewers recheck this exact timing successor and handoff. Append-only receipts under reviews/retention and reviews/skeptic are bound by SHA256SUMS. Earlier completed assembly receipts remain valid only for their exact historical input bytes.'
new['retained_limits']+=['The original native pair used wrapper-generation timestamps. The selected successor labels started_at as the earliest recorded root assessment milestone, preserves the unknown earlier reading start and attributes independent review times to their own frozen reports. No scientific reassessment or payload change resulted.']
for k in ['authoritative_selection','authoritative_core','complete_bridge','payload','accounting','retained_limits']:
 if k!='retained_limits':assert new[k]==old[k]
save(S/'HANDOFF-v2.json',new)
text=(S/'HANDOFF.md').read_text().replace('[HANDOFF.json](HANDOFF.json)','[HANDOFF-v2.json](HANDOFF-v2.json)')
text+='\nThis is the authoritative handoff successor. The original HANDOFF and native pair remain historical, unchanged observations. Independent reviewer finding `SV4-NATIVE-TIMING-001` identified that the first native timestamps described wrapper generation without saying so. The new canonical review `'+new['native_review']['review_id']+'` labels the earliest recorded root assessment milestone, acknowledges that earlier reading start is unknown, and attributes independent reviewer timing to their frozen reports. It changes no target, scientific assessment, candidate or core decision. The new complete native check passes with '+str(new['native_complete_review_check']['valid_reviews'])+' valid declared-scope reviews. See [timing-correction.json](native-v2/timing-correction.json) for exact retained preimages.\n'
with (S/'HANDOFF-v2.md').open('x') as f:f.write(text)
print(json.dumps({'handoff':bind(S/'HANDOFF-v2.json'),'markdown':bind(S/'HANDOFF-v2.md'),'native':new['native_review']['review_id']},indent=2))
