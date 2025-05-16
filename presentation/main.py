

import streamlit as st

st.set_page_config(
    page_title="Sales Dashboard", layout="wide", initial_sidebar_state="expanded"
)


import data_insertion_and_overveiw
import pre_processing
import visualization

st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3063/3063826.png", width=80)
st.sidebar.title("📊 Sales Dashboard")
st.sidebar.markdown(
    "Welcome to the 2-Year Sales Analysis App. Use the navigation below to explore different parts of the data."
)

view = st.sidebar.radio(
    "🔍 Navigate to:", ["📥 Data Overview", "🧹 Preprocessing", "📈 visualization"]
)


st.title("📊 Sales Analytics Dashboard")

st.markdown("### 🔢 Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Revenue", "$1.23M")
with col2:
    st.metric("Total Profit", "$430K")
with col3:
    st.metric("Countries", "15+")

st.markdown("---")


if view == "📥 Data Overview":
    data_insertion_and_overveiw.show()
elif view == "🧹 Preprocessing":
    pre_processing.show()
elif view == "📈 visualization":
    visualization.show()


st.markdown("---")
st.markdown(
    "<p style='text-align: center;'>Built with ❤️ using Streamlit</p>",
    unsafe_allow_html=True,
)
