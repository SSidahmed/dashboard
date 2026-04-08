import streamlit as st
import ocp_e2e

st.set_page_config(layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>

/* ===== COLOR SYSTEM ===== */
:root {
    --ocp-dark: #004b2d;
    --ocp-dark-2: #0a6a41;
    --ocp-light: #f7f7f5;
    --ocp-border: #d9e6da;
    --ocp-text: #0f3b2e;
    --ocp-muted: #6b7c72;
}

/* ===== GLOBAL ===== */
.stApp {
    background-color: var(--ocp-light);
    color: var(--ocp-text);
}

/* Force light theme text everywhere */
body {
    color: var(--ocp-text) !important;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #004b2d 0%, #003a23 100%);
}

/* Only sidebar text is white */
section[data-testid="stSidebar"] {
    color: white !important;
}

/* ===== KPI / CARDS ===== */
.card {
    background: white;
    padding: 16px;
    border-radius: 14px;
    border: 1px solid var(--ocp-border);
    color: var(--ocp-text) !important;
}

/* Force ALL text inside cards to be visible */
.card * {
    color: var(--ocp-text) !important;
}

/* KPI titles */
.kpi-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--ocp-text) !important;
}

/* KPI values */
.kpi-value {
    font-size: 26px;
    font-weight: 800;
    color: var(--ocp-dark) !important;
}

/* ===== TABLES ===== */
[data-testid="stDataFrame"] {
    background-color: white !important;
    color: var(--ocp-text) !important;
}

/* ===== SELECT BOXES ===== */
div[data-baseweb="select"] > div {
    background-color: white !important;
    border-radius: 10px !important;
    border: 1px solid var(--ocp-border) !important;
    color: var(--ocp-text) !important;
}

/* ===== GENERAL TEXT ===== */
.small-muted {
    color: var(--ocp-muted) !important;
    font-size: 0.9rem;
}

/* ===== DIVIDERS ===== */
hr {
    border-color: #dde6dc;
}

</style>
""", unsafe_allow_html=True)
# ---------- SIDEBAR ----------
st.sidebar.markdown("## OCP")

if "page" not in st.session_state:
    st.session_state.page = "OCP E2E"

page = st.sidebar.radio(
    "Main Menu",
    ["OCP E2E", "Loading", "Global Supply", "Freight & Costs"]
)

# ---------- ROUTING ----------
if page == "OCP E2E":
    ocp_e2e.render()

else:
    st.title(page)
