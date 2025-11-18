import streamlit as st
import pandas as pd

def app():
    st.header("Data Profiler")
    st.write("Upload a CSV file to see basic statistics and preview.")
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Preview:")
        st.dataframe(df.head())
        st.write("Summary Statistics:")
        st.write(df.describe())
