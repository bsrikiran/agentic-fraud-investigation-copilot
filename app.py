# --- STREAMLIT CLOUD CHROMADB COMPATIBILITY PATCH ---
import sys
try:
    __import__('pysqlite3')
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    pass
# ----------------------------------------------------

# Purpose: Main application entry point for the Agentic Fraud Investigation Copilot UI.
# Orchestrates sidebar routing, layout templates configuration, and global logs.
from datetime import datetime
import logging
import streamlit as st
from ui.styles import apply_custom_css
from ui.pages import render_case_queue_view, render_investigation_view, render_analytics_view
from ui.components import ANALYST_NAME, ANALYST_LOCATION

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("ui.main_app")

def main() -> None:
    """Configures main workspace layout wrappers, tracking sidebars navigation matrices options."""
    st.set_page_config(
        page_title="Agentic Fraud Investigation Copilot",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    apply_custom_css()

    # A widget's session_state value can't be mutated after it's instantiated in the same run,
    # so cross-view navigation (e.g. the queue's "Open" button) stages the target here and this
    # runs before the radio widget below is created.
    if "_pending_nav" in st.session_state:
        st.session_state["nav_radio"] = st.session_state.pop("_pending_nav")

    st.sidebar.markdown("### Agentic Fraud Investigation Copilot")
    st.sidebar.write("---")

    navigation_route = st.sidebar.radio(
        "Navigate",
        ["Home", "Investigation", "Analytics"],
        key="nav_radio"
    )

    st.sidebar.write("---")
    st.sidebar.caption("Compliance Protection Enforced")

    _, identity_col = st.columns([4, 1])
    with identity_col:
        st.markdown(f"""
            <div class="identity-header">
                <div class="identity-name">{ANALYST_NAME}</div>
                <div class="identity-meta">{ANALYST_LOCATION} · {datetime.now().strftime('%B %d, %Y')}</div>
            </div>
        """, unsafe_allow_html=True)

    if navigation_route == "Home":
        logger.info("Rendering case queue view.")
        render_case_queue_view()
    elif navigation_route == "Investigation":
        logger.info("Rendering investigation workspace view.")
        render_investigation_view()
    elif navigation_route == "Analytics":
        logger.info("Rendering analytics view.")
        render_analytics_view()

if __name__ == "__main__":
    main()
