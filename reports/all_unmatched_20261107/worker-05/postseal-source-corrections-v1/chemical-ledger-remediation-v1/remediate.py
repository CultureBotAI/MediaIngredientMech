"""Four report-string corrections; the sealed primary tree is read-only."""
from pathlib import Path
import copy,datetime,difflib,hashlib,json
OUT=Path(__file__).parent
S=OUT.parent
OLD=S/'chemicals'
SOURCE=OLD/'family-applicability-audit-v1.json'
FINDING=S/'review/family-audit/new-findings-v1.json'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def binding(p):return {'path':str(p),'sha256':sha(p)}
def dump(n,obj):
 p=OUT/n;assert not p.exists(),p;p.write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n');return p
assert sha(SOURCE)=='91031fef92918eab50f2a1ea411d78f413dd877ebb904797a189ba16ec93f6dd'
assert sha(FINDING)=='ee9a8646e93cffddff8e167bd65e8b9aee2c5f272979c1d5283fc51c717269c0'
manifest=json.loads((OLD/'FINAL-MANIFEST-v1.json').read_text())
before_inventory={str(p.relative_to(OLD)):sha(p) for p in OLD.rglob('*') if p.is_file()}
assert len(manifest['files'])==39
for f in manifest['files']:assert sha(OLD/f['path'])==f['sha256'],f['path']
before=json.loads(SOURCE.read_text());after=copy.deepcopy(before)
changes={
 2:'The NBRC1321 cyanocobalamin stock is W08 frozen entry 747. Its source explicitly names cyanocobalamin, while the JCM403 generic B12 comparison remains unresolved as a possible same preparation. The existing W05 thiamine403 stock is a different solute and is not implicated by name or medium number alone. No B12 owner is created or changed here.',
 8:'W05 Polypeptone already uses a generic local identity and rejects the three unsupported Hipolypepton product aliases. Bare historical labels do not establish a BD/Japanese product. The competing W06 whole-owner proposal, frozen entry 540, requires coordinator reconciliation; this audit chooses no winner and does not merge its history into W05.',
 11:'The Hutner DSMZ590/1144 union is parent-authored. The source comparison supports one nominal preparation while retaining both 3.335/3.34 g calcium literals, the nested Metals44 list, pH7 to6.8 adjustment, approximately7.3 g KOH, and NaOH-or-H2SO4 details. Historical malformed molybdate literals remain ungrounded; they do not establish alternative chemical identities. COMPLETE refers to the immediate source list, not complete molecular grounding. Comparison to JCM900/979 remains separately unresolved. This audit does not duplicate that union.',
 20:'The W10 JCM1303 heat-inactivated calf-serum proposal shares MediaDive2061 source continuity with the existing Bovine_Calf_Serum owner. Reconcile that continuity and the broader/Gibco occurrences before adding or narrowing an owner; omitted heat metadata or a new filename does not establish a different material. No W05 selected candidate is this source. The calf-blood wording issue in comment6719103915 concerns a separate TOGO M2854 proposal and remains in the distinct additional-comment disposition.'
}
finding=json.loads(FINDING.read_text()); recorded=[]
for reproduction in finding['reproduction']:
 i=reproduction['matrix_row_index'];assert before['rows'][i]['applicability_assessment']==reproduction['authored_before']
 after['rows'][i]['applicability_assessment']=changes[i]
 recorded.append({'json_pointer':f'/rows/{i}/applicability_assessment','finding_ids':before['rows'][i]['finding_ids'],'entry_indices':before['rows'][i]['entry_indices'],'before':reproduction['authored_before'],'after':changes[i]})
def differences(a,b,path=''):
 if type(a)!=type(b):return [path]
 if isinstance(a,dict):
  assert set(a)==set(b)
  return [p for k in a for p in differences(a[k],b[k],path+'/'+k)]
 if isinstance(a,list):
  assert len(a)==len(b)
  return [p for i,(x,y) in enumerate(zip(a,b)) for p in differences(x,y,path+'/'+str(i))]
 return [] if a==b else [path]
actual=differences(before,after);expected=[x['json_pointer'] for x in recorded]
assert actual==expected,(actual,expected)
new=dump('family-applicability-audit-v2.json',after)
diff=OUT/'family-applicability-v1-to-v2.diff';assert not diff.exists()
diff.write_text(''.join(difflib.unified_diff(SOURCE.read_text().splitlines(True),new.read_text().splitlines(True),fromfile=str(SOURCE),tofile=str(new))))
after_inventory={str(p.relative_to(OLD)):sha(p) for p in OLD.rglob('*') if p.is_file()}
assert before_inventory==after_inventory
receipt=dump('remediation-receipt-v1.json',{
 'finding_id':'W05-POSTSEAL-FAMILY-REVIEW-001','author':'/root/chemicals_research','llm_assisted':True,
 'timestamp':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'reported_before_fix':'Parent /root reported the independent finding to the coordinator/user before authorizing this isolated successor.',
 'finding':binding(FINDING),'predecessor_ledger':binding(SOURCE),'successor_ledger':binding(new),'diff':binding(diff),
 'matrix':finding['matrix'],'issue_comment_binding':finding['comment_binding'],'exact_field_changes':recorded,
 'structural_verification':{'changed_json_pointers':actual,'expected_field_change_count':4,'observed_field_change_count':len(actual),'source_disposition_objects_unchanged':True,'all_other_ledger_fields_unchanged':True,'sealed_39_manifest_members_unchanged':True,'entire_sealed_tree_file_count':len(before_inventory),'entire_sealed_tree_unchanged':True},
 'scope':'Ledger descriptions only. D/P/E, YAMLs, source_disposition objects, row IDs, cases, source captures, ownership and scientific decisions remain unchanged. The full successor keeps original ledger metadata verbatim; this receipt records the new authorship and ancestry.',
 'sealed_primary_manifest':binding(OLD/'FINAL-MANIFEST-v1.json'),'independent_review':'pending exact successor review',
 'old_tree_before_and_after_inventory':before_inventory})
handoff=OUT/'HANDOFF.md';handoff.write_text('Corrected four applicability descriptions only: entry747 is W08; competing Polypeptone entry540 is W06; the Hutner union is DSMZ590/1144; BIO-F03 concerns JCM1303 calf serum and MediaDive2061 continuity, separately from the calf-blood comment.\n\nThe full selected successor is `family-applicability-audit-v2.json`. Exact field changes and ancestry are in `remediation-receipt-v1.json`. The 39 sealed primary members and the complete prior tree remain unchanged. No scientific payload, D/P/E fragment, source disposition, case, owner or hold changed. Independent review is separate.\n')
files=[{'path':str(p.relative_to(OUT)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(OUT.rglob('*')) if p.is_file()]
seal=dump('FINAL-MANIFEST-v1.json',{'status':'primary_complete_independent_review_pending','author':'/root/chemicals_research','finding_id':finding['finding_id'],'selected_ledger':'family-applicability-audit-v2.json','files':files,'preservation_receipt':binding(receipt),'no_payload_or_core_changes':True})
print(json.dumps({'selected_ledger':binding(new),'manifest':binding(seal),'receipt':binding(receipt),'changed_fields':actual,'preserved_files':len(before_inventory)},indent=2))
