import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import (
    init_state, programme_names, compute_scenario, priority_points_summary, save_scenario,
)
from utils import content

st.set_page_config(page_title="Scenario Modelling", page_icon="🔀", layout="wide")
init_state()

st.title("🔀 Recommend — Model Scenarios (optional)")
st.markdown(content.SCENARIO_GUIDANCE)
st.divider()

names = programme_names()
if not names:
    st.info("Add programme areas on the Define Scope page first.")
else:
    st.subheader("Set up a scenario")
    inputs = st.session_state.scenario_inputs
    for p in names:
        cfg = inputs.setdefault(p, {"direction": "No change", "adjust_pct": 0, "pre_agreed": None})
        with st.container(border=True):
            st.markdown(f"**{p}**")
            c1, c2, c3 = st.columns(3)
            with c1:
                cfg["direction"] = st.selectbox(
                    "Spend recommendation", ["No change", "Increase", "Decrease"],
                    index=["No change", "Increase", "Decrease"].index(cfg["direction"]),
                    key=f"scen_dir_{p}",
                )
            with c2:
                cfg["adjust_pct"] = st.slider(
                    "% of budget to adjust using prioritisation score", 0, 100,
                    int(cfg["adjust_pct"]), key=f"scen_pct_{p}",
                )
            with c3:
                cfg["pre_agreed"] = st.number_input(
                    "Pre-agreed amount (overrides calc, +/-)", value=float(cfg["pre_agreed"] or 0),
                    key=f"scen_pre_{p}",
                )

    scenario_df = compute_scenario(inputs)
    st.divider()
    st.subheader("Revised budget")
    st.dataframe(scenario_df, use_container_width=True, hide_index=True)

    result = priority_points_summary(scenario_df)
    if result:
        detail_df, summary = result
        st.subheader("Priority points & added value")
        m1, m2, m3 = st.columns(3)
        m1.metric("Prioritisation priority points", f"{summary['total_prioritisation_points']:.0f}")
        m2.metric("Equal proportion priority points", f"{summary['total_equal_proportion_points']:.0f}")
        m3.metric("Added value (€)", f"{summary['added_value']:,.0f}")
        st.caption(
            "Added value represents the extra value achieved for the same money — "
            "not cash savings."
        )
        chart_data = scenario_df.set_index("Programme area")[
            ["Original budget", "Prioritisation budget", "Equal proportion budget"]
        ]
        st.bar_chart(chart_data)

    st.divider()
    st.subheader("Save this scenario")
    c1, c2 = st.columns([3, 1])
    with c1:
        scenario_name = st.text_input("Scenario name", value=f"Scenario {len(st.session_state.scenarios) + 1}")
    with c2:
        st.write("")
        if st.button("💾 Save scenario", use_container_width=True):
            import copy
            if save_scenario(scenario_name, copy.deepcopy(inputs)):
                st.success(f"Saved '{scenario_name}'. View it on the Compare Scenarios page.")
            else:
                st.error("You can save up to 5 scenarios. Delete one on the Compare Scenarios page first.")
