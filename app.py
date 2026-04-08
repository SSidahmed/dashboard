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
    :root {
        --ocp-dark: #004b2d;
        --ocp-dark-2: #0a6a41;
        --ocp-light: #f4f7f3;
        --ocp-border: #d9e6da;
        --ocp-text: #0f3b2e;
        --ocp-muted: #6b7c72;
        --ocp-accent: #a7c957;
    }

    .stApp {
        background-color: #f7f7f5;
        color: var(--ocp-text);
    }

    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 1rem;
        max-width: 96%;
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #004b2d 0%, #003a23 100%);
        border-right: 1px solid rgba(255,255,255,0.08);
    }

    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    .sidebar-logo {
        font-size: 2rem;
        font-weight: 800;
        letter-spacing: 0.5px;
        margin-bottom: 1.2rem;
    }

    .sidebar-subtitle {
        font-size: 0.8rem;
        text-transform: uppercase;
        color: rgba(255,255,255,0.78) !important;
        margin-bottom: 0.5rem;
        letter-spacing: 0.5px;
    }

    .header-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: var(--ocp-dark);
        margin: 0;
        line-height: 1.05;
    }

    .kpi-box {
        background: white;
        padding: 1rem 1.2rem;
        border-radius: 16px;
        border: 1px solid var(--ocp-border);
        min-height: 118px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }

    .kpi-title {
        font-size: 0.88rem;
        font-weight: 700;
        color: var(--ocp-text);
        text-transform: uppercase;
        letter-spacing: 0.2px;
        margin-bottom: 0.65rem;
    }

    .kpi-value {
        font-size: 2.25rem;
        font-weight: 800;
        color: var(--ocp-dark);
        line-height: 1;
    }

    .kpi-sub {
        color: var(--ocp-muted);
        font-size: 0.92rem;
        margin-top: 0.35rem;
    }

    .kpi-foot {
        color: #1f8f4e;
        font-size: 0.9rem;
        font-weight: 600;
        margin-top: 0.8rem;
    }

    .section-box {
        background: white;
        padding: 1rem 1.2rem;
        border-radius: 16px;
        border: 1px solid var(--ocp-border);
        min-height: 260px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }

    .section-title {
        color: var(--ocp-dark);
        font-weight: 800;
        font-size: 1.15rem;
        margin-bottom: 0.5rem;
    }

    .small-muted {
        color: var(--ocp-muted);
        font-size: 0.92rem;
    }

    div[data-baseweb="select"] > div {
        border-radius: 12px !important;
        border-color: var(--ocp-border) !important;
        background-color: white !important;
    }

    .stRadio > div {
        gap: 0.5rem;
    }

    .stRadio label {
        background: transparent;
        border-radius: 12px;
        padding: 0.35rem 0.45rem;
    }

    .stRadio label:has(input:checked) {
        background: rgba(167, 201, 87, 0.2);
    }

    hr {
        border-color: #dde6dc;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- SIDEBAR / MAIN MENU ----------
st.sidebar.markdown('<div class="sidebar-logo">OCP</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-subtitle">Main menu</div>', unsafe_allow_html=True)

main_section = st.sidebar.radio(
    "",
    [
        "OCP E2E",
        "Loading",
        "Global Supply",
        "Freight & Costs",
    ],
    index=0,
)

st.sidebar.markdown("---")
st.sidebar.caption("Prototype dashboard")

# ---------- TOP HEADER ----------
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown(f'<div class="header-title">{main_section}</div>', unsafe_allow_html=True)

with col2:
    f1, f2, f3 = st.columns(3)
    with f1:
        st.selectbox("Date", ["May 20, 2024"], label_visibility="visible")
    with f2:
        st.selectbox("Scope", ["Global"], label_visibility="visible")
    with f3:
        st.selectbox("Port", ["All"], label_visibility="visible")

st.divider()

# ---------- KPI ROW ----------
k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.markdown(
        '''
        <div class="kpi-box">
            <div class="kpi-title">Production</div>
            <div class="kpi-value">--</div>
            <div class="kpi-sub">This decade</div>
            <div class="kpi-foot">Placeholder KPI</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
with k2:
    st.markdown(
        '''
        <div class="kpi-box">
            <div class="kpi-title">Morocco Stocks</div>
            <div class="kpi-value">--</div>
            <div class="kpi-sub">Total stock</div>
            <div class="kpi-foot">Placeholder KPI</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
with k3:
    st.markdown(
        '''
        <div class="kpi-box">
            <div class="kpi-title">Total Flows</div>
            <div class="kpi-value">--</div>
            <div class="kpi-sub">Active cargoes</div>
            <div class="kpi-foot">Placeholder KPI</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
with k4:
    st.markdown(
        '''
        <div class="kpi-box">
            <div class="kpi-title">Volume In Transit</div>
            <div class="kpi-value">--</div>
            <div class="kpi-sub">Current</div>
            <div class="kpi-foot">Placeholder KPI</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
with k5:
    st.markdown(
        '''
        <div class="kpi-box">
            <div class="kpi-title">On-Time Arrival</div>
            <div class="kpi-value">--</div>
            <div class="kpi-sub">Current rate</div>
            <div class="kpi-foot">Placeholder KPI</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

st.write("")

# ---------- MAIN CONTENT ----------
c1, c2 = st.columns([3, 1])
with c1:
    st.markdown(
        '''
        <div class="section-box">
            <div class="section-title">Flows Overview</div>
            <p class="small-muted">Main cargo table placeholder</p>
        </div>
        ''',
        unsafe_allow_html=True,
    )
with c2:
    st.markdown(
        '''
        <div class="section-box">
            <div class="section-title">Deported Stocks by Location</div>
            <p class="small-muted">Right-side summary placeholder</p>
        </div>
        ''',
        unsafe_allow_html=True,
    )

st.write("")

b1, b2 = st.columns([2, 2])
with b1:
    st.markdown(
        '''
        <div class="section-box">
            <div class="section-title">Open Destination Cargoes</div>
            <p class="small-muted">Optionality / cargoes still open</p>
        </div>
        ''',
        unsafe_allow_html=True,
    )
with b2:
    st.markdown(
        '''
        <div class="section-box">
            <div class="section-title">Best Markets</div>
            <p class="small-muted">Market ranking placeholder</p>
        </div>
        ''',
        unsafe_allow_html=True,
    )

st.write("")

d1, d2, d3 = st.columns(3)
with d1:
    st.markdown(
        '''
        <div class="section-box">
            <div class="section-title">Production Plan by Decade</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
with d2:
    st.markdown(
        '''
        <div class="section-box">
            <div class="section-title">Stocks by Product</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )
with d3:
    st.markdown(
        '''
        <div class="section-box">
            <div class="section-title">Volumes by Status</div>
        </div>
        ''',
        unsafe_allow_html=True,
    )

st.caption(f"Current section: {main_section}")
