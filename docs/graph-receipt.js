/* Verify the bytes a graph page plots; absent receipts remain explicitly legacy. */
(function (scope) {
    'use strict';
    const SHA256 = /^[0-9a-f]{64}$/;
    async function verify(bytes, receipt, basename) {
        const data = JSON.parse(new TextDecoder('utf-8', {fatal: true}).decode(bytes));
        if (!Array.isArray(data) || data.length === 0 || data.some(row =>
            !row || typeof row.id !== 'string' || !row.id ||
            !Number.isFinite(row.umap_x) || !Number.isFinite(row.umap_y)) ||
            new Set(data.map(row => row.id)).size !== data.length) {
            throw new Error('Invalid ingredient graph points');
        }
        if (receipt === null) {
            return {data, verified: false, title: 'Ingredient graph embedding map',
                description: `Legacy graph coordinates for ${data.length.toLocaleString()} ingredients; source and reducer provenance are unverified.`};
        }
        if (receipt.schema_version !== 2 || receipt.embedding_family !== 'kg_microbe_deepwalk' ||
            receipt.source?.lineage !== 'parsed-source-bytes' || !SHA256.test(receipt.source?.sha256) ||
            typeof receipt.source.filename !== 'string' || !receipt.source.filename ||
            !receipt.outputs || Object.keys(receipt.outputs).length !== 1 || !SHA256.test(receipt.outputs[basename])) {
            throw new Error('Unsupported or incomplete graph receipt');
        }
        const hash = Array.from(new Uint8Array(await scope.crypto.subtle.digest('SHA-256', bytes)))
            .map(value => value.toString(16).padStart(2, '0')).join('');
        if (hash !== receipt.outputs[basename]) throw new Error('Graph JSON checksum mismatch');
        const coverage = receipt.coverage;
        const matrix = receipt.matrix;
        const ledger = receipt.matching?.rows;
        const labels = {pacmap: 'PaCMAP', umap: 'UMAP', sfdp: 'Graphviz sfdp'};
        const method = receipt.projection?.method;
        if (!Object.hasOwn(labels, method) || !coverage || !Number.isInteger(coverage.eligible) ||
            coverage.projected !== data.length || coverage.eligible < data.length ||
            !Array.isArray(matrix?.row_ids) || matrix.row_ids.length !== data.length ||
            !Array.isArray(ledger) || ledger.length !== coverage.eligible ||
            new Set(ledger.map(row => row.identifier)).size !== ledger.length ||
            matrix.row_ids.some((identifier, index) => identifier !== data[index].id)) {
            throw new Error('Graph receipt coverage or ordered identities mismatch');
        }
        const projected = new Map(ledger.filter(row => row.status === 'projected').map(row => [row.identifier, row]));
        if (projected.size !== data.length || data.some(row => {
            const matched = projected.get(row.id);
            return !matched || matched.match_method !== row.embedding_method ||
                matched.source_nodes?.length !== 1 || matched.source_nodes[0] !== row.embedding_source_node;
        })) throw new Error('Graph receipt lookup ledger mismatch');
        return {data, verified: true, title: `Ingredient graph embedding map — ${labels[method]}`,
            description: `${labels[method]}: ${coverage.projected.toLocaleString()} of ${coverage.eligible.toLocaleString()} eligible ingredients; ` +
                `${(coverage.eligible - coverage.projected).toLocaleString()} omitted without graph vectors. ` +
                `Source: ${receipt.source.filename}; SHA-256 ${receipt.source.sha256}.`, receipt};
    }
    async function load(dataUrl, receiptUrl) {
        const response = await fetch(dataUrl);
        if (!response.ok) throw new Error(`Graph data request failed: ${response.status}`);
        const bytes = await response.arrayBuffer();
        const metadata = await fetch(receiptUrl);
        if (!metadata.ok && metadata.status !== 404) throw new Error(`Graph receipt request failed: ${metadata.status}`);
        const result = await verify(bytes, metadata.status === 404 ? null : await metadata.json(), dataUrl.split('/').pop());
        result.receiptUrl = receiptUrl;
        return result;
    }
    function pointDescription(row, verified) {
        return verified ? `Graph match: ${row.embedding_method}; source node: ${row.embedding_source_node}.` :
            'Legacy graph point; matching method and source node are unverified.';
    }
    function display(result, heading, subtitle, explanation) {
        heading.textContent = result.title;
        subtitle.textContent = result.description;
        explanation.textContent = result.verified ?
            'Only ingredients matched to graph vectors are plotted; ingredients without vectors are omitted. ' +
            'Mapping status describes record curation. Hover for the verified graph match and source node.' :
            'These legacy coordinates have unverified matching and coverage. Mapping status alone does not establish a graph source.';
        if (result.verified) {
            const link = document.createElement('a');
            link.href = result.receiptUrl;
            link.textContent = ' Source, coverage and projection receipt';
            subtitle.appendChild(link);
        }
    }
    const api = {verify, load, display, pointDescription};
    if (typeof module === 'object' && module.exports) module.exports = api;
    else scope.IngredientGraphReceipt = api;
})(globalThis);
