import streamlit as st
import pandas as pd
import os
from webScrap import fetch_daily_data

def show():
    st.title("🟡 Today's Egg Prices")

    if st.button("🔁 Fetch Latest Data"):
        with st.spinner("Scraping website..."):
            df = fetch_daily_data()
            if df is not None:
                st.success("✅ Data fetched and saved successfully!")
            else:
                st.error("❌ Failed to fetch data.")
    
    # Display data from CSV if it exists
    if os.path.exists("egg_prices_today.csv"):
        df = pd.read_csv("egg_prices_today.csv")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No data found. Please click the button above to fetch data.")
