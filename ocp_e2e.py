import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

def render():

    # ---------- HEADER ----------
    st.title("OCP E2E")

    f1, f2, f3 = st.columns(3)
    f1.selectbox("Date", ["May 2024"])
    f2.selectbox("Scope", ["Global"])
    f3.selectbox("Port", ["All"])

    st.divider()

    # ---------- KPI DATA ----------
    available_volume = 2600
    stock = 2700
    flows = 28
    transit = 4800
    ontime = 91

    # ---------- KPI DISPLAY ----------
    cols = st.columns(5)
    kpis = [
        ("PRODUCTION", "7.8 Mt"),
        ("MOROCCO STOCKS", "2.7 Mt"),
        ("TOTAL FLOWS", "28"),
        ("IN TRANSIT", "4.8 Mt"),
        ("ON-TIME", "91%")
    ]

    for col, (title, value) in zip(cols, kpis):
        with col:
            st.markdown(f"""
            <div class="card">
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

    # ---------- PRODUCTION DATA ----------
    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep"]

    df_prod = pd.DataFrame({
        "Month": months,
        "Rock": [1200,1400,1600,1800,2000,2200],
        "Fert": [1800,2000,2200,2400,2600,2800],
        "Acid": [400,500,600,700,800,900]
    })

    fig_prod = px.bar(df_prod, x="Month", y=["Rock","Fert","Acid"],
                      title="Production Plan",
                      color_discrete_sequence=["#7a7a7a","#2e7d32","#1976d2"],
                      template="plotly_white")

    # ---------- STOCK DATA ----------
    df_stock = pd.DataFrame({
        "Product":["Fert","Rock","Acid"],
        "Volume":[1600,800,300]
    })

    fig_stock = px.pie(df_stock, values="Volume", names="Product",
                       title="Morocco Stocks",
                       template="plotly_white")

    # ---------- FLOWS TABLE ----------
    df_flows = pd.DataFrame({
        "Vessel":["MV Oceanic","MV Arrow","MV Green","MV Blue","MV Horizon"],
        "Product":["Fert","Rock","Fert","Acid","Fert"],
        "Volume":[65,55,40,30,70],
        "Origin":["Jorf","Safi","Jorf","Safi","Jorf"],
        "Destination":["India","TBD","Brazil","Togo","USA"],
        "Status":["Loading","Searching","At Anchor","In Transit","Planned"],
        "ETA":["Jun 05","Jun 10","Jun 08","May 25","Jun 12"]
    })

    # ---------- LAYOUT ----------
    c1, c2 = st.columns([3,1])

    with c1:
        st.subheader("Flows Overview")
        st.dataframe(df_flows, use_container_width=True)

    with c2:
        st.subheader("Deported Stocks")
        st.dataframe(pd.DataFrame({
            "Location":["Brazil","West Africa","Europe"],
            "Stock":[1200,450,300],
            "Utilization":[68,55,45]
        }))

    st.write("")

    # ---------- SECOND ROW ----------
    b1, b2 = st.columns(2)

    with b1:
        st.subheader("Open Destination Cargoes")
        st.dataframe(df_flows[df_flows["Destination"]=="TBD"])

    with b2:
        st.subheader("Best Markets")
        st.metric("India", "615 $/t")
        st.metric("Brazil", "575 $/t")
        st.metric("USA", "540 $/t")

    st.write("")

    # ---------- BOTTOM ----------
    d1, d2, d3 = st.columns(3)

    with d1:
        st.plotly_chart(fig_prod, use_container_width=True)

    with d2:
        st.plotly_chart(fig_stock, use_container_width=True)

    with d3:
        status_counts = df_flows["Status"].value_counts().reset_index()
        status_counts.columns = ["Status","Count"]

        fig_status = px.bar(status_counts, x="Status", y="Count",
                            title="Volumes by Status")

        st.plotly_chart(fig_status, use_container_width=True)
