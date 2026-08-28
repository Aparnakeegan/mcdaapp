"""
Guidance / reference text carried over from the original
Prioritisation_framework_Sept19.xlsm workbook (originally produced by
Public Health England). Reproduced here as static reference content so
the full walkthrough is available inside the app.
"""

INTRODUCTION = """
The Prioritisation Framework is a flexible tool designed to support teams in making
evidence-based spending decisions across different programme areas.

The burden and complexity of decision making is increasing, while the resource
available to carry out the exercise is decreasing. The framework gives teams the
resources they need to conduct a robust prioritisation exercise. The approach is
based on the work led by David Gardiner in Public Health England's North East
Centre, developed in collaboration with several Local Authorities, and refined
through consultation and testing to ensure it is transparent, flexible and easy
to use.

The process evaluates programmes through **triangulation of the potential state,
the current state and the programme budgets**, all the while considering what is
feasible. The primary technique used is **multi-criteria decision analysis
(MCDA)**.

MCDA has been used effectively to support strategic decision making in a number
of contexts and is recommended for central government policy setting, being the
subject of supplementary guidance on HM Treasury's Green Book. It has also been
endorsed by the London School of Economics (LSE), the London School of Hygiene &
Tropical Medicine (LSHTM) and the World Trade Organisation (WTO), among others.

The framework helps users translate the results of MCDA into real-world impact
by also setting out the methodology for gaining buy-in for the process,
including communications, scoping and project planning.

**Further reading**
- Green Book supplementary guidance: multi-criteria decision analysis, HM Treasury (2013)
- Multiple Criteria Decision Analysis (MCDA) for evaluating new medicines in Health
  Technology Assessment and beyond, Angelis and Kanavos (2017)
- Multi-Criteria Decision Analysis (MCDA) as the basis for the development,
  implementation and evaluation of interactive patient decision aids, Ponzo-Martin (2015)
- Evidence-based approach to prioritize SPS investments, World Trade Organisation (2012)

The original Prioritisation Framework was the subject of an independent evaluation
funded and undertaken by a team from the NIHR School for Public Health Research
Centre for Translational Research in Public Health (Fuse).
"""

OVERVIEW_STEPS = [
    ("1. Initiate", "Explain the process, define scope, form the team, map stakeholders, and create a plan."),
    ("2. Define Scope", "Agree the background, objectives, exclusions, programme areas and project logistics."),
    ("3. Create Plan", "Lay out the timeline of activities, milestones and responsibilities."),
    ("4. Prioritise", "Define criteria and weights, gather evidence, then score Potential and Current states."),
    ("5. Recommend", "Triangulate scores into a direction-of-travel recommendation per programme area, "
                      "optionally model budget scenarios, and reflect via a structured discussion."),
    ("6. Communicate", "Share the findings, methodology and rationale with decision makers and stakeholders."),
]

