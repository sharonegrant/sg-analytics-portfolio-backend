import streamlit as st

def app():
    st.header("KPI Scenario Modeler")
    st.write("Connect leads, conversion rate, and deal value to revenue.")
    leads = st.number_input("Number of leads", value=1000)
    conversion = st.slider("Conversion rate (%)", 0, 100, 10)
    deal_value = st.number_input("Average deal value ($)", value=5000)
    revenue = leads * (conversion/100) * deal_value
    st.metric("Projected Revenue", f"${revenue:,.2f}")
