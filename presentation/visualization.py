import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.preprocessing import OneHotEncoder,LabelEncoder, OrdinalEncoder
import streamlit as st 
import io

def show():
    df=pd.read_csv("sales_for_course.csv")  
    st.header("pre_processing")
    analysis_type = st.selectbox(
    "Select Analysis Type",
    ["date","Age","Gender","country","main_category","sub_category","country_product"]
)
    df["profit"] = df["Revenue"] - df["Cost"]

    if analysis_type=="date":
        
        st.markdown("### ✅ Step 1: Data Preparation")
        st.markdown("""
        In this step, we converted the `Date` column to datetime format and extracted additional time-based features like year, month, and day.  
        This will help in performing time-series analysis and understanding trends over time.
        """)

        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date").reset_index(drop=True)
        df["year"] = df["Date"].dt.year
        df["month"] = df["Date"].dt.month
        df["day"] = df["Date"].dt.day

        st.markdown("### 📅 Step 2: Monthly Distribution of Sales")
        st.markdown("""
        Here we analyze how sales are distributed across different months using a pie chart.  
        🟢 **Observation:** Most of the sales seem to occur in **January** and **December**, indicating strong seasonal activity — possibly due to holiday promotions or end-of-year offers.
        """)

        fig1, ax1 = plt.subplots()
        month_counts = df["Month"].value_counts()
        ax1.pie(month_counts, labels=month_counts.index, autopct='%1.1f%%', startangle=90, shadow=True)
        ax1.axis('equal')
        st.pyplot(fig1)

        st.markdown("### 📈 Step 3: Revenue Over 2015")
        st.markdown("""
        We visualize revenue trends throughout 2015 to identify performance over time.  
        🟢 **Observation:** There are fluctuations in revenue, with noticeable spikes — possibly caused by high-volume purchases or promotions during certain periods.
        """)

        df_2015 = df[df["year"] == 2015.0]
        fig2, ax2 = plt.subplots(figsize=(15, 4))
        ax2.plot(df_2015["Date"], df_2015["Revenue"])
        ax2.set_xlabel("Date")
        ax2.set_ylabel("Revenue")
        ax2.set_title("Revenue Over 2015")
        st.pyplot(fig2)

        st.markdown("### 📈 Step 4: Revenue Over 2016")
        st.markdown("""
        A similar trend analysis for the year 2016.  
        🟢 **Observation:** Compared to 2015, revenue appears more stable in 2016 with fewer spikes, possibly indicating a more consistent customer base or better inventory control.
        """)

        df_2016 = df[df["year"] == 2016.0]
        fig3, ax3 = plt.subplots(figsize=(15, 4))
        ax3.plot(df_2016["Date"], df_2016["Revenue"])
        ax3.set_xlabel("Date")
        ax3.set_ylabel("Revenue")
        ax3.set_title("Revenue Over 2016")
        st.pyplot(fig3)

        st.markdown("### 💰 Step 5: Profit Over Time")
        st.markdown("""
        We calculate profit by subtracting cost from revenue, and plot it over time.  
        🟢 **Observation:** Profit trends reflect revenue behavior but can be more sensitive to cost changes. Some dips might indicate discounts or high-cost items sold.
        """)

        
        fig, ax = plt.subplots(figsize=(20, 5))
        sns.lineplot(data=df, x="Date", y="profit", ax=ax)
        ax.set_title("Profit Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Profit")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

      
        st.markdown("### 📄 Step 6: Sample of Raw Data")
        st.markdown("""
        A view the cleaned dataset to help understand the structure and verify the preprocessing steps.
        """)
        st.dataframe(df.head(10))
        
      
        st.markdown("### 📅 Revenue Trend in Each Month of 2015")
        st.markdown("""
        We analyze the revenue day-by-day for each month in 2015 to spot detailed fluctuations or trends inside months.  
        🟢 **Observation:** Some months have strong mid-month spikes, while others peak at the end, indicating varied shopping behaviors.
        """)

        fig5, axes = plt.subplots(4, 3, figsize=(20, 10))
        axes = axes.flatten()

        for month in range(1, 13):
            ax = axes[month - 1]
            x_axis = df_2015[df_2015["month"] == month]
            sns.lineplot(data=x_axis, x="day", y="Revenue", ax=ax)
            ax.set_title(f"Revenue in {month}/2015")

        plt.suptitle("Revenue over Months in 2015", fontsize=16, fontweight="bold")
        plt.tight_layout()
        st.pyplot(fig5)

        st.markdown("### 📅 Revenue Trend in Each Month of 2016")
        st.markdown("""
        We repeat the same day-by-day revenue analysis for the available months in 2016.  
        🟢 **Observation:** 2016 shows more stable revenue patterns per month, with less variability than 2015.
        """)

        fig6, axes = plt.subplots(2, 4, figsize=(20, 10))
        axes = axes.flatten()

        for month in range(1, 8):  
            ax = axes[month - 1]
            data = df_2016[df_2016["month"] == month]
            sns.lineplot(data=data, x="day", y="Revenue", ax=ax)
            ax.set_title(f"Revenue in {month}/2016")

        plt.suptitle("Revenue over Months in 2016", fontsize=16, fontweight="bold")
        plt.tight_layout()
        st.pyplot(fig6)

    elif analysis_type=="Age":

       

        st.title("Customer Age Analysis with Gaussian Bell 'Normal Distribution'")


        st.markdown("""
        ### Analyzing Customer Age

        In this section, we analyze the distribution of customer ages using the `seaborn` library with a `pairplot`.

        This visualization helps us understand how the values of the **Customer Age** feature are distributed.
        """)

     
        fig = sns.pairplot(df, vars=["Customer Age"], height=3)
        st.pyplot(fig.figure)  
        plt.tight_layout()
  
        st.markdown("""
        > 🔍 **Observation:**  
        > Most customers are between the ages of **20 and 40**.  
        > This age group represents the majority of the dataset, indicating that the business attracts mostly young adults.
        """)

        st.markdown("### Preview of the First Five Rows of the Data")
        st.dataframe(df.head())
    elif analysis_type == "Gender":
    
        st.title("Customer Gender Analysis")

 
        st.markdown("""
        ### Analyzing Customer Gender

        In this section, we visualize the distribution of customers by gender using a simple bar chart.
        """)


        gender_count = df["Customer Gender"].value_counts().reset_index()
        gender_count.columns = ["Customer Gender", "Count"]


        fig, ax = plt.subplots()
        ax.bar(gender_count["Customer Gender"], gender_count["Count"], color=["skyblue", "lightgreen"])
        ax.set_xlabel("Gender")
        ax.set_ylabel("Count")
        ax.set_title("Gender Count")
        plt.tight_layout()
        st.pyplot(fig)

        st.markdown("""
        > 🔍 **Observation:**  
        > The number of **male and female customers is nearly equal**, indicating a balanced gender distribution in the dataset.
        """)


        st.markdown("### Gender Count Table")
        st.dataframe(gender_count)
    
    elif analysis_type == "country":

        st.title("Sales Analysis by Country and State")

        st.markdown("""
        ### Total Sales Quantity by Country
        This chart shows which countries have the highest number of items sold.
        """)

        sum_quantity_per_country = df.groupby("Country")["Quantity"].sum().sort_values(ascending=False)
        fig1, ax1 = plt.subplots(figsize=(14, 7))
        ax1.bar(sum_quantity_per_country.index, sum_quantity_per_country.values, color='skyblue')
        ax1.set_xlabel("Country")
        ax1.set_ylabel("Total Quantity")
        ax1.set_title("Total Quantity of Sales per Country")
        plt.tight_layout()
        plt.xticks(rotation=90)
        st.pyplot(fig1)

        st.markdown("""
        ### Total Profit by Country
        This chart shows where the most profit is being generated from sales.
        """)

        sum_profit_per_country = df.groupby("Country")["profit"].sum().sort_values(ascending=False)
        fig2, ax2 = plt.subplots(figsize=(14, 7))
        ax2.bar(sum_profit_per_country.index, sum_profit_per_country.values, color='skyblue')
        ax2.set_xlabel("Country")
        ax2.set_ylabel("Total Profit")
        ax2.set_title("Total Profit of Sales per Country")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.ylim(0, 1000000)
        st.pyplot(fig2)

        st.markdown("### State-Level Sales Quantity in Top Countries")

        fig3, axes1 = plt.subplots(2, 2, figsize=(20, 10))
        axes1 = axes1.flatten()
        countries = ['United States', 'United Kingdom', 'Germany', 'France']

        for idx, country in enumerate(countries):
            ax = axes1[idx]
            state_quantity = df[df["Country"] == country].groupby("State")["Quantity"].sum().reset_index()
            ax.bar(state_quantity["State"], state_quantity["Quantity"], color='mediumseagreen')
            ax.set_xlabel(f"Sales in {country}")
            ax.set_ylabel("Total Quantity")
            ax.set_title(f"Sales Quantity in {country}")
            ax.tick_params(axis='x', rotation=85)
            plt.tight_layout()
            for j, v in enumerate(state_quantity["Quantity"]):
                ax.text(j, v + 0.1, str(int(v)), ha='center', va='bottom', fontsize=7)
        st.pyplot(fig3)

        st.markdown("### State-Level Profit in Top Countries")

        fig4, axes2 = plt.subplots(2, 2, figsize=(20, 7))
        axes2 = axes2.flatten()

        for idx, country in enumerate(countries):
            ax = axes2[idx]
            state_profit = df[df["Country"] == country].groupby("State")["profit"].sum().reset_index()
            ax.bar(state_profit["State"], state_profit["profit"], color='salmon')
            ax.set_xlabel(f"Sales in {country}")
            ax.set_ylabel("Total Profit")
            ax.set_title(f"Sales Profit in {country}")
            ax.tick_params(axis='x', rotation=85)
            plt.tight_layout()
            for j, v in enumerate(state_profit["profit"]):
                ax.text(j, v + 0.1, str(int(v)), ha='center', va='bottom', fontsize=7)
        st.pyplot(fig4)

        st.markdown("""
        > 🔍 **Observation:**  
        > The **United States** shows the highest total sales and profit among all countries.  
        > Within countries, certain states contribute significantly more than others to overall sales.
        """)
    elif analysis_type == "main_category":
   
        st.subheader("Total Quantity by Product Category")
        sum_quantity_per_subcategory = df.groupby("Product Category")["Quantity"].sum().sort_values(ascending=False)
        
        fig1, ax1 = plt.subplots(figsize=(14, 7))
        ax1.bar(sum_quantity_per_subcategory.index, sum_quantity_per_subcategory.values, color='skyblue')
        ax1.set_xlabel("Product Category")
        ax1.set_ylabel("Total Quantity")
        ax1.set_title("Total Quantity by Product Category")
        plt.xticks(rotation=90)
        plt.tight_layout()  
        st.pyplot(fig1)

        st.subheader("Profit Distribution (Percentage)")

        Accessories = df[df["Product Category"] == "Accessories"]["profit"].sum()
        Bikes = df[df["Product Category"] == "Bikes"]["profit"].sum()
        Clothing = df[df["Product Category"] == "Clothing"]["profit"].sum()
        
        categories = ["Accessories", "Bikes", "Clothing"]
        profits = [Accessories, Bikes, Clothing]
        
        fig2, ax2 = plt.subplots()
        ax2.pie(profits, labels=categories, autopct='%1.1f%%', startangle=140)
        ax2.set_title("Total Profit by Product Category")
        ax2.axis('equal')
        plt.tight_layout()  
        st.pyplot(fig2)

        st.markdown("**Observation:**")
        st.markdown("- Accessories: **61%**")
        st.markdown("- Bikes: **14.9%**")
        st.markdown("- Clothing: **24.1%**")

      
        st.subheader("Profit Distribution (Absolute Values)")

        def show_values(pct, all_vals):
            absolute = int(pct / 100. * sum(all_vals))
            return f"{absolute}"
        
        fig3, ax3 = plt.subplots()
        ax3.pie(
            profits,
            labels=categories,
            autopct=lambda pct: show_values(pct, profits),
            startangle=140
        )
        ax3.set_title("Total Profit by Product Category (Absolute Values)")
        ax3.axis('equal')
        plt.tight_layout() 
        st.pyplot(fig3)
    elif analysis_type == "sub_category":
       
        st.subheader("Profit by Sub Category (within each Product Category)")
        
        profit = df.groupby(["Product Category", "Sub Category"])["profit"].sum().reset_index()
        fig1, axes1 = plt.subplots(1, 3, figsize=(12, 5))
        axes1 = axes1.flatten()
        products = ['Bikes', 'Accessories', 'Clothing']
        
        for idx, product in enumerate(products):
            ax = axes1[idx]
            profit_product = profit[profit["Product Category"] == product][["Sub Category", "profit"]]
            ax.bar(profit_product["Sub Category"], profit_product["profit"])
            ax.set_xlabel(f"{product} Sub Categories")
            ax.set_ylabel("Profit")
            ax.set_title(f"Profit in {product}")
            ax.set_xticks(range(len(profit_product["Sub Category"])))
            ax.set_xticklabels(profit_product["Sub Category"], rotation=85, fontsize=7)
            

            for j, v in enumerate(profit_product["profit"]):
                ax.text(j, v + 1, str(int(v)), ha="center", va="bottom", fontsize=6)
        
        plt.tight_layout()
        st.pyplot(fig1)


        st.subheader("Total Profit by Sub Category")
        total_profit_by_subcategory = df.groupby("Sub Category")["profit"].sum().reset_index()
        total_profit_by_subcategory = total_profit_by_subcategory.sort_values(by="profit", ascending=False)
        
        fig2, ax2 = plt.subplots(figsize=(12, 6))
        ax2.bar(total_profit_by_subcategory["Sub Category"], total_profit_by_subcategory["profit"])
        ax2.set_xlabel("Sub Category")
        ax2.set_ylabel("Profit")
        ax2.set_title("Profit by Sub Category")
        plt.xticks(rotation=85)
        plt.tight_layout()
        st.pyplot(fig2)

        st.subheader("Quantity by Sub Category (within each Product Category)")
        
        quantity = df.groupby(["Product Category", "Sub Category"])["Quantity"].sum().reset_index()
        fig3, axes3 = plt.subplots(1, 3, figsize=(12, 5))
        axes3 = axes3.flatten()
        
        for idx, product in enumerate(products):
            ax = axes3[idx]
            quantity_product = quantity[quantity["Product Category"] == product][["Sub Category", "Quantity"]]
            ax.bar(quantity_product["Sub Category"], quantity_product["Quantity"])
            ax.set_xlabel(f"{product} Sub Categories")
            ax.set_ylabel("Quantity")
            ax.set_title(f"Quantity in {product}")
            ax.set_xticks(range(len(quantity_product["Sub Category"])))
            ax.set_xticklabels(quantity_product["Sub Category"], rotation=85, fontsize=7)
            
            for j, v in enumerate(quantity_product["Quantity"]):
                ax.text(j, v + 1, str(int(v)), ha="center", va="bottom", fontsize=6)
        
        plt.tight_layout()
        st.pyplot(fig3)


        st.subheader("Total Quantity by Sub Category")
        sum_quantity_per_subcategory = df.groupby("Sub Category")["Quantity"].sum().sort_values(ascending=False)
        
        fig4, ax4 = plt.subplots(figsize=(14, 7))
        ax4.bar(sum_quantity_per_subcategory.index, sum_quantity_per_subcategory.values, color='skyblue')
        ax4.set_xlabel("Sub Category")
        ax4.set_ylabel("Total Quantity")
        ax4.set_title("Total Quantity by Sub Category")
        plt.xticks(rotation=90)
        plt.tight_layout()
        st.pyplot(fig4)
    elif analysis_type == "country_product":
       
        st.subheader("Top Product Categories per Country")
        

        country_main = df[["Country", "Product Category"]].value_counts().reset_index(name="count")
        
        fig1, ax1 = plt.subplots(figsize=(14, 6))
        sns.barplot(
            data=country_main,
            x='Country',
            y='count',
            hue='Product Category',
            ax=ax1
        )
        ax1.set_title('Top Product Categories by Country')
        ax1.set_xlabel('Country')
        ax1.set_ylabel('Number of Purchases')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig1)

        st.subheader("Top Sub Categories per Country")
        country_sub = df[["Country", "Sub Category"]].value_counts().reset_index(name="count")
        
        fig2, ax2 = plt.subplots(figsize=(14, 6))
        sns.barplot(
            data=country_sub,
            x='Country',
            y='count',
            hue='Sub Category',
            ax=ax2
        )
        ax2.set_title('Top Sub Categories by Country')
        ax2.set_xlabel('Country')
        ax2.set_ylabel('Number of Purchases')
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig2)


        st.subheader("Top Product Categories per State")
        state_main = df[["State", "Product Category"]].value_counts().reset_index(name="count")
        
        fig3, ax3 = plt.subplots(figsize=(14, 8))
        sns.barplot(
            data=state_main,
            x='State',
            y='count',
            hue='Product Category',
            ax=ax3
        )
        ax3.set_title('Top Product Categories by State')
        ax3.set_xlabel('State')
        ax3.set_ylabel('Number of Purchases')
        plt.xticks(rotation=90)
        plt.tight_layout()
        st.pyplot(fig3)

     
        st.markdown("---")
        st.markdown("### 🧡 After all, you should know that:")
        st.markdown("**BY: OMAR SHOHIEB** 🎯")