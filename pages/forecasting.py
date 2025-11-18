import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def app():
    st.header("Forecasting Simulator")
    st.write("Adjust parameters to simulate future outcomes.")
    periods = st.slider("Number of periods", 5, 50, 20)
    growth = st.slider("Growth rate (%)", -10.0, 20.0, 5.0)
    noise_level = st.slider("Noise level", 0.0, 1.0, 0.2)
    time = np.arange(periods)
    data = (1 + growth/100)**time + noise_level * np.random.randn(periods)
    df = pd.DataFrame({"Period": time, "Value": data})
    fig = px.line(df, x="Period", y="Value", title="Forecast Simulation")
    st.plotly_chart(fig)
