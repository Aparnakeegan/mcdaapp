import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state
from utils import content

st.set_page_config(page_title="Discussion", page_icon="🗣️", layout="wide")
init_state()

st.title("🗣️ Recommend — Discuss Process (optional)")
st.write(content.DISCUSSION_INTRO)

for i, q in enumerate(content.DISCUSSION_QUESTIONS, start=1):
    st.session_state.discussion.setdefault(q, "")
    st.session_state.discussion[q] = st.text_area(
        f"{i}. {q}", value=st.session_state.discussion[q], key=f"disc_{i}", height=80
    )
