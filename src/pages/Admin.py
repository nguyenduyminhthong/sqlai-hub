import streamlit as st

try:
    from client import create_client, get_training_data
    from utils import clear_cache


    st.set_page_config(page_title="Admin")
    st.sidebar.button("Refresh Program", on_click=clear_cache)

    database_client = create_client()

    df = get_training_data(database_client)

    st.dataframe(df)
except:
    st.error("You don't have access to the database. Please contact the administrator.")
