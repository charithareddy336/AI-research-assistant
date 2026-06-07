# Personal AI Research Assistant

A Personal AI Research Assistant built using Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), and Vector Databases. The application helps users interact with documents, retrieve relevant information, and generate intelligent responses through a simple Streamlit interface.

This project combines document retrieval and conversational AI to create an assistant capable of answering questions based on uploaded documents and external knowledge sources.

## Features

* AI-powered question answering
* Retrieval-Augmented Generation (RAG)
* Document ingestion and processing
* Vector search using ChromaDB
* Support for local and cloud-based LLMs
* Interactive Streamlit user interface
* PDF and document-based knowledge retrieval

## Technologies Used

* Python
* Streamlit
* ChromaDB
* Ollama
* Groq API
* LangChain
* Large Language Models (LLMs)

## Project Structure

* `app/`

  * `main.py` – Streamlit application entry point
  * `ingest.py` – Document processing and chunking
  * `retriever.py` – Embedding generation and vector search
  * `llm.py` – LLM integration layer
  * `agent.py` – Tool orchestration and workflow management
* `mcp_server/`

  * `server.py` – Custom MCP tools and services
* `data/`

  * Stores uploaded documents and PDFs
* `chroma_db/`

  * Vector database storage

## Setup

1. Clone the repository.
2. Create and activate a Python environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure API keys in the `.env` file.
5. Run the application:

```bash
streamlit run app/main.py
```

## Applications

* Research assistance
* Document-based question answering
* Knowledge management
* Academic and technical document analysis
* AI-powered information retrieval

## Future Improvements

* Multi-document querying
* Advanced agent workflows
* Web search integration
* Conversation memory
* Improved citation and source tracking

## Author

Charitha Reddy
