"""
Shared data model, session-state initialisation, and MCDA calculation
helpers for the Population Based Planning Prioritisation Tool.

All working data lives in st.session_state so it persists as the user
moves between pages within a single browser session. Nothing is saved
to disk automatically -- use the "Save / Load project" controls in the
sidebar (added on the Dashboard and Define Scope pages) to export and
re-import a project as JSON.
"""
import streamlit as st
import pandas as pd
import uuid
import json


# ---------------------------------------------------------------------
# Defaults (mirroring the example content in the original workbook)
# ---------------------------------------------------------------------

DEFAULT_PROGRAMME_AREAS = [
    {"name": "Smoking / Tobacco", "current_spend": 100000},
    {"name": "Obesity", "current_spend": 80000},
    {"name": "Sexual Health Services", "current_spend": 120000},
]

DEFAULT_CATEGORIES = [
    {
        "id": "cat-health-benefits",
        "name": "Health Benefits",
        "weight": 40,
        "criteria": [
            {"id": "crit-effectiveness", "name": "Effectiveness", "weight": 30},
            {"id": "crit-prevention", "name": "Prevention", "weight": 10},
        ],
    },
    {
        "id": "cat-cost",
        "name": "Cost",
        "weight": 20,
        "criteria": [
            {"id": "crit-net-cost", "name": "Net cost", "weight": 20},
        ],
    },
]


def new_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8]}"


# ---------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------

def init_state():
    ss = st.session_state

    ss.setdefault("project_name", "Untitled Population Based Planning Prioritisation")

    ss.setdefault("project_scope", {
        "background": "",
        "objectives": "",
        "exclusions": "",
        "outputs": "",
        "outcomes": "",
        "restrictions": "",
        "dependencies": "",
        "assumptions": "",
        "risks": "",
        "roles": "",
        "stakeholder_plan": "",
        "communication_plan": "",
        "additional_info": "",
    })

    ss.setdefault("programme_areas", [dict(p) for p in DEFAULT_PROGRAMME_AREAS])

    ss.setdefault("categories", [
        {"id": c["id"], "name": c["name"], "weight": c["weight"],
         "criteria": [dict(cr) for cr in c["criteria"]]}
        for c in DEFAULT_CATEGORIES
    ])

    # potential_scores[programme_name][criterion_id] = score (1-5)
    ss.setdefault("potential_scores", {})
    ss.setdefault("potential_evidence", {})   # [programme_name] = text
    ss.setdefault("potential_rationale", {})  # [programme_name] = text

    # current_scores[programme_name] = {"investment":, "outcome":, "feasibility":}
    ss.setdefault("current_scores", {})
    ss.setdefault("current_evidence", {})
    ss.setdefault("current_rationale", {})

    # rationale[programme_name] = {"recommendation": , "rationale": }
    ss.setdefault("rationale", {})

    ss.setdefault("scenarios", [])  # list of saved scenario dicts (max 5)
    ss.setdefault("scenario_inputs", {})  # working (unsaved) scenario inputs

    ss.setdefault("discussion", {})   # free text answers, keyed by question
    ss.setdefault("feedback_notes", "")
    ss.setdefault("plan_tasks", None)  # DataFrame-like list of dicts


# ---------------------------------------------------------------------
# Programme area helpers
# ---------------------------------------------------------------------

def programme_names():
    return [p["name"] for p in st.session_state.programme_areas]


def add_programme_area(name, spend=0):
    if not name:
        return
    names = programme_names()
    if name in names:
        return
    st.session_state.programme_areas.append({"name": name, "current_spend": spend})


def remove_programme_area(name):
    st.session_state.programme_areas = [
        p for p in st.session_state.programme_areas if p["name"] != name
    ]
    for d in (st.session_state.potential_scores, st.session_state.potential_evidence,
              st.session_state.potential_rationale, st.session_state.current_scores,
              st.session_state.current_evidence, st.session_state.current_rationale,
              st.session_state.rationale):
        d.pop(name, None)


