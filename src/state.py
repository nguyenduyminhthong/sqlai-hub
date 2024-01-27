import streamlit as st


def reset_session_state():
    st.session_state["question"] = None
