# Ingredient causal graphs and cross-Mech links

<!-- Not named docs/causal_graphs.md on purpose: `just gen-docs` writes that path
     as the generated page for the causal_graphs slot, and on a case-insensitive
     filesystem CAUSAL_GRAPHS.md would collide with it too. -->

This page is the curator's contract for `causal_graphs` on MediaIngredientMech
(MIM) ingredient records: what a graph is for, its shape, its node types and
predicates, how its evidence is checked, how it links to records in sibling
Mechs, where organisms and genomes fit, what consumes it, and how to add one.

**Authority.** `MAPPING_SEMANTICS.md` Section 7 governs what may anchor a graph,
the bridges from a supplied form to its active species, and when a link to a
sibling record is admissible. It outranks this page, as it outranks the schema
(see the source precedence in `CLAUDE.md`). Once the slot lands, the LinkML
schema governs the data shape. This page restates both for curators; where it
disagrees with either of them, they win.

## Status

When this page was written (2026-10-05, `main` at `6643131b`), none of the
machinery it describes was on `main`: there was no `causal_graphs` slot, no
record carried a graph, and there were no sibling pins, snapshot files or gate.
Paths and recipes below that do not exist yet are marked as planned where they
first appear. Phase 1 lands in this order:

| Step | What lands | Status on 2026-10-05 |
|---|---|---|
| 1 | This page and `MAPPING_SEMANTICS.md` Section 7 | added with this page |
| 2 | Schema: `causal_graphs` with its classes and enums, the regenerated datamodel and schema pages, schema rule tests | not on `main` |
| 3 | `conf/sibling_pins.yaml`, the committed snapshot files, the refresh and fetch recipes, and the offline gate `qc-causal-graphs` (added to `just qc`) | not on `main` |
| 4 | culturebotai-claw: a MIM coverage stanza, narrowed record globs, and an evidence walker that reads graphs | MIM's `causal_graph_coverage` was `disabled` in a local claw checkout's `fleet.yaml` |
| 5 | A graph writer, a one-record canary (`Na2moo4_X_2_H2o.yaml`), then the other worked examples | not on `main` |
| 6 | Consumers: readiness-scorer columns, ingredient-page panels, `docs/data/cross_mech_links.json` | not on `main` |
| 7 | Mechanistic graphs on species records first, then `SPECIATION` proposals for salts and hydrates | not on `main` |

Phase 2, the KGX export of causal edges (section 9.2), is **not yet
implemented**.

## 1. Purpose and design decisions

A causal graph explains, with evidence, how an ingredient *as supplied* acts on
cultured microbes: what it becomes in the medium, which activities, transporters
and pathways act on what it becomes, and which roles on the record the graph
explains. Graphs are also how MIM links to records in its sibling Mechs:
ProteinTraitsMech, PathwayMech, CellStructureMech, TraitMech and TaxonMech.

The design rests on ten decisions:

1. **One new slot**, `IngredientRecord.causal_graphs`, in claw's `graph_list`
   shape (section 2).
2. **One anchor per graph**: a single `INGREDIENT` node grounded to the record
   `identifier`, which names the supplied form. Only a resolved identity may
   anchor a graph.
3. **Active species are separate `CHEMICAL` nodes**, reached only through a
   closed set of chemistry edges (`bridge_kind`). CI recomputes every bridge from
   committed ChEBI facts.
4. **Links to siblings go only through node grounding**, and are admitted only
   when the pinned sibling record states the relation for exactly that
   grounding. Four reported match kinds are the only exceptions.
5. **Organisms are scope, not nodes.** They appear as a graph's
   `organism_scope` and as `protein_examples[].taxon_id`. Strains and genome
   assemblies are reached through TaxonMech; MIM stores no genome data.
6. **Evidence uses the fleet `EvidenceItem`.** The source kind is read from the
   reference, snippets are allowed only where a committed copy makes them
   checkable, and `MECHANISTIC` is reachable only through a scope gate that
   requires literature.
7. **CI runs offline.** Siblings are pinned by commit, and committed snapshots
   hold every sibling statement, ontology fact and UniProt entry CI reads.
8. **Links are a derived ledger**, `mappings/cross_mech_links.tsv` (planned),
   regenerated and diffed in CI.
9. **KGX is phased.** Phase 1 changes nothing in the export: graphs ride inside
   `record_json`. Phase 2 adds causal-edge assertions behind a review gate.
10. **Salts, hydrates and stock solutions delegate.** A `SPECIATION` graph,
    always `NONMECHANISTIC`, points at the species or component records that
    carry the mechanism, so the mechanistic count is not inflated.

A graph never changes `identifier`, `ontology_mapping` or `components`, never
writes an SSSOM row, and never creates or removes a role.

The design rejected organism nodes and organism-to-chemical edges
(utilization is a KG-Microbe query-time join), "is a" over any ChEBI subclass
and has-part read off a formula (they admit isotopologues, the wrong
stereoisomer and the wrong oxidation state), counting salt graphs as
mechanistic, MIM-only chemistry predicates that KG-Microbe cannot read, graphs
on unresolved identities, and protein nodes grounded to UniProtKB.

## 2. Shape: claw's `graph_list`

**Why this shape.** TraitMech and CellStructureMech already store graphs in
claw's `graph_list` shape: a list of graphs, each holding plain `nodes` and
`edges` lists. MIM keeps every slot name, range and requiredness of their
`CausalGraph`, `CausalNode`, `CausalEdge` and `EvidenceItem` classes, and uses
TraitMech's `ProteinExample`. claw's coverage report and structure audit then
read MIM with their default field names, and a graph fragment can be copied
between Mechs. MIM adds only the slots marked "MIM" below.

A trimmed example, from the design's worked example for `Na2so4.yaml`:

