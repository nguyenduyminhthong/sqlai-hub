import streamlit as st
from database import ChromaDBAgent


@st.cache_resource
def create_client():
    return ChromaDBAgent(path=st.secrets["VECTOR_DB_PATH"], client_type="PersistentClient")


@st.cache_data(ttl=30)
def get_training_data(_database_client):
    return _database_client.get_training_data()


@st.cache_data(ttl=30)
def remove_training_data(_database_client, id):
    return _database_client.remove_training_data(id)


@st.cache_data(ttl=30)
def add_ddl(_database_client, ddl):
    return _database_client.add_ddl(ddl)


@st.cache_data(ttl=30)
def add_doc(_database_client, doc):
    return _database_client.add_doc(doc)
