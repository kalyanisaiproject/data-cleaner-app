import streamlit as st
import pandas as pd
from cleaner import clean_data

st.set_page_config("Data Cleaner App", layout="wide")

st.title("Smart Data Cleaning Tool")

file = st.file_uploader("Upload Excel or CSV", type=["xlsx","csv"])

if file:

    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.subheader("Original Data")
    st.dataframe(df.head())

    if st.button("Clean Data"):

        clean_df = clean_data(df)

        st.subheader("Cleaned Data")
        st.dataframe(clean_df.head())

        # Download
        csv = clean_df.to_csv(index=False).encode()

        st.download_button(
            "Download Clean File",
            csv,
            "clean_data.csv",
            "text/csv"
        )