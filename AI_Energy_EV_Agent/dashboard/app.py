import streamlit as st
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="EV Fleet Optimization",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ EV Fleet Optimization Agent")
st.write("EV Fleet Monitoring Dashboard")

df = pd.read_csv("data/ev_fleet.csv")

col1, col2, col3 = st.columns(3)

col1.metric("Total EVs", len(df))
col2.metric(
    "Average Battery",
    f"{df['battery_percent'].mean():.1f}%"
)
col3.metric(
    "Available EVs",
    len(df[df["status"] == "Available"])
)

st.subheader("🚗 EV Fleet Data")

st.dataframe(df, use_container_width=True)

st.subheader("🔋 Battery Status")

critical = len(df[df["battery_percent"] <= 20])
high = len(df[
    (df["battery_percent"] > 20) &
    (df["battery_percent"] <= 40)
])
normal = len(df[df["battery_percent"] > 40])

c1, c2, c3 = st.columns(3)

c1.metric("🔴 Critical", critical)
c2.metric("🟡 Charging Required", high)
c3.metric("🟢 Sufficient", normal)