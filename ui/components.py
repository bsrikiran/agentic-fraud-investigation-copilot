"""
Purpose: Structuring metrics loaders, rendering widgets, and abstracting data parsing frameworks.
"""
import json
import logging
import pandas as pd
import streamlit as st
from typing import List, Dict, Any, Optional

logger = logging.getLogger("ui.components")

ANALYST_NAME = "Sr Fraud Investigator"
ANALYST_LOCATION = "Wilmington, DE"

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

def badge_html(label: str, variant: str) -> str:
    """Returns a colored status/priority pill span. Variant must match a .badge-<variant> CSS class
    (high, medium, low, neutral, approved, declined, escalated, review)."""
    return f'<span class="badge badge-{variant}">{label}</span>'

def tier_variant(tier: Optional[str]) -> str:
    """Maps a free-text risk/priority label to its badge color variant."""
    return {"high": "high", "medium": "medium", "low": "low"}.get((tier or "").strip().lower(), "neutral")

def case_status_variant(status_label: str) -> str:
    """Maps a case's derived status label to its badge color variant."""
    return {
        "approved": "approved",
        "declined": "declined",
        "escalated": "escalated",
        "under review": "review",
    }.get(status_label.strip().lower(), "neutral")

def resolve_case_id(c: Dict[str, Any], idx: int) -> str:
    """Resolves a stable ID for a case record, regardless of nested vs. flat structure.
    Used everywhere a case is identified (queue rows, selectors, lookups) so different views
    can never disagree on what a given case's ID is."""
    tid = c.get("transaction_id")
    if not tid and isinstance(c.get("transaction"), dict):
        tid = c["transaction"].get("transaction_id")
    if not tid:
        tid = c.get("case_id") or c.get("id") or f"CASE-TICKET-{idx+1:03d}"
    return str(tid)

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

        case_id = resolve_case_id(c, idx)
        customer = txn.get("customer_name") or txn.get("customer", "N/A")
        amount = float(txn.get("amount") or 0.0)
        merchant = txn.get("merchant", "N/A")
        location = txn.get("location") or txn.get("transaction_location", "N/A")

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
            "past_fraud": past_fraud,
            "priority": c.get("priority", "N/A"),
            "case_status": c.get("case_status", "New"),
            "created_date": c.get("created_date", "N/A"),
        })

    return pd.DataFrame(flattened_rows)

