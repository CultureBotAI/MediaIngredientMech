"""Report-local exact-predecessor preservation path, not a maintained gate change."""
from pathlib import Path
import hashlib

def validate_retained_payloads(proposals, predecessor_proposals, artifact_root):
    failures=[]; selected={p['proposal_id']:p for p in proposals}
    if len(selected)!=len(proposals):failures.append({'code':'DUPLICATE_PROPOSAL_ID'})
    for before in predecessor_proposals:
        pid=before['proposal_id']; after=selected.get(pid)
        if after is None:failures.append({'proposal_id':pid,'code':'MISSING_PREDECESSOR'});continue
        path=Path(artifact_root)/after['after_capture']['path']
        actual=hashlib.sha256(path.read_bytes()).hexdigest()
        if actual!=after['after_capture']['sha256']:failures.append({'proposal_id':pid,'code':'DECLARED_CAPTURE_MISMATCH'})
        if actual!=before['after_capture']['sha256']:failures.append({'proposal_id':pid,'code':'RETAINED_PAYLOAD_BYTES_CHANGED','expected':before['after_capture']['sha256'],'actual':actual})
        for key in ['case_ids','owner_path','kind','before_sha256']:
            if after.get(key)!=before.get(key):failures.append({'proposal_id':pid,'code':'PREDECESSOR_BINDING_CHANGED','field':key})
    return failures
