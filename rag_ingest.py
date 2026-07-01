"""
Purpose: One-click extraction workflow script to parse PDF files and fully populate ChromaDB.
Save as: root directory 'rag_ingest.py'
"""
import logging
from rag.loader import PolicyDocumentLoader
from rag.embeddings import PolicyEmbeddingEngine
from rag.vector_store import PolicyVectorStore

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    print("=== INITIATING FRAUD CO-PILOT POLICY DATA INDEXING INGESTION ===")
    
    # 1. Scan and clean text windows from policies documents folder
    loader = PolicyDocumentLoader()
    chunks = loader.read_and_chunk_policies()
    
    if not chunks:
        print("[-] Verification failed: No policy PDF documents found inside 'policies/' folder.")
        exit(1)
        
    # 2. Vectorize all items in a single step
    texts_only = [item["text"] for item in chunks]
    engine = PolicyEmbeddingEngine()
    vectors = engine.generate_batch_embeddings(texts_only)
    
    # 3. Store the items inside ChromaDB
    store = PolicyVectorStore()
    store.upsert_policy_records(chunks, vectors)
    
    print("\n=== SUCCESS: DATABASE POPULATED AND READY TO WORK ===")
