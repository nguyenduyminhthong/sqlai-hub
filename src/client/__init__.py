import streamlit as st

try:
    from database import ChromaDBAgent
except RuntimeError:
    st.error("You don't have access to the database. Please contact the administrator.")


@st.cache_resource
def create_client():
    return ChromaDBAgent(path=st.secrets["VECTOR_DB_PATH"], client_type="PersistentClient")


@st.cache_data(ttl=30)
def get_training_data(_database_client):
    return _database_client.get_training_data()
