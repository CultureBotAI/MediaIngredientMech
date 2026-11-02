from pathlib import Path
import importlib.util,json,hashlib,sys
RUN=Path(__file__).resolve().parent
W=RUN/"step7c"
path=W/"scripts/validate_sssom_invariants.py"
spec=importlib.util.spec_from_file_location("actual_b4",path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
m.KGM_TRANSFORMS_DIR=Path("/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe/data/transformed/ontologies")
def sha(p):
 h=hashlib.sha256()
 with p.open("rb") as f:
  for b in iter(lambda:f.read(8*1024*1024),b""):h.update(b)
 return h.hexdigest()
inputs={str(path):sha(path)}; available={}
for prefix in sorted(m.B4_PREFIXES):
 p=m.KGM_TRANSFORMS_DIR/(prefix.lower()+"_nodes.tsv");available[prefix]=p.is_file()
 if p.is_file():inputs[str(p)]=sha(p)
results={}
for n,p in [("canonical",W/"mappings/ingredient_mappings.sssom.tsv"),("candidate",W/"output/step7c-native-candidate-v2/candidate.sssom.tsv")]:
 inputs[str(p)]=sha(p); _,_,rows=m._read_sssom(p);present={};rejects=list(m.evaluate_rule_b4(rows,transforms_present=present));results[n]={"rows":len(rows),"rejects":rejects,"transforms_present":present}
assert all(sha(Path(p))==h for p,h in inputs.items())
result={"scope":"Native evaluate_rule_b4 with explicit read-only existing kg-microbe transformed ontology path; does not change the standard QC invocation or claim missing prefixes were checked.","inputs":inputs,"available_prefixes":available,"results":results,"input_bytes_unchanged":True}
p=RUN/"step7c-b4-transformed-results.json"
with p.open("x") as f:json.dump(result,f,indent=2);f.write("\n")
print(json.dumps({"available":available,"results":{k:{"rows":v["rows"],"reject_count":len(v["rejects"]),"transforms_present":v["transforms_present"]} for k,v in results.items()},"report_sha256":sha(p)},indent=2))
