import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import (
    init_state, programme_names, weighted_potential_score, current_total,
    normalised_current_score, get_current, get_recommendation, set_recommendation,
    get_rationale_text, set_rationale_text,
)
from utils import content

st.set_page_config(page_title="Provide Rationale", page_icon="💬", layout="wide")
init_state()

st.title("💬 Recommend — Provide Rationale")
st.markdown(content.RECOMMEND_GUIDANCE)
st.divider()
st.markdown(content.PROVIDE_RATIONALE_TEXT)

names = programme_names()
if not names:
    st.info("Add programme areas on the Define Scope page first.")
else:
    rows = []
    for p in names:
        rows.append({
            "Programme area": p,
            "Potential score (/100)": weighted_potential_score(p),
            "Current total (2-10)": current_total(p),
            "Feasibility score (1-5)": get_current(p).get("feasibility"),
            "Recommendation": get_recommendation(p),
        })
    st.dataframe(rows, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("Make recommendations and capture rationale")
    for p in names:
        with st.container(border=True):
            st.markdown(f"**{p}**")
            c1, c2 = st.columns([1, 3])
            with c1:
                rec = st.selectbox(
                    "Spend recommendation", ["Not yet set", "Increase", "Decrease", "No change"],
                    index=["Not yet set", "Increase", "Decrease", "No change"].index(
                        get_recommendation(p) if get_recommendation(p) in
                        ["Not yet set", "Increase", "Decrease", "No change"] else "Not yet set"
                    ),
                    key=f"rec_{p}",
                )
                set_recommendation(p, rec)
            with c2:
                text = st.text_area(
                    "Rationale for this recommendation", value=get_rationale_text(p),
                    key=f"rationale_{p}", height=90
                )
                set_rationale_text(p, text)
