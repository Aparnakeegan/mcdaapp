import streamlit as st
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state, compute_scenario, priority_points_summary

st.set_page_config(page_title="Compare Scenarios", page_icon="📉", layout="wide")
init_state()

st.title("📉 Recommend — Compare Scenarios")
st.write("Compare your saved scenarios (up to 5) side by side.")

scenarios = st.session_state.scenarios
if not scenarios:
    st.info("No scenarios saved yet. Build and save one on the Scenario Modelling page.")
else:
    summary_rows = []
    budget_frames = {}
    for s in scenarios:
        df = compute_scenario(s["inputs"])
        result = priority_points_summary(df)
        budget_frames[s["name"]] = df.set_index("Programme area")["Prioritisation budget"]
        if result:
            _, summary = result
            summary_rows.append({
                "Scenario": s["name"],
                "Total prioritisation budget": round(summary["total_prioritisation_budget"], 2),
                "Total priority points": round(summary["total_prioritisation_points"], 1),
                "Equal proportion priority points": round(summary["total_equal_proportion_points"], 1),
                "Added value (€)": round(summary["added_value"], 2),
            })

    st.subheader("Scenario summary")
    st.dataframe(pd.DataFrame(summary_rows), use_container_width=True, hide_index=True)

    st.subheader("Prioritisation budget by programme area")
    compare_df = pd.DataFrame(budget_frames)
    st.bar_chart(compare_df)

    st.divider()
    st.subheader("Manage saved scenarios")
    for i, s in enumerate(scenarios):
        c1, c2 = st.columns([4, 1])
        with c1:
            st.write(f"**{s['name']}**")
        with c2:
            if st.button("🗑 Delete", key=f"del_scenario_{i}"):
                st.session_state.scenarios.pop(i)
                st.rerun()
