import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.preprocessing import OneHotEncoder,LabelEncoder, OrdinalEncoder
import streamlit as st 



def show():
    df=pd.read_csv("sales_for_course.csv")  
    st.header("pre_processing")

    """# Pre-processing

    detect duplicates
    """
    st.subheader("Detecting Duplicates")
    duplicates = df[df.duplicated()]
    st.write("Number of duplicate rows in the data:")
    st.dataframe(duplicates)
    df = df.drop_duplicates()
    duplicates_left = df.duplicated().sum()

    if duplicates_left == 0:
        st.success("All duplicates have been successfully not exist 🎉")
    else:
        st.warning(f"There are {duplicates_left} duplicates left in the data.")

    st.markdown("""
    ### Handling Method:

    - We detected duplicates using `duplicated()`, which returns only the duplicate rows.
    - Then, we removed these duplicate rows using `drop_duplicates()`, which keeps the first occurrence of each duplicate set.
    - Finally, we checked the number of remaining duplicates using `duplicated().sum()` to ensure there were none left.
    """)



    """nulls"""
    st.subheader("Discovering Missing Values (Null Values)")
    null_counts = df.isnull().sum()
    st.write("Number of missing values in each column:")
    st.dataframe(null_counts[null_counts > 0])

    if null_counts.sum() == 0:
        st.success("There are no missing values in the data 🎉")
    else:
        st.warning(f"There are {null_counts.sum()} missing values in total.")

    st.markdown("""
    ### Handling Method:

    - We removed the rows with missing values using `dropna(axis=0)`
    - This decision was made because the number of missing values is not large, and it is better not to include incomplete data that might affect analytical or graphical models.
    """)

    """outliers"""
    st.subheader("Boxplot of Revenue vs Customer Age to detect outlier")
    fig, ax = plt.subplots()
    sns.boxplot(data=df[["Revenue", "Customer Age"]], ax=ax)
    ax.set_title("Revenue vs Customer Age Boxplot")


    st.pyplot(fig)


    st.markdown("""
    ### Explanation:
    - The boxplot shows the distribution of both **Revenue** and **Customer Age**.
    - The lines in the box (whiskers) represent the range of the data, and the points outside these lines are generally considered outliers.
    - However, in this case, the data points outside the whiskers are not outliers. 
    - They represent a **normal increase in revenue**, meaning that as the **Customer Age** increases, **Revenue** tends to rise as well. This is a typical pattern and not an anomaly in the data.
    """)

    """ Dropping unnecessary columns"""
    st.subheader("Dropping Unnecessary Columns")
    df = df.drop(columns=["index", "Column1", "Year"])

    st.write("Here are the first 10 rows of the dataset after dropping unnecessary columns:")
    st.dataframe(df.head(10))

    st.markdown("""
    ### Explanation:
    - In the dataset, we decided to **drop** certain columns that are not important for our analysis or modeling.
    - The columns dropped are:
        - `index`: This column likely just contains row numbers and doesn't provide meaningful information for our analysis.
        - `Column1`: This column may not contain relevant data for our analysis and can be safely removed.
        - `Year`: Depending on the context, this column may not be needed for the current analysis, so we decided to remove it.
    - After dropping these columns, we are left with a cleaner dataset containing only the relevant data.
    """)



    """# create columns to date"""

    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by="Date").reset_index(drop=True)

    df["year"] = df["Date"].dt.year
    df["month"] = df["Date"].dt.month
    df["day"] = df["Date"].dt.day

    st.write("Here are the first 10 rows after extracting year, month, and day:")
    st.dataframe(df.head(10))

    st.markdown("""
    ### Explanation:
    - We started by converting the **"Date"** column into a **datetime** format using `pd.to_datetime()`. This ensures that the column is recognized as a proper date and allows us to perform date-related operations.
    - Then, we sorted the dataset by the **"Date"** column using `sort_values()` and reset the index to maintain a clean structure with `reset_index(drop=True)`.
    - After that, we extracted three new columns from the **"Date"** column:
        - `year`: The year part of the date.
        - `month`: The month part of the date.
        - `day`: The day part of the date.
    - These new columns will allow for easier analysis based on year, month, or day.
    """)



    '''Feature selection: Reordering columns'''
    st.subheader("Feature Selection: Reordering Columns")
    order = ["Date", "day", "month", "Month", "year", "Customer Age", "Customer Gender", 
            "Country", "State", "Product Category", "Sub Category", "Quantity", 
            "Unit Cost", "Unit Price", "Cost", "Revenue"]

    df = df[order]
    st.write("Here are the first 10 rows of the dataset after feature selection:")
    st.dataframe(df.head(10))

    st.markdown("""
    ### Explanation:
    - **Feature selection** involves choosing only the relevant features (columns) for further analysis or modeling.
    - In this case, we **reordered** the columns in a specific order that is most relevant for the analysis. 
    - By reordering, we prioritize the most important columns, such as **Date**, **Revenue**, **Cost**, **Customer Information**, and other business-relevant features.
    - This step helps in focusing on the necessary data for further exploration and modeling while removing unnecessary or irrelevant features.
    """)
    st.subheader("Feature Extraction: Calculating Profit")


    df["profit"] = df["Revenue"] - df["Cost"]

    fig, ax = plt.subplots(figsize=(20, 5))
    sns.lineplot(data=df, x="Date", y="profit", ax=ax)
    ax.set_title("Profit Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Profit")
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    st.markdown("""
    ### Explanation:
    - We created a new column called **"profit"** by subtracting the **"Cost"** column from the **"Revenue"** column: `df["profit"] = df["Revenue"] - df["Cost"]`.
    - This represents the profit for each entry in the dataset.
    - We then visualized the profit over time using a **line plot** to observe how the profit changes with respect to the **Date**.
    - The line plot helps us identify trends, patterns, and potential fluctuations in the profit data over time.
    """)