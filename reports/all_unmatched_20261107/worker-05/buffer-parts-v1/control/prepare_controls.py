from pathlib import Path
import json
W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';S=W/'.temp/w05-buffer-parts-v1';P=B/'buffer-parts-v1';O=B/'tellurium-polypeptone-v1'
for name in ['assemble.py','validate_selected.py','preserve_final.py']:
    text=(O/'control'/name).read_text()
    text=text.replace("O=B/'postseal-source-corrections-v1'", "O=B/'tellurium-polypeptone-v1'")
    text=text.replace("P=B/'tellurium-polypeptone-v1'", "P=B/'buffer-parts-v1'")
    text=text.replace("S=W/'.temp/w05-tellurium-polypeptone-v1'", "S=W/'.temp/w05-buffer-parts-v1'")
    text=text.replace('76bca688b4f55e8bdf791079df8d4156cded6c4c','0bac12cabfd1f67f212631d8eef9aa46379f6b41')
    text=text.replace('tellurium_polypeptone','buffer_parts')
    text=text.replace('previous_supplement_independent_review','previous_buffer_parts_independent_review')
    text=text.replace('Full exact declared source-origin supplement, changed Polypeptone and retained Tellurium/Hipolypepton scopes; actual case/payload/primary bindings in receipt.','Full exact two-case/four-payload buffer source supplement; corrected current payloads retained unchanged with actual source/filing/private-history/publication chronology.')
    text=text.replace('Authorship-separated source science review, with unresolved Japanese historical product bridge and all owner/source/role/export limits retained. No coordinator combined-union approval.','Authorship-separated complete buffer source/partonomy review. Whole-stock strength/source pH preserved; composition and source-qualified identity limits retained. No guessed component, owner union or source/role/export approval.')
    q=S/'control'/name;assert not q.exists();q.write_text(text)
selection={lane:{kind:str((P/lane/(kind+'.json')).relative_to(W)) for kind in ['decisions','proposals','evidence']} for lane in ['hepes','tris']}
(S/'control/selection.json').write_text(json.dumps(selection,indent=2)+'\n')
print(json.dumps(selection))
