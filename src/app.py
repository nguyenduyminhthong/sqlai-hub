import streamlit as st
from code_editor import code_editor

from interface import submit_retreive_request, submit_train_request
from state import reset_session_state


st.set_page_config(layout="wide")


st.chat_message("assistant").write("How can I help you today?")

question = st.session_state.get("question", default=None)
if question is None:
    question = st.chat_input("Your question...")

if question:
    st.session_state["question"] = question

    st.chat_message("user").write(f"{question}")

    sql, e = submit_retreive_request(question)
    if sql is None:
        assistant = st.chat_message("assistant")
        assistant.error(e)
        assistant.button("New chat", on_click=reset_session_state)

    else:
        assistant = st.chat_message("assistant")
        assistant.code(sql, language="sql", line_numbers=True)
        st.button("New chat", on_click=reset_session_state)

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
            success, e = submit_train_request(fixed_sql, question)
            if success:
                assistant.write("Model trained successfully!")
            else:
                assistant.error(e)
