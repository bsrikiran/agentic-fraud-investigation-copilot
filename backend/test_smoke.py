"""
Purpose: End-to-end integrated smoke test fusing the RAG module and Backend engine.
"""
import logging
from backend.investigator import run_investigation
from rag.retriever import retrieve_policy_context

if __name__ == "__main__":
    # Configure logs to capture the integrated workflow steps cleanly
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    print("\n=== STARTING END-TO-END INTEGRATED INVESTIGATION TEST ===")
    
    # 1. High-risk mock transaction data payload matching contract definitions
    mock_txn = {
        "transaction_id": "TXN-10001", 
        "customer_id": "CUST-1001", 
        "customer_name": "John Smith",
        "account_age_years": 8, 
        "merchant": "Apple Store", 
        "merchant_category": "Electronics",
        "amount": 3250.00, 
        "currency": "USD", 
        "transaction_time": "2026-06-30T02:14:00",
        "location": "Miami, FL", 
        "home_location": "Arlington, VA", 
        "device": "New iPhone 16",
        "known_device": False, 
        "travel_notice": False
    }
    
    # 2. Historical profile parameters tracking standard baseline user performance
    mock_history = {
        "average_transaction": 95.00, 
        "highest_transaction": 820.00,
        "transactions_last_30_days": 43, 
        "previous_fraud_cases": 0,
        "preferred_locations": ["Virginia", "Maryland"]
    }
    
    # 3. STEP 1: Invoke RAG Semantic Search over our 10 ingested PDF policies
    # We formulate a real investigation search intent statement query
    search_query = "Unknown device high-value transaction above 2000 dollars"
    print(f"\n[RAG] Searching knowledge base for context matching: '{search_query}'...")
    
    real_policy_context = retrieve_policy_context(query=search_query, top_k=2)
    print("\n--- RETRIEVED RAG CONTEXT BLOCK START ---")
    print(real_policy_context if real_policy_context else "[Empty Context - Proceeding on base rules]")
    print("--- RETRIEVED RAG CONTEXT BLOCK END ---\n")

    # 4. STEP 2: Feed the live retrieved context directly into the Backend Agent
    print("[BACKEND] Forwarding transaction analytics and real policy metrics downstream...")
    output_result = run_investigation(
        transaction=mock_txn, 
        customer_history=mock_history, 
        policy_context=real_policy_context
    )
    
    print("\n=== FINAL COPILOT AGENT PAYLOAD JSON OUTPUT ===")
    import json
    print(json.dumps(output_result, indent=2))
