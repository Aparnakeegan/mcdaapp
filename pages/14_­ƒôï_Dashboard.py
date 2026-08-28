import streamlit as st
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import (
    init_state, programme_names, weighted_potential_score, normalised_current_score,
    normalised_feasibility_score, get_recommendation, get_rationale_text,
)

st.set_page_config(page_title="Dashboard", page_icon="📋", layout="wide")
init_state()

st.title("📋 Dashboard")
st.write("This page shows a review of the key findings of the prioritisation analysis.")

names = programme_names()
spend_map = {p["name"]: p.get("current_spend", 0) for p in st.session_state.programme_areas}

if not names:
    st.info("Add programme areas on the Define Scope page to populate the dashboard.")
else:
    rows = []
    total_spend = sum(spend_map.values()) or 1
    for p in names:
        rows.append({
            "Programme area": p,
            "Potential score": weighted_potential_score(p),
            "Current score": normalised_current_score(p),
            "Feasibility score": normalised_feasibility_score(p),
            "Spend recommendation": get_recommendation(p),
            "Current spend": spend_map.get(p, 0),
            "% of total spend": round(spend_map.get(p, 0) / total_spend * 100, 1),
            "Rationale": get_rationale_text(p),
        })
    df = pd.DataFrame(rows)
    st.dataframe(df, use_container_width=True, hide_index=True)

    st.divider()
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Potential vs Current score")
        chart_df = df.set_index("Programme area")[["Potential score", "Current score"]].dropna(how="all")
        if not chart_df.empty:
            st.bar_chart(chart_df)
    with c2:
        st.subheader("Current spend split")
        spend_df = df.set_index("Programme area")[["Current spend"]]
        st.bar_chart(spend_df)

    st.divider()
    st.subheader("Recommendations at a glance")
    for _, r in df.iterrows():
        icon = {"Increase": "🔼", "Decrease": "🔽", "No change": "➡️"}.get(
            r["Spend recommendation"], "⏳"
        )
        with st.container(border=True):
            st.markdown(f"**{icon} {r['Programme area']}** — {r['Spend recommendation']}")
            cols = st.columns(3)
            cols[0].metric("Potential", r["Potential score"] if r["Potential score"] is not None else "—")
            cols[1].metric("Current", r["Current score"] if r["Current score"] is not None else "—")
            cols[2].metric("Feasibility", r["Feasibility score"] if r["Feasibility score"] is not None else "—")
            if r["Rationale"]:
                st.caption(r["Rationale"])
