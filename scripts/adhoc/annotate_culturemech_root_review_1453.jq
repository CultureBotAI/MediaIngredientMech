# Purpose: attach explicitly inspected primary references to root's authored review.
# Input: root-annotations.json; output: frozen root-tail-reviewed-annotations.json.
# Issue: 1453 / PR1460. Date: 2026-11-17. No scientific dispositions are inferred.
.entries |= map(
  if .owner_index == 401 then
    .evidence_locators += ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1471"]
  elif .owner_index == 404 then
    .evidence_locators += ["https://github.com/CultureBotAI/MediaIngredientMech/issues/1480 nonblocking formula-synonym classification follow-up"]
  elif .owner_index == 424 then
    .review_reason += " The manufacturer's inspected Vitox IFU identifies the named supplement with proportional SR0090A/H formulations; this corroborates the named supplement category, without selecting either vial product or asserting equal stock volume."
    | .evidence_locators += ["https://documents.thermofisher.com/TFS-Assets/MBD/Instructions/MBD_BT_IFU-0451%20SR0090H_SR0090A%20VITOX%20SUPP_RECONSTITUTION%20FLUID%2010X2LTRS.pdf page1 product identity/formula, inspected2026-11-17"]
  elif .owner_index == 428 then
    .review_reason += " The inspected primary MediaDive J609/solution4469 recipe independently names X10 Jamarin S and identifies Jamarin S as the manufacturer's synthetic seawater preparation; its210mL input is distinct from the erroneous percentage."
    | .evidence_locators += ["https://www.bacmedia.dsmz.de/solutions/4469 named preparation and source input inspected2026-11-17"]
  else . end
)
