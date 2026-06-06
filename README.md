# Personal AI Research Assistant

A local AI research assistant built with Streamlit, ChromaDB, and LLMs (Ollama + Groq).

## Structure

- `app/` — Core application modules
  - `main.py` — Streamlit app entry point
  - `ingest.py` — Document loading and chunking
  - `retriever.py` — Embedding and vector search
  - `llm.py` — LLM wrapper (Ollama + Groq)
  - `agent.py` — MCP tool orchestration
- `mcp_server/server.py` — Custom MCP tools
- `data/` — Upload your PDFs and docs here
- `chroma_db/` — Auto-created by ChromaDB

## Setup

1. Copy `.env.example` to `.env` and add your API keys
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app/main.py`
