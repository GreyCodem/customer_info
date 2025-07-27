import streamlit as st
from db import fetch_dealers, get_connection,fetch_price

def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def show():
    st.title("Dealer List")
    data_info = fetch_dealers()
    data_price = fetch_price()

    if not data_info:
        st.warning("NO Dealer found")
        
    
    col1, col2 = st.columns(2)

    
    with col1:
        if data_info:
            st.subheader("ALL Dealers")
            st.table(
                [{"ID": row[0], "Name" :row[1], "Contact Number": row[2]} for row in data_info]
            )
    with col2:
        if data_price:
            st.subheader("Regular Price")
            st.table(
                [{"ID": row[0], "Name" :row[1], "Date": row[2],"Price": row[3]} for row in data_price]
            )

    if "show_new_dealer" not in st.session_state:
        st.session_state["show_new_dealer"] = False
    if "show_update_price" not in st.session_state:
        st.session_state["show_update_price"] = False
    if "show_edit" not in st.session_state:
        st.session_state["show_edit"] = False
    if "show_delete" not in st.session_state:
        st.session_state["show_delete"] = False

    col1,col2,col3,col4 = st.columns(4)
    with col1:
        if st.button("New Dealer"):
            st.session_state["show_new_dealer"] = True
            st.session_state["show_update_price"] = False
            st.session_state["show_edit"] = False
            st.session_state["show_delete"] = False
    with col2:
        if st.button("Update Price"):
            st.session_state["show_new_dealer"] = False
            st.session_state["show_update_price"] = True
            st.session_state["show_edit"] = False
            st.session_state["show_delete"] = False
    with col3:
        if st.button("Edit"):
            st.session_state["show_new_dealer"] = False
            st.session_state["show_update_price"] = False
            st.session_state["show_edit"] = True
            st.session_state["show_delete"] = False
    with col4:
        if st.button("Delete"):
            st.session_state["show_new_dealer"] = False
            st.session_state["show_update_price"] = False
            st.session_state["show_edit"] = False
            st.session_state["show_delete"] = True

#Add new dealers
    if st.session_state["show_new_dealer"]:
        col,col1 = st.columns(2)
        with col:
            name = st.text_input("Name:",key="new_dealer_name")
        with col1:
            phnumber = st.text_input("Contact Number:",key="new_dealer_phonenumber",value=None)
    
        with col:
            if st.button("save"):
                if name and is_valid_phone(phnumber):
                    conn = get_connection()
                    if conn:

                        phnumber = int(phnumber) if int(phnumber) else None
                        cursor = conn.cursor()
                        sql = "INSERT INTO dealer_info (name, ph) VALUES(%s,%s)"
                        
                        cursor.execute(sql,(name, phnumber))
                        conn.commit()
                        cursor.close()
                        conn.close()
                        
                        st.success("Successfully Added...")
                        st.session_state["show_new_dealer"] = False
                        st.session_state["show_update_price"] = ""
                        st.session_state["show_edit"] = ""
                        
                    else:
                        st.warning("Fill all fields..")
                else:
                    st.warning("Wrong Entry. Try again...")
                st.rerun()

        with col1:
            close_clicked = st.button("Close")
            if close_clicked:
                st.session_state["show_new_dealer"] = False
                st.session_state["show_update_price"] = False
                st.session_state["show_edit"] = False
                st.rerun()



# update dealer selling price
    if st.session_state["show_update_price"]:
        col1,col2 = st.columns(2)
        with col1:
            dealer_names = [f"{row[0]}-{row[1]}" for row in data_info ]
            selected = st.selectbox("Select Dealer", dealer_names,placeholder="Search by ID")
            if selected:
                id = int(selected.split("-")[0])
                name = selected.split("-")[1]
        with col2:
            date = st.date_input("Date")
        with col1:
            st.text_input("Name",name,disabled=True)
        with col2:
            price = st.number_input("Price",value=None)

        if not(id and date and price):
            st.warning("Fill all..")

            
        if st.button("save"):
            if name:
                conn = get_connection()
                if conn:
                    cursor = conn.cursor()
                    sql = "INSERT into dealer_price (id,name,date,price) VALUES(%s,%s,%s,%s)"
                    cursor.execute(sql,(id,name,date,price))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    st.success("Successfully Added...")
                else:
                    st.warning("Fill all fields..")


    if st.session_state["show_edit"]:
        st.warning("Do something")

    if st.session_state["show_delete"]:
        st.warning("do something")