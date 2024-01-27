import requests
import streamlit as st


@st.cache_data
def submit_retreive_request(question):
    try:
        response = requests.post(
            f"{st.secrets['SERVER_HOST']}/retreive_query",
            json={
                "consumer_host": st.secrets["CONSUMER_HOST"],
                "package": {
                    "vector_db_host": st.secrets["VECTOR_DB_HOST"],
                    "llm_api_key": st.secrets["LLM_API_KEY"],
                    "question": question,
                },
            },
        )

        response.raise_for_status()

        return response.json()["sql"], None

    except Exception as e:
        return None, e


@st.cache_data
def submit_train_request(sql=None, question=None, ddl=None, doc=None):
    try:
        response = requests.post(
            f"{st.secrets['SERVER_HOST']}/train_model",
            json={
                "consumer_host": st.secrets["CONSUMER_HOST"],
                "package": {
                    "vector_db_host": st.secrets["VECTOR_DB_HOST"],
                    "sql": sql,
                    "question": question,
                    "ddl": ddl,
                    "doc": doc,
                },
            },
        )

        response.raise_for_status()

        return True, None

    except Exception as e:
        return False, e
