import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# PAGE CONFIG
# ----------------------------------
st.set_page_config(
    page_title="Data Cleaning Visual Dashboard",
    layout="wide"
)

st.title("📊 Data Cleaning & Visualization Dashboard")

# ----------------------------------
# UPLOAD DATA
# ----------------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📁 Raw Data Preview")
    st.dataframe(df)

    # ----------------------------------
    # MISSING VALUE ANALYSIS
    # ----------------------------------
    st.subheader("🧹 Missing Value Analysis")

    missing = df.isnull().sum().reset_index()
    missing.columns = ["Column", "Missing Values"]
    st.table(missing)

    # PIE CHART
    fig_pie = px.pie(
        missing,
        names="Column",
        values="Missing Values",
        title="Missing Values Distribution",
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True)

    # BAR CHART
    fig_bar = px.bar(
        missing,
        x="Column",
        y="Missing Values",
        title="Missing Values per Column",
        text="Missing Values"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # ----------------------------------
    # DUPLICATES
    # ----------------------------------
    st.subheader("📑 Duplicate Data Summary")

    duplicate_count = df.duplicated().sum()
    st.metric(label="Number of Duplicate Rows", value=duplicate_count)

    # ----------------------------------
    # OUTLIER VISUALIZATION (BOX PLOT)
    # ----------------------------------
    st.subheader("📦 Outlier Detection (Box Plot)")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) > 0:
        outlier_col = st.selectbox("Choose a column for box plot:", numeric_cols)
        fig_box = px.box(df, y=outlier_col, title=f"Outlier Box Plot for {outlier_col}")
        st.plotly_chart(fig_box, use_container_width=True)

    # ----------------------------------
    # HISTOGRAM & SCATTER PLOT
    # ----------------------------------
    st.subheader("📈 Data Distribution & Relationship")

    col1, col2 = st.columns(2)

    with col1:
        if len(numeric_cols) > 0:
            hist_col = st.selectbox("Select column for Histogram", numeric_cols)
            fig_hist = px.histogram(df, x=hist_col, title=f"Histogram of {hist_col}")
            st.plotly_chart(fig_hist, use_container_width=True)

    with col2:
        if len(numeric_cols) > 1:
            scatter_x = st.selectbox("X-Axis", numeric_cols)
            scatter_y = st.selectbox("Y-Axis", numeric_cols, index=1)
            fig_scatter = px.scatter(df, x=scatter_x, y=scatter_y,
                                     title=f"Scatter Plot: {scatter_x} vs {scatter_y}")
            st.plotly_chart(fig_scatter, use_container_width=True)

    # ----------------------------------
    # CATEGORY DISTRIBUTION
    # ----------------------------------
    st.subheader("📊 Categorical Column Distribution")

    cat_cols = df.select_dtypes(include=['object']).columns

    if len(cat_cols) > 0:
        cat_col = st.selectbox("Choose a Category Column", cat_cols)
        fig_cat = px.bar(
            df[cat_col].value_counts().reset_index(),
            x="index",
            y=cat_col,
            title=f"Category Distribution for {cat_col}",
            labels={"index": cat_col, cat_col: "Count"}
        )
        st.plotly_chart(fig_cat, use_container_width=True)

    st.success("Dashboard Updated Successfully! 🎉")
else:
    st.info("Please upload a CSV file to generate the dashboard.")