GLOSSARY = [
    ("Process Owner", "The person who leads and manages the prioritisation process, receiving technical "
                       "information from specialists and presenting recommendations to the Decision Maker."),
    ("Decision Maker", "The person who receives recommendations from the Process Owner and makes final "
                        "decisions about spending on programme areas."),
    ("Executive Lead", "The person who initiates the need for a prioritisation process, for example by "
                        "requiring directorates to submit budgets or to deliver specified levels of savings."),
    ("Lead Specialist", "The person tasked with collating and providing key information about current and "
                         "potential performance of their particular programme."),
    ("Lead Analyst", "The person tasked with collating and synthesising evidence and data on a range of "
                      "programmes, as requested."),
    ("Programme area", "A broad area of spending, for example tobacco control, alcohol, sexual health "
                        "services or obesity. Categories should be broad enough to capture large areas of spend."),
    ("Category", "Broad groupings of criteria that the team agree are important in deciding which programme "
                  "areas to fund, e.g. 'Political Benefits' or 'Health Benefits'."),
    ("Criteria", "Factors the team have agreed are most important in deciding which programme areas to "
                  "fund, e.g. 'return on investment', 'impact on health inequalities'."),
    ("Rationale", "A brief statement describing why a score has been given, or a decision taken, at each "
                   "stage. Capturing rationale supports transparency and future reference."),
    ("MCDA model (Potential)", "A model for determining categories and criteria during the 'potential' phase "
                                 "of the analysis, built up by combining criteria into categories and categories "
                                 "into a single objective."),
    ("MCDA", "Multi-Criteria Decision Analysis: a model to help decision makers prioritise a range of "
              "alternatives in an environment where many complex criteria affect the decision."),
    ("Potential state", "A hypothetical future state, where the programme is performing in the best way it "
                          "possibly can, subject to restrictions outside of local control."),
    ("Potential score", "The score obtained by each programme area when assessed against the weighted "
                          "criteria agreed during MCDA analysis. A high potential score suggests the programme "
                          "can deliver strong outcomes."),
    ("Current state", "An assessment of investment and outcomes of the currently delivered programme relative "
                        "to other similar areas -- not to label current performance as good or poor, but to "
                        "objectively benchmark it."),
    ("Current scores", "Scores representing the investment and outcomes of currently funded programme areas, "
                         "and the likelihood the programme will reach its full potential."),
    ("Investment score", "A score from 1 to 5 which indicates the level of investment in this programme area, "
                           "relative to other comparable areas (1 = very high relative investment, 5 = very low)."),
    ("Outcome score", "A score from 1 to 5 representing the outcomes achieved in this programme area relative "
                        "to other comparable areas (1 = much lower outcomes, 5 = much better outcomes)."),
    ("Feasibility score", "A subjective score from 1 to 5 which rates the feasibility of making changes to "
                            "investment in / delivery of current programmes, taking into account 'real-world' "
                            "political and practical considerations."),
    ("Prioritise", "The central process of the exercise, where potential state, current state and the "
                    "programme budget are brought together, all while considering feasibility."),
    ("Recommendation / direction of travel", "The outcome of the prioritisation process: a simple statement "
                                               "of intention to invest further, disinvest, or maintain the "
                                               "current level of investment in a programme."),
    ("Prioritisation budget", "A budget model achieved using intelligence from the prioritisation process. "
                               "The budget for each programme area may increase, decrease or remain stable."),
    ("Equal proportion budget", "A budget model achieved by adding an equal proportion to, or taking an equal "
                                  "proportion from, each programme area ('salami slicing'), included as a "
                                  "point of comparison."),
    ("Priority points", "Obtained by multiplying the budget for each topic area by its Potential score. "
                          "Comparing total priority points between two budget scenarios shows the relative "
                          "spread of investment towards high vs low priority programme areas."),
]

RESOURCES = [
    ("Spend and Outcomes Tool (SPOT)", "An overview of spend and outcomes in local authorities and CCGs, "
     "for public health teams and commissioners.", "https://www.gov.uk/government/publications/spend-and-outcome-tool-spot"),
    ("Health Economics Evidence Resource (HEER)", "Shows key cost-effectiveness and return-on-investment "
     "evidence on activities in the public health domain.", "https://www.gov.uk/government/publications/health-economics-evidence-resource"),
    ("Fingertips", "A rich source of indicators across a range of health and wellbeing themes designed to "
     "support needs assessment and commissioning.", "https://fingertips.phe.org.uk/"),
    ("Health economics guide for public health teams", "Resources to estimate return on investment and "
     "cost-effectiveness of public health programmes.", "https://www.gov.uk/guidance/health-economics-a-guide-for-public-health-teams"),
    ("SHAPE Atlas", "A web-enabled, evidence-based application informing the strategic planning of services "
     "and physical assets across a whole health economy.", ""),
    ("NICE Return on Investment tools", "Modelling tools for public health commissioners and decision-makers.",
     "https://www.nice.org.uk/about/what-we-do/into-practice/return-on-investment-tools"),
    ("NHS RightCare Atlas", "Interrogates routinely available data relating investment, activity and "
     "outcome to the whole population in need.", "https://www.england.nhs.uk/rightcare/products/atlas/"),
    ("Public Health Outcomes Framework", "Sets out a vision for public health, desired outcomes and the "
     "indicators used to track progress.", "http://www.phoutcomes.info/"),
    ("Health profiles / local factsheets", "Health intelligence products summarising trends in health "
     "outcomes and local authority public health functions.", "https://www.gov.uk/government/publications/public-health-in-local-government"),
    ("JSNA packs", "Joint Strategic Needs Assessments looking at current and future health and care needs "
     "of local populations to inform commissioning.", "http://www.devonhealthandwellbeing.org.uk/jsna/about/"),
    ("Health England Leading Prioritisation (H.E.L.P.)", "Cost-effectiveness, health-inequalities impact "
     "and reach data to support prioritisation of interventions.", "http://help.matrixknowledge.com/"),
    ("Greater Manchester Cost Benefit Analysis tool", "Simplifies and lowers the cost of performing CBA in "
     "the context of local programmes.", "http://neweconomymanchester.com/stories/1855-cost_benefit_analysis_guidance_and_model"),
    ("Informing Investment to reduce health Inequalities (III)", "Numerical models of the potential impact "
     "of interventions on health inequalities.", "http://www.scotpho.org.uk/comparative-health/health-inequalities-tools/informing-investment-to-reduce-health-inequalities-iii"),
    ("Socio-Technical Allocation of Resources (STAR)", "An approach to priority setting helping commissioners "
     "allocate health resources to benefit patients.", "http://www.health.org.uk/collection/star-socio-technical-allocation-resources"),
    ("Public Health Dashboard", "Brings a number of data sources into one accessible place to support "
     "local decision-making.", "https://healthierlives.phe.org.uk/topic/public-health-dashboard"),
]

