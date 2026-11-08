"""Seal append-only canonical packet after exact independent assembly review."""
from pathlib import Path
import json,hashlib,datetime,shutil
R=Path.cwd();O=R/'.temp/columbia-controls-successor-v1';S=R/'reports/all_unmatched_20261107/worker-10/successor-v7';load=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();now=lambda:datetime.datetime.now(datetime.timezone.utc).isoformat();cap=lambda p:{'path':str(p.relative_to(R)),'sha256':sha(p)}
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
# Reviewer chooses its own filename and seals before this script is run.
reviewfile=O/'final-skeptic/final-assembly-review-v1.json';review=load(reviewfile)
assert review.get('verdict')=='pass_with_limitations' and review.get('findings')==[],reviewfile
shutil.copytree(O/'final-skeptic',S/'reviews/final-skeptic')
for p in (O/'final-skeptic').rglob('*'):
 if p.is_file():assert sha(p)==sha(S/'reviews/final-skeptic'/p.relative_to(O/'final-skeptic'))
h=load(S/'HANDOFF-author.json');h['status']='complete_exact_candidate_reviewed_ready_for_ordinary_publication';h['finalized_at']=now();h['review_stage_interpretation']='Quoted source-review limitations retain their original author-v3 stage. Exact final-core and final native assembly completion is established only by the later separately bound receipts; future distinct published-head review remains with coordinator.';h['author_handoff']=cap(S/'HANDOFF-author.json');h['final_assembly_review']=cap(S/'reviews/final-skeptic/final-assembly-review-v1.json');h['review_receipts'].append(h['final_assembly_review']);h['seal']='MANIFEST.json lists every canonical successor member plus native review pair, excluding MANIFEST.json and SHA256SUMS themselves. SHA256SUMS additionally binds MANIFEST.json. Actual future published Git head is recorded separately in private publication receipt.';save(S/'HANDOFF.json',h)
md='''Worker10 completed this bounded successor to `c66d6d3665368fe1ae8986fb7c16340a103582c1`. Select [selection.json](selection.json); [HANDOFF.json](HANDOFF.json), [MANIFEST.json](MANIFEST.json), and [complete-bridge.json](complete-bridge.json) bind the exact full result. Earlier author cores, reviews, failures and all prior successor seals remain immutable.

The authentic existing `Columbia_Blood_Agar_Base / UNMAPPED_0118` receives a genuine dependent edit from maintained before `29ed63a00d3f4f7a1652beee549526d625eef231f29b40691bd128d2f7608324`. Its generic identity, scope, statistics and five original history events remain. Both vendor strings and original sources are retained as `REJECTED_LABEL` on this residual owner. The source-supported BD-Difco string is added to the separate Difco dry-base proposal, coupled to the exact existing-owner correction; new vendor destinations retain null maintained preimages.

Three later Difco dry contexts are supported; four CM331 prepared-base contexts remain held with their literal quantities. Seven context rows are separate from the assigned cohort. The unchanged W10 Oxoid origin and W04's actual current `7cc3c2540fd1b55281c6f5551f13a90a1e7916b1` / payload `4a3d54349a5c37167c2e13823d67808114c84212cea7dadc876334d4b10904d7` are bound read-only. Source 300 retains variable quantity and printed CM0331; source 921 retains 39 g without a historical catalogue claim. **Coordinator composition and review of one Oxoid nominal-family candidate remain required.** Neither original is a second installation instruction, and this packet chooses no arbitrary winning owner.

Controls 941 and 955 change only component completeness `PARTIAL` to `UNKNOWN`, plus truthful native history. Each literal named UNMAPPED part, method, strength, pH, quantities and chemical/source uncertainty remains. Controls 280/938 and complete named-input Wolfe/Hutner lists remain unchanged. Receiving-medium water is not stock-carrier evidence. Older PARTIAL wording stays verbatim in historical reassessments and is explicitly marked as historical.

All 188 cases, 304 occurrences and 127 original proposal IDs remain. One new dependent existing-owner correction gives 128 selected proposals. Three original payloads change, 124 remain byte-identical; four original proposal metadata objects and four cases change, leaving 123 proposal objects and 184 whole case decisions exact. All 1,218 old evidence objects remain; 11 new scoped entries give 1,229. No new vendor identity or assigned source case is minted. Prior carbonate/calf/ISP4 and other retained corrections remain selected.

Separate actual subagents reviewed full changed science, complete lineage and native behavior. Their original authorship conflicts are disclosed in [subagent-scopes.json](subagent-scopes.json): the original buffer and bio authors provide technical/lineage review, while an author-independent scientist provides source review. All 128 payloads pass closed schema; four full payloads reproduce real native history-helper and guarded byte roundtrips; both 3,037-record overlays pass partonomy. Precise identifier/alias/projection and negative controls pass. Final full-case structural accounting passes. The native 325 target / 325 assessment pair binds 1,053 inputs and distinguishes bounded fresh science from inherited retention. The native wrapper is root self-review; final exact assembly is separately reviewed.

Two author-draft metadata clarifications and two wrapper validation attempts are retained with actual rechecks; no source or payload was changed to bypass validation. The public issue decisions were filed before this work; this worker made no GitHub issue/comment changes. No source/whole-owner/role/export acceptance follows from this packet. Root arranges the distinct published-head review and final integration. Ordinary nonforce publication receipts and final remote head are retained under `.temp/columbia-controls-successor-v1/`.
'''
with (S/'HANDOFF.md').open('x') as f:f.write(md)
shutil.copy2(Path(__file__),S/'scripts'/Path(__file__).name)
files=sorted(p for p in S.rglob('*') if p.is_file());native=load(S/'native-v3/saved-pair.json')['files'];files += [R/x['path'] for x in native]
manifest={'schema_version':'1','sealed_at':now(),'path_root':'repository','member_count':len(files),'files':[cap(p)|{'bytes':p.stat().st_size} for p in files],'excludes':['reports/all_unmatched_20261107/worker-10/successor-v7/MANIFEST.json','reports/all_unmatched_20261107/worker-10/successor-v7/SHA256SUMS'],'prior_seals_rewritten':False,'published_head':'Recorded after ordinary commit/push in private publication receipt; no invented future head.'};save(S/'MANIFEST.json',manifest)
with (S/'SHA256SUMS').open('x') as f:
 for p in files+[S/'MANIFEST.json']:f.write(sha(p)+'  '+str(p.relative_to(R))+'\n')
for x in manifest['files']:assert sha(R/x['path'])==x['sha256']
print(json.dumps({'members':len(files),'handoff':cap(S/'HANDOFF.json'),'manifest':cap(S/'MANIFEST.json'),'checksums':cap(S/'SHA256SUMS')},indent=2))