```yaml
causal_graphs:
- graph_id: sulfate_uptake_activation_ecoli
  title: Sulfate released by sodium sulfate is taken up and activated in Escherichia coli K-12
  graph_kind: ASSIMILATION
  scope_status: REVIEW_NEEDED
  scope_notes: >-
    Proposed. The salt-to-sulfate edge is MIM-asserted from ChEBI structure
    (ChEBI has no such axiom). Family records are SEEDED; no literature cached.
  explains: ["nutritional_roles#SULFUR_SOURCE"]
  organism_scope: "NCBITaxon:83333"
  nodes:
  - {node_id: na2so4, label: "sodium sulfate", node_type: INGREDIENT, grounding: "CHEBI:32149"}
  - {node_id: sulfate, label: "sulfate", node_type: CHEMICAL, grounding: "CHEBI:16189"}
  - {node_id: cysz_family, label: "The Sulfate Transporter (CysZ) Family", node_type: MOLECULAR_FUNCTION, grounding: "TCDB:2.A.121"}
  edges:
  - edge_id: salt_has_part_sulfate
    subject: na2so4
    predicate: has part
    predicate_id: "BFO:0000051"
    object: sulfate
    bridge_kind: ION_PART
    stoichiometry: 1
    assertion_basis: [CHEMICAL_STRUCTURE]
    evidence:
    - {reference: "CHEBI:32149", notes: "SMILES O=S(=O)([O-])[O-].[Na+].[Na+] has one component equal to the SMILES of CHEBI:16189; charges -2 + 2(+1) = 0."}
  - edge_id: cysz_transports_sulfate
    subject: cysz_family
    predicate: transports
    predicate_id: "RO:0002020"
    object: sulfate
    assertion_basis: [SIBLING_RECORD]
    evidence:
    - reference: "https://github.com/CultureBotAI/proteintraitsmech/blob/71499ae52aa05d60c781991df5cbf8dcc20eca10/data/traits/function/transport/tcdb/the-sulfate-transporter-cysz-family-2-a-121.yaml"
      snippet: "Mediates the transmembrane transport of sulfate."
      notes: "chemical_participants lists CHEBI:16189 with role TRANSPORTED. SEEDED; names no organism."
```

### Graph slots

| Slot | Required | Meaning |
|---|---|---|
| `graph_id` | yes | Identifier, `^[a-z][a-z0-9_]*$`, stable: discussions and reviews anchor on `causal_graphs#<graph_id>`. |
| `title`, `description` | no | Free text. |
| `graph_kind` | yes | What the graph explains (table below); claw tabulates graphs by it. |
| `scope_status` | yes | `MECHANISTIC`, `NONMECHANISTIC` or `REVIEW_NEEDED` (below). |
| `scope_notes` | no | Required by the gate for `NONMECHANISTIC`; names the delegated records for `SPECIATION`. |
| `explains` (MIM) | no | Roles on this record that the graph explains, as `<facet>#<ROLE>` anchors, with facet one of `nutritional_roles`, `physicochemical_roles` or `cellular_metabolic_roles`. Each must name a role the record already carries. A pointer only: a role never creates an edge and an edge never creates a role. |
| `organism_scope` (MIM) | no | The one `NCBITaxon:` id in which the biological edges hold, a TaxonMech record where one exists. Every organism-specific source the graph cites must lie on its lineage. Omit it only for a taxon-agnostic graph, which cannot become `MECHANISTIC` if it cites organism-specific evidence. |
| `nodes`, `edges` | yes, at least one each | Below. |

### Node slots

| Slot | Required | Meaning |
|---|---|---|
| `node_id` | yes | Local identifier, `^[a-z][a-z0-9_]*$`. |
| `label` | yes | The grounding's canonical label: the ChEBI or GO label, or the sibling record's label. The anchor uses `ontology_label` when `identifier` equals `ontology_id`, else `preferred_term`. |
| `node_type` | yes | Section 3 of this page. |
| `grounding` | no | The node's CURIE. For a sibling record this is that record's identifier, the only way a graph links out. The local part may contain `~`. Organism, strain, genome and protein-instance prefixes are refused (the genome firewall, section 3). |
| `target_mech` (MIM) | no | The owning Mech, when a CURIE is a record in more than one Mech and node-type precedence does not decide (section 3). |
| `grounding_status`, `grounding_notes` | no | `REVIEWED_LABEL_ONLY` for a node whose evidence supports the label but no exact CURIE. |
| `component_ref` | no | The `components[].component_id` this node restates (`COMPONENT` edges only). |
| `xrefs` | no | CURIEs for exactly this node's entity, never a parent or related form (`MAPPING_SEMANTICS.md` Section 7.1, A4). |
| `description`, `gene_symbols` | no | Genes and operons are metadata, not nodes. |
| `protein_examples` | no | Organism-specific UniProt proteins on a `GENE_OR_PROTEIN` or `MOLECULAR_FUNCTION` node (section 8). |

### Edge slots

| Slot | Required | Meaning |
|---|---|---|
| `edge_id` (MIM) | yes | Stable within the graph, `^[a-z][a-z0-9_]*$`. Review dispositions and discussions anchor on it. |
| `subject`, `object` | yes | Local `node_id`s. |
| `predicate` | yes | Must equal the canonical label (title) of `predicate_id`. |
| `predicate_id` (MIM: required) | yes | Closed vocabulary (section 4). |
| `description` | no | Free text. |
| `bridge_kind` (MIM) | chemistry edges only | Closed set of supplied-form-to-species steps (section 5). |
| `stoichiometry` (MIM) | `ION_PART` only | Ions released per formula unit, at least 1. |
| `assertion_basis` (MIM) | yes | The offline checks the edge claims; the gate must confirm every one (section 6). |
| `evidence` | yes, at least one | `EvidenceItem`s (section 6). |

A `ProteinExample` has the TraitMech fields: `uniprot_id` (`UniProtKB:`
accession), `protein_label`, `gene_symbol`, `taxon_id` (`NCBITaxon:`),
`taxon_label`, `entry_status` (`REVIEWED` for Swiss-Prot, `UNREVIEWED` for
TrEMBL), `proteome_id`, `retrieved_on` (a quoted date), `entry_version`,
`sequence_version`, `role`, and at least one `evidence` item.

### Schema rules

- A record with `causal_graphs` has `mapping_status: MAPPED`.
- A record with `ingredient_type: NAMED_MEDIUM` has no `causal_graphs`; a
  record with no `ingredient_type` may have them.
- `graph_kind: SPECIATION` forces `scope_status: NONMECHANISTIC`.
- `stoichiometry` is allowed only with `bridge_kind: ION_PART`.
- Every graph has at least one node and one edge, and every edge and protein
  example has at least one evidence item.

The remaining identity conditions (no placeholder grounding, no unresolved
duplicate family, no shared identifier) are checked by the gate, not the
schema; see `MAPPING_SEMANTICS.md` Section 7.1.

### Graph kinds

The gate warns `GRAPH_KIND_ROLE_UNUSUAL` when `explains` names roles outside a
kind's typical set; it never rejects the pairing.

