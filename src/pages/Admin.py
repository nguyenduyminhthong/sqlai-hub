import streamlit as st

try:
    from client import add_ddl, add_doc, create_client, get_training_data, remove_training_data
    from utils import clear_cache, reset_session_state

    reset_session_state()
    st.set_page_config(page_title="Admin", layout="wide")
    st.sidebar.button("Refresh Program", on_click=clear_cache)

    database_client = create_client()

    df = get_training_data(database_client)
    df_sorted = df.sort_values(by="time_created", ascending=False)

    st.dataframe(df_sorted, use_container_width=True)

    st.markdown(f"Enter :green[ID] below to remove the training data from the database.")
    id = st.text_input("ID")
    if id:
        success = remove_training_data(database_client, id)
        if success:
            st.success(f"Successfully removed training data with ID: {id}")
        else:
            st.error(f"Failed to remove training data with ID: {id}")

    st.markdown(f"Enter :green[DDL] below to train the model about structure of tables and other objects in the database.")
    ddl = st.text_input("DDL")
    if ddl:
        add_ddl(database_client, ddl)
        st.success(f"Successfully added DDL.")

    st.markdown(f"Enter :green[Document] below to train the model about the meaning of the data in the database.")
    doc = st.text_input("Document")
    if doc:
        add_doc(database_client, doc)
        st.success(f"Successfully added Document.")

except Exception as e:
    st.error("You don't have access to the database. Please contact the administrator.")
