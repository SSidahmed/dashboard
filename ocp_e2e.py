import streamlit as st
import pandas as pd
import plotly.express as px

def render():

    # ---------- HEADER ----------
    st.title("OCP E2E")

    f1, f2, f3 = st.columns(3)
    f1.selectbox("Date", ["May 2024"])
    f2.selectbox("Scope", ["Global"])
    f3.selectbox("Port", ["All"])

    st.divider()

    # ---------- KPI ----------
    cols = st.columns(5)

    def kpi(col, title, value):
        with col:
            st.markdown(f"""
            <div class="card">
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)

    kpi(cols[0], "PRODUCTION", "7.8 Mt")
    kpi(cols[1], "MOROCCO STOCKS", "2.7 Mt")
    kpi(cols[2], "TOTAL FLOWS", "28")
    kpi(cols[3], "IN TRANSIT", "4.8 Mt")
    kpi(cols[4], "ON-TIME", "91%")

    st.write("")

    # ---------- FLOWS DATA ----------
    df = pd.DataFrame({
        "Vessel":["MV Oceanic","MV Arrow","MV Green","MV Blue","MV Ducellier"],
        "Product":["Fert","Rock","Fert","Acid","Fert"],
        "Volume":[65,55,40,30,70],
        "Origin":["Jorf","Safi","Jorf","Safi","Jorf"],
        "Destination":["India","TBD","Brazil","Togo","USA"],
        "Status":["Loading","Searching","At Anchor","In Transit","Planned"],
        "ETA":["Jun 05","Jun 10","Jun 08","May 25","Jun 12"]
    })

    # ---------- STATUS BADGE ----------
    def style_status(val):
        classes = {
            "Loading":"loading",
            "Searching":"searching",
            "At Anchor":"anchor",
            "In Transit":"transit",
            "Planned":"planned",
            "Arrived":"arrived"
        }
        return f'<span class="badge {classes[val]}">{val}</span>'

    df["Status"] = df["Status"].apply(style_status)

    # ---------- MAIN TABLE ----------
    c1, c2 = st.columns([3,1])

    with c1:
        st.markdown('<div class="section"><b>Flows Overview</b>', unsafe_allow_html=True)
        st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section"><b>Deported Stocks</b>', unsafe_allow_html=True)

        df_deported = pd.DataFrame({
            "Location": ["Brazil", "West Africa", "Europe"],
            "Stock": [1200, 450, 300],
            "Utilization": [68, 55, 45]
        })

        st.markdown(
            df_deported.to_html(index=False),
            unsafe_allow_html=True
        )

        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

    # ---------- OPEN DEST ----------
    b1, b2 = st.columns(2)

    with b1:
        st.markdown('<div class="section"><b>Open Destination Cargoes</b>', unsafe_allow_html=True)
        filtered = df[df["Destination"]=="TBD"]
        st.markdown(filtered.to_html(escape=False, index=False), unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with b2:
        st.markdown('<div class="section"><b>Best Markets</b>', unsafe_allow_html=True)
        st.metric("India", "615 $/t")
        st.metric("Brazil", "575 $/t")
        st.metric("USA", "540 $/t")
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("")

    # ---------- CHARTS ----------
    d1, d2, d3 = st.columns(3)

    df_prod = pd.DataFrame({
        "Month":["Apr","May","Jun","Jul","Aug","Sep"],
        "Rock":[1200,1400,1600,1800,2000,2200],
        "Fert":[1800,2000,2200,2400,2600,2800],
        "Acid":[400,500,600,700,800,900]
    })

    fig1 = px.bar(
        df_prod,
        x="Month",
        y=["Rock","Fert","Acid"],
        template="plotly_white",
        color_discrete_sequence=["#7a7a7a","#2e7d32","#1976d2"]
    )

    fig1.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="#0f3b2e",
        title_font_size=16,
        legend_title_text=""
    )

    df_stock = pd.DataFrame({
        "Product":["Fert","Rock","Acid"],
        "Volume":[1600,800,300]
    })

    fig2 = px.pie(df_stock, values="Volume", names="Product", template="plotly_white")

    fig2.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        font_color="#0f3b2e",
        title_font_size=16
 )

    df_status = pd.DataFrame({
        "Status":["Loading","Searching","At Anchor","In Transit","Planned"],
        "Count":[5,4,3,6,2]
    })

    fig3 = px.bar(df_status, x="Status", y="Count", template="plotly_white")

    d1.plotly_chart(fig1, use_container_width=True)
    d2.plotly_chart(fig2, use_container_width=True)
    d3.plotly_chart(fig3, use_container_width=True)
