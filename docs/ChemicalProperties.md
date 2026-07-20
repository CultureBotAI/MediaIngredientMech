

# Class: ChemicalProperties 


_Chemical structure and properties for CHEBI-mapped ingredients_





URI: [mediaingredientmech:ChemicalProperties](https://w3id.org/mediaingredientmech/ChemicalProperties)





```mermaid
 classDiagram
    class ChemicalProperties
    click ChemicalProperties href "../ChemicalProperties/"
      ChemicalProperties : cas_rn
        
      ChemicalProperties : data_source
        
      ChemicalProperties : inchi
        
      ChemicalProperties : molecular_formula
        
      ChemicalProperties : molecular_weight
        
      ChemicalProperties : pubchem_cid
        
      ChemicalProperties : retrieval_date
        
      ChemicalProperties : smiles
        
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [cas_rn](cas_rn.md) | 0..1 <br/> [String](String.md) | Chemical Abstracts Service Registry Number (CAS-RN) in format XXX-XX-X or XXX... | direct |
| [molecular_formula](molecular_formula.md) | 0..1 <br/> [String](String.md) | Molecular formula (e | direct |
| [smiles](smiles.md) | 0..1 <br/> [String](String.md) | Simplified Molecular Input Line Entry System notation | direct |
| [inchi](inchi.md) | 0..1 <br/> [String](String.md) | IUPAC International Chemical Identifier | direct |
| [molecular_weight](molecular_weight.md) | 0..1 <br/> [Float](Float.md) | Molecular weight in g/mol | direct |
| [pubchem_cid](pubchem_cid.md) | 0..1 <br/> [Integer](Integer.md) | PubChem Compound Identifier (CID), stored as a positive integer | direct |
| [data_source](data_source.md) | 0..1 <br/> [String](String.md) | Source of chemical properties (e | direct |
| [retrieval_date](retrieval_date.md) | 0..1 <br/> [Datetime](Datetime.md) | When these properties were retrieved | direct |





## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [IngredientRecord](IngredientRecord.md) | [chemical_properties](chemical_properties.md) | range | [ChemicalProperties](ChemicalProperties.md) |







## Identifier and Mapping Information






### Schema Source


* from schema: https://w3id.org/mediaingredientmech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | mediaingredientmech:ChemicalProperties |
| native | mediaingredientmech:ChemicalProperties |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ChemicalProperties
description: Chemical structure and properties for CHEBI-mapped ingredients
from_schema: https://w3id.org/mediaingredientmech
attributes:
  cas_rn:
    name: cas_rn
    description: Chemical Abstracts Service Registry Number (CAS-RN) in format XXX-XX-X
      or XXXX-XX-X. Primary chemical identifier used in regulatory and commercial
      contexts. Retrieved from CultureBotHT/MicroMediaParam mappings or external databases.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - ChemicalProperties
    - MappingEvidence
    pattern: ^\d+-\d+-\d+$
  molecular_formula:
    name: molecular_formula
    description: Molecular formula (e.g., H2O, C6H12O6)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - ChemicalProperties
  smiles:
    name: smiles
    description: Simplified Molecular Input Line Entry System notation
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - ChemicalProperties
  inchi:
    name: inchi
    description: IUPAC International Chemical Identifier
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - ChemicalProperties
  molecular_weight:
    name: molecular_weight
    description: Molecular weight in g/mol
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - ChemicalProperties
    range: float
  pubchem_cid:
    name: pubchem_cid
    description: PubChem Compound Identifier (CID), stored as a positive integer.
      Populated by the PubChem enrichment path in `scripts/enrich_chemical_properties.py`
      when chemical properties are sourced from PubChem rather than ChEBI.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - ChemicalProperties
    range: integer
    minimum_value: 1
  data_source:
    name: data_source
    description: Source of chemical properties (e.g., ChEBI, PubChem, CultureBotHT/MicroMediaParam)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - ChemicalProperties
  retrieval_date:
    name: retrieval_date
    description: When these properties were retrieved
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    domain_of:
    - ChemicalProperties
    range: datetime

```
</details>

### Induced

<details>
```yaml
name: ChemicalProperties
description: Chemical structure and properties for CHEBI-mapped ingredients
from_schema: https://w3id.org/mediaingredientmech
attributes:
  cas_rn:
    name: cas_rn
    description: Chemical Abstracts Service Registry Number (CAS-RN) in format XXX-XX-X
      or XXXX-XX-X. Primary chemical identifier used in regulatory and commercial
      contexts. Retrieved from CultureBotHT/MicroMediaParam mappings or external databases.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: cas_rn
    owner: ChemicalProperties
    domain_of:
    - ChemicalProperties
    - MappingEvidence
    range: string
    pattern: ^\d+-\d+-\d+$
  molecular_formula:
    name: molecular_formula
    description: Molecular formula (e.g., H2O, C6H12O6)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: molecular_formula
    owner: ChemicalProperties
    domain_of:
    - ChemicalProperties
    range: string
  smiles:
    name: smiles
    description: Simplified Molecular Input Line Entry System notation
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: smiles
    owner: ChemicalProperties
    domain_of:
    - ChemicalProperties
    range: string
  inchi:
    name: inchi
    description: IUPAC International Chemical Identifier
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: inchi
    owner: ChemicalProperties
    domain_of:
    - ChemicalProperties
    range: string
  molecular_weight:
    name: molecular_weight
    description: Molecular weight in g/mol
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: molecular_weight
    owner: ChemicalProperties
    domain_of:
    - ChemicalProperties
    range: float
  pubchem_cid:
    name: pubchem_cid
    description: PubChem Compound Identifier (CID), stored as a positive integer.
      Populated by the PubChem enrichment path in `scripts/enrich_chemical_properties.py`
      when chemical properties are sourced from PubChem rather than ChEBI.
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: pubchem_cid
    owner: ChemicalProperties
    domain_of:
    - ChemicalProperties
    range: integer
    minimum_value: 1
  data_source:
    name: data_source
    description: Source of chemical properties (e.g., ChEBI, PubChem, CultureBotHT/MicroMediaParam)
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: data_source
    owner: ChemicalProperties
    domain_of:
    - ChemicalProperties
    range: string
  retrieval_date:
    name: retrieval_date
    description: When these properties were retrieved
    from_schema: https://w3id.org/mediaingredientmech
    rank: 1000
    alias: retrieval_date
    owner: ChemicalProperties
    domain_of:
    - ChemicalProperties
    range: datetime

```
</details>