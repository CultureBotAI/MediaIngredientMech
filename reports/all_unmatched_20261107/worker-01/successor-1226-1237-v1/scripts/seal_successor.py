"""Exclusive outer seal after final independent assembly review; no payload writes."""
import collections
import datetime
import hashlib
import json
from pathlib import Path

D=Path(__file__).resolve().parents[1]


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    manifest=D/'MANIFEST.json'
    assert not manifest.exists()
    required=['HANDOFF.json','HANDOFF.md','cores/final/SELECTION.json','cores/final/decisions.json','cores/final/proposals.json','cores/final/evidence.json','reviews/skeptical/final-assembly-review-v1.json']
    for name in required:assert (D/name).is_file(),name
    paths=sorted(D.rglob('*'))
    assert not any(p.is_symlink() for p in paths)
    files=[{'path':str(p.relative_to(D)),'sha256':sha(p),'bytes':p.stat().st_size} for p in paths if p.is_file()]
    hashes=collections.defaultdict(list)
    for row in files:hashes[row['sha256']].append(row['path'])
    result={'schema_version':1,'sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':'reports/all_unmatched_20261107/worker-01/successor-1226-1237-v1','source_head':'26445f23b5a905ac26d864acfbd658570c88769c','publication_branch':'review/all-unmatched-w01-source-review-20261107','scope':'Report-only authorized #1226 exact76-entry/66-payload provenance correction and #1237 four-proposal scientific successor; all188 source cases and76 proposal IDs retained.','active_handoff':{'path':'HANDOFF.json','sha256':sha(D/'HANDOFF.json')},'active_selection':{'path':'cores/final/SELECTION.json','sha256':sha(D/'cores/final/SELECTION.json')},'independent_final_assembly_review':{'path':'reviews/skeptical/final-assembly-review-v1.json','sha256':sha(D/'reviews/skeptical/final-assembly-review-v1.json')},'member_count':len(files),'unique_content_count':len(hashes),'total_member_bytes':sum(x['bytes'] for x in files),'files':files,'duplicate_content_paths':[{'sha256':h,'paths':ps} for h,ps in sorted(hashes.items()) if len(ps)>1],'symlink_count':0,'excluded':['MANIFEST.json (self-reference; hash reported with published Git head externally)'],'interpretation':['Only cores/final/SELECTION.json selects application candidates; native staging, predecessor input copies, failed attempts and negative controls are evidence, not extra proposals.','Copied historical planner and author manifests retain their original roots/interpretations and do not become outer successor manifests.','No maintained source, shared export, policy, workflow, gate or coordinator composed-candidate changes are authorized by this seal.','New whole-owner content has no inherited scientific/role/export approval. All source and integration holds remain content-bound.'],'published_head_note':'The ordinary Git commit tree binds this seal and its members. Its exact remotely verified head is reported after publication, avoiding a self-referential commit hash.'}
    with manifest.open('x') as f:json.dump(result,f,indent=2,ensure_ascii=False);f.write('\n')
    print(json.dumps({'manifest_sha256':sha(manifest),'members':len(files),'unique_contents':len(hashes),'selection_sha256':sha(D/'cores/final/SELECTION.json')}))


if __name__=='__main__':main()