INITIATE_GUIDANCE = """
The first step of the prioritisation process is to ensure a controlled initiation through
five activities. It is recommended that sufficient time is spent on these early tasks to
ensure the process runs smoothly and that the outcomes are seen as robust.

**1) Explain the process** -- make sure everyone has a shared understanding of the process
from the start; this is critical to maintaining buy-in throughout.

**2) Define scope** -- the scope defines the 'what' and 'why' of the exercise, often
starting from an initial terms-of-reference (areas in scope, budget available, deadlines).
This should be formally captured and reviewed with key decision-making bodies before the
exercise begins.

**3) Form team** -- the team is the 'who': an Executive Lead, a Decision Maker, a Process
Owner, and however many Lead Specialists and Lead Analysts are needed. The Process Owner
facilitates the process, runs workshops, collects evidence, communicates findings and
engages stakeholders.

**4) Map your stakeholders** -- develop an understanding of who will implement the final
recommendations and who should be included in the process itself, from simple progress
updates through to direct participation in workshops.

**5) Create plan** -- communicates the key activities, milestones, dates and status of the
process to the team and stakeholders. The plan can be as detailed or as high-level as suits
you, and should be updated as it progresses.

**Key aspects to get right**
- Clearly explain the process and gain buy-in from senior stakeholders
- Decide what is included in the exercise
- Think about who should be involved, and how
- Be clear on who conducts each aspect of the exercise
- Identify resource and support to keep the process straightforward
"""

PRIORITISE_GUIDANCE = """
In the Prioritise step there are two parts: the calculation of **Potential scores** and the
calculation of **Current scores**.

- **Potential scores** relate to scoring programme areas against weighted criteria, based
  on Multi-Criteria Decision Analysis (MCDA) -- the potential outcome each programme area
  could have for different criteria, if it performed at its best.
- **Current scores** relate to scoring the current situation per programme area, in terms
  of investment and outcomes, by benchmarking to comparable areas. A feasibility score is
  also generated at this stage.

Prioritise is the core and most challenging step of the process. It is recommended to
divide the process into three workshops:

**Workshop 1 -- Define criteria and weights.** The Process Owner introduces stakeholders to
the process; stakeholders identify and describe criteria, and assign weights reflecting
relative importance.

**Between workshops -- Gather evidence.** Specialists from each programme area separately
collect evidence related to the potential performance that programme could achieve for the
identified criteria.

**Workshop 2 -- Assign Potential scores.** Based on the evidence collected and discussion,
each programme is scored from 1 to 5 on each criterion; weighted scores are calculated
automatically.

**Between workshops -- Gather current-state evidence.** Specialists collect evidence
related to the current state of each programme area, in terms of current investments and
outcomes relative to comparable areas.

**Workshop 3 -- Assign Current scores.** Based on evidence and expert opinion, Current
scores are calculated: relative investments and outcomes are rated from 1 to 5, and a
feasibility score is agreed.
"""

POTENTIAL_GUIDANCE = """
The potential scores relate to a hypothetical future state, where the programme is
performing in the best way it possibly can, subject to restrictions outside of local
control. Potential scores are calculated through a four-stage process:

1. **Criteria selection and relative weighting** (first workshop)
2. **Evidence gathering** (desk research)
3. **Scoring of programme areas** against selected criteria (second workshop)
4. **Calculation of weighted scores** for each programme area (done automatically by this tool)

The calculation is based on the Multi-Criteria Decision Analysis (MCDA) methodology, a
systematic approach that allows you to compare different options across several criteria
and rank them from most to least preferred -- combining available evidence with expert
judgement to make implicit decision-making explicit.

**Setting up the analysis**
- Establish the decision context and one high-level objective (e.g. how to best manage
  your budget across competing programme areas)
- Identify all programme areas you want to compare (captured in Define Scope)

**First workshop**
- Identify operational criteria (e.g. Effectiveness, Impact on Health Inequalities,
  Acceptability)
- Assign weights to each criterion reflecting its relative importance

**Desk research**
- Collect evidence to support scoring decisions against the chosen criteria

**Second workshop**
- Score programme areas against all criteria (1 = poorest, 5 = best)
- Combine weights and scores to derive an overall value (calculated automatically)
- Examine and agree results; use sensitivity analysis (changing weights or scores) to
  help resolve disagreements
"""

