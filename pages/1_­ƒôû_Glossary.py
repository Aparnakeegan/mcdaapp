import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state
from utils import content

st.set_page_config(page_title="Glossary", page_icon="📖", layout="wide")
init_state()

st.title("📖 Glossary")
st.caption("Key terms used throughout the Population Based Planning Prioritisation Tool.")

search = st.text_input("Filter terms", "")

for term, definition in content.GLOSSARY:
    if search and search.lower() not in term.lower() and search.lower() not in definition.lower():
        continue
    with st.expander(term):
        st.write(definition)
