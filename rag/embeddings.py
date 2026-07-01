"""
Purpose: Connecting to the OpenAI Embeddings API to vectorize policy text windows.
"""
import logging
from typing import List
from openai import OpenAI
from backend.config import OPENAI_API_KEY

logger = logging.getLogger("rag.embeddings")

class PolicyEmbeddingEngine:
    """Manages secure communication pipelines to download metric arrays from the OpenAI Embeddings framework."""
    
    def __init__(self, embedding_model: str = "text-embedding-3-small") -> None:
        self.embedding_model = embedding_model
        # Use existing verified token reference directly
        self.client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

    def generate_single_embedding(self, text_snippet: str) -> List[float]:
        """Translates a single block string value into standard vector coordinates."""
        if not self.client:
            raise RuntimeError("OpenAI client missing configuration settings inside environment parameters.")
            
        response = self.client.embeddings.create(
            input=text_snippet,
            model=self.embedding_model
        )
        return response.data[0].embedding

    def generate_batch_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Executes high-speed batched vectors retrieval requests from the remote platform cluster."""
        if not self.client or not texts:
            return []
            
        logger.info(f"Generating embeddings for {len(texts)} vector chunks...")
        response = self.client.embeddings.create(
            input=texts,
            model=self.embedding_model
        )
        return [item.embedding for item in response.data]
