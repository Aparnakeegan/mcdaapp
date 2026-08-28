import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from utils.state import (
    init_state, new_id, programme_names, all_criteria,
    category_weight_total, criteria_weight_total, all_criteria_weight_total,
    get_potential_score, set_potential_score, potential_scores_table,
    weighted_potential_score,
)
from utils import content

st.set_page_config(page_title="Potential Scores", page_icon="📈", layout="wide")
init_state()

st.title("📈 Prioritise — Potential Scores")

tab_guide, tab_criteria, tab_evidence, tab_scores, tab_results = st.tabs(
    ["Guidance", "1. Define criteria & weights", "2. Evidence", "3. Assign scores", "Weighted results"]
)

with tab_guide:
    st.markdown(content.POTENTIAL_GUIDANCE)

# ---------------------------------------------------------------------
with tab_criteria:
    st.markdown(content.POTENTIAL_CRITERIA_TEXT)
    st.divider()
    st.subheader("Categories and criteria")
    st.caption(
        "We advise no more than 8 criteria in total. Category weights should sum to "
        "100; within each category, criteria weights should sum to that category's weight."
    )

    for ci, cat in enumerate(st.session_state.categories):
        with st.container(border=True):
            c1, c2, c3 = st.columns([4, 2, 1])
            with c1:
                cat["name"] = st.text_input(
                    "Category name", value=cat["name"], key=f"cat_name_{cat['id']}"
                )
            with c2:
                cat["weight"] = st.number_input(
                    "Category weight", value=int(cat["weight"]), min_value=0, max_value=100,
                    key=f"cat_weight_{cat['id']}"
                )
            with c3:
                st.write("")
                if st.button("🗑 Delete category", key=f"cat_del_{cat['id']}"):
                    st.session_state.categories.pop(ci)
                    st.rerun()

            crit_total = criteria_weight_total(cat)
            if crit_total != cat["weight"]:
                st.warning(
                    f"Sum of criteria weights ({crit_total}) should equal the category "
                    f"weight ({cat['weight']})."
                )

            for cj, crit in enumerate(cat["criteria"]):
                cc1, cc2, cc3 = st.columns([4, 2, 1])
                with cc1:
                    crit["name"] = st.text_input(
                        "Criterion", value=crit["name"], key=f"crit_name_{crit['id']}",
                        label_visibility="collapsed"
                    )
                with cc2:
                    crit["weight"] = st.number_input(
                        "Weight", value=int(crit["weight"]), min_value=0, max_value=100,
                        key=f"crit_weight_{crit['id']}", label_visibility="collapsed"
                    )
                with cc3:
                    if st.button("🗑", key=f"crit_del_{crit['id']}"):
                        cat["criteria"].pop(cj)
                        st.rerun()

            if st.button("➕ Add criterion", key=f"add_crit_{cat['id']}"):
                cat["criteria"].append({"id": new_id("crit"), "name": "New criterion", "weight": 0})
                st.rerun()

    if st.button("➕ Add category"):
        st.session_state.categories.append(
            {"id": new_id("cat"), "name": "New category", "weight": 0, "criteria": []}
        )
        st.rerun()

    st.divider()
    total_cat = category_weight_total()
    total_crit = all_criteria_weight_total()
    m1, m2 = st.columns(2)
    m1.metric("Total category weight", total_cat, delta=(total_cat - 100), delta_color="off")
    m2.metric("Total criteria weight", total_crit, delta=(total_crit - 100), delta_color="off")
    if total_cat != 100:
        st.error("Total category weight should equal 100.")
    if total_crit != 100:
        st.error("Total criteria weight should equal 100.")

# ---------------------------------------------------------------------
with tab_evidence:
    st.markdown(content.POTENTIAL_EVIDENCE_TEXT)
    st.divider()
    if not programme_names():
        st.info("Add programme areas on the Define Scope page first.")
    for p in programme_names():
        st.session_state.potential_evidence.setdefault(p, "")
        st.session_state.potential_evidence[p] = st.text_area(
            f"Evidence summary — {p}", value=st.session_state.potential_evidence[p],
            key=f"pot_evidence_{p}", height=100
        )

# ---------------------------------------------------------------------
with tab_scores:
    st.markdown(content.POTENTIAL_SCORING_TEXT)
    st.divider()
    crits = all_criteria()
    names = programme_names()
    if not crits:
        st.info("Define at least one criterion in the 'Define criteria & weights' tab first.")
    elif not names:
        st.info("Add programme areas on the Define Scope page first.")
    else:
        for c in crits:
            st.markdown(f"**{c['category']} → {c['name']}**  (weight {c['weight']})")
            cols = st.columns(len(names))
            for i, p in enumerate(names):
                with cols[i]:
                    current = get_potential_score(p, c["id"], default=3)
                    val = st.slider(
                        p, min_value=1, max_value=5,
                        value=int(current) if current else 3,
                        key=f"pot_score_{c['id']}_{p}"
                    )
                    set_potential_score(p, c["id"], val)

        st.divider()
        st.subheader("Rationale")
        for p in names:
            st.session_state.potential_rationale.setdefault(p, "")
            st.session_state.potential_rationale[p] = st.text_area(
                f"Rationale for scores — {p}",
                value=st.session_state.potential_rationale[p],
                key=f"pot_rationale_{p}", height=80
            )

# ---------------------------------------------------------------------
with tab_results:
    st.write(
        "Scores are combined with the weights assigned to the criteria, to calculate "
        "the overall Potential score (out of 100) for each programme area."
    )
    df = potential_scores_table()
    if df.empty:
        st.info("Add programme areas to see results here.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)
        chart_df = df.set_index("Programme area")[["Potential score (/100)"]].dropna()
        if not chart_df.empty:
            st.bar_chart(chart_df)
