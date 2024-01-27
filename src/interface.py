import requests
import streamlit as st


def submit_retreive_request(assistant, question):
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

        generated_sql = response.json()["sql"]
        assistant.write(generated_sql)

        return generated_sql

    except Exception as e:
        assistant.error(e)


def submit_train_request(assistant, sql=None, question=None, ddl=None, doc=None):
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
        assistant.write("Model trained successfully!")

    except Exception as e:
        assistant.error(e)