# ---------------------------------------------------------------------
# Criteria helpers
# ---------------------------------------------------------------------

def all_criteria():
    """Flat list of (category, criterion) dicts."""
    out = []
    for cat in st.session_state.categories:
        for crit in cat["criteria"]:
            out.append({"category": cat["name"], "category_id": cat["id"],
                        "id": crit["id"], "name": crit["name"], "weight": crit["weight"]})
    return out


def category_weight_total():
    return sum(c["weight"] for c in st.session_state.categories)


def criteria_weight_total(cat):
    return sum(cr["weight"] for cr in cat["criteria"])


def all_criteria_weight_total():
    return sum(cr["weight"] for cat in st.session_state.categories for cr in cat["criteria"])


# ---------------------------------------------------------------------
# Potential score calculations
# ---------------------------------------------------------------------

def get_potential_score(programme, criterion_id, default=None):
    return st.session_state.potential_scores.get(programme, {}).get(criterion_id, default)


def set_potential_score(programme, criterion_id, value):
    st.session_state.potential_scores.setdefault(programme, {})[criterion_id] = value


def weighted_potential_score(programme):
    """Returns potential score normalised to 0-100 (weights sum to 100,
    each criterion scored 1-5 -> max weighted contribution = weight*5,
    so total is divided by 5 to normalise to 100)."""
    crits = all_criteria()
    if not crits:
        return None
    total_weight = sum(c["weight"] for c in crits) or 1
    weighted_sum = 0
    any_score = False
    for c in crits:
        score = get_potential_score(programme, c["id"])
        if score is not None:
            any_score = True
            weighted_sum += c["weight"] * score
    if not any_score:
        return None
    # normalise: max possible = total_weight * 5 -> scale to 100
    return round((weighted_sum / (total_weight * 5)) * 100, 1)


def potential_scores_table():
    """DataFrame: rows = programme areas, cols = criteria, plus weighted total."""
    crits = all_criteria()
    rows = []
    for p in programme_names():
        row = {"Programme area": p}
        for c in crits:
            row[c["name"]] = get_potential_score(p, c["id"])
        row["Potential score (/100)"] = weighted_potential_score(p)
        rows.append(row)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------
# Current score calculations
# ---------------------------------------------------------------------

def get_current(programme):
    return st.session_state.current_scores.get(programme, {})


def set_current(programme, key, value):
    st.session_state.current_scores.setdefault(programme, {})[key] = value


def current_total(programme):
    d = get_current(programme)
    inv, out = d.get("investment"), d.get("outcome")
    if inv is None or out is None:
        return None
    return inv + out


def current_scores_table():
    rows = []
    for p in programme_names():
        d = get_current(p)
        rows.append({
            "Programme area": p,
            "Investment score (1-5)": d.get("investment"),
            "Outcome score (1-5)": d.get("outcome"),
            "Current total (2-10)": current_total(p),
            "Feasibility score (1-5)": d.get("feasibility"),
        })
    return pd.DataFrame(rows)


def normalised_current_score(programme):
    """Current total (2-10) normalised to 0-100."""
    t = current_total(programme)
    if t is None:
        return None
    return round(((t - 2) / 8) * 100, 1)


def normalised_feasibility_score(programme):
    d = get_current(programme)
    f = d.get("feasibility")
    if f is None:
        return None
    return round(((f - 1) / 4) * 100, 1)


# ---------------------------------------------------------------------
# Rationale / recommendation
# ---------------------------------------------------------------------

def get_recommendation(programme):
    return st.session_state.rationale.get(programme, {}).get("recommendation", "Not yet set")


def set_recommendation(programme, value):
    st.session_state.rationale.setdefault(programme, {})["recommendation"] = value


def get_rationale_text(programme):
    return st.session_state.rationale.get(programme, {}).get("rationale", "")


def set_rationale_text(programme, value):
    st.session_state.rationale.setdefault(programme, {})["rationale"] = value


# ---------------------------------------------------------------------
# Scenario modelling calculations
# ---------------------------------------------------------------------

