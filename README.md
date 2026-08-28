# Population Based Planning Prioritisation Tool

An interactive Streamlit conversion of `Prioritisation_framework_Sept19.xlsm`
(the Public Health England MCDA-based Prioritisation Framework), covering the
full workflow: Initiate → Define Scope → Create Plan → Prioritise (Potential &
Current scores) → Recommend (Rationale, Scenario Modelling, Compare Scenarios,
Discussion) → Communicate → Dashboard → Feedback, plus reference pages
(Glossary, Resources, Terms, Acknowledgements).

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this folder to a GitHub repository (must include `app.py`,
   `requirements.txt`, the `pages/` folder and the `utils/` folder).
2. Go to https://share.streamlit.io, sign in, and click **"New app"**.
3. Point it at your repo, branch, and set the main file path to `app.py`.
4. Click **Deploy**. No secrets or extra configuration are required.

## Notes on the conversion

- The original workbook has 29 sheets, several containing thousands of blank
  template rows (for up to 30 evidence templates) — those have been
  represented as dynamic, add-as-you-go forms instead of fixed row grids.
- **Potential score** = (sum of criterion weight × score) ÷ (total weight × 5)
  × 100, i.e. normalised to 0–100. This mirrors the workbook's approach
  (weights summing to 100, scores 1–5) but the exact cell formula for the
  final weighted total wasn't recoverable from the extracted workbook data,
  so this is a documented best-effort reconstruction — sense-check it against
  a known example from your own workbook before relying on it.
- **Current score** = investment score + outcome score (2–10), shown both raw
  and normalised to 0–100 on the Dashboard.
- **Scenario modelling** follows the formula given in the workbook's own
  guidance text: new budget = original × (1 + adjust% × potential score%) for
  an increase, or original × (1 − adjust% × (1 − potential score%)) for a
  decrease; a pre-agreed amount, if entered, overrides this.
- Data lives only in the browser session (`st.session_state`). Use the
  **Save / load project** controls in the sidebar to export/import a project
  as JSON between sessions — there is no database or file storage wired up.
- Static guidance text (Introduction, Glossary, Resources, workshop guidance,
  etc.) was extracted from the original workbook and lightly reformatted for
  Streamlit; original authorship (Public Health England / Fuse / partner
  local authorities) is credited on the Acknowledgements page.

## Possible follow-ups

- Wire the JSON save/load into a database or cloud storage bucket if you need
  multiple people editing the same project concurrently.
- Add authentication if this will be deployed somewhere more people than your
  immediate team can reach.
- Add PDF/Word export of the Dashboard for sharing recommendations outside
  the app.