POTENTIAL_CRITERIA_TEXT = """
The selection of operational criteria is the first step of the Prioritise step. The
selected criteria become the chosen indicators for programme areas' performance.

The final criteria (no more than 8 recommended) should represent the key and most
differentiating factors, as programme areas will be scored against these on a scale of
1 (poorest) to 5 (best).

**How to identify criteria**
Criteria are identified in the first workshop using hierarchical trees with two levels:
1. **Categories** -- the first branch level, capturing all aspects that derive from the
   overall objective (e.g. making the most out of the available budget)
2. **Criteria** -- the second branch level, specific factors within each category

Start with a longlist of criteria and organise them into categories.

**Checking chosen criteria**
1. *Completeness* -- all major criteria needed to score performance are included
2. *Non-redundancy* -- no unnecessary criteria included
3. *Operationality* -- all criteria can be judged against all topic areas
4. *Independence* -- limited overlap between criteria, and no overlap with spend,
   outcomes and feasibility (assessed separately)
5. *Size* -- limit to the 8 most important and differentiating criteria

**Example long list of criteria**: Effectiveness, Cost-effectiveness, Impact on health
inequalities, Local need, Mandation, Prevention, Acceptability, Connectedness, Building
community strengths, Innovation, Local growth.

**Assigning weights**
1. Assign weights to each **category**, so they sum to 100
2. Assign weights to each **criterion** within a category; the criteria weights within a
   category should sum to that category's weight, and all criteria weights overall
   should sum to 100
"""

POTENTIAL_EVIDENCE_TEXT = """
After defining the criteria, Lead Specialists should gather evidence and summarise it for
their programme area. Short, separate evidence summaries (a few lines) should be collected
for each criterion within each programme, supplemented with local knowledge.

Evidence for potential scores should represent **what could potentially be achieved** in
each programme area, for each criterion.

**Example** -- if 'Obesity' is being assessed against 'burden of disease', 'health
inequalities' and 'cost savings', evidence might include:
- The burden of illness related to obesity locally, and the potential of obesity
  programmes to reduce this
- Health inequalities related to obesity, and the potential impact of programmes on
  reducing them
- The cost-effectiveness of interventions aiming to help people lose weight
"""

POTENTIAL_SCORING_TEXT = """
After collecting evidence for each programme area, rate each topic area from 1 (poorest)
to 5 (best) against all criteria, in the second workshop. Higher scores indicate the
potential performance of the programme area is high against a specific criterion.

This can be done relatively (worst programme scored 1, best scored 5) or by assigning
specific values to each score.

**Example**: scoring "Sexual Health Services" a "2" for "Impact on Health Inequalities"
means you believe that, based on the evidence, the potential for reducing health
inequalities -- if sexual health services performed at their best -- is poor.

Scores are then combined with the weighting decided previously to calculate the overall
Potential score for each programme area.
"""

CURRENT_GUIDANCE = """
As opposed to the potential scores, current scoring focuses on what's actually happening
now. Assess each programme area's expenditure and outcomes compared to other comparable
areas, and the feasibility of achieving the potential state.

First, gather evidence on the current situation by programme area. Then score each topic
area on the relative level of current investment, outcomes observed, and feasibility of
moving from the current state to the potential state.

There will not always be sufficient evidence to allow scoring decisions for current
investments and outcomes -- local knowledge from workshop attendees is important here.
Discussion should be captured in the Rationale box, along with any gaps in the evidence
base.

Before commencing current scoring, agree the approach: what resources to use, how long
to collect evidence for, how to treat topic areas with insufficient evidence, and what
constraints, dependencies and assumptions apply (captured in Define Scope).
"""

