# `data/ingredients/mapped/Lanthanum_Iii_Chloride.yaml`

## Verdict

Needs curation. The PubChem structure, CHEBI:231515 structure, final exact CAS
row, and final exact KG-Microbe registry row are internally consistent, but the
record currently treats exact lanthanum trichloride as a broader CHEBI parent
and should be promoted from `NARROW_MATCH` to exact CHEBI grounding.

## Identity

- Reviewed record: `data/ingredients/mapped/Lanthanum_Iii_Chloride.yaml`.
- Identifier and grounding: `identifier: cas:20211-76-1` with
  `ontology_mapping.ontology_id: CHEBI:231515`, label
  `lanthanum trichloride`, source `CHEBI`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `20211-76-1`, PubChem CID `64735`, molecular
  formula `Cl3La`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lactose` through `Lanthanum_Iii_Chloride`: exited 0 and wrote zero ERROR
  rows.
- LinkML term validation was skipped for this CAS-primary record because the
  successful batch check covered only the CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:231515` as active `lanthanum trichloride`, lists
  `lanthanum(III) chloride` as a related synonym, and lists formula `Cl3La`
  with the same InChI as the YAML record.
- PubChem CID `64735` has formula `Cl3La` and the same InChI as the YAML
  record.
- The final SSSOM publishes a `skos:narrowMatch` row to `CHEBI:231515`, an
  identity-preserving exact row to `cas:20211-76-1`, and an exact KG-Microbe
  registry sibling row.
- Major: `CHEBI:231515` is not just a parent for this record. Its label and
  synonyms match `Lanthanum (III) chloride`, and its formula and InChI match the
  record's PubChem CID. Keeping this as `NARROW_MATCH` leaves a same-structure
  exact CHEBI term behind CAS/local registry rows.
- Minor: PubChem CID `64735` no longer resolves from the stored CAS RN
  `20211-76-1` by name lookup and exposes CAS `10099-58-8` instead, matching
  the CHEBI xref. The CAS value needs to be checked during the exact-CHEBI
  promotion.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  rows and no sibling MIM record that would split the same lanthanum trichloride
  identity.

## Completeness

- The active CHEBI identity, formula, structure block, aggregate copy, and final
  SSSOM rows are present.
- The mapping grade is too broad for the resolved CHEBI term.

## Recommended Edits

- Major: promote `data/ingredients/mapped/Lanthanum_Iii_Chloride.yaml` to exact
  `CHEBI:231515` grounding, checking whether `chemical_properties.cas_rn` should
  be retained as `20211-76-1` or updated to the ChEBI/PubChem CAS value
  `10099-58-8`.
- Regenerate final SSSOM after the YAML change so the `skos:narrowMatch`, CAS
  identity row, and KG-Microbe registry row collapse to the exact CHEBI row;
  rerun strict, product, component, and SSSOM validation.
