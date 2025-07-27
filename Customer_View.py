import streamlit as st
from db import fetch_customers

def show():
    st.title("Customer List")
    data = fetch_customers()

    if data:
        st.subheader("ALL Customer")
        st.table(
            [{"ID": row[0], "Name" :row[1], "Number": row[2],"location":row[3]} for row in data]
        )