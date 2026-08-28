import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state
from utils import content

st.set_page_config(page_title="Communicate", page_icon="📣", layout="wide")
init_state()

st.title("📣 Step 6 — Communicate")
st.markdown(content.COMMUNICATE_GUIDANCE)
