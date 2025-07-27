import streamlit as st
from db import get_connection
def show():
    st.title("Add New Customer")
    
    col = st.columns(1)[0]

    with col:
        name = st.text_input("Name:")
        number = st.text_input("Number:")
        location = st.text_input("Location:")
        
    if st.button("Save"):
        if name and location:
            conn = get_connection()
            if conn:
                cursor = conn.cursor()
                sql = "INSERT INTO customer_info (name, number, location) VALUES (%s,%s,%s)"
                cursor.execute(sql, (name,number,location))
                conn.commit()
                cursor.close()
                conn.close()
                st.success("Successfully Added")
            else:
                st.warning("Fill all columns.")