import streamlit as st
import pandas as pd
import plotly.express as px

# Page setup
st.set_page_config(
    page_title="Titanic Dashboard",
    page_icon="🚢",
    layout="wide"
)

# Title
st.title("🚢 Titanic Data Visualization Dashboard")

st.markdown("Interactive Titanic Passenger Analysis")

# Dataset
DATA_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"

# Read data
df = pd.read_csv(DATA_URL)

# Fill missing values
df["sex"] = df["sex"].fillna("Unknown")
df["class"] = df["class"].fillna("Unknown")
df["embark_town"] = df["embark_town"].fillna("Unknown")

# Sidebar
st.sidebar.header("Filters")

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df["sex"].unique(),
    default=df["sex"].unique()
)

filtered_df = df[df["sex"].isin(gender_filter)]

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Passengers", len(filtered_df))

col2.metric(
    "Survived",
    int(filtered_df["survived"].sum())
)

col3.metric(
    "Average Age",
    round(filtered_df["age"].mean(), 1)
)

st.divider()

# Survival Chart
st.subheader("📊 Survival Distribution")

fig1 = px.pie(
    filtered_df,
    names="survived",
    title="Passenger Survival"
)

st.plotly_chart(fig1, use_container_width=True)

# Passenger Class Chart
st.subheader("🎟 Passenger Class Distribution")

class_data = filtered_df["class"].value_counts()

fig2 = px.bar(
    x=class_data.index,
    y=class_data.values,
    labels={"x": "Class", "y": "Count"},
    title="Passenger Classes"
)

st.plotly_chart(fig2, use_container_width=True)

# Age Distribution
st.subheader("📅 Age Distribution")

fig3 = px.histogram(
    filtered_df,
    x="age",
    nbins=30,
    title="Age Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# Data Preview
st.subheader("🗂 Dataset Preview")

st.dataframe(filtered_df.head(20))

st.success("Dashboard Loaded Successfully 🚀")