"""
Purpose: Defines custom UI presentation styles and banking operational aesthetic themes.
"""
import streamlit as st

def apply_custom_css(theme_mode: str = "Dark") -> None:
    """Injects institutional typography, brand color tokens, and status-badge color coding.
    Brand palette: midnight surfaces, electric cyan primary, violet accent, gold highlights,
    and critical red reserved for fraud/risk states only."""
    normalized_theme = (theme_mode or "Dark").strip().lower()
    is_light = normalized_theme == "light"

    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');

            :root {
                --color-primary: #22D3EE;
                --color-primary-dark: #06B6D4;
                --color-primary-light: rgba(34, 211, 238, 0.16);
                --color-primary-light-text: #CFFAFE;

                --color-secondary: #0F172A;
                --color-secondary-soft: #111827;
                --color-border: rgba(148, 163, 184, 0.22);

                --color-accent: #A855F7;
                --color-accent-dark: #7C3AED;
                --color-accent-light: rgba(168, 85, 247, 0.16);
                --color-accent-light-text: #F3E8FF;

                --color-critical: #FB7185;
                --color-critical-light: rgba(251, 113, 133, 0.16);

                --color-neutral-bg: rgba(30, 41, 59, 0.92);
                --color-neutral-text: #CBD5E1;

                --color-highlight: #FBBF24;
                --color-highlight-light: rgba(251, 191, 36, 0.18);
                --color-highlight-text: #FEF3C7;

                --color-panel: rgba(15, 23, 42, 0.94);
                --color-panel-soft: rgba(17, 24, 39, 0.98);
                --color-glow-primary: rgba(34, 211, 238, 0.26);
                --color-glow-accent: rgba(168, 85, 247, 0.22);

                --color-text-heading: #F8FAFC;
                --color-text-body: #E2E8F0;
                --color-text-muted: #94A3B8;

                --color-sidebar-bg: #0B1220;
                --color-sidebar-text: #F8FAFC;
                --color-sidebar-muted: rgba(248, 250, 252, 0.72);
                --color-sidebar-hr: rgba(148, 163, 184, 0.24);
                --color-sidebar-active-bg: rgba(34, 211, 238, 0.16);
            }

            /* Global Application Alignment and Typography */
            [data-testid="stHeader"] {
                height: 1.5rem !important;
                min-height: 1.5rem !important;
                background: linear-gradient(180deg, rgba(15,23,42,0.98), rgba(17,24,39,0.96)) !important;
                border-bottom: 1px solid rgba(34, 211, 238, 0.15);
                backdrop-filter: blur(14px);
            }
            [data-testid="stMainBlockContainer"] { padding-top: 1.5rem !important; padding-bottom: 2rem; }
            [data-testid="stAppViewContainer"] {
                background:
                    radial-gradient(circle at top right, rgba(168, 85, 247, 0.14), transparent 26%),
                    radial-gradient(circle at left 20%, rgba(34, 211, 238, 0.13), transparent 22%),
                    radial-gradient(circle at 85% 80%, rgba(251, 191, 36, 0.10), transparent 18%),
                    radial-gradient(circle at 50% 0%, rgba(34, 211, 238, 0.06), transparent 24%),
                    linear-gradient(180deg, #050816 0%, #0B1220 100%);
                background-size: 100% 100%, 100% 100%, 100% 100%, 100% 100%, 100% 100%;
                animation: ambientShift 18s ease-in-out infinite alternate;
            }
            h1, h2, h3 {
                color: var(--color-text-heading) !important;
                font-family: 'Space Grotesk', 'Manrope', -apple-system, sans-serif;
                text-shadow: 0 1px 0 rgba(0,0,0,0.25);
                letter-spacing: -0.03em;
            }
            body, p, .stMarkdown, [data-testid="stMarkdownContainer"] { color: var(--color-text-body); }
            a, a:visited { color: var(--color-primary); }
            a:hover { color: #67E8F9; }

            p, li, td, th, label, input, textarea, button {
                font-family: 'Manrope', -apple-system, sans-serif;
            }

            @keyframes ambientShift {
                0% { filter: saturate(1) brightness(1); }
                100% { filter: saturate(1.12) brightness(1.04); }
            }

            /* Sidebar - primary brand color anchors the whole app */
            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, #060A14 0%, #0F172A 100%) !important;
                border-right: 1px solid rgba(34, 211, 238, 0.18);
                box-shadow: 12px 0 40px rgba(0, 0, 0, 0.34);
                backdrop-filter: blur(18px);
            }
            [data-testid="stSidebar"] * { color: var(--color-sidebar-text); }
            [data-testid="stSidebar"] h1,
            [data-testid="stSidebar"] h2,
            [data-testid="stSidebar"] h3 { color: var(--color-sidebar-text) !important; }
            [data-testid="stSidebar"] [data-testid="stCaptionContainer"] p { color: var(--color-sidebar-muted) !important; }
            [data-testid="stSidebar"] hr { border-top: 1px solid var(--color-sidebar-hr); }
            /* Native radio: force ring/dot to sidebar-text regardless of the app-wide primaryColor,
            since the theme's primaryColor (green) would otherwise render invisible on this green bg */
            [data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {
                background-color: transparent !important;
                border: 1px solid rgba(148, 163, 184, 0.68) !important;
                border-radius: 50%;
            }
            [data-testid="stSidebar"] [role="radiogroup"] label > div:first-child > div {
                background-color: var(--color-sidebar-text) !important;
            }
            [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) > div:first-child {
                border-color: var(--color-primary) !important;
                background-color: var(--color-sidebar-active-bg) !important;
            }

            [data-testid="stSidebar"] [role="radiogroup"] label:hover > div:first-child {
                border-color: rgba(34, 211, 238, 0.72) !important;
                background-color: rgba(34, 211, 238, 0.10) !important;
            }

            /* Sidebar collapse control */
            [data-testid="stSidebarCollapseButton"] {
                color: var(--color-sidebar-text) !important;
                background: linear-gradient(180deg, rgba(34, 211, 238, 0.18), rgba(168, 85, 247, 0.14)) !important;
                border: 1px solid rgba(34, 211, 238, 0.30) !important;
                border-radius: 999px !important;
                box-shadow: 0 8px 22px rgba(0, 0, 0, 0.28);
            }
            [data-testid="stSidebarCollapseButton"] svg,
            [data-testid="stSidebarCollapseButton"] path {
                fill: currentColor !important;
                color: inherit !important;
            }
            [data-testid="stSidebarCollapseButton"]:hover {
                color: #FFFFFF !important;
                background: linear-gradient(180deg, rgba(34, 211, 238, 0.32), rgba(168, 85, 247, 0.24)) !important;
                border-color: rgba(103, 232, 249, 0.60) !important;
            }

            /* Native alert banners (st.info/warning/error/success) - replace Streamlit's default
            blue/yellow/red/green with brand-consistent tints */
            [data-testid="stAlertContainer"] { background-color: transparent !important; }
            [data-testid="stAlertContentInfo"] {
                background-color: rgba(8, 145, 178, 0.16) !important;
                color: #E0F2FE !important;
                border-left: 4px solid var(--color-primary);
                border-radius: 10px;
            }
            [data-testid="stAlertContentWarning"] {
                background-color: rgba(251, 191, 36, 0.16) !important;
                color: var(--color-highlight-text) !important;
                border-left: 4px solid var(--color-highlight);
                border-radius: 10px;
            }
            [data-testid="stAlertContentError"] {
                background-color: rgba(251, 113, 133, 0.16) !important;
                color: #FFE4E6 !important;
                border-left: 4px solid var(--color-critical);
                border-radius: 10px;
            }
            [data-testid="stAlertContentSuccess"] {
                background-color: rgba(34, 197, 94, 0.14) !important;
                color: #DCFCE7 !important;
                border-left: 4px solid #22C55E;
                border-radius: 10px;
            }
            [data-testid="stAlertContentInfo"] p,
            [data-testid="stAlertContentWarning"] p,
            [data-testid="stAlertContentError"] p,
            [data-testid="stAlertContentSuccess"] p { color: inherit !important; }
            [data-testid="stAlertContentInfo"] [data-testid="stIconMaterial"],
            [data-testid="stAlertContentWarning"] [data-testid="stIconMaterial"],
            [data-testid="stAlertContentError"] [data-testid="stIconMaterial"],
            [data-testid="stAlertContentSuccess"] [data-testid="stIconMaterial"] { color: inherit !important; }

            /* Buttons: primary = brand green (native theme), secondary = accent terracotta */
            [data-testid="stBaseButton-primary"] {
                background: linear-gradient(135deg, #22D3EE 0%, #A855F7 55%, #06B6D4 100%) !important;
                border-color: #06B6D4 !important;
                color: #042F2E !important;
                box-shadow: 0 14px 30px rgba(34, 211, 238, 0.28), 0 0 0 1px rgba(34, 211, 238, 0.10);
                text-shadow: 0 1px 0 rgba(255, 255, 255, 0.35);
                transition: transform 180ms ease, box-shadow 180ms ease, filter 180ms ease;
            }
            [data-testid="stBaseButton-primary"]:hover {
                background: linear-gradient(135deg, #67E8F9 0%, #C084FC 55%, #22D3EE 100%) !important;
                border-color: #22D3EE !important;
                transform: translateY(-1px);
                box-shadow: 0 18px 36px rgba(34, 211, 238, 0.34), 0 0 0 1px rgba(103, 232, 249, 0.14);
            }
            [data-testid="stBaseButton-secondary"] {
                color: #F8FAFC !important;
                border-color: rgba(168, 85, 247, 0.85) !important;
                background-color: rgba(168, 85, 247, 0.16) !important;
                box-shadow: 0 8px 20px rgba(168, 85, 247, 0.12);
                transition: transform 180ms ease, box-shadow 180ms ease, background-color 180ms ease;
            }
            [data-testid="stBaseButton-secondary"]:hover {
                color: #FFFFFF !important;
                border-color: var(--color-accent-dark) !important;
                background-color: var(--color-accent-dark) !important;
                transform: translateY(-1px);
                box-shadow: 0 14px 28px rgba(168, 85, 247, 0.22);
            }

            /* AI System Status panel: multiple check rows + a last-refreshed footer */
            .status-panel {
                border: 1px solid rgba(34, 211, 238, 0.18);
                border-radius: 12px;
                padding: 0.75rem 1rem;
                background: linear-gradient(180deg, rgba(15, 23, 42, 0.92) 0%, rgba(17, 24, 39, 0.96) 100%);
                margin-bottom: 1.25rem;
                box-shadow: 0 12px 28px rgba(0, 0, 0, 0.28), inset 0 1px 0 rgba(255,255,255,0.04);
            }
            .status-row { display: flex; align-items: center; gap: 0.55rem; font-size: 0.85rem; color: #E2E8F0; padding: 0.2rem 0; }
            .status-row.down { color: var(--color-critical); }
            .status-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
            .status-dot.ok { background-color: var(--color-primary); }
            .status-dot.down { background-color: var(--color-critical); }
            .status-panel-footer {
                font-size: 0.75rem; color: var(--color-text-muted); margin-top: 0.4rem;
                padding-top: 0.4rem; border-top: 1px solid rgba(148, 163, 184, 0.22);
            }

            /* Metric Cards (Analytics KPIs) */
            .metric-container {
                background: linear-gradient(180deg, rgba(15, 23, 42, 0.96) 0%, rgba(17, 24, 39, 0.98) 100%);
                border: 1px solid rgba(34, 211, 238, 0.18);
                border-top: 4px solid var(--color-primary);
                border-radius: 14px;
                padding: 1.25rem;
                text-align: center;
                box-shadow: 0 14px 32px rgba(0, 0, 0, 0.30), 0 0 0 1px rgba(34, 211, 238, 0.04);
            }
            .metric-value { font-size: 2.25rem; font-weight: 700; color: #F8FAFC; margin: 0.5rem 0; }
            .metric-label { font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--color-text-muted); }

            /* Status / Priority / Risk badges - the primary place accent/critical color is allowed */
            .badge {
                display: inline-block;
                padding: 0.15rem 0.6rem;
                border-radius: 999px;
                font-size: 0.78rem;
                font-weight: 600;
                letter-spacing: 0.02em;
                white-space: nowrap;
                border: 1px solid transparent;
                box-shadow: 0 6px 14px rgba(0, 0, 0, 0.12);
            }
            .badge-high       { background-color: rgba(251, 113, 133, 0.20) !important; color: #FFE4E6 !important; border-color: rgba(251, 113, 133, 0.26) !important; }
            .badge-medium     { background-color: rgba(251, 191, 36, 0.18) !important; color: #FEF3C7 !important; border-color: rgba(251, 191, 36, 0.24) !important; }
            .badge-low        { background-color: rgba(251, 191, 36, 0.18) !important; color: #FEF3C7 !important; border-color: rgba(251, 191, 36, 0.24) !important; }
            .badge-neutral    { background-color: var(--color-neutral-bg); color: var(--color-neutral-text); border-color: rgba(148, 163, 184, 0.16); }
            .badge-approved   { background-color: rgba(34, 197, 94, 0.18); color: #DCFCE7; border-color: rgba(34, 197, 94, 0.24); }
            .badge-declined   { background-color: rgba(251, 113, 133, 0.20); color: #FFE4E6; border-color: rgba(251, 113, 133, 0.26); }
            .badge-escalated  { background-color: rgba(251, 113, 133, 0.20); color: #FFE4E6; border-color: rgba(251, 113, 133, 0.26); }
            .badge-review     { background-color: rgba(168, 85, 247, 0.18); color: #F5D0FE; border-color: rgba(168, 85, 247, 0.26); }
            .badge-returned   { background-color: rgba(251, 191, 36, 0.18); color: #FEF3C7; border-color: rgba(251, 191, 36, 0.24); }
            .badge-closed     { background-color: rgba(15, 23, 42, 0.96); color: #E2E8F0; border-color: rgba(148, 163, 184, 0.18); }

            /* Case Queue rows */
            .queue-row {
                border-bottom: 1px solid rgba(148, 163, 184, 0.18);
                padding: 0.65rem 0.25rem;
            }
            .queue-header {
                font-size: 0.75rem;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                color: var(--color-text-muted);
                border-bottom: 1px solid rgba(148, 163, 184, 0.18);
                padding-bottom: 0.4rem;
            }

            /* Analyst identity block, top-right of every page */
            .identity-header { text-align: right; margin-bottom: 0.5rem; }
            .identity-name { font-weight: 600; color: var(--color-text-heading); font-size: 0.95rem; }
            .identity-meta { font-size: 0.82rem; color: var(--color-text-muted); margin-top: 0.1rem; }

            /* Case lifecycle flow stepper (Investigation view) */
            .flow-stepper { display: flex; align-items: flex-start; margin: 0.25rem 0 1.75rem 0; }
            .flow-step { display: flex; flex-direction: column; align-items: center; gap: 0.5rem; flex-shrink: 0; }
            .flow-dot {
                width: 16px; height: 16px; border-radius: 50%;
                border: 2px solid rgba(148, 163, 184, 0.28); background-color: var(--color-secondary-soft); box-sizing: border-box;
            }
            .flow-step.done .flow-dot { background-color: var(--color-primary); border-color: var(--color-primary); }
            .flow-step.current .flow-dot { background-color: var(--color-secondary-soft); border-color: var(--color-accent); box-shadow: 0 0 0 3px rgba(168,85,247,0.22); }
            .flow-label { font-size: 0.78rem; color: var(--color-text-muted); white-space: nowrap; }
            .flow-step.done .flow-label { color: var(--color-primary-dark); font-weight: 500; }
            .flow-step.current .flow-label { color: var(--color-accent); font-weight: 700; }
            .flow-connector { flex: 1 1 auto; height: 2px; background-color: rgba(148, 163, 184, 0.24); margin: 7px 0.5rem 0 0.5rem; min-width: 24px; }
            .flow-connector.done { background-color: var(--color-primary); }

            /* Case header bar (Investigation view) */
            .case-header {
                border-bottom: 1px solid rgba(148, 163, 184, 0.18);
                padding-bottom: 0.75rem;
                margin-bottom: 0.75rem;
            }
            .case-header-id { font-size: 1.4rem; font-weight: 700; color: var(--color-text-heading); }
            .case-header-meta { font-size: 0.85rem; color: var(--color-text-muted); margin-top: 0.15rem; }

            /* AI Assessment strip - compact verdict row, not a marketing banner */
            .assessment-strip {
                border-left: 4px solid var(--color-primary);
                background: linear-gradient(180deg, rgba(15, 23, 42, 0.96) 0%, rgba(17, 24, 39, 0.98) 100%);
                border-radius: 12px;
                padding: 0.9rem 1.1rem;
                margin-bottom: 1rem;
                box-shadow: 0 10px 24px rgba(0, 0, 0, 0.28), 0 0 0 1px rgba(34, 211, 238, 0.05);
            }
            .assessment-strip.tier-high   { border-left-color: var(--color-critical); }
            .assessment-strip.tier-medium { border-left-color: var(--color-highlight); }
            .assessment-strip.tier-low    { border-left-color: #22C55E; }
            .assessment-label { font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--color-text-muted); }
            .assessment-value { font-size: 1.05rem; font-weight: 600; color: var(--color-text-heading); margin-top: 0.1rem; }
            .assessment-summary { font-size: 0.92rem; color: var(--color-text-body); margin-top: 0.6rem; line-height: 1.5; }

            /* Fraud indicator tags */
            .tag-pill {
                display: inline-block;
                background-color: rgba(15, 23, 42, 0.98);
                border: 1px solid rgba(34, 211, 238, 0.18);
                color: #E2E8F0;
                border-radius: 999px;
                padding: 0.2rem 0.55rem;
                margin: 0 0.35rem 0.35rem 0;
                font-size: 0.82rem;
                box-shadow: 0 6px 14px rgba(0, 0, 0, 0.12);
            }

            /* Policy citation trail */
            .policy-citation {
                font-size: 0.85rem;
                color: var(--color-text-muted);
                border-left: 2px solid rgba(34, 211, 238, 0.28);
                padding-left: 0.6rem;
                margin-bottom: 0.35rem;
            }

            /* Analyst decision record (locked disposition) */
            .decision-record {
                border: 1px solid rgba(34, 211, 238, 0.18);
                border-radius: 12px;
                padding: 0.9rem 1.1rem;
                background: linear-gradient(180deg, rgba(15, 23, 42, 0.96) 0%, rgba(17, 24, 39, 0.98) 100%);
                box-shadow: 0 12px 28px rgba(0, 0, 0, 0.30), 0 0 0 1px rgba(168, 85, 247, 0.05);
            }
            .decision-record-note { font-size: 0.88rem; color: var(--color-text-body); margin-top: 0.4rem; line-height: 1.5; }
            .decision-record-meta { font-size: 0.78rem; color: var(--color-text-muted); margin-top: 0.5rem; }

            /* Targeted Streamlit generated class override */
            .st-c2.st-bo.st-c3.st-c4.st-br.st-bs.st-c5.st-bt.st-c6 {
                background-color: #E5E7EB !important;
                border-color: #D1D5DB !important;
                color: #374151 !important;
            }

            /* Stable selector for Streamlit/BaseWeb select controls */
            div[data-baseweb="select"] {
                background-color: #E5E7EB !important;
                border-color: #D1D5DB !important;
                border-radius: 10px !important;
            }
            div[data-baseweb="select"] > div {
                background-color: #E5E7EB !important;
                border-color: #D1D5DB !important;
            }
            div[data-baseweb="select"] input,
            div[data-baseweb="select"] [role="combobox"],
            div[data-baseweb="select"] [aria-label*="Case"] {
                color: #374151 !important;
                background-color: transparent !important;
            }
            div[data-baseweb="select"] svg,
            div[data-baseweb="select"] path {
                color: #6B7280 !important;
                fill: currentColor !important;
            }

            /* Dropdown menu for BaseWeb select */
            div[role="listbox"],
            ul[role="listbox"],
            [data-baseweb="popover"] [role="listbox"] {
                background-color: #F3F4F6 !important;
                border: 1px solid #D1D5DB !important;
            }
            div[role="option"],
            li[role="option"],
            [data-baseweb="popover"] [role="option"] {
                background-color: #F3F4F6 !important;
                color: #374151 !important;
            }
            div[role="option"]:hover,
            li[role="option"]:hover,
            [data-baseweb="popover"] [role="option"]:hover,
            div[role="option"][aria-selected="true"],
            li[role="option"][aria-selected="true"],
            [data-baseweb="popover"] [role="option"][aria-selected="true"] {
                background-color: #E5E7EB !important;
                color: #111827 !important;
            }
        </style>
    """, unsafe_allow_html=True)

    if is_light:
        st.markdown("""
            <style>
                :root {
                    --color-primary: #1D4ED8;
                    --color-primary-dark: #1E40AF;
                    --color-primary-light: rgba(29, 78, 216, 0.14);
                    --color-primary-light-text: #1E3A8A;

                    --color-secondary: #F1F5F9;
                    --color-secondary-soft: #FFFFFF;
                    --color-border: rgba(100, 116, 139, 0.26);

                    --color-accent: #6D28D9;
                    --color-accent-dark: #5B21B6;
                    --color-accent-light: rgba(109, 40, 217, 0.14);
                    --color-accent-light-text: #4C1D95;

                    --color-critical: #BE123C;
                    --color-critical-light: rgba(190, 18, 60, 0.14);

                    --color-neutral-bg: rgba(226, 232, 240, 0.98);
                    --color-neutral-text: #334155;

                    --color-highlight: #D97706;
                    --color-highlight-light: rgba(217, 119, 6, 0.16);
                    --color-highlight-text: #7C2D12;

                    --color-panel: rgba(255, 255, 255, 0.96);
                    --color-panel-soft: rgba(248, 250, 252, 1);
                    --color-glow-primary: rgba(29, 78, 216, 0.20);
                    --color-glow-accent: rgba(109, 40, 217, 0.18);

                    --color-text-heading: #0F172A;
                    --color-text-body: #111827;
                    --color-text-muted: #475569;

                    --color-sidebar-bg: #FFFFFF;
                    --color-sidebar-text: #0F172A;
                    --color-sidebar-muted: rgba(15, 23, 42, 0.72);
                    --color-sidebar-hr: rgba(100, 116, 139, 0.30);
                    --color-sidebar-active-bg: rgba(29, 78, 216, 0.12);
                }

                [data-testid="stHeader"] {
                    background: linear-gradient(180deg, rgba(255,255,255,0.99), rgba(241,245,249,0.98)) !important;
                    border-bottom: 1px solid rgba(100, 116, 139, 0.18);
                }
                [data-testid="stAppViewContainer"] {
                    background:
                        radial-gradient(circle at top right, rgba(29, 78, 216, 0.10), transparent 28%),
                        radial-gradient(circle at left 20%, rgba(109, 40, 217, 0.08), transparent 22%),
                        radial-gradient(circle at 85% 80%, rgba(217, 119, 6, 0.08), transparent 18%),
                        linear-gradient(180deg, #F8FAFC 0%, #E2E8F0 100%);
                    animation: none;
                }
                [data-testid="stSidebar"] {
                    background: linear-gradient(180deg, #FFFFFF 0%, #F1F5F9 100%) !important;
                    border-right: 1px solid rgba(100, 116, 139, 0.20);
                    box-shadow: 12px 0 30px rgba(15, 23, 42, 0.08);
                    backdrop-filter: blur(12px);
                }
                [data-testid="stSidebar"] * { color: var(--color-sidebar-text); }
                [data-testid="stSidebar"] [data-testid="stCaptionContainer"] p { color: var(--color-sidebar-muted) !important; }
                [data-testid="stSidebar"] hr { border-top: 1px solid var(--color-sidebar-hr); }
                [data-testid="stSidebar"] [role="radiogroup"] label > div:first-child {
                    border-color: rgba(100, 116, 139, 0.60) !important;
                }
                [data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) > div:first-child {
                    border-color: var(--color-primary) !important;
                    background-color: var(--color-sidebar-active-bg) !important;
                }
                [data-testid="stSidebar"] [role="radiogroup"] label:hover > div:first-child {
                    border-color: rgba(29, 78, 216, 0.78) !important;
                    background-color: rgba(29, 78, 216, 0.10) !important;
                }
                [data-testid="stSidebarCollapseButton"] {
                    color: var(--color-sidebar-text) !important;
                    background: linear-gradient(180deg, rgba(29, 78, 216, 0.14), rgba(109, 40, 217, 0.12)) !important;
                    border: 1px solid rgba(29, 78, 216, 0.24) !important;
                }
                [data-testid="stBaseButton-primary"] {
                    color: #FFFFFF !important;
                    background: linear-gradient(135deg, #1D4ED8 0%, #6D28D9 100%) !important;
                    border-color: #1D4ED8 !important;
                    box-shadow: 0 14px 30px rgba(29, 78, 216, 0.24);
                }
                [data-testid="stBaseButton-primary"]:hover {
                    background: linear-gradient(135deg, #1E40AF 0%, #5B21B6 100%) !important;
                    border-color: #1E40AF !important;
                }
                .st-key-run_investigation_action [data-testid="stBaseButton-primary"],
                .st-key-run_investigation_action [data-testid="stBaseButton-primary"] p {
                    color: #D1D5DB !important;
                }
                [data-testid="stBaseButton-secondary"] {
                    color: #4C1D95 !important;
                    border-color: rgba(109, 40, 217, 0.36) !important;
                    background-color: rgba(109, 40, 217, 0.10) !important;
                }
                [data-testid="stBaseButton-secondary"]:hover {
                    color: #FFFFFF !important;
                    background-color: #6D28D9 !important;
                }
                [data-testid="stAlertContentInfo"] {
                    background-color: rgba(29, 78, 216, 0.10) !important;
                    color: #1E3A8A !important;
                    border-left: 4px solid var(--color-primary) !important;
                }
                [data-testid="stAlertContentWarning"] {
                    background-color: rgba(217, 119, 6, 0.12) !important;
                    color: #7C2D12 !important;
                    border-left: 4px solid var(--color-highlight) !important;
                }
                [data-testid="stAlertContentError"] {
                    background-color: rgba(190, 18, 60, 0.10) !important;
                    color: #9F1239 !important;
                    border-left: 4px solid var(--color-critical) !important;
                }
                [data-testid="stAlertContentSuccess"] {
                    background-color: rgba(34, 197, 94, 0.12) !important;
                    color: #14532D !important;
                    border-left: 4px solid #22C55E !important;
                }
                body, p, .stMarkdown, [data-testid="stMarkdownContainer"] {
                    color: #111827 !important;
                }
                .status-panel, .metric-container, .assessment-strip, .decision-record {
                    background: linear-gradient(180deg, #FFFFFF 0%, #EEF2F7 100%) !important;
                    box-shadow: 0 12px 28px rgba(15, 23, 42, 0.10) !important;
                }
                .status-row, .metric-value, .assessment-value, .decision-record-note, .tag-pill {
                    color: #0F172A;
                }
                .badge-high, .badge-declined, .badge-escalated {
                    background-color: rgba(190, 18, 60, 0.12) !important;
                    color: #9F1239 !important;
                }
                .badge-medium {
                    background-color: rgba(251, 191, 36, 0.16) !important;
                    color: #92400E !important;
                }
                .badge-review, .badge-returned {
                    background-color: rgba(109, 40, 217, 0.12) !important;
                    color: #5B21B6 !important;
                }
                .badge-low {
                    background-color: rgba(251, 191, 36, 0.16) !important;
                    color: #92400E !important;
                }
                .badge-approved {
                    background-color: rgba(34, 197, 94, 0.14) !important;
                    color: #166534 !important;
                }
                .badge-neutral, .badge-closed {
                    background-color: rgba(226, 232, 240, 0.98);
                    color: #1E293B;
                }
                .tag-pill {
                    background-color: #FFFFFF;
                    border-color: rgba(100, 116, 139, 0.28);
                }
                .flow-step.current .flow-dot {
                    box-shadow: 0 0 0 3px rgba(109, 40, 217, 0.16);
                }
            </style>
        """, unsafe_allow_html=True)
