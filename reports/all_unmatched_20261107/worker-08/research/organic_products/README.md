# Worker08 organic-products source review

Primary reviewer: in-process child `/root/organics`. All 51 assigned cases were inspected individually against frozen full occurrences/raw records, current candidate owners and cited primary evidence. Independent skeptical review completed by `/root/vitamins` for all 51 cases and 11 v3 payloads with no open findings; these remain proposals, not applied changes or release approvals.

## Exact outputs

- `decisions.json`: 51 complete original case digests and occurrence accounting.
- `evidence.json`: 180 evidence references, including primary pages, exact frozen recipes, shared source captures and honest failed lookups.
- `proposals.json` and `proposals/`: 11 exact payloads: five alias edits, five new distinct compound proposals, and one source-provenance notes/history enrichment.
- `owners/`: 31 current candidate owner snapshots; every decision lists actual before hashes.
- `fragment-validation.json`: exact51 subset integrity using official auditor on a declared derived subset; original188 integration audit remains with parent.
- `schema-validation.tsv`: zero schema errors in all11 proposed payloads.

## Revision boundary

Current fragments are v3. The coordinator preserves original v1 at `review-history/organic-primary-v1`; local `revision-history/v2` retains the interim successor. Review corrections distinguish dTMP unavailable quantity from the withdrawn VARIABLE default, document source1754-to-JCM60 without equating the generic owner to that formulation, and attach exact primary IDs/URLs to newly added aliases. Diff and remediation JSON files bind the changes. The independent reviewer approved the source-review scope on current exact bytes; receipt is `../../independent/vitamins-reviews-organics/review.json` (SHA256 `32aebf8f2bdccf6812012dfc87eec0dfef63e8a8733d0418099ffd3e28fc279a`).

## Material findings

- TOGO M2844 describes5mL of0.5% bromothymol-blue in0.2N KOH; parsed KOH alone loses the mixture boundary and5G_PER_L is incorrect.
- JCM600 specifies40mL of5mM toluene stock; JCM906 specifies100mL of0.5M glycine-NaOH buffer. Frozen CultureMech rows use mass units instead. Parent verified CultureMech issue408 for volume-unit substitution.
- NBRC1394 specifies PQQ1mg/L; the frozen normalized row says1G_PER_L, a1000-fold difference. Salt form remains unspecified.
- MediaDive2119 automatically assigns6-methylnicotinate CAS5470-70-2; TCI independently identifies that CAS as methyl6-methylnicotinate ester. Do not infer the ester from this conflict.
- Soytone and Bacto Soytone remain narrower than FOODON hydrolyzed vegetable protein. Preserve retired Bacto owner and all shared-owner/source holds.
- The malformed Fe4(PO4)2 name is not ferric pyrophosphate Fe4(P2O7)3. Auto-CAS and calculated mass do not independently repair the formula.
- DL-asparagine hydrate, sodium DL-lactate, MES hydrate, pH-adjusted HOMOPIPES and broad R2A/commercial-medium names retain their explicit form/stock boundaries.

## Limits and retained obligations

No maintained YAML, aggregate, canonical SSSOM, release decisions or generated surfaces were edited. Existing WITHHOLD and REJECTED dispositions are retained, including source-only negative holds bound by the original case digest. Alias edits invalidate inherited whole-payload support; coordinator must review complete changed owners and generated tokens before release. No roles are added or approved.

A direct network escalation was automatically rejected because the reviewer interpreted public HTTP retrieval as prohibited additional external sessions. It was not bypassed. The supported web tool and separately approved bounded HTTPS captures made by the parent supplied the evidence. DNS failures, failed web opens, JCM1120 HTTP200 Nothing found, and DSMZ560 HTTP404 are not positive evidence. The immutable shared FOODON03315720 capture preserves its original retrieval timestamp.

Cytovirin/primocarcin/chlororaphin/lactone registry continuity is not a claim of independently proved external structure. Underlying trait nodes lack structure and source reagent detail. Registry-only continuity does not clear external mapping or historical hold obligations. All unresolved decisions name their precise next evidence requirement.

## Validation

The official structural auditor was reused on a private derived51-case subset after comparing every case digest to the original188-case shard. Missing-case, changed-digest and dangling-evidence negative controls were rejected. This is an integrity check, not scientific approval. `validate_strict.py` scanned all11 proposal YAML files with zero errors. `git diff --name-only -- data/ingredients data/curated mappings UNIFIED_INGREDIENT_MAPPING.tsv` returned no changes. A pypdf extraction attempt was unavailable; the installed pdftotext successfully inspected the CCAP FCGM PDF instead.

## Case accounting

