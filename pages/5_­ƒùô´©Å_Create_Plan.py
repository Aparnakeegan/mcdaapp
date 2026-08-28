import streamlit as st
import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import init_state
from utils import content

st.set_page_config(page_title="Create Plan", page_icon="🗓️", layout="wide")
init_state()

st.title("🗓️ Step 3 — Create Plan")
st.write(content.CREATE_PLAN_INTRO)

if st.session_state.plan_tasks is None:
    st.session_state.plan_tasks = [
        {"Activity": t, "Owner": "", "Start date": None, "End date": None,
         "% complete": 0, "Status": "Not started"}
        for t in content.DEFAULT_PLAN_TASKS
    ]

df = pd.DataFrame(st.session_state.plan_tasks)

edited = st.data_editor(
    df,
    num_rows="dynamic",
    use_container_width=True,
    column_config={
        "% complete": st.column_config.ProgressColumn(
            "% complete", min_value=0, max_value=100, format="%d%%"
        ),
        "Status": st.column_config.SelectboxColumn(
            "Status", options=["Not started", "In progress", "Complete", "Blocked"]
        ),
        "Start date": st.column_config.DateColumn("Start date"),
        "End date": st.column_config.DateColumn("End date"),
    },
    key="plan_editor",
)
st.session_state.plan_tasks = edited.to_dict("records")

st.caption(
    "Double-click a cell to edit. Use the (+) row at the bottom to add activities, "
    "or the row checkbox + delete icon to remove one."
)
