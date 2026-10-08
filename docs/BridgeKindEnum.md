# Enum: BridgeKindEnum 




_Closed set of chemistry edges. Each fixes its predicate_id and required bases; qc-causal-graphs recomputes every one from mappings/ontology_facts.tsv._



URI: [mediaingredientmech:BridgeKindEnum](https://w3id.org/mediaingredientmech/BridgeKindEnum)

## Permissible Values

| Value | Meaning | Description |
| --- | --- | --- |
| HYDRATE_PART | None | Hydrate has part its anhydrous form (BFO:0000051) |
| ION_PART | None | Salt has part a constituent ion (BFO:0000051) with stoichiometry |
| PROTONATION | None | One ChEBI-asserted RO:0018033/RO:0018034 hop per edge |
| TAUTOMER | None | ChEBI-asserted RO:0018036 |
| STRUCTURAL_FORM | None | Structure-specific form is a (rdfs:subClassOf) structure-less supplied class,... |
| FORM_OF_PARENT | None | First hop only, from a cas:/kgmicrobe |
| COMPONENT | None | Mixture anchor has part one of its own components (BFO:0000051; node componen... |




## Slots

| Name | Description |
| ---  | --- |
| [bridge_kind](bridge_kind.md) | Set on chemistry edges only: what the supplied form becomes, or a protonation... |





## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech






## LinkML Source

<details>
```yaml
name: BridgeKindEnum
description: Closed set of chemistry edges. Each fixes its predicate_id and required
  bases; qc-causal-graphs recomputes every one from mappings/ontology_facts.tsv.
from_schema: https://w3id.org/mediaingredientmech
rank: 1000
permissible_values:
  HYDRATE_PART:
    text: HYDRATE_PART
    description: Hydrate has part its anhydrous form (BFO:0000051). ONTOLOGY_AXIOM;
      subject is a ChEBI hydrate.
  ION_PART:
    text: ION_PART
    description: Salt has part a constituent ion (BFO:0000051) with stoichiometry.
      ONTOLOGY_AXIOM when ChEBI asserts or entails it; otherwise CHEMICAL_STRUCTURE
      (the ion's ChEBI SMILES is a '.'-component of the salt's, counts match, charges
      balance). Transition-metal salts of carbon-containing anions also need LITERATURE
      (complexation).
  PROTONATION:
    text: PROTONATION
    description: One ChEBI-asserted RO:0018033/RO:0018034 hop per edge. ONTOLOGY_AXIOM.
  TAUTOMER:
    text: TAUTOMER
    description: ChEBI-asserted RO:0018036. ONTOLOGY_AXIOM.
  STRUCTURAL_FORM:
    text: STRUCTURAL_FORM
    description: 'Structure-specific form is a (rdfs:subClassOf) structure-less supplied
      class, e.g. D-glucopyranose is a D-glucose. ONTOLOGY_AXIOM (asserted direct
      subclass) plus CHEMICAL_STRUCTURE guards: the form has a SMILES and no isotopic
      layer, the class has no SMILES, formula and charge are equal, and no other non-isotopic
      direct subclass shares the form''s InChIKey connectivity block with a different
      stereo block.'
  FORM_OF_PARENT:
    text: FORM_OF_PARENT
    description: First hop only, from a cas:/kgmicrobe.* anchor to the ChEBI parent
      named by the record's own SSSOM skos:broadMatch row. RECORD_SSSOM. Not re-exported.
  COMPONENT:
    text: COMPONENT
    description: Mixture anchor has part one of its own components (BFO:0000051; node
      component_ref). RECORD_COMPONENT. No chemistry edge may start at a component
      node; its own record owns its speciation. Not re-exported.

```
</details>