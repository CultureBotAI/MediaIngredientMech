# Source defect inventory — worker02 B

No recipe changes or concentration conversions are approved here. Preserve exact raw strings and preparation hierarchy.

## B63 — volume_transcribed_as_mass
`CM_NAME:677eea89e6c05433665f6d3a63b923d0e2559ef3b4ea1cd117690d70a2db6639`

Frozen stock concentration field2.5G_PER_L; original addition2.5mL of8%w/vNa2CO3.
Preserve liquid addition and stock strength separately; do not reinterpret2.5 as grams or map stock to pure carbonate.

- `CM_OCC:5466186ebb341438bf1ba0e2ca0cbdda045212de7c59fef5a57a32493fdc0109`; `CultureMech:007600`; `data/normalized_yaml/bacterial/TOGO_M1084_Pyvl_Medium.yaml` → `ingredients/0`.
- `CM_OCC:341482ebbaaab8db2e0a10967b333a9c80201cc1736a62be06cfb69b6fb7d546`; `CultureMech:009737`; `data/normalized_yaml/bacterial/TOGO_M357_PY4S_Agar.yaml` → `ingredients/0`.
- Primary: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1023 — `b/captures/source-d98555f5a92588b70837.bin` / SHA256 `1ce34826de4c0b8f2eb7a32456dbd8c6c74fd647778ecb5ad9a8100f2e9afc60`.
- Primary: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=363 — `b/captures/source-0f367e017df3819933dd.bin` / SHA256 `c4a470170f39aa1e9effd3eb70b7c9ac96b51a109fced58f4b1b305c368e72cc`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M357 — `b/captures/togo-M357.json` / SHA256 `ee89ef826c7be6ddb5bb4e7e5b39ca5d0a78d85846598b261c7a899e4a030ed1`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1084 — `b/captures/retry-togo-M1084.json` / SHA256 `29a851437eba17bfa03bab5d2bd65d2d1efc2a3a7a832766783f84f3368e2745`.

## B64 — formula_typography_and_stock_units
`CM_NAME:6bbaec38cb2ee0c52194327b4584765d793a7b9da67c54e6715aecc4c57623f4`

Frozen CoCI2.6H2O190G_PER_L; TOGO names same raw token but labels cobalt dichloride hexahydrate190mg within Solution2(SL12).
Correct I/l using named source entity; retain190mg in its stock preparation, not190g/L final medium.

- `CM_OCC:7bb32bde12a10bcce030282456b74f8b980ae79e8cfa1f5d8346d8858174c2c6`; `CultureMech:008863`; `data/normalized_yaml/bacterial/pfennig_s_medium.yaml` → `ingredients/9`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2277 — `b/captures/retry-togo-M2277.json` / SHA256 `f655575e993dd27ffda8dd57afcdbce8c941ca22a9061a9b561199901dcdf04f`.

## B66 — hydrate_transcription
`CM_NAME:6f29a0416dad4b5abe39633c347267176782130cb98b269871909d3e1c4a24ee`

Frozen and TOGO raw KAl(SO4)2·2H2O; original NBRC1126 table KAl(SO4)2·12H2O0.018g in trace elements solution.
Occurrence-specific two-to-twelve water correction; preserve original erroneous token as non-resolving provenance.

- `CM_OCC:e6640f4c8df8d9a97bc891e9413c47a2d362ccf69ec85a90f108b11f9ee6737d`; `CultureMech:008456`; `data/normalized_yaml/archaea/TOGO_M1882_Methanoregula_medium.yaml` → `ingredients/25`.
- Primary: https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1126 — `b/captures/source-760da802b292f0cfa978.bin` / SHA256 `4b128503477c747ba28eba1b6e6e2860fd814f53d0471943a387f322322ffefd`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1882 — `b/captures/retry-togo-M1882.json` / SHA256 `102576db61ecdb04ea8dcab640b0f2fcc2d52776a7f5dded3c569cc9bfaf0ab5`.

## B70 — volume_transcribed_as_mass_and_version_drift
`CM_NAME:7a330523dd1cc8c7c0c5deee2e2a424ecefd3f2c969ec57245c8f46c733f2284`

Frozen10G_PER_L of0.2%w/vFeSO4·7H2O; source TOGOM2649 explicitly10mL/L of0.2%w/v stock. Current DSMZ503 instead describes0.1% stock.
Fix liquid quantity representation against pinnedTOGO source; keep currentDSMZ version discrepancy explicit and do not silently replace0.2% by0.1%.

- `CM_OCC:a16974d824ef8a056b111b4b0b4a4e5eea7c3b3630667131d4089fe0631cb03b`; `CultureMech:009205`; `data/normalized_yaml/bacterial/anaerobic_freshwater_fwm_medium_for_dsm_15978.yaml` → `ingredients/30`.
- Primary: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium503.pdf — `b/captures/source-b86ee1b419507c874128.bin` / SHA256 `2a3e34f68943a632052d156b00e910a1da44621a0256aa48c49b1a6580ca72fa`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2649 — `b/captures/togo-M2649.json` / SHA256 `b7eb3df13093707c514ade18961ee9b61452cf20509bf2cfdadd60059ea9a6a2`.

