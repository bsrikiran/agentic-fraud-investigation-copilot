"""
Purpose: Initializing ChromaDB, configuring the fraud_policy_knowledge_base collection, and handling inserts.
"""
import os
import logging
from typing import List, Dict, Any
import chromadb
from chromadb.config import Settings

logger = logging.getLogger("rag.vector_store")

class PolicyVectorStore:
    """Maintains transactional access routines over isolated local directory databases pools."""
    
    def __init__(self, database_directory: str = "chroma_db_store") -> None:
        self.database_directory = database_directory
        self.collection_name = "fraud_policy_knowledge_base"
        
        # Initialize persistent connection safely
        os.makedirs(self.database_directory, exist_ok=True)
        self.chroma_client = chromadb.PersistentClient(path=self.database_directory)
        
        # Initialize or grab active targeted data tables group indices reference
        self.collection = self.chroma_client.get_or_create_collection(
            name=self.collection_name,
            metadata={"hnsw:space": "cosine"}
        )

    def upsert_policy_records(self, chunks: List[Dict[str, Any]], embeddings: List[List[float]]) -> None:
        """Saves documents structures data payloads into storage matrices tables cleanly."""
        if not chunks or not embeddings:
            return

        ids: List[str] = []
        documents: List[str] = []
        metadata_list: List[Dict[str, Any]] = []

        for idx, chunk in enumerate(chunks):
            record_id = f"chunk_{chunk['metadata']['policy_id']}_{idx}"
            ids.append(record_id)
            documents.append(chunk["text"])
            metadata_list.append(chunk["metadata"])

        # Insert records into DB storage block array layout parameters
        self.collection.upsert(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadata_list
        )
        logger.info(f"Created ChromaDB collection records matching {len(ids)} target entities components.")

    def query_nearest_neighbors(self, query_vector: List[float], top_k: int = 3) -> List[Dict[str, Any]]:
        """Queries localized tables matrix maps to fetch near matched vector assets instances."""
        query_results = self.collection.query(
            query_embeddings=[query_vector],
            n_results=top_k
        )
        
        normalized_results: List[Dict[str, Any]] = []
        if not query_results or not query_results.get("documents") or not query_results["documents"][0]:
            return normalized_results
            
        docs = query_results["documents"][0]
        metas = query_results["metadatas"][0]
        
        for index in range(len(docs)):
            normalized_results.append({
                "text": docs[index],
                "metadata": metas[index]
            })
            
        return normalized_results
