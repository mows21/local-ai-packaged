# Vector DB initialization and schema setup for agent orchestration

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions
import os

# Initialize ChromaDB client
DB_PATH = os.path.join(os.path.dirname(__file__), 'chroma_db')
client = chromadb.Client(Settings(persist_directory=DB_PATH))

# Define collections for agents
collections = {
    'code': client.get_or_create_collection('code'),
    'tasks': client.get_or_create_collection('tasks'),
    'docs': client.get_or_create_collection('docs'),
    'workflows': client.get_or_create_collection('workflows'),
}

# Universal embedding function (can be swapped for OpenAI, HuggingFace, etc.)
embedder = embedding_functions.DefaultEmbeddingFunction()

def add_item(collection_name, item_id, content, metadata=None):
    if collection_name not in collections:
        raise ValueError(f'Unknown collection: {collection_name}')
    collections[collection_name].add(
        documents=[content],
        metadatas=[metadata or {}],
        ids=[item_id],
        embeddings=None # Use default embedder
    )

def query_collection(collection_name, query_text, n_results=5):
    if collection_name not in collections:
        raise ValueError(f'Unknown collection: {collection_name}')
    return collections[collection_name].query(
        query_texts=[query_text],
        n_results=n_results
    )

# Example usage (to be removed in prod)
if __name__ == '__main__':
    add_item('docs', 'global_rules', 'Sample global rules content')
    print(query_collection('docs', 'rules'))
