# Unmapped Ingredient Duplicate Review

Date: 2026-05-07

This review continues the unmapped ingredient standardization goal. It only
applies high-confidence local duplicate cleanup where an unmapped record already
has an exact mapped representative in `data/ingredients/mapped/`.

## Validation Used

- Local OAK CHEBI labels and aliases resolved the CHEBI representatives:
  `CHEBI:18290`, `CHEBI:31345`, `CHEBI:75836`, `CHEBI:63043`, `CHEBI:34683`,
  `CHEBI:37585`, `CHEBI:113455`, `CHEBI:87020`, and `CHEBI:63934`.
- EBI OLS resolved the checked CHEBI targets through `runoak -i ols:chebi info`.
  OLS returned resolvable CURIEs but did not expose labels through this OAK
  adapter path in this environment.
- EBI OLS resolved the checked MESH targets `mesh:C509797` and `mesh:C000366`
  through `runoak -i ols:mesh info`.

## Applied Duplicate Retirements

| Retired unmapped record | Mapped representative | Basis |
| --- | --- | --- |
| `(E)-4-Aminostyryl_Acetate.yaml` | `E_4_Aminostyryl_Acetate.yaml` | Same kgmicrobe compound placeholder identity; not promoted to CHEBI. |
| `Atrop-abyssomicin_C.yaml` | `Atrop_Abyssomicin_C.yaml` | Existing mapped MESH exact-synonym promotion; OLS resolves `mesh:C509797`. |
| `Bacteriocin_ISK-1.yaml` | `Bacteriocin_Isk_1.yaml` | Same kgmicrobe compound placeholder identity; `CHEBI:204272` was not promoted because the local evidence only supports Nukacin ISK-1. |
| `Bathocuproinedisulfonic_Acid_Disodium_Salt.yaml` | `Bathocuproine_Disulfonic_Acid_Disodium_Salt.yaml` | Same disodium salt surface form; mapped representative preserves CAS fallback identity and CHEBI parent semantics. |
| `Co-carboxylase.yaml` | `Thiamine_Pyrophosphate.yaml` | Local OAK CHEBI resolves `CHEBI:18290` and lists cocarboxylase synonym evidence. |
| `Hemicalcium_D--pantothenate.yaml` | `Calcium_Pantothenate.yaml` | Local mapped representative already carries hemicalcium D-(+)-pantothenate synonym evidence for `CHEBI:31345`. |
| `Iron(II)_Sulfate_Heptahydrate.yaml` | `Feso4_X_7_H2o.yaml` | Hydrate state matches mapped iron(II) sulfate heptahydrate `CHEBI:75836`. |
| `Kno.yaml` | `Kno3.yaml` | Local mapped representative is potassium nitrate `CHEBI:63043`; existing synonyms include `KNO`. Added 5 occurrence/media counts. |
| `Na2hpo47h2o.yaml` | `Na2hpo4_X_7_H2o.yaml` | Hydrate state matches mapped Na2HPO4 heptahydrate representative. Added 2 occurrence/media counts. |
| `O-carbamyl-D-serine.yaml` | `O_Carbamyl_D_Serine.yaml` | Existing mapped MESH exact-synonym promotion; OLS resolves `mesh:C000366`. |
| `Sodium_Dihydrogen_Phosphate.yaml` | `Nah2po4.yaml` | Local OAK CHEBI resolves `CHEBI:37585` and lists sodium dihydrogen phosphate synonym evidence. |
| `Sodiumbenzoate.yaml` | `Na-benzoate.yaml` | Spacing variant of sodium benzoate; local OAK CHEBI resolves `CHEBI:113455`. |
| `Trans-styrylacetic_Acid.yaml` | `Trans_Styrylacetic_Acid.yaml` | Same kgmicrobe compound placeholder identity; no CHEBI promotion applied. |
| `VOSO4_X_H2O.yaml` | `Voso4_X_N_H2o.yaml` | Source hydrate notation is covered by mapped vanadyl sulfate hydrate `CHEBI:87020`. |

## Left For Later

- `Nah2po4h2o.yaml` remains unmapped because the source is monohydrate-specific
  while the strongest local representative is the anhydrous sodium
  dihydrogenphosphate record; this needs hydrate-state curation before identity
  cleanup.
- Remaining unmapped records after this pass: 445.

