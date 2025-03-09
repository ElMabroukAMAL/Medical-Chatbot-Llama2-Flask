## Project Overview

A Flask-based medical chatbot using LangChain, Pinecone, and Meta's Llama 2 for efficient data retrieval and question answering.

1. **Extract & Process Data** – Load medical PDFs and extract text.
2. **Chunk Text** – Split content into manageable parts.
3. **Generate Embeddings** – Convert chunks into vector representations using MiniLM.
4. **Index Data** – Store embeddings in Pinecone for fast semantic search.
5. **Build Knowledge Base** – Organize vectorized data for efficient retrieval.
6. **User Query Processing** – Convert user questions into embeddings.
7. **Search Knowledge Base** – Retrieve relevant document vectors.
8. **Rank & Filter Results** – Select the most relevant text.
9. **Generate Response** – Use Llama 2 to formulate accurate answers.
10. **Deliver Answer** – Display response via Flask web app.
