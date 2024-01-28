import streamlit as st
from code_editor import code_editor

from interface import retreive_sql, train_model
from utils import clear_cache, reset_session_state


st.set_page_config(page_title="Chat", layout="wide")
st.sidebar.button("Refresh Program", on_click=clear_cache)


st.chat_message("assistant").write("How can I help you today?")

question = st.session_state.get("question", default=None)
if question is None:
    question = st.chat_input("Your question...")

if question:
    st.session_state["question"] = question
    st.chat_message("user").write(f"{question}")

    assistant = st.chat_message("assistant")
    sql, e = retreive_sql(question)
    if sql is not None:
        assistant = st.chat_message("assistant")
        assistant.code(sql, language="sql", line_numbers=True)

        sql_feedback = assistant.radio("Is this SQL query correct?", ["...", "Yes", "No"])

        fixed_sql = None
        if sql_feedback == "Yes":
            fixed_sql = sql
        elif sql_feedback == "No":
            assistant.write("Please modify the generated SQL query:")
            with assistant:
                sql_editor = code_editor(sql, lang="sql")
                fixed_sql = sql_editor["text"]

        if fixed_sql:
            success, e = train_model(fixed_sql, question)
            if success:
                assistant.write("Model trained successfully!")
            else:
                assistant.error(e)
    else:
        assistant.error(e)

    assistant.button("New chat", on_click=reset_session_state)
