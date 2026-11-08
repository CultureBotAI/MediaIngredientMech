The NBRC1308 andNBRC1356 primary documents prescribe the same trace-stock formulation:13 named solutes,1L distilled-water input and an unquantified NaOH pH adjustment. Separate local IDs are not justified by the printed stock recipe. This comparison supports a single successor proposal while preserving source-specific receiving-medium processing.

This is a comparison contribution by the author of the original1308 proposal, not the distinct skeptical final review. Root authors the reconciled payload and B reviews its exact bytes. Published commit`d5a7613c931d45d057eaca7b5ec15280aca76c9e` remains immutable.

| Printed input | NBRC1308 | NBRC1356 | Result |
|---|---:|---:|---|
| Nitrilotriacetic acid (NTA) | 12.8 g | 12.8 g | Identical input |
| FeCl3·6H2O | 1.35 g | 1.35 g | Identical input |
| MnCl2·4H2O | 0.1 g | 0.1 g | Identical input |
| CoCl2·6H2O | 0.024 g | 0.024 g | Identical input |
| CaCl2·2H2O | 0.1 g | 0.1 g | Identical input |
| ZnCl2 | 0.1 g | 0.1 g | Identical input |
| CuCl2·2H2O | 0.025 g | 0.025 g | Identical input |
| H3BO3 | 0.01 g | 0.01 g | Identical input |
| Na2MoO4·2H2O | 0.024 g | 0.024 g | Identical input |
| NaCl | 1 g | 1 g | Identical input |
| NiCl2·6H2O | 0.12 g | 0.12 g | Identical input |
| Na2SeO4 | 0.004 g | 0.004 g | Identical input |
| Na2WO4 | 0.004 g | 0.004 g | Identical input |
| Distilled water | 1 L | 1 L | Identical input |

Both recipes dissolve NTA first, adjust to pH6.5 with NaOH, then add minerals and state finalpH7.0. NaOH quantity/strength/volume and any final-pH correction are unspecified. Water is a1L ingredient, not an instruction to make the final solution up to1L. No200mL initial fraction is stated here. Unqualified selenate/tungstate are retained literally, without invented hydration or childCURIEs.

The complete receiving recipes differ. NBRC1308 uses1ml trace stock and autoclaves the mix containing it under80/20N2/CO2. NBRC1356 uses10ml and explicitly adds filter-sterile trace stock; its complete-medium pH9 is separate from stockpH7. Preserve these occurrence-specific conditions without inventing either analytical equivalence after treatment or a second printed formulation.

| Case/index | Recipe/source | Exact occurrence | Decision |
|---|---|---|---|
| 19 | CultureMech:007450 / nbrc.medium:1020 | `CM_OCC:d378f68946820ab704a621452e69c81b6679352a07fe38758e1499eb20e9e841` | Exclude; retain1020/824 stock |
| 19 | CultureMech:007471 / nbrc.medium:1308 | `CM_OCC:e689137127cd84bead1063ab24e931745a4a44fb673a953471ea3ab33e3a3df5` | Include |
| 19 | CultureMech:007496 / nbrc.medium:824 | `CM_OCC:e7c13d84e80927c02ae09fb68501cd9d8c84e442061bd42b9a58394e1f8fe03d` | Exclude; retain1020/824 stock |
| 133 | CultureMech:007474 / nbrc.medium:1356 | `CM_OCC:2c345cfde3bd9095fd0dad8782a6d904e0bf1ef8beb5c12333b78d7916f8cb03` | Include |

The excluded1020/824 stocks omit NaCl, selenate and tungstate from the trace table and useKOH; their separateSe/W stock includes selenite. Matching generic headings therefore do not permit globalalias reconciliation.

| Primary | Original retrieval UTC | SHA256 |
|---|---|---|
| [NBRC1308](https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1308) | 2026-11-08T05:07:01.897272+00:00 | `d00ccd979e58433b8e97aa0d84dbee50d3aa8c571e934f39dd7f261f99a7b8be` |
| [NBRC1356](https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1356) | 2026-11-08T05:07:36.621369+00:00 | `87b9e6d80867f35b31318154c798b6869c3246bb526a19dccc8e8be94019dd49` |
| [NBRC1020](https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1020) | 2026-11-08T05:07:01.529042+00:00 | `6b1d7b346a5f5de9dfd758198e56ef05ad43d8c68361e2ba72c9fbfae9876b7c` |
| [NBRC824](https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=824) | 2026-11-08T05:07:02.788752+00:00 | `0317a82ebb8fff38df7bb305fc69a392c2f45d4e63969a0a6714616fa9676c2e` |

The JSON report contains exact original capture paths, table-row locators, all four full frozen occurrence contexts, published payload hashes and metadata differences. No original source capture, old proposal, canonical bundle or maintained record was changed.