| Index | Source label | Disposition | Proposal |
|---:|---|---|---|
| 0 | laminarin (brown algae) | broad_parent_relation_only | No change; case-specific reason retained |
| 5 | sodium nicotinate | new_distinct_ingredient_proposal | op-sodium-nicotinate-new |
| 13 | Soya flour | existing_identity_or_alias | op-soy-flour-alias |
| 16 | 0.2NKOH | stock_product_mixture_context | No change; case-specific reason retained |
| 23 | Ethane | new_distinct_ingredient_proposal | op-ethane-new |
| 24 | Nalidixic acid | new_distinct_ingredient_proposal | op-nalidixic-new |
| 25 | iso -Valeric acid | existing_identity_or_alias | op-isovaleric-alias |
| 27 | 5.0 mM Toluene (water--saturated) | stock_product_mixture_context | No change; case-specific reason retained |
| 32 | Difco 0003 or Difco 0001 | stock_product_mixture_context | No change; case-specific reason retained |
| 41 | n--Valeric acid | existing_identity_or_alias | op-valeric-alias |
| 50 | Fluid thioglycolate (BD-BBL) | stock_product_mixture_context | No change; case-specific reason retained |
| 54 | iso--Valeric acid | existing_identity_or_alias | op-isovaleric-alias |
| 71 | R2A | stock_product_mixture_context | No change; case-specific reason retained |
| 74 | R2A (Difco) | stock_product_mixture_context | No change; case-specific reason retained |
| 75 | Peptic Pepton (USB) | stock_product_mixture_context | No change; case-specific reason retained |
| 77 | sulfide ore | stock_product_mixture_context | No change; case-specific reason retained |
| 81 | dTMP | unresolved | No change; case-specific reason retained |
| 83 | Glycine betaine | new_distinct_ingredient_proposal | op-glycine-betaine-new |
| 84 | 3-Sulfolactate | unresolved | No change; case-specific reason retained |
| 108 | n -Valeric acid | existing_identity_or_alias | op-valeric-alias |
| 113 | Trimethylglycine | new_distinct_ingredient_proposal | op-glycine-betaine-new |
| 121 | Trypticase Soy (BBL) | stock_product_mixture_context | No change; case-specific reason retained |
| 127 | 0.5 M Glycine--NaOH buffer (pH 10.0) | stock_product_mixture_context | No change; case-specific reason retained |
| 128 | Cereal grass leaves | stock_product_mixture_context | No change; case-specific reason retained |
| 131 | Methane gas | existing_identity_or_alias | op-methane-alias |
| 134 | Pyroroquinoline quinone (PQQ) | unresolved | No change; case-specific reason retained |
| 136 | L-Asparagine*H2O | existing_identity_or_alias | op-l-asn-hydrate-alias |
| 137 | Methanethiol | new_distinct_ingredient_proposal | op-methanethiol-new |
| 143 | 6-methylnicotinate | unresolved | No change; case-specific reason retained |
| 145 | Na-stearate | existing_identity_or_alias | No change; case-specific reason retained |
| 150 | DL-Na-lactate | broad_parent_relation_only | No change; case-specific reason retained |
| 152 | ß-nicotinamide adenine dinucleotide | existing_identity_or_alias | No change; case-specific reason retained |
| 154 | Soytone | broad_parent_relation_only | No change; case-specific reason retained |
| 155 | Glycyl-glycine | existing_identity_or_alias | No change; case-specific reason retained |
| 156 | cytovirin | existing_identity_or_alias | No change; case-specific reason retained |
| 157 | Soya flour | existing_identity_or_alias | op-soy-flour-alias |
| 159 | Bacto Soytone | broad_parent_relation_only | No change; case-specific reason retained |
| 160 | Alpha-hydroxyglutarate-gamma-lactone | existing_identity_or_alias | No change; case-specific reason retained |
| 164 | chlororaphin | existing_identity_or_alias | No change; case-specific reason retained |
| 166 | Glycerol-asparagine agar | stock_product_mixture_context | op-glycerol-asparagine-source-note |
| 168 | HOMOPIPES | stock_product_mixture_context | No change; case-specific reason retained |
| 173 | Se-acid | unresolved | No change; case-specific reason retained |
| 174 | Alpha-hydroxyglutarate-gamma-lactone | existing_identity_or_alias | No change; case-specific reason retained |
| 175 | chlororaphin | existing_identity_or_alias | No change; case-specific reason retained |
| 176 | primocarcin | existing_identity_or_alias | No change; case-specific reason retained |
| 180 | Plain flour | unresolved | No change; case-specific reason retained |
| 181 | DL-Asparagine x H2O | supplied_form_correction | No change; case-specific reason retained |
| 183 | Amphotericin | unresolved | No change; case-specific reason retained |
| 184 | MES Hydrat | existing_identity_or_alias | No change; case-specific reason retained |
| 186 | Fe4PO42 | malformed_or_nonchemical_token | No change; case-specific reason retained |
| 187 | D-Trehalose | existing_identity_or_alias | No change; case-specific reason retained |
