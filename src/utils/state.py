import streamlit as st


def clear_cache():
    st.cache_data.clear()


def reset_session_state():
    st.session_state["question"] = None
