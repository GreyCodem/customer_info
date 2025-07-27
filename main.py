import streamlit as st
from streamlit_option_menu import option_menu
import dashbord
import Customer_Add
import Customer_View
import Customer_delete
import regular_rate
import Dealer_info

# Set page layout
st.set_page_config(
    page_title="Customer Management Dashboard",
    page_icon="📊",
    layout="wide"
)

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu",
        ["Dashbord","Dealer details", "Add Customer", "View", "Delete Customer", "Regular rate"],
        icons=['bar-chart', 'person-plus', 'people', 'person-x', 'clock'],
        menu_icon="cast",
        default_index=0,
    )

# Load the selected page
if selected == "Dashbord":
    dashbord.show()

elif selected == "Dealer details":
    Dealer_info.show()

elif selected == "Add Customer":
    Customer_Add.show()

elif selected == "View":
    Customer_View.show()

elif selected == "Delete Customer":
    Customer_delete.show()

elif selected == "Regular rate":
    regular_rate.show()
