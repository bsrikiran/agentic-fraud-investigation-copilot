"""
Purpose: Orchestrating the semantic similarity search and exposing the primary public interface.
"""
import logging
from rag.embeddings import PolicyEmbeddingEngine
from rag.vector_store import PolicyVectorStore

logger = logging.getLogger("rag.retriever")

def retrieve_policy_context(query: str, top_k: int = 3) -> str:
    """
    Exposes the primary entry functional wrapper endpoint to resolve contextual compliance matching.
    
    Args:
        query (str): Natural language operational string tracking investigator search context.
        top_k (int): Threshold tracking maximum density count configurations.
        
    Returns:
        str: Multi-line consolidated text containing metadata headers and policy contents.
    ```"""
    logger.info("Retrieving policy context")
    
    if not query or not query.strip():
        return ""
        
    try:
        # 1. Transform request content parameters into coordinate space
        vector_agent = PolicyEmbeddingEngine()
        query_vector = vector_agent.generate_single_embedding(query.strip())
        
        # 2. Extract relative documents context arrays matches from db tables pools
        storage_engine = PolicyVectorStore()
        matched_records = storage_engine.query_nearest_neighbors(query_vector, top_k=top_k)
        
        logger.info(f"Retrieved {len(matched_records)} matching policy sections")
        if not matched_records:
            return ""
            
        # 3. Compile output string data containing structural metadata headers
        string_builder = []
        for record in matched_records:
            meta = record["metadata"]
            header = f"{meta['policy_name']} ({meta['policy_id']})\n{meta['section']}"
            body_content = record["text"].strip()
            string_builder.append(f"{header}\n\n{body_content}\n")
            
        return "\n".join(string_builder).strip()
        
    except Exception as general_retrieval_fault:
        logger.warning(f"Retrieval interface swallowed internal workflow exception tracking error: {str(general_retrieval_fault)}")
        # Safeguard fallback to prevent downstream operational backend crashes
        return ""