def compute_scenario(inputs):
    """
    inputs: dict[programme] = {
        "direction": "Increase" | "Decrease" | "No change",
        "adjust_pct": float (0-100),
        "pre_agreed": float or None,
    }
    Returns a DataFrame with the full scenario breakdown.
    """
    rows = []
    for p in st.session_state.programme_areas:
        name = p["name"]
        original = p.get("current_spend", 0) or 0
        potential = weighted_potential_score(name) or 0
        current = normalised_current_score(name)
        feasibility = normalised_feasibility_score(name)
        cfg = inputs.get(name, {"direction": "No change", "adjust_pct": 0, "pre_agreed": None})
        direction = cfg.get("direction", "No change")
        pct = (cfg.get("adjust_pct") or 0) / 100
        pre_agreed = cfg.get("pre_agreed")

        if pre_agreed not in (None, 0, "", 0.0):
            prioritisation_budget = original + pre_agreed
        elif direction == "Increase":
            prioritisation_budget = original + original * pct * (potential / 100)
        elif direction == "Decrease":
            prioritisation_budget = original - original * pct * (1 - potential / 100)
        else:
            prioritisation_budget = original

        diff = prioritisation_budget - original
        rows.append({
            "Programme area": name,
            "Potential score (/100)": potential,
            "Current score (/100)": current,
            "Feasibility score (/100)": feasibility,
            "Original budget": original,
            "Spend recommendation": direction,
            "% of budget to adjust": cfg.get("adjust_pct") or 0,
            "Pre-agreed amount": pre_agreed if pre_agreed not in (None, "") else "",
            "Prioritisation budget": round(prioritisation_budget, 2),
            "Difference vs original": round(diff, 2),
        })

    df = pd.DataFrame(rows)
    if not df.empty:
        total_prio = df["Prioritisation budget"].sum()
        total_orig = df["Original budget"].sum()
        if total_orig > 0:
            df["Equal proportion budget"] = round(
                df["Original budget"] / total_orig * total_prio, 2
            )
        else:
            df["Equal proportion budget"] = 0
    return df


def priority_points_summary(scenario_df):
    """Priority points = budget * potential score / 100. Added value calc
    as described in the ModelScenarios guidance."""
    if scenario_df.empty:
        return None
    df = scenario_df.copy()
    df["Prioritisation priority points"] = df["Prioritisation budget"] * df["Potential score (/100)"] / 100
    df["Equal proportion priority points"] = df["Equal proportion budget"] * df["Potential score (/100)"] / 100

    total_prio_budget = df["Prioritisation budget"].sum()
    total_prio_points = df["Prioritisation priority points"].sum()
    total_equal_points = df["Equal proportion priority points"].sum()

    point_value = (total_prio_budget / total_prio_points) if total_prio_points else 0
    added_value = point_value * (total_prio_points - total_equal_points)

    summary = {
        "total_prioritisation_budget": total_prio_budget,
        "total_prioritisation_points": total_prio_points,
        "total_equal_proportion_points": total_equal_points,
        "value_per_point": point_value,
        "added_value": added_value,
    }
    return df, summary


def save_scenario(name, inputs):
    if len(st.session_state.scenarios) >= 5:
        return False
    st.session_state.scenarios.append({"name": name, "inputs": inputs})
    return True


# ---------------------------------------------------------------------
# Export / import whole project
# ---------------------------------------------------------------------

PERSISTED_KEYS = [
    "project_name", "project_scope", "programme_areas", "categories",
    "potential_scores", "potential_evidence", "potential_rationale",
    "current_scores", "current_evidence", "current_rationale",
    "rationale", "scenarios", "discussion", "feedback_notes",
]


def export_project_json() -> str:
    data = {k: st.session_state.get(k) for k in PERSISTED_KEYS}
    return json.dumps(data, indent=2)


def import_project_json(text: str):
    data = json.loads(text)
    for k in PERSISTED_KEYS:
        if k in data:
            st.session_state[k] = data[k]
