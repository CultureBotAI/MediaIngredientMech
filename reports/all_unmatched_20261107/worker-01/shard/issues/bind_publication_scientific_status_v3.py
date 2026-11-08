from pathlib import Path
import json,re,hashlib,datetime
I=Path('reports/all_unmatched_20261107/worker-01/shard/issues');A=I/'publication-v2';O=I/'publication-v3';O.mkdir();B='https://github.com/CultureBotAI/MediaIngredientMech/blob/review/all-unmatched-w01-source-review-20261107/reports/all_unmatched_20261107/worker-01/shard/'
L=lambda t,p:f'[{t}]({B}{p})'
review=I.parent/'independent_review/final-188-scientific-review-v1.json';a=json.loads(review.read_text());assert a['final_scoped_review_complete'] and a['case_count']==188 and a['proposal_count']==76
proof=L('final independent scientific review','independent_review/final-188-scientific-review-v1.json');catalog=L('native full-catalog regression','validation/full-catalog-partonomy-corrected-v3.json');projection=L('isolated pinned-producer projection','validation/native-generated-predicates-corrected-v3.json')
for p in A.glob('*.md'):
 s=p.read_text()
 if '1159' in p.name:
  for old in ['Author successor; final independent disposition pending.','Author successors; final projection and independent disposition pending.','Final assembled uniqueness, backlinks and partonomy rereview pending.','Author/coordinator corrections independently reproduced; final successor disposition pending.']:
   s=s.replace(old,'Corrected and independently rereviewed in the final isolated artifacts; see final scientific receipt below.')
  s=s.replace('No full-shard approval, inherited hold release, merge or issue closure is claimed by this draft.','The '+proof+' covers all 188 source-case outcomes and 76 exact isolated proposals, and confirms IR1–12 plus the five coordinator corrections. It retains specific source and owner limitations. No maintained integration, inherited hold release, merge or issue closure is claimed.')
 elif '1163' in p.name:
  s=s.replace('The independent final rereview and full assembled-ledger receipt must be cited before treating this as final coordinator acceptance.','The '+proof+' confirms all nine cases and their seven proposals, plus the complete 78-case concentration allocation. The '+catalog+' checks the final combined overlay. Coordinator acceptance remains separate.')
 elif '1164' in p.name:
  s=s.replace('Final resolution requires the coordinator’s actual pinned-producer projection receipt across all final proposals and the separate independent rereview, including registry sibling rows. The helper-level predicate assertion in the author review is not presented as that full producer replay.','The '+projection+' invokes the actual pinned `_row_from_yaml` producer on all 76 isolated payloads with their intended owner filenames. It verifies the broad-parent predicates and exact registry sibling rows; the old wrong tomato predicate is preserved as a negative control. The '+proof+' independently confirms both corrected parent-grade proposals. This is an isolated row-producer replay, not canonical product generation or publication.')
 elif '1166' in p.name:
  s=s.replace('Final active-ledger uniqueness, unioned backlinks and unchanged native full-catalog validation require independent confirmation.','The '+proof+' confirms final active-ledger uniqueness and unioned backlinks; the '+catalog+' validates the complete combined overlay with zero violations.')
 elif '1167' in p.name:
  s=s.replace('Final independent successor and full assembled-catalog checks remain required; no maintained edit, whole-record approval or issue closure is claimed.','The '+proof+' confirms independent rereview of the three exact successors, including native bundle `20261108T050529Z-w01-independent-atmosphere-borax-successors`. The '+catalog+' reports zero violations for the full combined overlay. No maintained edit, whole-record approval or issue closure is claimed.')
 elif '1168' in p.name:
  s=s.replace('Root-owned final integration must also replay all campaign proposals with the same negative control.','The '+catalog+' also replays all 76 campaign proposals: the complete overlay has zero violations, while omitting these three dependencies reproduces exactly three orphan errors.')
  s=s.replace('final independent review and coordinator verification remain required.','the '+proof+' confirms independent review of all three exact dependent payloads, including native bundle `20261108T050529Z-w01-independent-atmosphere-borax-successors`. Coordinator verification remains separate.')
 elif '718' in p.name:
  s=s.replace('Final independent review and coordinator integration govern the proposed corrections.','The '+proof+' confirms the source-case outcomes and exact isolated proposals with their stated limits. Coordinator verification and future maintained integration remain separate.')
 elif p.name.startswith('new-KG'):
  s=s.replace('04:54 UTC','05:05 UTC').replace('publication-dedup-disposition-v2.json','publication-dedup-disposition-v3.json')
 (O/p.name).write_text(s)
plan=json.loads((A/'issue-plan.json').read_text());plan['created_at']=datetime.datetime.now(datetime.UTC).isoformat();plan['state']='scientific dispositions final; publication review and pushed commit permalinks pending';plan['supersedes']=str(A/'issue-plan.json');plan['scientific_review']={'path':str(review),'sha256':hashlib.sha256(review.read_bytes()).hexdigest(),'scope':a['scope'],'verdict':a['verdict']};plan['dedup_receipt']=str(I/'publication-dedup-disposition-v3.json')
for x in plan['actions']:x['body_file']=str(O/Path(x['body_file']).name)
plan['body_sha256']={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in O.glob('*.md')};plan['unfinalized_items']=['Publication artifact rereview and final metadata/branch review.','Replace branch links with the actual pushed reviewed commit before GitHub posting.','No GitHub writes by this agent.']
(O/'issue-plan.json').write_text(json.dumps(plan,indent=2)+'\n')
print('Final scientific statuses bound; ten bodies, branch links pending')
