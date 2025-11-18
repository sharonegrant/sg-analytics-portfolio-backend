import streamlit as st
from pages import forecasting, kpi_model, data_profiler

st.set_page_config(page_title="SG Analytics Portfolio", page_icon=":bar_chart:", layout="wide")

st.sidebar.title("SG Analytics Portfolio")
app_mode = st.sidebar.selectbox("Choose a module",
                                ["Home", "Forecasting Simulator", "KPI Scenario Modeler", "Data Profiler"])

if app_mode == "Home":
    st.title("Welcome to SG Analytics Portfolio")
    st.markdown("Explore interactive analytics modules from the sidebar.")
elif app_mode == "Forecasting Simulator":
    forecasting.app()
elif app_mode == "KPI Scenario Modeler":
    kpi_model.app()
elif app_mode == "Data Profiler":
    data_profiler.app()
