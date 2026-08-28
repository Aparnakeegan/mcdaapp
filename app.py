import streamlit as st
import sys, os

sys.path.append(os.path.dirname(__file__))
from utils.state import init_state, export_project_json, import_project_json
from utils import content

st.set_page_config(
    page_title="Population Based Planning Prioritisation Tool",
    page_icon="🧭",
    layout="wide",
)

init_state()

st.title("🧭 Population Based Planning Prioritisation Tool")
st.caption(
    "An interactive, Streamlit-based version of the Prioritisation Framework "
    "(Multi-Criteria Decision Analysis) -- covering the full walkthrough from "
    "Initiate through to Communicate."
)

with st.sidebar:
    st.header("Project")
    st.session_state.project_name = st.text_input(
        "Project name", value=st.session_state.project_name
    )

    st.divider()
    st.subheader("💾 Save / load project")
    st.download_button(
        "⬇️ Download project (.json)",
        data=export_project_json(),
        file_name=f"{st.session_state.project_name.replace(' ', '_')}.json",
        mime="application/json",
        use_container_width=True,
    )
    uploaded = st.file_uploader("⬆️ Load project (.json)", type=["json"])
    if uploaded is not None:
        if st.button("Load into session", use_container_width=True):
            import_project_json(uploaded.read().decode("utf-8"))
            st.success("Project loaded. Use the pages on the left to review it.")
            st.rerun()

    st.divider()
    st.caption(
        "Data is stored in your browser session only. Use Save/Load to keep a "
        "copy between visits, or before the app restarts."
    )

st.markdown(content.INTRODUCTION)

st.subheader("The six stages of the process")
cols = st.columns(3)
for i, (title, desc) in enumerate(content.OVERVIEW_STEPS):
    with cols[i % 3]:
        st.markdown(f"**{title}**")
        st.write(desc)

st.divider()
st.info(
    "👈 Use the page navigation in the sidebar to move through the tool: "
    "**Glossary**, **Resources**, **Initiate**, **Define Scope**, **Create Plan**, "
    "**Prioritise Guidance**, **Potential Scores**, **Current Scores**, "
    "**Provide Rationale**, **Scenario Modelling**, **Compare Scenarios**, "
    "**Discussion**, **Communicate**, **Dashboard**, **Feedback**, and "
    "**Terms & Acknowledgements**."
)

st.subheader("Quick status")
n_prog = len(st.session_state.programme_areas)
n_crit = sum(len(c["criteria"]) for c in st.session_state.categories)
c1, c2, c3 = st.columns(3)
c1.metric("Programme areas defined", n_prog)
c2.metric("Criteria defined", n_crit)
c3.metric("Saved scenarios", len(st.session_state.scenarios))
