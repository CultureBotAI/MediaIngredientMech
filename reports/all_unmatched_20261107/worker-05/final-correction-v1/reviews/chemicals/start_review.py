from pathlib import Path
import json,hashlib,datetime,yaml
W=Path.cwd();L=Path(__file__).resolve().parent;A=W/'.temp/w05-final-correction-v1/chemicals'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(n,d):(L/n).write_text(json.dumps(d,indent=2,ensure_ascii=False)+'\n')
ps=json.loads((A/'proposals-v3.json').read_text())
inputs=['decisions-v2.json','proposals-v3.json','evidence-v1.json','primary-case-conclusions-v1.json','finding-dispositions-v3.json','FINAL-MANIFEST-v1.json','conditional-family-matrix-v1.json']
save('preflight.json',{'started_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/materials_research','independence':'Independent of chemical primary and original source proposal authors; materials author role is disjoint and receives no approval here.','inputs':[{ 'path':str(A/n),'sha256':sha(A/n)} for n in inputs],'coverage_required':{'cases':67,'complete_payloads':57},'status':'in progress'})
targets=[]
for p in ps:
 f=W/'.temp/w05-final-correction-v1'/Path(p['after_capture']['path']).relative_to('final-correction-v1');assert sha(f)==p['after_capture']['sha256'];d=yaml.safe_load(f.read_text())
 targets.append({'target_id':p['proposal_id'],'path':str(f.relative_to(W)),'kind':'source','record_class':'Ingredient','label':d['preferred_term'],'selector':'Exact complete isolated report-only successor payload','ownership_note':'Maintained owner '+p['owner_path']+'; independent author-separated review, no application or release approval.'})
save('native-targets.json',{'targets':targets})
src=[A/'read-text/ROOT-jcm-628.txt',A/'read-text/ROOT-jcm-629.txt']
save('finding-001-initial.json',{'finding_id':'W05-FINAL-SKEPTIC-CHEM-001','recorded_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root/materials_research','status':'open','severity':'minor','scope':'Report scientific conclusion; selected payloads are correct on this point.','targets':['CM_NAME:0aaa9e92307c43baf12b66d61715b0bb66b69a915820768fc229f570b35e73a0','R1193-P-bottom-628','R1193-P-bottom-629'],'input':{'path':str(A/'primary-case-conclusions-v1.json'),'sha256':sha(A/'primary-case-conclusions-v1.json'),'locator':'case_reviews[0].assessment'},'observed':'The assessment says the preparations are FeS/agarose versus zero-valent iron/agarose. JCM 629 instead explicitly reuses Medium 628 with artificial saltwater replacing Modified Wolfe mineral solution. Both bottom preparations contain the washed FeS preparation.','evidence':[{'path':str(p),'sha256':sha(p)} for p in src],'bounded_fix':'Preserve this initial finding and the original report. Issue a successor primary-conclusions file correcting the distinguishing fact to Modified Wolfe mineral solution versus artificial saltwater, with FeS and agarose in both. Do not change either correct selected payload.','review_limit':'This finding does not yet disposition the remaining cases or payloads.'})
