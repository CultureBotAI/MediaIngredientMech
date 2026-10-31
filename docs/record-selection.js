/* Exact source-file selection for map links; ontology IDs can be shared. */
(function (root) {
    "use strict";
    const api = {
        recordFromHash(hash) {
            return new URLSearchParams(String(hash).replace(/^#/, "")).get("record") || "";
        },
        matches(ingredient, selectedRecord) {
            return !selectedRecord || ingredient.source_file === selectedRecord;
        },
        clearRecord(hash) {
            const parameters = new URLSearchParams(String(hash).replace(/^#/, ""));
            parameters.delete("record");
            const remaining = parameters.toString();
            return remaining ? "#" + remaining : "";
        }
    };
    root.MIMRecordSelection = api;
    if (typeof module !== "undefined" && module.exports) module.exports = api;
})(globalThis);
