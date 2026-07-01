"""
Purpose: Sharing formatting helpers and tracking structured chunk configurations.
"""
import re

def clean_text_whitespace(text: str) -> str:
    """Removes irregular newlines, excessive spacing, and page-break artifacts."""
    if not text:
        return ""
    # Replace multiple spaces/newlines with a single space
    cleaned = re.sub(re.compile(r'\s+'), ' ', text)
    return cleaned.strip()

def extract_policy_identifiers(filename: str) -> tuple[str, str]:
    """
    Parses structural file string names to extract document titles and codes.
    Example: 'Fraud Investigation Policy (FP-214).pdf' -> ('Fraud Investigation Policy', 'FP-214')
    """
    clean_name = filename.replace(".pdf", "")
    match = re.search(re.compile(r'\((.*?)\)'), clean_name)
    
    if match:
        policy_id = match.group(1)
        policy_name = clean_name.split("(")[0].strip()
        return policy_name, policy_id
        
    return clean_name, "GEN-POLICY"
