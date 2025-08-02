# app.py

import streamlit as st
import pandas as pd
from src.ingest import load_all_data
from src.transform import clean_dataframe
from src.analyze import plot_trend
from src.indicators import compute_climate_resilience

# Set page config
st.set_page_config(page_title="Climate Resilience Dashboard", layout="wide")

st.title("🌾 Climate Resilience Dashboard")

# Sidebar: State selection
state = st.sidebar.selectbox("📍 Select State", ["Maharashtra", "Madhya Pradesh"])

# Sidebar: Temperature column selection
temp_option = st.sidebar.radio("🌡 Select Temperature Type", ["mean", "max", "min"])

# Load and prepare data
data = load_all_data()

if state == "Maharashtra":
    temp_df = clean_dataframe(data["MH_temp"])
    precip_df = clean_dataframe(data["MH_precip"])
else:
    temp_df = clean_dataframe(data["MP_temp"])
    precip_df = clean_dataframe(data["MP_precip"])

# Main content
st.subheader(f"📊 Analyzing {state} with '{temp_option}' temperature")

# Plot Temperature
st.markdown("#### 🌡 Temperature Trend")
fig1 = plot_trend(temp_df, temp_option, state, "Temperature")
if fig1:
    st.pyplot(fig1)

# Plot Precipitation
st.markdown("#### 🌧 Precipitation Trend")
fig2 = plot_trend(precip_df, "rainfall_mm", state, "Precipitation")
if fig2:
    st.pyplot(fig2)

# Compute and display climate indicators
indicators = compute_climate_resilience(temp_df, precip_df, temp_col=temp_option, precip_col="rainfall_mm")

st.markdown("#### 📈 Climate Resilience Indicators")
for key, val in indicators.items():
    st.write(f"**{key}**: {val:.2f}")
