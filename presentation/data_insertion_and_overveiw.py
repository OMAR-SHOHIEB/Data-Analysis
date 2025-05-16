import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.preprocessing import OneHotEncoder,LabelEncoder, OrdinalEncoder
import streamlit as st 
import io

st.title("DATA")
"""# date insertion"""

def data_insertion():
    df=pd.read_csv('sales_for_course.csv')
    return df
df=data_insertion()


def show():
    st.header("data_insertion_and_overveiw")
    st.subheader("show data before start")
    st.dataframe(df)
    """# over veiw"""

    col1, col2 = st.columns([1, 5])
    with col1:
        show_info = st.button("information")
    with col2:
        st.write("view general information about data")

    if show_info:
        buffer = io.StringIO()
        df.info(buf=buffer)
        s = buffer.getvalue()
        st.text(s)

    st.markdown("---")  

    col3, col4 = st.columns([1, 5])
    with col3:
        show_stats = st.button("describtion")
    with col4:
        st.write("View meta statistics")

    if show_stats:
        st.write(df.describe())


        
