import streamlit as st
from database import ChromaDBAgent


@st.cache_resource
def create_client():
    return ChromaDBAgent(st.secrets["VECTOR_DB_PATH"])

@st.cache_data(ttl=30)
def get_training_data(_database_client):
    return _database_client.get_training_data()
