import streamlit as st
import ocp_e2e

st.set_page_config(layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>

/* ===== GLOBAL ===== */
.stApp {
    background-color: #f7f7f5;
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
    background: white;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #d9e6da;
}

.kpi-title {
    font-size: 12px;
    font-weight: 700;
}

.kpi-value {
    font-size: 26px;
    font-weight: 800;
    color: #004b2d;
}

/* ===== SECTIONS ===== */
.section {
    background: white;
    padding: 14px;
    border-radius: 14px;
    border: 1px solid #d9e6da;
}

/* ===== TABLE STYLE ===== */
table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
}

th {
    background-color: #f1f5f3;
    text-align: left;
    padding: 8px;
    font-weight: 700;
}

td {
    padding: 8px;
    border-bottom: 1px solid #e5e7eb;
}

/* ===== STATUS BADGES ===== */
.badge {
    padding: 3px 8px;
    border-radius: 8px;
    font-size: 11px;
    font-weight: 600;
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
