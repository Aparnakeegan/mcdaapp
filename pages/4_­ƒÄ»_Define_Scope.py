import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state, add_programme_area, remove_programme_area
from utils import content

st.set_page_config(page_title="Define Scope", page_icon="🎯", layout="wide")
init_state()

st.title("🎯 Step 2 — Define Scope")
st.write(
    "Deciding what is in and out of scope through discussion with senior stakeholders "
    "is a critical first step in the prioritisation process. Capture the project scope "
    "below."
)

scope = st.session_state.project_scope

with st.expander("Project scope", expanded=True):
    scope["background"] = st.text_area(
        "Background / current state", value=scope["background"],
        help=content.DEFINE_SCOPE_FIELD_HELP["background"], height=100)
    scope["objectives"] = st.text_area(
        "Objectives / desired state", value=scope["objectives"],
        help=content.DEFINE_SCOPE_FIELD_HELP["objectives"], height=100)
    scope["exclusions"] = st.text_area(
        "Exclusions", value=scope["exclusions"],
        help=content.DEFINE_SCOPE_FIELD_HELP["exclusions"], height=80)
    col1, col2 = st.columns(2)
    with col1:
        scope["outputs"] = st.text_area(
            "Expected outputs", value=scope["outputs"],
            help=content.DEFINE_SCOPE_FIELD_HELP["outputs"], height=80)
        scope["restrictions"] = st.text_area(
            "Restrictions", value=scope["restrictions"],
            help=content.DEFINE_SCOPE_FIELD_HELP["restrictions"], height=80)
        scope["assumptions"] = st.text_area(
            "Assumptions", value=scope["assumptions"],
            help=content.DEFINE_SCOPE_FIELD_HELP["assumptions"], height=80)
        scope["roles"] = st.text_area(
            "Roles and responsibilities", value=scope["roles"],
            help=content.DEFINE_SCOPE_FIELD_HELP["roles"], height=80)
    with col2:
        scope["outcomes"] = st.text_area(
            "Expected outcomes / impact", value=scope["outcomes"],
            help=content.DEFINE_SCOPE_FIELD_HELP["outcomes"], height=80)
        scope["dependencies"] = st.text_area(
            "Dependencies", value=scope["dependencies"],
            help=content.DEFINE_SCOPE_FIELD_HELP["dependencies"], height=80)
        scope["risks"] = st.text_area(
            "Risks", value=scope["risks"],
            help=content.DEFINE_SCOPE_FIELD_HELP["risks"], height=80)
        scope["additional_info"] = st.text_area(
            "Additional information", value=scope["additional_info"],
            help=content.DEFINE_SCOPE_FIELD_HELP["additional_info"], height=80)

    scope["stakeholder_plan"] = st.text_area(
        "Stakeholder engagement plan", value=scope["stakeholder_plan"],
        help=content.DEFINE_SCOPE_FIELD_HELP["stakeholder_plan"], height=80)
    scope["communication_plan"] = st.text_area(
        "Communication plan", value=scope["communication_plan"],
        help=content.DEFINE_SCOPE_FIELD_HELP["communication_plan"], height=80)

st.divider()
st.subheader("Programme areas to be evaluated")
st.write(
    "List out all programme areas you wish to include in the prioritisation analysis, "
    "and the current investment in each."
)

for i, p in enumerate(st.session_state.programme_areas):
    c1, c2, c3 = st.columns([3, 2, 1])
    with c1:
        st.text_input("Programme area", value=p["name"], key=f"pa_name_{i}", disabled=True)
    with c2:
        new_spend = st.number_input(
            "Current spend (€)", value=float(p.get("current_spend", 0)),
            key=f"pa_spend_{i}", step=1000.0, min_value=0.0
        )
        st.session_state.programme_areas[i]["current_spend"] = new_spend
    with c3:
        st.write("")
        st.write("")
        if st.button("Remove", key=f"pa_remove_{i}"):
            remove_programme_area(p["name"])
            st.rerun()

st.markdown("**Add a new programme area**")
c1, c2, c3 = st.columns([3, 2, 1])
with c1:
    new_name = st.text_input("Name", key="new_pa_name", label_visibility="collapsed",
                              placeholder="e.g. Sexual Health Services")
with c2:
    new_spend = st.number_input("Current spend (€)", key="new_pa_spend",
                                 label_visibility="collapsed", min_value=0.0, step=1000.0)
with c3:
    if st.button("➕ Add", use_container_width=True):
        add_programme_area(new_name, new_spend)
        st.rerun()
