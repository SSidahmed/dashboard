import streamlit as st
import ocp_e2e

st.set_page_config(layout="wide")

# ---------- GLOBAL STYLE ----------
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

/* ===== KPI CARDS ===== */
.kpi {
    background: white;
    border-radius: 14px;
    padding: 14px;
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

/* ===== SECTION ===== */
.section {
    background: white;
    border-radius: 14px;
    padding: 14px;
    border: 1px solid #d9e6da;
}

/* ===== STATUS BADGES ===== */
.badge {
    padding: 4px 8px;
    border-radius: 10px;
    font-size: 12px;
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
