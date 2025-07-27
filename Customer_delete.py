import streamlit as st
from db import get_connection, fetch_customers

def show():
    st.title("Delete Customer")

    data = fetch_customers()

    if data:
        st.subheader("ALL Customers:")
        st.table(
            [{"ID": row[0], "Name" :row[1], "Number": row[2],"Location":row[3]} for row in data]
        )

    if not data:
        st.warning("No customer found")
        return

    customer_names = [f"{row[0]} - {row[1]}" for row in data]
    selected = st.selectbox("Select customer to delete (You can search by ID)", customer_names,placeholder="example: 15-Alex")

    if st.button("Delete Selected Customer"):
        id_to_delete = int(selected.split(" - ")[0])
        customer_name = selected.split(" - ")[1]
        st.session_state.confirm_delete = {
            "id": id_to_delete,
            "name": customer_name
        }

    # Show confirmation popup if user triggered deletion
    if "confirm_delete" in st.session_state:
        customer_name = st.session_state.confirm_delete["name"]
        customer_id = st.session_state.confirm_delete["id"]

        st.warning(f"⚠️ Are you sure you want to delete **{customer_name}**?")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Confirm Delete"):
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("DELETE FROM customer_info WHERE id = %s", (customer_id,))
                conn.commit()
                cursor.close()
                conn.close()

                st.success(f"Customer **{customer_name}** deleted successfully.")
                del st.session_state.confirm_delete
                st.rerun()


        with col2:
            if st.button("Cancel"):
                st.info("Cancelled deletion.")
                del st.session_state.confirm_delete
