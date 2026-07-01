"""
Purpose: Structuring metrics loaders, rendering widgets, and abstracting data parsing frameworks.
"""
import json
import logging
import pandas as pd
import streamlit as st
from typing import List, Dict, Any, Optional

logger = logging.getLogger("ui.components")

@st.cache_data
def load_investigation_cases() -> List[Dict[str, Any]]:
    """Loads operational anomalies portfolio logs directly from project data caches."""
    target_path = "sample_data/fraud_investigation_cases.json"
    try:
        with open(target_path, "r", encoding="utf-8") as file_buffer:
            cases_data = json.load(file_buffer)
            logger.info(f"Loaded {len(cases_data)} investigation cases successfully.")
            return cases_data if isinstance(cases_data, list) else []
    except Exception as read_fault:
        logger.error(f"Unable to load investigation cases from context path structure: {str(read_fault)}")
        st.error("Data Infrastructure Error: Failed to ingest active data registers portfolio logs.")
        return []

def render_metric_card(label: str, value: Any, delta_status: Optional[str] = None) -> None:
    """Renders a clean operational dashboard metric block layout."""
    st.markdown(f"""
        <div class="metric-container">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{value}</div>
            {"<div style='color:#059669; font-size:0.85rem; font-weight:500;'>" + delta_status + "</div>" if delta_status else ""}
        </div>
    """, unsafe_allow_html=True)

# Change the arrow at the end to -> pd.DataFrame
def parse_cases_dataframe(cases: List[Dict[str, Any]]) -> pd.DataFrame:
    """Transforms raw record collections directly into standard tracking dataframes adaptively."""
    flattened_rows = []
    for idx, c in enumerate(cases):
        # 1. Adaptively isolate the transaction dataset block (handles nested or flat root)
        if "transaction" in c and isinstance(c["transaction"], dict):
            txn = c["transaction"]
            hist = c.get("customer_history", {})
        else:
            txn = c
            hist = c.get("customer_history") or c

        # 2. Extract value variables with bulletproof structural fallbacks
        case_id = str(
            txn.get("transaction_id") or 
            c.get("transaction_id") or 
            c.get("case_id") or 
            c.get("id") or 
            f"CASE-{idx+1:03d}"
        )
        customer = txn.get("customer_name") or txn.get("customer", "N/A")
        amount = float(txn.get("amount") or 0.0)
        merchant = txn.get("merchant", "N/A")
        location = txn.get("location", "N/A")
        
        # 3. Extract customer history baselines metrics safely
        avg_spending = float(hist.get("average_transaction") or 0.0)
        past_fraud = int(hist.get("previous_fraud_cases") or 0)
        
        flattened_rows.append({
            "case_id": case_id,
            "customer": customer,
            "amount": amount,
            "merchant": merchant,
            "location": location,
            "avg_spending": avg_spending,
            "past_fraud": past_fraud
        })
        
    return pd.DataFrame(flattened_rows)

