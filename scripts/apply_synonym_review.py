#!/usr/bin/env python3
"""Apply the synonym-review findings to data/curated/mapped_ingredients.yaml.

Three deterministic transforms over MAPPED CHEBI-mapped records (synonyms only —
never touches ontology_id / ontology_label):

  1. FIX defects — drop role-text leaked into synonyms ("carbon source: …",
     "(an)aerobic catabolization: …", "Role: …") and repair/drop malformed
     entries (leading stray quote or unbalanced "(").
  2. RETYPE formula/hydrate-notation variants mis-typed as EXACT_SYNONYM →
     HYDRATE_FORM (when water is present) or ALTERNATE_FORM (formula-only).
  3. ENRICH — add CHEBI exact-synonyms (from the local OAK chebi.db) that the
     record is missing, typed EXACT_SYNONYM, source chebi_synonym_review.

`--apply` writes via the canonical save_yaml; default is a dry-run report.
"""
from __future__ import annotations
import argparse, re, sqlite3, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
import yaml
from mediaingredientmech.utils.yaml_handler import save_yaml

COLL = Path("data/curated/mapped_ingredients.yaml")
CHEBI_DB = f"sqlite:///{Path.home()/'.data'/'oaklib'/'chebi.db'}"

def norm(s): return " ".join(str(s).strip().split()).casefold()

ROLE_LEAK = re.compile(r'^\s*((an)?aerobic\s+catabolization|carbon\s+source|nitrogen\s+source|energy\s+source|role)\s*:', re.I)
# formula + hydrate/notation marker (mirrors the review's classifier)
FORMULA = re.compile(r'[A-Z][a-z]?\d')
NOTATION = re.compile(r'(H2O|H₂O|H\sO|[·・]|\bx\b|\.\s*\d*\s*H)')
WATER = re.compile(r'(H2O|H₂O|H\sO)')

def chebi_exact(con, cid):
    rows = con.execute(
        "SELECT predicate,value FROM statements WHERE subject=? AND predicate IN "
        "('rdfs:label','oio:hasExactSynonym')", (cid,)).fetchall()
    lab = next((v for p,v in rows if p=='rdfs:label'), None)
    exact = [v for p,v in rows if p=='oio:hasExactSynonym']
    return lab, exact

def run(apply: bool):
    con = sqlite3.connect(f"file:{Path.home()/'.data'/'oaklib'/'chebi.db'}?mode=ro", uri=True)
    data = yaml.safe_load(COLL.read_text())
    n_dropped=n_repaired=n_retyped=n_enriched=0
    EXACT_TYPES={"EXACT_SYNONYM","EXACT","RELATED_SYNONYM","RELATED","SYSTEMATIC_NAME"}
    for r in data["ingredients"]:
        if r.get("mapping_status")!="MAPPED": continue
        om=r.get("ontology_mapping") or {}
        cid=om.get("ontology_id")
        if not (cid and str(cid).startswith("CHEBI:") and om.get("ontology_source")=="CHEBI"): continue
        syns=r.get("synonyms") or []
        kept=[]
        for s in syns:
            txt=s.get("synonym_text",""); st=s.get("synonym_type")
            # 1. role-leak -> drop ONLY when typed as a chemical synonym (the
            # legitimate RAW_TEXT "Role: …" CultureMech provenance is left alone —
            # the role-extraction pipeline reads it).
            if st in EXACT_TYPES and ROLE_LEAK.search(txt): n_dropped+=1; continue
            # 1. malformed -> repair or drop
            if txt[:1] in {'"',"'","`"}:
                txt=txt.lstrip('"\'`').strip(); s["synonym_text"]=txt; n_repaired+=1
            elif txt.startswith("(") and ")" not in txt:
                txt=txt.lstrip("(").strip(); s["synonym_text"]=txt; n_repaired+=1
            # 2. retype formula/hydrate variants mis-typed as exact/related
            if st in EXACT_TYPES and FORMULA.search(txt) and NOTATION.search(txt):
                s["synonym_type"]="HYDRATE_FORM" if WATER.search(txt) else "ALTERNATE_FORM"
                n_retyped+=1
            kept.append(s)
        # collapse only EXACT-duplicate synonym texts (e.g. a repair that recreates
        # an existing string, or a pre-existing identical dup) — case/whitespace/
        # unicode variants are DISTINCT and kept untouched (out of scope here).
        seen=set(); dedup=[]
        for s in kept:
            txt=s.get("synonym_text","")
            if txt and txt not in seen: seen.add(txt); dedup.append(s)
        r["synonyms"]=dedup
        # 3. enrich with missing CHEBI exact-synonyms
        lab, exact = chebi_exact(con, cid)
        have={norm(s.get("synonym_text")) for s in dedup} | ({norm(lab)} if lab else set())
        for e in exact:
            if norm(e) not in have:
                dedup.append({"synonym_text":e,"synonym_type":"EXACT_SYNONYM","source":"chebi_synonym_review"})
                have.add(norm(e)); n_enriched+=1
    con.close()
    print(f"role-leak/Role dropped:   {n_dropped}")
    print(f"malformed repaired:       {n_repaired}")
    print(f"formula variants retyped: {n_retyped}")
    print(f"CHEBI exact-syns added:   {n_enriched}")
    if apply:
        save_yaml(data, COLL, validate=True, target_class="IngredientCollection")
        print(f"\nSaved {COLL}")
    else:
        print("\n(dry-run — no changes written; pass --apply)")

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--apply",action="store_true")
    run(ap.parse_args().apply)
