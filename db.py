import streamlit as st
import mysql.connector

db_config = {
    "host" : "localhost",
    "user" : "root",
    "password" : "7439",
    "database" : "customer_management",
    "port": 3306
}

def get_connection():
    try:
        # conn = mysql.connector.connect(
        #     host = "127.0.0.1",
        #     user = "root",
        #     password = "7439",
        #     database = "customer_management"
        # )
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as e:
        st.error(f"Connection Error: {e}")
        return None


def fetch_customers():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customer_info")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    else:
        return []

def fetch_dealers():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dealer_info")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    else:
        return []
    
def fetch_price():
    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dealer_price")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data
    else:
        return []