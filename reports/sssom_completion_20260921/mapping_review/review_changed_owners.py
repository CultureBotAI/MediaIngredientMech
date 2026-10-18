"""Record the explicit mapping-only calls for the 23 changed-owner records.

The selection below is a curator decision after reading the original reports
and current complete rows, not a classifier that infers scientific approval.
"""

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUPPORTED = {
    "3-indolyl_Acetic_Acid.yaml": "Official ChEBI identity, CAS:87-51-4 and 1H-indol-3-ylacetic acid are explicitly supported. The two wrong ethyl-ester labels have been rejected and removed; these are the complete remaining other values.",
    "Dl-mevalonic_Acid.yaml": "The report explicitly supports racemic CHEBI:25351, rac-3,5-dihydroxy-3-methylpentanoic acid and CAS:150-97-0. The unrelated polysaccharide label has been rejected and removed.",
    "Lithocholic_Acid.yaml": "OLS and PubChem evidence explicitly supports CHEBI:16325, 3alpha-hydroxy-5beta-cholan-24-oic acid and CAS:434-13-9. Tricine and berbaman labels are now rejected and absent; the complete remaining row is supported.",
    "Phenyl_Acetic_Acid.yaml": "The report supports neutral phenylacetic acid CHEBI:30745 and CAS:103-82-2. LSM-15166 has been rejected and removed; the CAS token is the sole remaining other value.",
    "Ca_No32.yaml": "The report supports anhydrous calcium nitrate CHEBI:64205, calcium dinitrate and CAS:10124-37-5. All six cadmium-nitrate aliases have been rejected and removed; only the two supported other values remain.",
    "K2s4o6.yaml": "OLS/PubChem evidence explicitly verifies potassium tetrathionate CHEBI:86466, all specific dipotassium-tetrathionate aliases and CAS:13932-13-3. The mapping payload is unchanged by subsequent role curation.",
    "Nitrous_Oxide.yaml": "OLS/PubChem evidence explicitly verifies dinitrogen oxide CHEBI:17045 and every current other token, including the separately reviewed source spelling #N2O and CAS:10024-97-2. Subsequent role curation does not change the mapping payload.",
    "Tetrachloroethene.yaml": "OLS/PubChem evidence explicitly verifies CHEBI:17300, all nine current aliases and CAS:127-18-4. Subsequent role curation does not change the mapping payload.",
    "GYPS.yaml": "The source-specific named mixture remains the same local kgmicrobe.ingredient:gyps identity with empty other. Correcting its sulfur-versus-starch component does not alter this mapping or receive approval from it.",
    "BHI.yaml": "The archived source review supports retaining BHI as local kgmicrobe.ingredient:bhi identity with empty other. Downgrading the separate CultureMech formulation link does not alter or receive approval from this mapping.",
    "TYGVS_Glucose.yaml": "The report documents the imported TYGVS + Glucose label and its local kgmicrobe.ingredient:tygvs_glucose identity with empty other. Component membership is independently reviewed and outside this decision.",
}
WITHHOLD = {
    "Dl-malic_Acid.yaml": "The wrong garciniaxanthone aliases are removed, but DL-Malate remains on a neutral acid row; the original review does not resolve that ion/acid alias scope or the DL-versus-unspecified concept boundary.",
    "4-hydroxyphenyl_Acetic_Acid.yaml": "The aspyrone labels are removed, but 4-Hydroxyphenylacetate remains on a neutral acid row. Ontology synonym text alone does not settle conjugate-base versus acid identity for downstream synonym use.",
    "L-cysteine_Hcl.yaml": "The QSY9 label is removed. Unqualified cysteine hydrochloride aliases remain on an L-specific identity; the report does not establish the stereochemical scope of every remaining source alias.",
    "Na2s2o3.yaml": "Old nonaethylene-glycol labels are removed, but NaS2O3, Na2S2SO3 and the conditional Na2S2O3 (if needed) remain, as explicitly flagged in the original review.",
    "Na2s2o3_X_5_H2o.yaml": "Current other still emits concentration-qualified preparations, a catalog/instruction label and formula typos, explicitly distinguished from clean pentahydrate names in the report.",
    "Sodium_Perchlorate.yaml": "The anhydrous row still emits Sodium perchlorate monohydrate; the original report explicitly rejects that hydrate alias.",
    "Sodium_Perchlorate_Monohydrate.yaml": "The report supports the exact hydrate CAS, but the sibling close row attaches that CAS synonym to an anhydrous target. Preserve the pair pending an explicit mapping and alias-scope review.",
    "Sodium_Succinate_Dibasic.yaml": "Old glycoside aliases are removed; the broader-parent relation and residual same-CAS record boundary still require explicit review, as documented in the report.",
    "Thiamine_pyrophosphate.yaml": "Current other still carries chloride-specific names and CAS inherited from the earlier salt grounding, despite the chloride-free target; the original report explicitly flags this mismatch.",
    "Thiosulfate.yaml": "The original report lists ester and plural RELATED_SYNONYM values, but does not resolve the inorganic source-versus-ester class meaning or justify those values as same-subject synonyms.",
    "Trisodium_Citrate.yaml": "Na2-citrate remains an active other token against trisodium citrate; rejecting Citric Acid only partially resolved the reported salt-scope defect (#704).",
    "Arsenate.yaml": "The arsenite aliases were rejected, and the report supports the remaining arsenate names. A concurrent trait correction requires an explicit refreshed decision, supplied separately in the final mapping review.",
}


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, required=True)
    args = parser.parse_args()
    data = args.inventory.read_bytes()
    if (
        hashlib.sha256(data).hexdigest()
        != "09b44134985347b8f4e39f81ce59d5fba57034091019668f815f4609f85b810a"
    ):
        raise ValueError("Changed inventory; the explicit scientific calls require a fresh review")
    inventory = json.loads(data)
    selected = [
        r
        for r in inventory["rows"]
        if r["triage_cohort"] == "changed_owner_record_requires_mapping_scoped_refresh"
    ]
    for entry in selected:
        name = Path(entry["owner"]).name
        entry["disposition"] = "SUPPORTED" if name in SUPPORTED else "WITHHOLD"
        entry["reason"] = SUPPORTED.get(name) or WITHHOLD[name]
        entry["original_report_text"] = Path(entry["review_report"]["path"]).read_text()
        entry.pop("historical_matching_mapping_assertions", None)
    if len(selected) != 26:
        raise ValueError("Changed-owner review scope drifted")
    (HERE / "changed-owner-review.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "scope": "Explicit mapping-only decisions for 26 rows / 23 changed owners; unrelated roles/components remain separate.",
                "rows": selected,
            },
            indent=2,
        )
        + "\n"
    )


if __name__ == "__main__":
    main()