## B74 — supplied_counterion_lost
`CM_NAME:8039182ccb56665e768289fb1a2063527f85a0e26a2984ea03323179ecb84441`

Frozen CDM/LP ATP(CHEBI15422)0.00036mM; original Merlen1999 Table1 ATP(Na2)0.36µM. Quantity agrees, supplied disodium form was omitted.
Correct onlyCultureMech007240 occurrence to source-specific disodiumATP context; do not generalize to25 otherATP cases or infer hydration.

- `CM_OCC:fdffaad87b725dedd6eb08e7e52d3f375b86991dafdaff0d047cefd347e2a1fd`; `CultureMech:007240`; `data/normalized_yaml/bacterial/cdm_lp.yaml` → `ingredients/0`.
- Primary: https://citeseerx.ist.psu.edu/document?doi=6d6d6ab5ec65f241db3a1bf37332a12556aa254c&repid=rep1&type=pdf — `b/captures/review-a-merlen-293cd6aa6001a127.bin` / SHA256 `36aab822e2b8cbabd34c1239364e4b669e010e186f79c9896e7dcae6c6cd3bdc`.

## B76 — source_formula_field_conflict
`CM_NAME:849cf52732c076356294f5f6158cab770bc61a61f46f4c0fe3f60f2d68c7c165`

Frozen and TOGO rawCd(NO3).4H2O3µM; same primaryAPI separately types Cadmium nitrate tetrahydrateGMO002395.
Provider/case-scoped formula repair toCd(NO3)2·4H2O is supported by named compound; do not publish malformed literal as global alias.

- `CM_OCC:1599db70fd05b6d4e592334c3f2735faa12b50230c8810a7d08c76f6277bfe81`; `CultureMech:008849`; `data/normalized_yaml/bacterial/pcr_s11_medium.yaml` → `ingredients/23`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2262 — `b/captures/reused-togo-M2262.json` / SHA256 `b5776fddefb8ec19fb2321bda3dad07b72cc0b0ed0cb9f27b9b39847803d7c22`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2262 — `b/captures/retry-togo-M2262.json` / SHA256 `b5776fddefb8ec19fb2321bda3dad07b72cc0b0ed0cb9f27b9b39847803d7c22`.

## B86 — volume_transcribed_as_mass
`CM_NAME:9b83239a183cd5bdb20173204afaac7510ddac5d267a462fbc118e46da0df159`

Frozen5G_PER_L ofMgSO4·7H2O(6g/L); TOGOM2231 specifies5mL addition of that6g/L stock.
Preserve stock strength6g/L and addition5mL as separate quantities; no5g/L claim.

- `CM_OCC:e9c9d8e00a2d78070e4c469e60a0333c7d509a09e977784dd7784410b5c85a80`; `CultureMech:008820`; `data/normalized_yaml/bacterial/allen_medium.yaml` → `ingredients/4`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2231 — `b/captures/retry-togo-M2231.json` / SHA256 `2327091527bfed277c4a2538ae739de9467901f20ec6f3197bd2c040e760fd5f`.

## B87 — stock_and_medium_contributions_flattened
`CM_NAME:9df2e5383945c29981721560d28379995b38003d759f55082d8ffead8447fdea`

Frozen0.8500000000000001G_PER_L with note merged0.05+0.8; originalTOGOM3155 states0.05g/L directFeSO4·7H2O plus10mL/L trace stock containing0.8g/L.
Restore preparation hierarchy.0.8g/L stock composition must not be summed directly with0.05g/L final-medium input; derived effective concentration is not proposed by this inventory.

- `CM_OCC:2804e07f495199d6aad49107b3d8701bcf79c8eef1f82e9c89fb250734b47e8d`; `CultureMech:009617`; `data/normalized_yaml/bacterial/petc_mes_medium.yaml` → `ingredients/5`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M3155 — `b/captures/togo-M3155.json` / SHA256 `40cd8eac51ed9b8273911b94971469722a6df62198d2398a8654653be060866e`.

## B91 — hydrate_transcription
`CM_NAME:a6e96e8274e90caec9533eec13e45fb8cf4a38a137877e5292b4af7ea9b21b2d`

Frozen Ca(NO3)2x5H2O0.02G_PER_L; originalDSMZ1250 tableCa(NO3)2·4H2O0.02g.
Source-scoped correctionfive-to-four waters; rawfive-water token stays non-resolving.

- `CM_OCC:5339e9aa028fc894a251ea64c6d24430b7f95f713f97ebfcd9b8f3bb2bb06a47`; `CultureMech:009101`; `data/normalized_yaml/bacterial/TOGO_M2531_Desulfosporosinus_Acidophilus_Medium.yaml` → `ingredients/8`.
- Primary: https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1250.pdf — `b/captures/source-c7c5bd7a6a5433b22b6b.bin` / SHA256 `5649f6ceee1b07f3e78dc25b8b85864fe2e89ec66f1a12d0ebca3c8842c227dc`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2531 — `b/captures/retry-togo-M2531.json` / SHA256 `3649d6873cf44799f252f55e1fa47a0a53a272324270e565831a643cc29edbda`.

