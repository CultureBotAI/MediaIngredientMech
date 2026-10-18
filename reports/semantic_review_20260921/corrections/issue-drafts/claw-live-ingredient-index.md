Destination: https://github.com/CultureBotAI/culturebotai-claw/issues
Title: Exclude MIM backups and merge tombstones from the unified name index

`build_unified_ingredient_mapping.py::load_mim_index` recursively loads ingredient YAML, including six ignored backup records in the current MIM checkout. Its first-writer-wins name index can also retain a REJECTED record: `Nano.yaml` sorts before `Nano3.yaml`, so the retired NCIT nano-prefix identity can win the corrected sodium-nitrate synonym.

Read only direct `data/ingredients/{mapped,unmapped}/*.yaml` files and resolve merged labels through active representatives. Preserve explicitly ambiguous/unmapped records as nonidentities. Add regression tests covering a nested backup and a rejected record that sorts before its active representative.

MIM's correction batch uses an isolated live-record input tree as a local workaround. The shared producer still needs this fix.
