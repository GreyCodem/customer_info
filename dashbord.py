import streamlit as st
import pandas as pd
from db import fetch_customers


# ✅ Cached function to fetch and convert data

# @st.cache_data
def get_customer_df():
    data = fetch_customers()
    return pd.DataFrame(data, columns=["ID", "Name", "Number", "Location"])


# 🎯 Main dashboard display
def show():
    st.title("Customer Dashboard")

    # 🔽 Get the customer DataFrame
    df = get_customer_df()

    if not df.empty:
        st.subheader("All Customers")
        st.dataframe(df)

        st.subheader("Quick Stats")
        st.metric("Total Customers", len(df))

        st.subheader("Customers by Location")
        location_count = df["Location"].value_counts()
        st.bar_chart(location_count)

        # 🎯 Optional: search by name
        search = st.text_input("Search by Name")
        if search:
            result = df[df["Name"].str.contains(search, case=False)]
            st.write("Search Results:")
            st.dataframe(result)
    else:
        st.warning("No customer data found.")

