"""
Purpose: Reading the 10 PDF documents from policies/ and parsing text into structural text chunks.
"""
import os
import logging
from typing import List, Dict, Any
from pypdf import PdfReader
from rag.utils import clean_text_whitespace, extract_policy_identifiers

logger = logging.getLogger("rag.loader")

class PolicyDocumentLoader:
    """Handles text extraction and programmatic chunk generation for internal compliance documents."""
    
    def __init__(self, target_directory: str = "policies", chunk_size: int = 700, chunk_overlap: int = 100) -> None:
        self.target_directory = target_directory
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def read_and_chunk_policies(self) -> List[Dict[str, Any]]:
        """
        Scans target directories, extracts PDF content, and builds contextual overlapping windows.
        
        Returns:
            List[Dict[str, Any]]: Formal array containing chunk parameters and source tracking layouts.
        """
        processed_chunks: List[Dict[str, Any]] = []
        
        if not os.path.exists(self.target_directory):
            logger.warning(f"Target library path folder location not found: '{self.target_directory}'")
            return processed_chunks

        files = [f for f in os.listdir(self.target_directory) if f.endswith(".pdf")]
        logger.info(f"Loading policy documents: Found {len(files)} target files.")

        for file_name in files:
            file_path = os.path.join(self.target_directory, file_name)
            policy_name, policy_id = extract_policy_identifiers(file_name)
            
            try:
                reader = PdfReader(file_path)
                full_text_buffer = []
                
                for page_num, page in enumerate(reader.pages):
                    page_text = page.extract_text() or ""
                    full_text_buffer.append(page_text)
                
                combined_text = clean_text_whitespace(" ".join(full_text_buffer))
                
                # Sliding execution window split processing logic
                start_index = 0
                chunk_sequence_id = 0
                
                while start_index < len(combined_text):
                    end_index = start_index + self.chunk_size
                    chunk_text = combined_text[start_index:end_index]
                    
                    # Dynamically append headers to track lines safely
                    chunk_data = {
                        "text": chunk_text,
                        "metadata": {
                            "policy_name": policy_name,
                            "policy_id": policy_id,
                            "section": f"Segment Section {chunk_sequence_id + 1}",
                            "source_file": file_name
                        }
                    }
                    processed_chunks.append(chunk_data)
                    
                    # Slide window forward by offset size factor
                    start_index += (self.chunk_size - self.chunk_overlap)
                    chunk_sequence_id += 1
                    
            except Exception as read_fault:
                logger.error(f"Failed to process target content mapping elements for file {file_name}: {str(read_fault)}")
                
        logger.info(f"Indexed {len(files)} PDF documents into {len(processed_chunks)} clean metadata-tracked blocks.")
        return processed_chunks