CURRENT_SCORING_TEXT = """
Each topic area is assessed against three measures:

**a. Current investment** -- amount currently spent relative to other comparable areas
(1 = very high relative investment, 5 = very low relative investment)

**b. Current outcomes** -- outcomes resulting from the programme relative to other
comparable areas (1 = very poor relative outcomes, 5 = very good relative outcomes).
Investment and outcome scores are combined: a total of 2 is the lowest possible current
score, 10 is the highest.

**c. Feasibility** -- the feasibility of reaching the potential of the programme area
(1 = very low, 5 = very high). This is a standalone score, since it measures the
potential of achieving a future state rather than current status. Consider:
- Current context (demographic/epidemiological factors that enable or inhibit outcomes)
- The extent to which investment would need to shift from currently funded programmes
- The extent to which increased funding would help achieve the potential state
"""

CURRENT_EVIDENCE_TEXT = """
Lead Specialists should collect evidence and summarise it for their programme area.
Short, separate evidence summaries should be collected for investment and outcomes.

Evidence for current scores should represent **what is actually being achieved**.

**Key aspects to get right**
- Use benchmarking tools (such as SPOT) wherever possible
- Think widely about feasibility -- the commissioning cycle matters, but workforce and
  other factors can also affect whether change is possible
- Capture background information relevant to understanding *why* things are the way
  they are -- this informs the narrative around spend directions

**Example** -- for 'Obesity', look specifically for:
- How much is currently spent locally relative to other comparable areas?
- What outcomes are being achieved relative to other comparable areas?
"""

RECOMMEND_GUIDANCE = """
The Recommend stage links the results of the prioritisation analysis to the budget
recommendations. At this stage you triangulate the findings by considering:

1. Potential scores (and the context around them)
2. Current scores and feasibility scores (and the context around them)
3. The current budget broken down across programmes

This triangulation lets you recommend **increasing, decreasing or maintaining** the same
level of investment for each programme area (direction of travel) -- the aim is not to
set specific programme budgets.

It's important to consider the wider context -- strategic pressures, delivery issues,
existing political priorities -- alongside the scores.

**Three elements of the Recommend stage**
1. **Provide rationale** -- view a summary of the prioritise stage, make direction-of-
   travel recommendations, and capture the rationale
2. **Model / Compare scenarios** -- optional: compare various budget recommendations
3. **Discuss process** -- optional: critique the process, outcomes and recommendations
"""

PROVIDE_RATIONALE_TEXT = """
Based on the scores calculated in the Prioritise step (and any further discussion),
recommend the direction of travel for investment in each programme area
(**Increase / Decrease / No change**), and capture the rationale for each recommendation.
"""

SCENARIO_GUIDANCE = """
Scenario Modelling is an **optional** step. The aim is to demonstrate how a budget based
on the potential scores of different topic areas can be more efficient than proportional
(dis)investment across all programme areas ("salami-slicing").

**How it works**

For each programme area, you specify whether the budget should **increase, decrease or
stay the same**, and what proportion of the budget could be adjusted. A new
("Prioritisation") budget is then created by weighting that adjustable proportion by the
programme's Potential score (out of 100).

*Example*: the budget for Sexual Health Services should increase, and the adjustable
proportion is 20%. If the Potential score is 75/100, the new budget adds
20% x 75% = 15% to the original budget. If a decrease is recommended instead, the new
budget subtracts 20% x (1 - 75%) = 5% from the original budget.

If a **pre-agreed amount** has already been agreed for a programme area, entering it
overrides the calculation above.

**Comparing budgets: priority points**

Priority points are obtained by multiplying the budget for each programme area by its
Potential score. Comparing total priority points between the Prioritisation budget and
an Equal Proportion budget (the same total, spread proportionately) shows the relative
spread of investment towards high vs low priority programme areas.

The difference in priority points is converted into a monetary value ("added value"):
the value of one priority point = total Prioritisation budget / total Prioritisation
priority points; added value = value-per-point x (Prioritisation points - Equal
Proportion points). This does not represent cash savings, but the *extra value*
achieved for the same money.

You can save up to 5 scenarios and compare them on the Compare Scenarios page.
"""

DISCUSSION_QUESTIONS = [
    "Why was the process needed?",
    "State the results of the process",
    "Consider the meaning of the findings, and their importance",
    "Implications of the recommendations in terms of potential actions and their "
    "consequences -- what do the direction-of-travel recommendations mean in practical terms?",
    "Consider alternative explanations of the findings (e.g. could findings have been biased?)",
    "Key assumptions and dependencies",
    "Risk and sensitivity analysis",
    "Strengths of the process",
    "Limitations of the process",
    "Highlight gaps in research (if evidence was missing)",
    "Conclusion and future steps",
]

