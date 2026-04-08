import streamlit as st

st.set_page_config(
    page_title="OCP Logistics Dashboard",
    page_icon="🌍",
    layout="wide",
)

# ---------- STYLE ----------
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7f5;
    }
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .kpi-box {
        background: white;
        padding: 1rem 1.2rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        min-height: 110px;
    }
    .section-box {
        background: white;
        padding: 1rem 1.2rem;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        min-height: 260px;
    }
    .menu-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1rem;
    }
    .small-muted {
        color: #6b7280;
        font-size: 0.9rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- SIDEBAR ----------
st.sidebar.markdown(
    """
    <div class="menu-title">OCP</div>
    """,
    unsafe_allow_html=True,
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Production",
        "Stocks",
        "Flows",
        "Deported Stocks",
        "Open Destination",
        "Reports",
    ],
)

# ---------- TOP HEADER ----------
col1, col2 = st.columns([3, 2])

with col1:
    st.title("OCP E2E")

with col2:
    f1, f2, f3 = st.columns(3)
    with f1:
        st.selectbox("Date", ["May 20, 2024"])
    with f2:
        st.selectbox("Scope", ["Global"])
    with f3:
        st.selectbox("Port", ["All"])

# ---------- TOP MENU ----------
m1, m2, m3, m4 = st.columns(4)
with m1:
    st.button("OCP E2E", use_container_width=True)
with m2:
    st.button("Loading", use_container_width=True)
with m3:
    st.button("Global Supply", use_container_width=True)
with m4:
    st.button("Freight & Costs", use_container_width=True)

st.divider()

# ---------- KPI ROW ----------
k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(
        """
        <div class="kpi-box">
            <h4>Production</h4>
            <h2>--</h2>
            <div class="small-muted">This decade</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k2:
    st.markdown(
        """
        <div class="kpi-box">
            <h4>Morocco Stocks</h4>
            <h2>--</h2>
            <div class="small-muted">Total stock</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k3:
    st.markdown(
        """
        <div class="kpi-box">
            <h4>Total Flows</h4>
            <h2>--</h2>
            <div class="small-muted">Active cargoes</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k4:
    st.markdown(
        """
        <div class="kpi-box">
            <h4>Volume In Transit</h4>
            <h2>--</h2>
            <div class="small-muted">Current</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with k5:
    st.markdown(
        """
        <div class="kpi-box">
            <h4>On-Time Arrival</h4>
            <h2>--</h2>
            <div class="small-muted">Current rate</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

# ---------- MAIN CONTENT ----------
c1, c2 = st.columns([3, 1])

with c1:
    st.markdown(
        """
        <div class="section-box">
            <h4>Flows Overview</h4>
            <p class="small-muted">Main cargo table placeholder</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        """
        <div class="section-box">
            <h4>Deported Stocks by Location</h4>
            <p class="small-muted">Right-side summary placeholder</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

b1, b2 = st.columns([2, 2])

with b1:
    st.markdown(
        """
        <div class="section-box">
            <h4>Open Destination Cargoes</h4>
            <p class="small-muted">Optionality / cargoes still open</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with b2:
    st.markdown(
        """
        <div class="section-box">
            <h4>Best Markets</h4>
            <p class="small-muted">Market ranking placeholder</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")

d1, d2, d3 = st.columns(3)

with d1:
    st.markdown(
        """
        <div class="section-box">
            <h4>Production Plan by Decade</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

with d2:
    st.markdown(
        """
        <div class="section-box">
            <h4>Stocks by Product</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

with d3:
    st.markdown(
        """
        <div class="section-box">
            <h4>Volumes by Status</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.caption(f"Current page: {page}")