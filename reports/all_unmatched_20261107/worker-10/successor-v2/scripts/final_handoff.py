from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,copy
R=Path.cwd();S=R/'reports/all_unmatched_20261107/worker-10/successor-v2';P=R/'.temp/all-unmatched-worker-10/successor-v2';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();load=lambda p:json.loads(p.read_text());now=datetime.now(timezone.utc).isoformat()
def save(p,d):
 with p.open('x') as f:json.dump(d,f,indent=2,ensure_ascii=False);f.write('\n')
def b(p):return {'path':str(p.relative_to(R)),'sha256':sha(p)}
peer=S/'reviews/skeptic/assembly-review-v1.json';review=load(peer);assert review
check=load(S/'native-check-v2-command.json');assert check['exit_code']==0;native_out=load(S/'native-check-v2.stdout');assert native_out['valid_reviews']==1023
baseline=load(P/'preservation-baseline.json');counts={}
for kind in ['old_artifact_files','owners']:
 for name,expected in baseline[kind].items():assert sha(R/name)==expected,name
 counts[kind]=len(baseline[kind])
comparison=R/'.temp/final-preparation-comparison-v1';manifest=load(comparison/'MANIFEST.json')
for x in manifest['files']:assert sha(comparison/x['path'])==x['sha256'],x['path']
assert sha(comparison/'MANIFEST.json')=='b63eef440fb6ca056382f6ac6a899efa4f8629f5f2eb96e6d771858eadfef1b8'
counts['sealed_comparison_files']=len(manifest['files']);assert subprocess.check_output(['git','diff','--name-only','468766d941e35a74eb2de3c95096660987277d9b'],text=True)==''
# Original records and reports are unaffected; all additions have not yet been staged.
save(S/'final-preservation.json',{'at':now,'status':'PASS','counts':counts,'tracked_diff_before_staging':[],'baseline':b(S/'context/preservation-baseline.json'),'old_native_reviews_verified':b(S/'preservation-check.json'),'comparison_and_prior_stock_review':b(S/'comparison-impact.json'),'science_or_release_approval':False})
draft=load(S/'HANDOFF-draft-v1.json');final=copy.deepcopy(draft);final['at']=now;final['status']='Bounded source corrections and final assembly complete; packet ready for authorized ordinary same-branch publication';final['independent_final_assembly']=b(peer);final['validation']['full_native_check_after_metadata_successor']={'command':b(S/'native-check-v2-command.json'),'result':b(S/'native-check-v2.stdout'),'valid_reviews':1023,'scope':'Declared native review scopes only; no role/export approval'};final['final_preservation']=b(S/'final-preservation.json');final['draft_reviewed']=b(S/'HANDOFF-draft-v1.json');final['manifest_path']=str((S/'SHA256SUMS').relative_to(R));final['final_handoff_review_path']=str((S/'reviews/skeptic/final-handoff-review-v1.json').relative_to(R));final['post_publication_receipt_path']=str((P/'completion-receipt.json').relative_to(R));final['publication_note']='A committed handoff cannot embed its own commit hash. Exact ordinary commit/push result and verified remote SHA are recorded in the immutable worker-local post-publication receipt and final coordinator message. This packet is the content-addressed prepublication evidence, not a claim of coordinator acceptance.';save(S/'HANDOFF.json',final)
md='''Worker10 completed the two source-completion corrections recorded in [issue1201](https://github.com/CultureBotAI/MediaIngredientMech/issues/1201#issuecomment-6718398061), with separate author-independent science and final assembly review. The selected successor contains188 cases and128 payloads: only cases143/187 change, one ISP4 payload is replaced, and186 other decisions plus127 payloads remain exact.

- C-001: the authentic UNMAPPED_0123 ISP4 owner has the complete nine-input JCM58 formulation. All four nested trace inputs are retained without flattening. The correct1188 parent removal and all earlier history remain.
- C-002: the positive J209/M98-5 source bridge binds case187 to the existing case21 carbonate/CO2 stock. That stock and the pure-carbonate alias-rejection payload remain unchanged. No duplicate owner or guessed percentage basis, carrier, hydrate or CO2 endpoint.
- Full188 structural accounting passed. Native strict validation covered273 authentic owners and128 proposals;128 guarded scratch copies roundtripped;3039 in-memory records passed partonomy. The full native review check passed1023 declared review scopes. No maintained data was written.

Use `decisions.json`, `evidence.json`, `proposals.json`, and `selection.json` in this directory as the new selected ledger. They explicitly supersede the old ISP4 proposal, preserve its bytes historically, and select the carbonate stock once with both case backlinks. `issue-linked-lineage.json` and `subagent-scopes.json` retain exact filing, source, author and reviewer attribution.

The selected native pair is [YAML](../../../../reviews/structured/20261108T072434Z-w10-completeness-c001-c002-owner-notes/review.yaml) / [Markdown](../../../../reviews/structured/20261108T072434Z-w10-completeness-c001-c002-owner-notes/review.md). It covers316 exact targets, distinguishes fresh science from preserved provenance, and retains one open trace-stock integration dependency. The first pair remains immutable; its successor corrects83 new-owner target notes only. Separate science and final assembly evidence are under `reviews/skeptic/`.

The19-family comparison remains sealed:526 files and96 selected entries were reverified, with zero affected assigned inputs. Its handoff SHA256 is `e65d989fa6b950e8b56096c3b50bd667c3576bf0f66c7ae7a4bc7f0c4b3b8840`; manifest SHA256 is `b63eef440fb6ca056382f6ac6a899efa4f8629f5f2eb96e6d771858eadfef1b8`. JCM58's matching provisional W06entry548 is outside the frozen19-family assignment and needs separate coordinator dedup/filing and exact reconciliation before a stock reference is resolved. No new trace stock was minted or adopted.

The coordinator owns final independent review of the new published head and any owner application. Existing EDTA, alias, source, role and export holds remain. No PR, merge, downstream rebuild, paid provider or additional external session occurred. All1880 old source artifacts,2956 maintained owner files and2042 prior canonical review files were preserved. Historical rejection and coordinator verification of pre-existing authorization remain exact; no fresh user approval is invented.

`SHA256SUMS` covers the successor artifacts and both new native pairs, excluding itself. `HANDOFF.json` binds the exact scientific/core/validation/review hashes. The final verified remote SHA and ordinary publication receipts are saved in `.temp/all-unmatched-worker-10/successor-v2/completion-receipt.json` after commit/push; the committed handoff cannot contain its own commit hash. Leave this branch and worktree intact for coordinator review.
'''
with (S/'HANDOFF.md').open('x') as f:f.write(md)
save(S/'progress-final.json',{'at':now,'phase':'bounded source correction complete; final seal/publication follows','cases':188,'fresh_changed_cases':2,'unaffected_decisions':186,'selected_payloads':128,'changed_payloads':1,'unchanged_payloads':127,'independent_science':b(S/'reviews/skeptic/scientific-review-v1.json'),'independent_assembly':b(peer),'native_reviews_valid':1023,'handoff':b(S/'HANDOFF.json'),'coordinator_new_head_review_pending':True,'scientific_release_approval':False})
print(json.dumps({'handoff_json':b(S/'HANDOFF.json'),'handoff_md':b(S/'HANDOFF.md'),'preservation':counts},indent=2))