DISCUSSION_INTRO = """
This page is an opportunity to reflect on the prioritisation process, considering its
strengths, limitations, and the relevance and implications of the findings.
"""

COMMUNICATE_GUIDANCE = """
The Prioritisation Framework relies upon group consensus in order to help inform funding
decisions. Throughout, the thoughts and opinions of stakeholders should be captured and
incorporated into the process. At the end, there remains a necessary step of communicating
the recommendations with the Decision Maker, Executive Lead and other senior stakeholders.
It's important that those making decisions based on the outputs understand both the
recommended spend directions and the surrounding narrative.

The tool should make this simpler, having captured much of the information needed to
explain decisions throughout the process. Remember that those who have not been closely
involved need to be walked through each stage. Sharing results clearly, transparently and
frankly builds confidence in the process.

**Key aspects to get right**
- Identify who your stakeholders are
- Explain the methodology of multi-criteria decision analysis, and that it's a widely
  accepted decision-making framework
- Explain the criteria that have been used to drive the process
- Emphasise how the knowledge, skills and experience of multiple parties fed into the results
"""

FEEDBACK_INTRO = """
The intention of this tool is that it can be returned to in the future, both for
reference and as a starting point for a repeat of the process. Use the box below to
capture any final thoughts that could be helpful for next time.
"""

TERMS_TEXT = """
This tool is adapted from a framework originally provided by Public Health England to aid
decision-making around use of the Public Health Grant. Public Health England and its
employees cannot be held liable for any investment or other decisions made using this
resource. Teams are advised to seek independent advice prior to using this tool or the
methodology described within.
"""

ACKNOWLEDGEMENTS_TEXT = """
**Multi-Criteria Decision Analysis (MCDA) methodology**

The calculation of potential scores is based on the Multi-Criteria Decision Analysis
(MCDA) methodology, adapted from *'Multi-criteria analysis: a manual'* by the Department
for Communities and Local Government
(https://www.gov.uk/government/publications/green-book-supplementary-guidance-multi-criteria-decision-analysis).

**Shifting the Gravity of Spend**

The early stages of the Prioritisation Framework were informed by the Shifting the
Gravity of Spend research programme, funded and undertaken by a team from the NIHR
School for Public Health Research Centre for Translational Research in Public Health
(Fuse), the London School of Hygiene and Tropical Medicine, and the University of
Sheffield.

With thanks to everyone involved in the original discovery workshops, alpha / beta
testing, and live testing of the framework, and to the National Institute for Health
Research (NIHR) School for Public Health Research for funding the independent evaluation
undertaken by Fuse (Newcastle University and Northumbria University).
"""

CREATE_PLAN_INTRO = """
Use this page to plan the timeline of the prioritisation exercise, from start to finish.
Below is a starting checklist of the activities typically required.
"""

DEFAULT_PLAN_TASKS = [
    "Create plan & schedule workshops",
    "Define criteria for Potential score",
    "Gather evidence for Potential score",
    "Analyse evidence for Potential score",
    "Assign scores, weights & commentary for Potential score",
    "Define approach to Current score",
    "Gather evidence for Current score",
    "Analyse evidence for Current score",
    "Assign scores & add commentary for Current score",
    "Triangulate findings & provide rationale",
    "Model scenarios & update rationale",
    "Discuss & document process",
    "Review and update recommendations",
]

DEFINE_SCOPE_FIELD_HELP = {
    "background": "Background / current state -- why is this prioritisation exercise happening now?",
    "objectives": "Objectives / desired state -- what should this exercise achieve?",
    "exclusions": "State what will be excluded from the prioritisation analysis.",
    "outputs": "Define the expected outputs of the prioritisation analysis.",
    "outcomes": "Define the expected outcomes / impact of the prioritisation analysis.",
    "restrictions": "Consider any restrictions that could limit the scope of the analysis.",
    "dependencies": "Consider any existing dependencies that would impact the analysis.",
    "assumptions": "State any assumptions being made before the start of the analysis.",
    "risks": "Identify potential risks that could impact progression and completion, "
              "their likelihood, potential impact, and mitigation.",
    "roles": "Roles and responsibilities -- distribute tasks among stakeholders.",
    "stakeholder_plan": "Describe how, and in what timeframe, stakeholder engagement will occur.",
    "communication_plan": "Describe how, and in what timeframe, communication of findings will occur.",
    "additional_info": "Capture any additional information that might be useful for the project.",
}
