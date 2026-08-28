import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state
from utils import content

st.set_page_config(page_title="Feedback", page_icon="✉️", layout="wide")
init_state()

st.title("✉️ Feedback")
st.write(content.FEEDBACK_INTRO)

st.session_state.feedback_notes = st.text_area(
    "Notes for next time", value=st.session_state.feedback_notes, height=200
)
