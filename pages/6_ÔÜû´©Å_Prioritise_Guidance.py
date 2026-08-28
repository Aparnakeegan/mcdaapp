import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state
from utils import content

st.set_page_config(page_title="Prioritise Guidance", page_icon="⚖️", layout="wide")
init_state()

st.title("⚖️ Step 4 — Prioritise: Guidance")
st.markdown(content.PRIORITISE_GUIDANCE)

st.divider()
st.subheader("Table: Potential and Current scores")
st.table({
    "": ["What it captures", "Represents", "Typical evidence sources"],
    "Potential score": [
        "Scoring programme areas against weighted criteria, using MCDA",
        "The potential outcome each programme area could have for different "
        "criteria, if it performed at its best",
        "Health economics evidence resources, Fingertips, local analysis",
    ],
    "Current score": [
        "Scoring the current situation per programme area, in terms of "
        "investment and outcomes, by benchmarking to other areas. A "
        "feasibility score is also generated.",
        "Current status of each programme area, relative to comparable areas, "
        "and the feasibility of reaching its potential",
        "SPOT, insight from local leads",
    ],
})