| `graph_kind` | What it explains | Typical roles |
|---|---|---|
| `ASSIMILATION` | The active species is taken up and incorporated into biomass or a cellular pool. | nutritional: `CARBON_SOURCE`, `NITROGEN_SOURCE`, `SULFUR_SOURCE`, `PHOSPHATE_SOURCE`, `IRON_SOURCE`, `TRACE_ELEMENT`, `MINERAL_SOURCE`, `AMINO_ACID_SOURCE`, `PROTEIN_SOURCE`, `VITAMIN_SOURCE`; cellular_metabolic: `SUBSTRATE`, `MEMBRANE_COMPONENT` |
| `ENERGY_CONSERVATION` | The species is an electron donor, terminal electron acceptor or energy substrate. | nutritional: `ENERGY_SOURCE`, `LIGHT_SOURCE`; cellular_metabolic: `ELECTRON_DONOR`, `ELECTRON_ACCEPTOR` |
| `COFACTOR_FUNCTION` | The species is, or is converted into, a cofactor or prosthetic group an enzyme requires. | nutritional: `VITAMIN_SOURCE`, `COFACTOR_PROVIDER`, `TRACE_ELEMENT`, `IRON_SOURCE`; cellular_metabolic: `COFACTOR`, `PROSTHETIC_GROUP_PRECURSOR` |
| `REGULATION` | The species changes gene expression or protein activity without being consumed. | cellular_metabolic: `INDUCER`, `QUENCHER` |
| `INHIBITION` | The species inhibits a target or growth. Link an AntibioticMech or NaturalProductMech record by shared grounding rather than re-curating its graph. | cellular_metabolic: `INHIBITOR`; physicochemical: `SELECTIVE_AGENT` |
| `STRESS_PROTECTION` | The species protects cells against a stress. | cellular_metabolic: `OSMOPROTECTANT` |
| `MEDIUM_CONDITIONING` | The ingredient changes a medium property (pH, redox, osmolarity, metal availability, gel state), and through it the culture. | physicochemical: `BUFFER`, `CHELATOR`, `REDUCING_AGENT`, `OXIDIZING_AGENT`, `OSMOTIC_AGENT`, `SOLIDIFYING_AGENT`, `PRECIPITATION_INHIBITOR`, `SURFACTANT`, `ANTIFOAM`, `PH_INDICATOR`, `REDOX_INDICATOR` |
| `SPECIATION` | Chemistry only: what the supplied form becomes, with the mechanism delegated to the species' or components' own records. Always `NONMECHANISTIC`. | none |

### Scope status

Every proposal starts as `REVIEW_NEEDED` (proposed or incomplete).
`NONMECHANISTIC` means reviewed with no cellular mechanism to model, such as a
`SPECIATION` graph or an indicator dye; it is explained in `scope_notes` and is
never a way to defer work. `MECHANISTIC` means a source-backed biological
mechanism that passed the scope gate (section 6) and reviewer sign-off.

## 3. Node types and ownership

| `node_type` | Meaning | Allowed grounding prefixes | Owning Mech (resolution order) |
|---|---|---|---|
| `INGREDIENT` | This record as supplied; exactly one per graph. | The record identifier: `CHEBI`, `FOODON`, `NCIT`, `MICRO`, `mesh`, `ENVO`, `UBERON`, `BTO`, `cas`, `kgmicrobe.compound`, `kgmicrobe.ingredient` | MIM. An AntibioticMech or NaturalProductMech record with the same CURIE is reported as a co-reference in the links ledger. |
| `CHEMICAL` | An active species, metabolite, cofactor form, or another MIM record. | `CHEBI`; other MIM identity prefixes when the node is a MIM record | MIM when an active record carries that identifier (for example `Sulfate.yaml` on `CHEBI:16189`, `Nitrite.yaml`, `Ammonium.yaml`, `Methylcobalamin.yaml`); otherwise external. |
| `GENE_OR_PROTEIN` | A taxon-agnostic protein family, function-defined protein or complex; never a UniProtKB instance. | `NCBIfam`, `Pfam`, `InterPro`, `PANTHER`, `ComplexPortal`, `GO` (complex), `proteintraitsmech` | ProteinTraitsMech (protein-family, sequence, interaction-partner and localization-complex records). |
| `MOLECULAR_FUNCTION` | An activity or reaction. TCDB families are typed here as transport functions, as ProteinTraitsMech types them (`FUNC_TRANSPORT`). | `EC`, `RHEA`, `GO` (molecular function), `TCDB` | ProteinTraitsMech (enzymatic-activity, molecular-function and transport records). |
| `BIOLOGICAL_PROCESS` | A GO biological process. | `GO` (biological process) | ProteinTraitsMech pathway records; otherwise external. |
| `PATHWAY` | A pathway record; organism-specific. | `MetaCyc`, `gomodel`, `Reactome`, `WikiPathways` | PathwayMech, then ProteinTraitsMech. |
| `STRUCTURE` | A cell structure or complex. | `GO` (cellular component), `cellstructuremech` | CellStructureMech, then ProteinTraitsMech. |
| `CELLULAR_LOCALIZATION` | A location with no CellStructureMech record. | `GO` (cellular component) | ProteinTraitsMech localization records. |
| `TRAIT` | An organism trait class, only in a graph explaining an organism-conditional role the record carries. | `traitmech`, `METPO` (classes only) | TraitMech, then ProteinTraitsMech. |
| `QUALITY` | An attribute, including a requirement trait. | `proteintraitsmech` (`COFACTOR_REQ_*`), `PATO` | ProteinTraitsMech. |
| `ORGANELLE`, `CAPACITY`, `STATE`, `RNA`, `GENETIC_ELEMENT`, `ENVIRONMENTAL_FACTOR`, `EXPERIMENTAL_FACTOR` | TraitMech vocabulary, kept for fleet parity. | `GO`, `PATO`, `ENVO`, `Rfam`, `SO`, or label-only with `grounding_status` | As resolved. |

**Ownership.** When one CURIE is a record in more than one Mech, the owner is
decided first by the node-type precedence in the last column, then by
`target_mech`. `GO:0005886`, `GO:0030288` and `GO:0009279`, for example, are
records in both CellStructureMech and ProteinTraitsMech; as `STRUCTURE` nodes
they resolve to CellStructureMech. If neither decides, the gate reports
`AMBIGUOUS_OWNER`.

**Genome firewall.** The grounding pattern refuses `UniProtKB`, `NCBITaxon`,
`ncbi.assembly`, `kgmicrobe.strain`, `insdc`, `RefSeq`, `GenBank`, `ENA`,
`biosample`, `bioproject`, `img.taxon`, `patric` and `gtdb`, and there is no
`TAXON` node type. Organisms enter only as `organism_scope` and
`protein_examples[].taxon_id` (section 8).

## 4. Predicates and endpoint rules

`predicate_id` is a closed vocabulary, and `predicate` must equal its label
(`PREDICATE_LABEL_MISMATCH`). An edge whose endpoint node types are not listed
for its predicate fails `ENDPOINT_TYPE`. Where a sibling record verifies an
edge, the MIM predicate mirrors the sibling's own assertion type;
`MAPPING_SEMANTICS.md` Section 7.3 says exactly what the sibling must state. In the
subject → object column, MF is `MOLECULAR_FUNCTION` and BP is
`BIOLOGICAL_PROCESS`. The last column is the planned phase 2 KGX projection,
**not yet implemented**.

