import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state
from utils import content

st.set_page_config(page_title="Resources", page_icon="🔗", layout="wide")
init_state()

st.title("🔗 Resources")
st.write(
    "This page presents a list of resources that can be used throughout the "
    "prioritisation process to collect evidence and data for both Potential "
    "and Current scoring."
)

for name, desc, url in content.RESOURCES:
    with st.container(border=True):
        st.markdown(f"**{name}**")
        st.write(desc)
        if url:
            st.markdown(f"[{url}]({url})")
