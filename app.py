import streamlit as st
import ocp_e2e

st.set_page_config(layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>

/* ===== GLOBAL ===== */
.stApp {
    background-color: #f7f7f5;
    color: #0f3b2e;
}

/* ===== SIDEBAR ===== */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #004b2d 0%, #003a23 100%);
}
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* ===== KPI ===== */
.card {
    background: white !important;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #d9e6da;
    color: #0f3b2e !important;
}

/* ===== SECTION ===== */
.section {
    background: white !important;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #d9e6da;
    color: #0f3b2e !important;
}

/* ===== TABLE FIX (CRITICAL) ===== */
table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
    background-color: white !important;
    color: #0f3b2e !important;
}

thead {
    background-color: #f1f5f3 !important;
    color: #0f3b2e !important;
}

th {
    padding: 8px;
    font-weight: 700;
    color: #0f3b2e !important;
}

td {
    padding: 8px;
    border-bottom: 1px solid #e5e7eb;
    color: #0f3b2e !important;
}

/* ===== KPI ===== */
.kpi-title {
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 0.5px;
    color: #0f3b2e;
    text-transform: uppercase;
}

.kpi-value {
    font-size: 30px;
    font-weight: 900;
    color: #004b2d;
    margin-top: 6px;
}

/* ===== STREAMLIT DATAFRAME OVERRIDE ===== */
[data-testid="stDataFrame"] {
    background-color: white !important;
    color: #0f3b2e !important;
}

[data-testid="stDataFrame"] * {
    color: #0f3b2e !important;
}

/* ===== STATUS BADGES ===== */
.badge {
    padding: 4px 8px;
    border-radius: 10px;
    font-size: 11px;
    font-weight: 600;
    display: inline-block;
}

.loading {background:#d0ebff;color:#0b7285;}
.searching {background:#fff3bf;color:#e67700;}
.anchor {background:#ffe3e3;color:#c92a2a;}
.transit {background:#e5dbff;color:#5f3dc4;}
.planned {background:#e9ecef;color:#495057;}
.arrived {background:#d3f9d8;color:#2b8a3e;}

</style>
""", unsafe_allow_html=True)

# ---------- MENU ----------
page = st.sidebar.radio(
    "Main Menu",
    ["OCP E2E", "Loading", "Global Supply", "Freight & Costs"]
)

# ---------- ROUTING ----------
if page == "OCP E2E":
    ocp_e2e.render()
else:
    st.title(page)
