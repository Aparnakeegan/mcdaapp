import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state
from utils import content

st.set_page_config(page_title="Terms & Acknowledgements", page_icon="📄", layout="wide")
init_state()

st.title("📄 Terms & Acknowledgements")

st.subheader("Terms")
st.markdown(content.TERMS_TEXT)

st.divider()
st.subheader("Acknowledgements")
st.markdown(content.ACKNOWLEDGEMENTS_TEXT)
