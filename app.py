import streamlit as st
import ocp_e2e

st.set_page_config(layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
:root {
    --ocp-dark: #004b2d;
    --ocp-light: #f7f7f5;
    --ocp-border: #d9e6da;
}

.stApp {
    background-color: var(--ocp-light);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: var(--ocp-dark);
}
section[data-testid="stSidebar"] {
    color: white !important;
}


.card {
    background: white;
    color: #0f3b2e !important;
}

.card * {
    color: #0f3b2e !important;
}


/* KPI */
.card {
    background: white;
    padding: 16px;
    border-radius: 14px;
    border: 1px solid var(--ocp-border);
}

.kpi-title {
    font-size: 13px;
    font-weight: 700;
}

.kpi-value {
    font-size: 26px;
    font-weight: 800;
    color: #004b2d;
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
