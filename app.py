import streamlit as st
import pandas as pd
from cleaner.cleaning import DataCleaner

st.title("🤖 AI-Powered Data Cleaning Assistant")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📌 Uploaded Data")
    st.dataframe(df)

    cleaner = DataCleaner(df)

    st.subheader("🔍 Missing Value Detection")
    st.write(cleaner.missing_values())

    st.subheader("🧹 Duplicate Removal")
    removed = cleaner.remove_duplicates()
    st.write(f"Removed {removed} duplicate rows")

    st.subheader("⚠ Outlier Detection")
    st.write(cleaner.detect_outliers())

    st.subheader("🧾 SQL Schema Generator")
    sql_code = cleaner.generate_sql()
    st.code(sql_code, language="sql")

    st.subheader("📥 Download Cleaned Dataset")
    st.download_button(
        label="Download Cleaned CSV",
        data=cleaner.df.to_csv(index=False),
        file_name="cleaned_data.csv",
        mime="text/csv"
    )