| Label | `predicate_id` | Subject → object | Verified by | KGX (phase 2) |
|---|---|---|---|---|
| has part | `BFO:0000051` | INGREDIENT/CHEMICAL → CHEMICAL (`HYDRATE_PART`, `ION_PART`); mixture INGREDIENT → component (`COMPONENT`); BP/PATHWAY → MF/BP | ONTOLOGY_AXIOM; CHEMICAL_STRUCTURE; RECORD_COMPONENT | `biolink:has_part`; ChEBI-axiom and `COMPONENT` bridges not exported |
| part of | `BFO:0000050` | MF/BP → BP/PATHWAY | SIBLING_RECORD (PathwayMech participants or edges); ONTOLOGY_AXIOM | `biolink:part_of` |
| is a | `rdfs:subClassOf` | CHEMICAL → INGREDIENT/CHEMICAL (`STRUCTURAL_FORM` only) | ONTOLOGY_AXIOM + CHEMICAL_STRUCTURE guards | not exported (ChEBI) |
| has broader match | `skos:broadMatch` | `cas:`/`kgmicrobe.*` INGREDIENT → CHEMICAL (`FORM_OF_PARENT`, first hop only) | RECORD_SSSOM | not exported (SSSOM) |
| is deprotonated form of / is protonated form of | `RO:0018033` / `RO:0018034` | CHEMICAL/INGREDIENT ↔ CHEMICAL (`PROTONATION`) | ONTOLOGY_AXIOM (asserted, one hop) | not exported (ChEBI) |
| is tautomer of | `RO:0018036` | CHEMICAL/INGREDIENT ↔ CHEMICAL (`TAUTOMER`) | ONTOLOGY_AXIOM | not exported |
| transports | `RO:0002020` | MF (including TCDB) → CHEMICAL/INGREDIENT | SIBLING_RECORD; DATABASE_RECORD (UniProt TCDB xref and catalytic participants); LITERATURE | `biolink:affects`, object aspect `transport` |
| has input / has output | `RO:0002233` / `RO:0002234` | MF/BP/PATHWAY → CHEMICAL/INGREDIENT | SIBLING_RECORD; DATABASE_RECORD (UniProt catalytic activity, direction from `PhysiologicalDirection`); ONTOLOGY_AXIOM (via sub-properties `RO:0004009` / `RO:0004008`); LITERATURE | `biolink:has_input` / `biolink:has_output` |
| has primary input / has primary output | `RO:0004009` / `RO:0004008` | MF/BP → CHEMICAL | ONTOLOGY_AXIOM (GO logical definitions) | `biolink:has_input` / `biolink:has_output` |
| has intermediate | `RO:0002505` | BP/PATHWAY → CHEMICAL | ONTOLOGY_AXIOM | `biolink:has_participant` |
| has participant | `RO:0000057` | MF/BP/PATHWAY → CHEMICAL/INGREDIENT, when the source's direction is unreliable | SIBLING_RECORD; ONTOLOGY_AXIOM | `biolink:has_participant` |
| participates in | `RO:0000056` | CHEMICAL/INGREDIENT → TRAIT/BP | SIBLING_RECORD (a TraitMech `MECHANISTIC` graph grounds the chemical) | `biolink:participates_in` |
| input of / output of | `RO:0002352` / `RO:0002353` | CHEMICAL/INGREDIENT → PATHWAY/BP/MF | SIBLING_RECORD (PathwayMech `consumes` / `produces`) | `biolink:participates_in` |
| enables | `RO:0002327` | GENE_OR_PROTEIN/STRUCTURE → MF | SIBLING_RECORD (xref closure) | `biolink:enables` |
| contributes to | `RO:0002326` | GENE_OR_PROTEIN (subunit) → MF/BP | SIBLING_RECORD (xref closure) | `biolink:contributes_to` |
| involved in | `RO:0002331` | GENE_OR_PROTEIN/MF → BP/PATHWAY | SIBLING_RECORD (xref) | `biolink:actively_involved_in` |
| starts with / ends with | `RO:0002224` / `RO:0002230` | BP/PATHWAY → MF/BP | ONTOLOGY_AXIOM | `biolink:has_part` |
| located in | `RO:0001025` | GENE_OR_PROTEIN/MF → STRUCTURE/CELLULAR_LOCALIZATION/ORGANELLE | SIBLING_RECORD (including `SHARED_MEMBER`); DATABASE_RECORD (a protein example's cached UniProt location equals the node label) | `biolink:located_in` |
| results in transport across | `RO:0002342` | BP/MF → STRUCTURE/CELLULAR_LOCALIZATION | ONTOLOGY_AXIOM | `biolink:related_to` |
| molecularly interacts with | `RO:0002436` | GENE_OR_PROTEIN/STRUCTURE ↔ CHEMICAL/INGREDIENT | SIBLING_RECORD + ONTOLOGY_AXIOM (GO binding term); SIBLING_RECORD (BioLiP ligand and receptor) | `biolink:physically_interacts_with` |
| has characteristic | `RO:0000053` | GENE_OR_PROTEIN/MF → QUALITY | SIBLING_RECORD; DATABASE_RECORD (UniProt cofactor) | `biolink:has_attribute` |
| satisfies cofactor requirement | `MIM.vocab:satisfies_cofactor_requirement` | CHEMICAL/INGREDIENT → QUALITY (`COFACTOR_REQ_*`) | SIBLING_RECORD (the requirement's `xrefs` contain exactly the chemical) | `biolink:related_to` |
| causally upstream of; …, positive effect; …, negative effect | `RO:0002411` / `RO:0002304` / `RO:0002305` | MF/BP/PATHWAY/STATE → BP/TRAIT/STATE/QUALITY | LITERATURE; SIBLING_RECORD | `biolink:affects` |
| positively regulates / negatively regulates | `RO:0002213` / `RO:0002212` | CHEMICAL/INGREDIENT/GENE_OR_PROTEIN/RNA → GENE_OR_PROTEIN/MF/BP | LITERATURE | `biolink:regulates` |
| is small molecule inhibitor of | `RO:0012006` | CHEMICAL/INGREDIENT → GENE_OR_PROTEIN/MF | LITERATURE (an AntibioticMech record with the same grounding is a co-reference) | `biolink:affects` |
| causally influences | `RO:0002566` | INGREDIENT/CHEMICAL → ENVIRONMENTAL_FACTOR/STATE/QUALITY | LITERATURE | `biolink:affects` |

Labels follow RO as published. `RO:0018033` is "is deprotonated form of" and
`RO:0018034` "is protonated form of"; "is conjugate base of / acid of" are
ChEBI's own names for the same relations.
`MIM.vocab:satisfies_cofactor_requirement` is the only MIM-defined predicate.

## 5. From supplied form to active species

`MAPPING_SEMANTICS.md` Section 7 is authoritative here and carries the
verified examples; this is the short version. In this section, "Section N"
means a section of `MAPPING_SEMANTICS.md`.

The anchor is the record exactly as Section 3 identifies it: the supplied form.
Species the cell meets are separate nodes, and a bridge says what the supplied
form becomes, never what the record is. A blocked bridge is a prompt to re-check
identity, never a reason to relax a guard. Graphs are allowed only on a resolved
identity (Section 7.1): `MAPPED`, not a `NAMED_MEDIUM`, not graded
`PLACEHOLDER`, not in `mappings/duplicate_identifier_baseline.tsv`, and not
sharing its `identifier` with another non-`REJECTED` record.

| `bridge_kind` | `predicate_id` | Basis | Says |
|---|---|---|---|
| `HYDRATE_PART` | `BFO:0000051` | ONTOLOGY_AXIOM | A ChEBI hydrate has part its anhydrous form. |
| `ION_PART` | `BFO:0000051` with `stoichiometry` | ONTOLOGY_AXIOM, else CHEMICAL_STRUCTURE | A salt has part a constituent ion (with LITERATURE too for a transition-metal cation with a carbon-containing component). |
| `PROTONATION` | `RO:0018033` / `RO:0018034` | ONTOLOGY_AXIOM | One asserted protonation step. |
| `TAUTOMER` | `RO:0018036` | ONTOLOGY_AXIOM | An asserted tautomer. |
| `STRUCTURAL_FORM` | `rdfs:subClassOf` | ONTOLOGY_AXIOM + CHEMICAL_STRUCTURE | A structure-specific form is a structure-less supplied class (D-glucopyranose is a D-glucose). |
| `FORM_OF_PARENT` | `skos:broadMatch` | RECORD_SSSOM | First hop from a `cas:` or `kgmicrobe.*` anchor to the ChEBI parent in the record's own SSSOM row. |
| `COMPONENT` | `BFO:0000051` | RECORD_COMPONENT | A mixture has part one of its own `components` (Section 6). |

Bridges chain from the anchor toward the species: iron(2+) sulfate heptahydrate
(`CHEBI:75836`) has part iron(2+) sulfate (anhydrous) (`CHEBI:75832`,
`HYDRATE_PART`), which has part iron(2+) (`CHEBI:29033`, `ION_PART`), the species
the FeoB transporter takes up. Chemistry moves only toward what the supplied
form becomes, never up to a broader class to reach a sibling, and chemistry
edges carry no organism context. Every node must be reachable from the anchor,
and each bridged species must touch a non-chemistry edge. A salt, hydrate or
stock solution whose species have their own MIM records can delegate to them
with a `SPECIATION` graph (Section 7.4).

## 6. Evidence

Every edge and every protein example carries at least one fleet `EvidenceItem`
(`reference`, `snippet`, `notes`). Every edge also declares `assertion_basis`,
the offline checks it claims; the gate must confirm each one, and an
unconfirmed claim fails `BASIS_UNVERIFIED`.

`ONTOLOGY_AXIOM` is confirmed when the triple, or a declared sub-property of
it, is asserted or entailed in the committed ontology facts, and
`CHEMICAL_STRUCTURE` when the committed ChEBI SMILES, formula, charge and
InChIKey facts reproduce it. `SIBLING_RECORD` needs the pinned sibling record to
state the relation for exactly this grounding (`MAPPING_SEMANTICS.md` Section
7.3), `DATABASE_RECORD` a cached database entry, and `LITERATURE` a verbatim
snippet in `references_cache/`. `RECORD_COMPONENT` restates one of the record's
`components` entries and inherits its `component_assertion`; `RECORD_SSSOM`
restates the record's own SSSOM row.

The kind of source is read from `reference`:

| Reference form | Kind | Snippet rule | Confirms |
|---|---|---|---|
| `PMID:<n>`, `doi:<…>` | Literature | Required, with `notes`. Must be verbatim, after claw's `normalize()` (NFKC, collapsed whitespace, lowercase), in `references_cache/PMID_<n>.md`. A missing cache file is `MISSING_CACHE`: a warning while the graph is `REVIEW_NEEDED`, an error for `MECHANISTIC`. | LITERATURE |
| `https://github.com/CultureBotAI/<Mech>/blob/<40-hex commit>/<path>` | Sibling record | Optional. Must be verbatim in that record's pinned text in the snapshot. The commit must equal the pin, and the path must match the snapshot. | SIBLING_RECORD, from the structured statement, not the snippet |
| `CHEBI:`, `GO:`, `RO:` CURIE | Ontology | Forbidden (`ONTOLOGY_EVIDENCE_MUST_NOT_QUOTE`). | ONTOLOGY_AXIOM, CHEMICAL_STRUCTURE |
| `UniProtKB:`, `RHEA:`, `EC:`, `PDB:`, `ComplexPortal:` CURIE | Database | Allowed only if a cached entry exists and contains it (`SNIPPET_WITHOUT_CACHE` otherwise). | DATABASE_RECORD, from structured fields: catalytic participants and EC/Rhea, `PhysiologicalDirection`, location, TCDB xrefs, cofactor |

**No fabrication.**

- An LLM is never evidence. LLM help is recorded only as `llm_assisted` and
  `llm_model` on the curation event that adds or updates the graph.
- A missing hop is not an edge. Record it as a Discussion of kind
  `KNOWLEDGE_GAP` attached to `causal_graphs#<graph_id>` or
  `causal_graphs#<graph_id>/<edge_id>`.
- Fetches are anonymous, with no email address in any request.

**Scope gate.** `MECHANISTIC` requires all of:

- **G1.** Every claimed basis is confirmed.
- **G2.** At least one edge has a confirmed `LITERATURE` basis.
- **G3.** No biological edge rests only on `SIBLING_RECORD` support from
  `SEEDED` or `PROPOSED` sibling records; it also needs `LITERATURE`,
  `DATABASE_RECORD` or `ONTOLOGY_AXIOM`, or `SIBLING_RECORD` support from a
  `REVIEWED` record.
- **G4.** `organism_scope` is set whenever organism-specific evidence is cited,
  and every cited taxon is on its lineage (`TAXON_SCOPE_MISMATCH` otherwise).
- **G5.** Every protein example has a verified literature or cached-database
  item, and its UniProt organism equals `taxon_id`.
- **G6.** `explains` names roles on the record. A role whose evidence is all
  computational prediction gives a warning.
- **G7.** No edge is `OBSOLETE_REPLACED`.
- **G8.** A curation event records the graph.

A `NONMECHANISTIC` graph needs `scope_notes`.

**Compatibility with `qc-evidence`.** `just qc-evidence` runs claw's
`validate_evidence_references.py` through `scripts/run_shared_evidence_validator.py`.
On 2026-10-05 that validator walked only `ontology_mapping.evidence`,
`role_assignments` and `cellular_role_assignments`, reading `pmid` and `doi`;
MIM has retired both role keys, so it sees neither role facets nor graphs. A
planned claw change extends the walk to the role facets, to
`causal_graphs[].edges[].evidence[]`,
`causal_graphs[].nodes[].protein_examples[].evidence[]` and
`discussions[].evidence`, parses `reference`, and is strict for the new
containers. Until it lands, `qc-causal-graphs` runs the same snippet check
locally with the same `normalize()`, so the gate is never lost.

**Curation event.** Every graph write appends an event whose `changes` names
the graph. `CurationEvent.action` is a free-form pattern; `CAUSAL_GRAPH_ADDED`
and `CAUSAL_GRAPH_UPDATED` are the two actions for graphs, and withdrawing a
graph is an update.

```yaml
- timestamp: "2026-10-05T12:00:00Z"
  curator: <curator id>
  action: CAUSAL_GRAPH_ADDED
  changes: "causal_graphs#dglc_pts_uptake_bsub added (7 nodes, 6 edges; REVIEW_NEEDED)"
  llm_assisted: true
  llm_model: <model id>
```

## 7. Links to sibling Mechs

A graph links to a record in another Mech in exactly one way: a node whose
`grounding` equals that record's identifier. The node's owner is resolved by
node-type precedence and `target_mech` (section 3), its `label` must equal the
owner record's label (`LABEL_DRIFT`), and each edge touching it must be
admissible under `MAPPING_SEMANTICS.md` Section 7.3.

### Pins

Each sibling is pinned by commit in `conf/sibling_pins.yaml` (planned). A pin
is an input, not an observation: it moves only through an explicit
`--advance-pin <key>`, which writes a link-diff report, and no tool reads a
sibling's HEAD or working tree.

| Pin key | Environment variable for a local checkout | Record files (id field) | Owned prefixes |
|---|---|---|---|
| `proteintraitsmech` | `PROTEINTRAITSMECH_ROOT` | `data/traits/**/*.yaml` (`identifier`) | `TCDB`, `EC`, `RHEA`, `NCBIfam`, `Pfam`, `InterPro`, `PANTHER`, `PROSITE`, `ComplexPortal`, `MCSA`, `CDD`, `HAMAP`, `proteintraitsmech`, `GO` |
| `pathwaymech` | `PATHWAYMECH_ROOT` | `data/pathways/*.yaml` (`id`) | `MetaCyc`, `gomodel`, `Reactome`, `WikiPathways` |
| `cellstructuremech` | `CELLSTRUCTUREMECH_ROOT` | `data/structures/**/*.yaml` (`identifier`) | `cellstructuremech`, `GO` |
| `traitmech` | `TRAITMECH_ROOT` | `data/traits/**/*.yaml` (`identifier`) | `traitmech`, `METPO` |
| `taxonmech` | `TAXONMECH_ROOT` | TaxonMech's `data/taxa/PATHS.tsv` index (`identifier`) | `NCBITaxon` |

### Committed snapshots

CI never needs a sibling checkout or an ontology database. Everything it reads
is committed (all planned):

| File | One row per | Holds |
|---|---|---|
| `mappings/cross_mech_references.tsv` | Sibling record referenced by a grounding, an evidence permalink, the xref closure or a co-reference | Its pinned commit, path, blob sha, label, status, taxa, how it is referenced, and the sha256 of its quotable text. |
| `mappings/cross_mech_assertions.jsonl` | Record above | The structured statements the gate checks (xrefs, mapped xrefs, chemical participants, graph nodes and edges, pathway edges, functions, protein examples) and the record's quotable text, which CI re-hashes. |
| `mappings/ontology_facts.tsv` | Ontology fact used by a bridge, axiom, guard, rival subclass or taxon lineage | Edges, entailed edges, SMILES, formulas, charges, InChI and InChIKeys, xrefs, replacements and labels, with the source database's sha256. |
| `references_cache/UniProtKB_<acc>.json` | Protein example or database citation | An anonymous UniProt REST entry: organism, catalytic activities with `PhysiologicalDirection`, location, cofactor, xrefs, versions and retrieval date. |
| `mappings/cross_mech_links.tsv` | Link (derived; CI regenerates it and fails `LINKS_STALE` on a diff) | `record_path, identifier, graph_id, node_id, link_kind, grounding, node_type, owner_mech, owner_record_path, owner_label, owner_status, match_kind, pinned_commit, organism_scope, genome_pointer`. |

### The links ledger

`mappings/cross_mech_links.tsv` (LINKS) lists every link a reader can follow
from a MIM record, by `link_kind`:

- **`GRAPH_NODE`**: a graph node grounded to a sibling record.
- **`PROTEIN_EXAMPLE_TAXON`**: a protein example's taxon, resolved to a
  TaxonMech record.
- **`GENOME_POINTER`**: an assembly reached through TaxonMech (section 8).
- **`SPECIES_COREFERENCE`**: a sibling record that grounds one of a graph's
  species without MIM asserting any relation to it. Respiration and energy
  traits in TraitMech that ground sulfate, nitrate or iron(2+) appear this way;
  they are candidates for organism-conditional graphs, which stay gated until
  the record carries the matching role (section 8). ProteinTraitsMech
  co-references are limited to `REVIEWED` records whose participant role for
  the species is `TRANSPORTED` or `COFACTOR`.
- **`VIA_SPECIES_RECORD`**: a link reached through a species record that a
  `SPECIATION` graph delegates to.

A generated `docs/data/cross_mech_links.json` (planned, step 6) publishes the
same links for pages and for siblings' backlinks.

### Refreshing (local, never in CI)

Three planned recipes regenerate the committed inputs; their diffs are reviewed
in the PR:

- `just refresh-cross-mech-snapshot [--advance-pin KEY]` reads each sibling
  checkout (found through the environment variables above) at its pinned commit
  only, and writes deterministic snapshot files plus a link-diff report.
- `just refresh-ontology-facts` extracts the facts from local OAK SemSQL
  databases and records each database's sha256.
- `just fetch-uniprot <acc...>` caches UniProt entries anonymously.

### The offline gate

`just qc-causal-graphs` (planned) exits 2 on any error and joins `just qc`. In
order, it runs: closed LinkML validation; claw's structure audit with the
`INGREDIENT` anchor; the identity gate and anchor rules; `explains` role checks;
predicate labels and endpoint types; ownership and labels; evidence permalinks
and snippets; confirmation of every claimed basis; bridge recomputation; taxon
lineage and TaxonMech resolution; the scope gate; the curation event; and the
links-ledger diff.

| Code | Severity | Meaning and remedy |
|---|---|---|
| `SNAPSHOT_INCOMPLETE`, `PIN_MISMATCH`, `SNAPSHOT_TAMPERED`, `ONTOLOGY_FACT_MISSING` | error | A grounding, permalink or fact is missing from the snapshot at the pin, or its text hash drifted. Run the refresh recipes. |
| `UNRESOLVED_SIBLING`, `RETIRED_TARGET`, `AMBIGUOUS_OWNER` | error | An owned-prefix CURIE is absent or deprecated at the pin, or has two owners and no precedence. Fix the grounding or set `target_mech`. |
| `LABEL_DRIFT`, `XREF_UNDECLARED`, `PREDICATE_LABEL_MISMATCH`, `ENDPOINT_TYPE` | error | Correct the label, xref or predicate, usually in the same PR as a pin advance. |
| `RECIPROCAL_GROUNDING_MISMATCH`, `BASIS_UNVERIFIED` | error | The sibling does not state the relation for this grounding, or a claimed check failed. Add a bridge, change the target, or drop the claim. |
| `BRIDGE_GUARD_FAILED`, `STOICHIOMETRY_MISMATCH`, `CHARGE_IMBALANCE`, `COMPLEXATION_NEEDS_LITERATURE` | error | Re-check identity (`MAPPING_SEMANTICS.md` Section 3) or add literature. |
| `IDENTITY_GATE`, `ANCHOR_MISMATCH`, `EXPLAINS_UNKNOWN_ROLE` | error | Resolve the identity, or curate the role first. |
| `SNIPPET_NOT_IN_SOURCE`, `SNIPPET_WITHOUT_CACHE`, `ONTOLOGY_EVIDENCE_MUST_NOT_QUOTE`, `LITERATURE_WITHOUT_SNIPPET_OR_NOTES` | error | Fix the evidence item. |
| `TAXON_SCOPE_MISMATCH`, `PROTEIN_EXAMPLE_TAXON`, `PROTEIN_EXAMPLE_NODE_TYPE` | error | Split the graph by organism, or fix the example. |
| `SCOPE_GATE`, `CURATION_EVENT_MISSING`, `LINKS_STALE` | error | Demote to `REVIEW_NEEDED`, add the event, or regenerate the ledger. |
| `MISSING_CACHE` | warning; error if `MECHANISTIC` | Fetch and commit the cache file. |
| `RECIPROCAL_DIRECTION_MISMATCH`, `OBSOLETE_REPLACED`, `XREF_EQUIVALENT`, `SHARED_MEMBER`, `NO_TAXONMECH_RECORD`, `GENOME_JOIN_UNAVAILABLE`, `GRAPH_KIND_ROLE_UNUSUAL`, `DELEGATION_TARGET_HAS_NO_MECHANISM`, `BRIDGE_WITHOUT_PURPOSE`, `SEEDED_ONLY_SUPPORT` | warning | Review; shown on pages and in the readiness scorer. |
| `GENERIC_SPECIALISATION` | info | None. |

A weekly, non-blocking drift probe is planned to compare the pins with each
sibling's `origin/main` and report which links would change. It never advances a
pin, edits a sibling or posts anything.

## 8. Genome and protein scope

| Information | Owner | How MIM refers to it |
|---|---|---|
| Protein family, function, transport function, complex | ProteinTraitsMech (CellStructureMech for complexes) | Node grounding (`GENE_OR_PROTEIN`, `MOLECULAR_FUNCTION`, `STRUCTURE`) |
| Organism-specific protein | UniProtKB | `protein_examples` on a `GENE_OR_PROTEIN` or `MOLECULAR_FUNCTION` node, with evidence and `taxon_id` |
| Organism, strain, genome assembly | TaxonMech | `organism_scope` and `taxon_id` resolve to a TaxonMech record; the ledger adds a `GENOME_POINTER` |
| Gene presence or loci in genomes; genome-predicted capability | KG-Microbe and annotation pipelines | Not stored. A query-time join through the EC, RHEA, GO process and GO component groundings in MIM graphs |
| Organism-level utilization ("ferments", "uses as carbon source") | KG-Microbe (BacDive), TraitMech | Never a graph edge. Existing role mappings (for example `NITROGEN_SOURCE` → `METPO:2000014`) align at export and target the active species, not the salt |

Rules:

1. Groundings refuse UniProtKB, NCBITaxon, assembly and strain prefixes, and
   there is no `TAXON` node type.
2. A protein example is either a `QUALIFIED` or `CURATOR` example in the sibling
   record, or is backed by a cached UniProt entry, a BioLiP or ComplexPortal
   structure, or literature. An unqualified `SWISSPROT_PROFILE` example in a
   sibling record is a pointer, not evidence.
3. The cached UniProt organism must equal `taxon_id`.
4. A genome pointer walks TaxonMech, because strain-rank records hold no
   assemblies. For *Bacillus subtilis* 168 (`NCBITaxon:224308`, rank strain),
   the assembly `GCA_000009045` sits on the species record
   `bacillus_subtilis.yaml`, under strain `bacdive_1156`. TaxonMech states that
   sharing a taxon is not link evidence, so a genome pointer never asserts that
   a genome carries a gene.
5. `GENOME_JOIN_UNAVAILABLE` warns when a mechanism's only protein-level
   groundings are TCDB, NCBIfam, Pfam, InterPro or PANTHER, with no EC, RHEA or
   GO activity, process or component neighbour, because KG-Microbe has no TCDB
   nodes to join on.
6. Organism-conditional respiration traits (TraitMech `traitmech:000105`,
   `000104`, `000122`, `000107`) enter a graph only after the record carries the
   matching curated `cellular_metabolic_roles` entry (`ELECTRON_ACCEPTOR` or
   `ELECTRON_DONOR`) with `metabolic_context`. Until then they appear in the
   ledger as `SPECIES_COREFERENCE` rows.

## 9. Consumers and phasing

### 9.1 Phase 1: the schema, the gate and the ledger (no KGX change)

- **Both data surfaces.** Graphs are authored in the per-record files and reach
  `data/curated/` through `just sync-curated`. `scripts/export_individual_records.py`
  treats only `discussions` as per-record-authored, so graphs round-trip like
  any other slot, and `just qc-roundtrip` covers them.
- **KGX.** `src/mediaingredientmech/export/kgx.py` already serializes each full
  record into `record_json`, and `src/mediaingredientmech/validation/semantic_release.py`
  checks that it equals the source record, so graphs ride along with no new
  assertions.
- **Section refresh.** `record_refresh.py` (PR #817, open on 2026-10-05) lists
  `causal_graphs` as a refreshable section with the `CAUSAL_GRAPH_ADDED` and
  `CAUSAL_GRAPH_UPDATED` actions. The section must leave that list in phase 2,
  once reviews read causal edges.
- **claw coverage.** The planned MIM stanza in claw's `fleet.yaml`:

  ```yaml
  causal_graph_coverage:
    status: enabled
    settings:
      graph_shape: graph_list
      record_id_field: identifier
      scope_field: scope_status
      mechanistic_scopes: [MECHANISTIC]
      graph_facets: [graph_kind]
      anchor_node_types: [INGREDIENT]
      duplicate_grounding_check: true
      exempt_when:
        - "mapping_status=REJECTED|UNMAPPED|AMBIGUOUS|NEEDS_EXPERT|PENDING_REVIEW|IN_PROGRESS"
        - "ingredient_type=NAMED_MEDIUM"
        - "ontology_mapping.mapping_quality=PLACEHOLDER"
      strata:
        - ingredient_type
        - ontology_mapping.mapping_quality
  ```

  The same claw change narrows MIM's record globs to
  `data/ingredients/mapped/*.yaml` and `data/ingredients/unmapped/*.yaml`,
  excluding the gitignored `mapped/backups`. A `SPECIATION` graph counts under
  `with_graph` but not as mechanistic.
- **Readiness scorer.** `scripts/score_causal_graph_readiness.py` keeps ranking
  graphless records first and gains columns for graph counts, roles explained,
  unverified bases, resolved and unresolved sibling links, co-reference
  candidates and the identity-gate block reason.
- **Pages.** `src/mediaingredientmech/render_ingredient_pages.py` gains panels
  for the mechanism graphs (tables canonical, a diagram optional), the active
  species and their bridge chain, linked records grouped by Mech (asserted links
  apart from co-references), and organisms and genomes.
- **Flat exports.** The `docs/data/cross_mech_links.json` producer is registered
  in `scripts/check_flat_export_coverage.py`, which `just qc-flat-coverage`
  runs.

### 9.2 Phase 2: KGX causal edges (not yet implemented)

Nothing in this subsection exists yet. The plan is one `causal_edge` assertion
per exported edge (`source_position` `<graph_id>/<edge_id>`), using the Biolink
predicate from section 4 with `relation` set to `predicate_id`. Grounded nodes
keep their CURIE, and the anchor uses its identifier, which the SSSOM identity
row already joins to `MIM:<slug>`. `organism_scope` becomes the species context
of non-chemistry edges only. Edges that KG-Microbe already has are not exported:
ChEBI-axiom chemistry, `COMPONENT` edges (exported as components) and
`FORM_OF_PARENT` edges (in the SSSOM), and nothing new is emitted on
`MIM:<slug>`. Publication is review-gated: an independent projection in
`semantic_release.py`, and a causal branch in `supported_kgx.py` that, among
other conditions, admits an edge only if its graph is `MECHANISTIC`, its bases
are confirmed at report time and it connects to the anchor through approved
edges. New causal rows stay `OPEN` until reviewed.

## 10. How to add a graph

Steps that name `qc-causal-graphs`, the refresh recipes or `fetch-uniprot`
need step 3 of the status table, and writing a graph needs the schema (step 2).

1. **Pass the identity gate first** (section 5). If the record fails it, fix the
   identity with the `curate-yaml-record` skill and `MAPPING_SEMANTICS.md`
   Section 3 before drawing anything.
2. **Name what the graph explains**: existing roles only, in `explains`. A
   missing role is curated first, with its own evidence. Pick the `graph_kind`.
3. **Choose one `organism_scope`**, or none for a taxon-agnostic graph. Split
   mixed-organism material into separate graphs.
4. **Draw the anchor and bridge to the active species**, stopping at the species
   the biology acts on. If that species or a component has its own MIM record,
   put the mechanism there and give this record a `SPECIATION` graph.
5. **Add the biology.** Ground each node to a sibling record's exact identifier
   and copy its label. Add only edges the pinned sibling states for that
   grounding, or that ontology, database or literature evidence supports, and
   claim only the bases that evidence supports.
6. **Add protein examples** from `QUALIFIED` or `CURATOR` sibling examples,
   cached UniProt entries or literature, each on the `organism_scope` lineage.
7. **Write the evidence**: at least one item per edge, with snippets only when
   verbatim in a committed copy. Fetch missing abstracts with `just fetch-pubmed`
   and UniProt entries with `just fetch-uniprot`. Record a missing hop as a
   `KNOWLEDGE_GAP` Discussion, never as an invented edge.
8. **Set the scope** to `REVIEW_NEEDED`, or `NONMECHANISTIC` with `scope_notes`
   for `SPECIATION`, and append a `CAUSAL_GRAPH_ADDED` or `CAUSAL_GRAPH_UPDATED`
   event, with `llm_assisted` and `llm_model` if an LLM helped.
9. **Refresh the snapshots** if the graph cites a new sibling record, ontology
   fact or UniProt entry, and review the diffs.
10. **Synchronize and validate**: `just sync-curated`, then `just validate-all`,
    `just qc-evidence`, `just qc-causal-graphs`, `just qc-sssom`,
    `just qc-roundtrip` and `just qc-flat-coverage`. Confirm on disk that the
    record, the aggregate, the snapshot files and the ledger rows changed, not
    only that the commands exited 0.

For a batch, canary one record end to end through the same script and output
path first. Generated proposals go to `proposals/causal_graphs/<stem>.yaml`
(planned, step 7), which coverage does not read, and are accepted one record at a
time.

## See also

- `MAPPING_SEMANTICS.md`: Section 3 (identity granularity), Section 6
  (component partonomy) and Section 7 (anchors, bridges and link admissibility).
- `docs/stock_components.md`: the `components` contract that `COMPONENT` edges
  mirror.
- `docs/KGX_EXPORT.md`: the current KGX export, which carries graphs only inside
  `record_json` until phase 2.
- `docs/attaches_to.md`: hash anchors for Discussions, such as
  `causal_graphs#<graph_id>/<edge_id>`.
- `.claude/skills/curate-yaml-record/SKILL.md`: single-record curation.
