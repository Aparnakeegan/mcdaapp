import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import (
    init_state, programme_names, get_current, set_current, current_scores_table,
)
from utils import content

st.set_page_config(page_title="Current Scores", page_icon="📊", layout="wide")
init_state()

st.title("📊 Prioritise — Current Scores")

tab_guide, tab_evidence, tab_scores, tab_results = st.tabs(
    ["Guidance", "Evidence", "Assign scores", "Results"]
)

with tab_guide:
    st.markdown(content.CURRENT_GUIDANCE)
    st.divider()
    st.markdown(content.CURRENT_SCORING_TEXT)
    st.table({
        "": ["Investment", "Outcome", "Feasibility", "Score"],
        "Very Low / Very High": ["Very High", "Very Poor", "Very Low", 1],
        "Low / Poor": ["High", "Poor", "Low", 2],
        "Similar": ["Similar", "Similar", "Similar", 3],
        "Good / High": ["Low", "Good", "High", 4],
        "Very Good / Very Low": ["Very Low", "Very Good", "Very High", 5],
    })

with tab_evidence:
    st.markdown(content.CURRENT_EVIDENCE_TEXT)
    st.divider()
    names = programme_names()
    if not names:
        st.info("Add programme areas on the Define Scope page first.")
    for p in names:
        st.session_state.current_evidence.setdefault(p, "")
        st.session_state.current_evidence[p] = st.text_area(
            f"Evidence summary — {p}", value=st.session_state.current_evidence[p],
            key=f"cur_evidence_{p}", height=100
        )

with tab_scores:
    names = programme_names()
    if not names:
        st.info("Add programme areas on the Define Scope page first.")
    for p in names:
        st.markdown(f"**{p}**")
        c1, c2, c3 = st.columns(3)
        cur = get_current(p)
        with c1:
            inv = st.slider("Investment score (1=very high spend, 5=very low spend)",
                             1, 5, int(cur.get("investment", 3)), key=f"inv_{p}")
            set_current(p, "investment", inv)
        with c2:
            out = st.slider("Outcome score (1=very poor, 5=very good)",
                             1, 5, int(cur.get("outcome", 3)), key=f"out_{p}")
            set_current(p, "outcome", out)
        with c3:
            feas = st.slider("Feasibility score (1=very low, 5=very high)",
                              1, 5, int(cur.get("feasibility", 3)), key=f"feas_{p}")
            set_current(p, "feasibility", feas)

    st.divider()
    st.subheader("Rationale")
    for p in names:
        st.session_state.current_rationale.setdefault(p, "")
        st.session_state.current_rationale[p] = st.text_area(
            f"Rationale for scores — {p}", value=st.session_state.current_rationale[p],
            key=f"cur_rationale_{p}", height=80
        )

with tab_results:
    df = current_scores_table()
    if df.empty:
        st.info("Add programme areas to see results here.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)