## B96 — milligram_transcribed_as_gram
`CM_NAME:ae541eb6dc54dff13a0406bbea554e9ed353683fe05493deb6192a5da62596f7`

Frozen2G_PER_L in both recipes; originalJCM950/JCM966 and correspondingTOGOM997/M1016 specify(NH4)2Fe(SO4)2·6H2O2.0mg.
Retain2mg addition in original recipe volume; identity alias approval does not certify frozen2g/L.

- `CM_OCC:22d979c16ae385ca67c9aaa4ed9464be60b73cfbd394ac56c64bccbae06914e8`; `CultureMech:007530`; `data/normalized_yaml/bacterial/TOGO_M1016_PA_Medium.yaml` → `ingredients/10`.
- `CM_OCC:d5112b0badcb05aab5be1e48e1ced8ba62e7acdc8efaf5a9118a5f47a6a3b232`; `CultureMech:010425`; `data/normalized_yaml/bacterial/TOGO_M997_NH-JN4_Medium.yaml` → `ingredients/11`.
- Primary: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=950 — `b/captures/source-51b504f992baa9fded36.bin` / SHA256 `df7564df3936a6a38cbf4b339dea5d51ccdb5e9f8e106a897fe0e7eadeb68d08`.
- Primary: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=966 — `b/captures/source-21fcdd4ef87d360ad1ef.bin` / SHA256 `15923f4ffd5529a3f049f606c1ce361981d3c76533c6c6dfc05149dec777ef2c`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M997 — `b/captures/togo-M997.json` / SHA256 `b1a39cac7864d65388d48ef2ca969e9855aa55844022d4b3a946ff5b72e3c312`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M1016 — `b/captures/retry-togo-M1016.json` / SHA256 `f0d5e45498fe89a99ae850d7ba1772ea80bc1e085b4359e2394b47067474ef75`.

## B98 — footnote_in_label_and_stock_units
`CM_NAME:b2842dee958925abda8f2e56af9eb9a5fd009b8306848c04ae6782597864506c`

Frozen MnSO4·5H2O1)217G_PER_L; originalNIES SOT footnote replaces250mg heptahydrate by217mg pentahydrate. TOGOM2509 puts217mg in100mL A5stock, with0.1mL A5 addition.
Remove footnote marker from chemical label while preserving footnote provenance; restore mg andstock hierarchy, not217g/L final concentration.

- `CM_OCC:eaaf0a6844aaf8749a8d742b8758d8d02f9513a7e14ac6369665ac2caf4b4bcc`; `CultureMech:009080`; `data/normalized_yaml/bacterial/sot_medium.yaml` → `ingredients/15`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2509 — `b/captures/retry-togo-M2509.json` / SHA256 `5cf01f0691361181fa733c2163aaed917feabce24da5c2fec876e5616ed83950`.
- Primary: https://mcc.nbrp.jp/medium/ja/sot.pdf — `b/captures/final-source-34442c33cf8fafdf.bin` / SHA256 `f862752213b8ab62c5b16234d08156ab3f6a7317ef0013c4921e65e4e73db0c4`.

## B101 — microlitre_transcribed_as_mass
`CM_NAME:b88bc93175e092f9aae91f120cd1f992e30e1e889f092f464b4741bb6b15ff4b`

Frozen1MMgSO4 with concentration200G_PER_L; originalTOGOM2790 specifies200ul of1Mstock.
Store200µL addition separately from1M stock concentration; no200g/L orsolid-hydrate inference.

- `CM_OCC:0dc9dc7db5cba718eb8a8f0e63be3cefdd54b3eb1d1b6be9693513a74932ddb3`; `CultureMech:009338`; `data/normalized_yaml/bacterial/m9_minimal_media.yaml` → `ingredients/1`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2790 — `b/captures/togo-M2790.json` / SHA256 `484ff25c250928b9ff3b98873ff4aa40492e17701226c88be3fe623c0196db2e`.

## B129 — nitrate_coefficient_lost
`CM_NAME:fe96db05f76e36ddfdb75c3d798b85585c055eba76a65cb961b96506d5b314d7`

Frozen/TOGO Mg(NO3)·6H2O2.54G_PER_L; originalJCM448 explicitlyMg(NO3)2·6H2O2.54g.
Restore second nitrate at the affected occurrence; malformed rawtoken remains provenance, notgloballyresolving alias.

- `CM_OCC:679296725a3a5c52f0a6b6911eb80e514c9df8dd0e0e6cf11e6bc91509974f13`; `CultureMech:009835`; `data/normalized_yaml/bacterial/TOGO_M449_KA22_Medium.yaml` → `ingredients/8`.
- Primary: https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=448 — `b/captures/source-efc59482d5f1002a9dce.bin` / SHA256 `ab7631296a07fdcdc03dacb55f3e508d3b6e97ce9f21f06690dbdfc4811b49cb`.
- Primary: https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M449 — `b/captures/togo-M449.json` / SHA256 `f9900ab7a6f34cc75cf7ea293386d335a3af65d9709b86ed34d247c9eb4472ba`.

