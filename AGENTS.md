# Agent Guide — monarch-mcp

Brief for AI coding agents (Claude Code, Codex) working in this repo or routing biomedical questions through it.

## What this server is
MCP server wrapping the Monarch Initiative API. Cross-species, phenotype-driven knowledge graph integrating 33 biomedical resources (HPO, MONDO, OMIM, Orphanet, MGI/ZFIN/etc., Reactome, STRING, Bgee, …).

## Run locally (stdio)
```bash
uv sync
uv run python -m monarch_mcp.server              # stdio (default)
```

HTTP/SSE: append `--transport http --host 127.0.0.1 --port 8000`.

## Use this server for
- Phenotype matching and semantic similarity (HPO-driven rare-disease diagnostics)
- Cross-species gene–phenotype–disease relationships (model-organism evidence)
- Disease ↔ phenotype, gene ↔ phenotype, disease models
- Ontology mapping between OMIM / MONDO / HPO / Orphanet
- Association walks across genes, diseases, phenotypes, chemicals, variants

Prefer over other servers when the question hinges on **HPO phenotype profiles**, **rare-disease ontology**, or **cross-species model-organism evidence**.

## Triage hints
- Phenotype-first questions ("what disease matches these HPO terms") → Monarch.
- Curated semantic similarity beats raw association lists for diagnostic-style queries.
- Ontology IDs use prefixes (`HP:0001250`, `MONDO:0007739`, `OMIM:143100`); pass them as-is.

## Pitfalls
- API endpoint default is `https://api.monarchinitiative.org/v3/api/`; override only via `MONARCH_API_URL`.
- Some associations are sparse for non-human organisms — empty results are not always errors.
- Pagination is required for large association sets; do not assume a single page covers everything.

## Source layout
- `src/monarch_mcp/server.py` — FastMCP entrypoint
- `src/monarch_mcp/client.py` — HTTP client to Monarch API
- `src/monarch_mcp/tools/` — tool implementations

## Dev
```bash
uv sync --extra dev
uv run pytest tests/ -v
```

## When editing tools
1. Add HTTP call in `client.py` if a new endpoint is needed.
2. Wrap in a tool under `src/monarch_mcp/tools/`; expose via the registry.
3. Add a unit test mocking the HTTP response.
