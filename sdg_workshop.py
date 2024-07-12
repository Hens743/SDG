# import streamlit as st
# import pandas as pd
# import time
# import ast

# # Load SDG data
# @st.cache_data
# def load_sdg_data():
#     df = pd.read_csv('sdg_data.csv')
#     if 'Sub_goals' not in df.columns:
#         df['Sub_goals'] = [[] for _ in range(len(df))]
#     else:
#         df['Sub_goals'] = df['Sub_goals'].apply(lambda x: x if isinstance(x, list) else ast.literal_eval(x))
#     return df

# sdg_data = load_sdg_data()

# st.title("SDG Workshop Simulator")

# # Step 1: Introduction and Warm-up
# st.header("1. Introduction and Warm-up")
# st.write("Discuss the following questions with your team:")
# st.write("- How do you measure sustainability?")
# st.write("- Whose vote counts in sustainability decisions?")
# st.write("- How are the UN goals valid across borders? Locally and internationally?")

# # Step 2: SDG Targets Review and Relevance Selection
# st.header("2. SDG Targets Review and Relevance Selection")
# st.write("Review all 17 SDGs and their targets, and select the relevance of each target to your project.")

# # Initialize session state for timer
# if 'start_time' not in st.session_state:
#     st.session_state.start_time = time.time()

# # Display timer
# elapsed_time = int(time.time() - st.session_state.start_time)
# remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
# st.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

# # Display SDGs and targets, and relevance selection for targets
# for _, row in sdg_data.iterrows():
#     with st.expander(f"{row['Goal']}"):
#         st.write(row['Description'])
        
#         if row['Sub_goals']:
#             st.write("Targets:")
#             for i, sub_goal in enumerate(row['Sub_goals']):
#                 st.write(f"- {sub_goal}")
#                 # Target relevance selection
#                 target_relevance = st.radio(
#                     f"Relevance of Target {i+1}",
#                     ["Not Relevant", "Partially Relevant", "Relevant"],
#                     key=f"target_relevance_{row['Goal']}_{i}"
#                 )

# # Step 3: Targets Summary
# st.header("3. Targets Summary")
# st.write("Here's a summary of all targets and their relevance:")

# summary_data = []
# for _, row in sdg_data.iterrows():
#     if row['Sub_goals']:
#         for i, sub_goal in enumerate(row['Sub_goals']):
#             relevance = st.session_state.get(f"target_relevance_{row['Goal']}_{i}", "Not Evaluated")
#             summary_data.append({
#                 "Goal": row['Goal'],
#                 "Target": sub_goal,
#                 "Relevant": 1 if relevance == "Relevant" else 0,
#                 "Partially Relevant": 1 if relevance == "Partially Relevant" else 0,
#                 "Not Relevant": 1 if relevance == "Not Relevant" else 0
#             })

# summary_df = pd.DataFrame(summary_data, columns=["Goal", "Target", "Relevant", "Partially Relevant", "Not Relevant"])
# st.dataframe(summary_df.style.highlight_max(axis=0), use_container_width=True, )

# # Filter relevant and partially relevant targets
# relevant_targets = summary_df[(summary_df["Relevant"] == 1) | (summary_df["Partially Relevant"] == 1)]

# # Step 4: Action Planning
# if not relevant_targets.empty:
#     st.header("4. Action Planning")
#     st.write("Develop concrete plans for implementing the selected targets.")
#     for _, target in relevant_targets.iterrows():
#         st.subheader(f"{target['Goal']}")
#         st.write(f"Target: {target['Target']}")
#         action = st.text_area(f"Actions for this target:", key=f"action_{target['Goal']}_{target['Target']}")
#         timeline = st.date_input(f"Timeline for this target:", key=f"timeline_{target['Goal']}_{target['Target']}")
#         responsible = st.text_input(f"Responsible person/team for this target:", key=f"responsible_{target['Goal']}_{target['Target']}")

#     # Step 5: Sustainability Reporting
#     st.header("5. Sustainability Reporting")
#     st.write("Based on your selections, here's a preliminary sustainability report:")
#     for _, target in relevant_targets.iterrows():
#         st.subheader(f"{target['Goal']}")
#         st.write(f"Target: {target['Target']}")
#         st.write(f"Actions: {{\st.session_state.get(f'action_{target['Goal']}_{target['Target']}', 'Not specified')}}")
#         timeline = st.session_state.get(f'timeline_{target["Goal"]}_{target["Target"]}', 'Not specified')
#         st.write(f"Timeline: {timeline}")
#         responsible = st.session_state.get(f'responsible_{target["Goal"]}_{target["Target"]}', 'Not specified')
#         st.write(f"Responsible: {responsible}")

#     # Step 6: Reflection and Learning
#     st.header("6. Reflection and Learning")
#     reflection = st.text_area("Share your key learnings and 'aha' moments from this workshop:")
#     if st.button("Submit Reflection"):
#         if 'reflections' not in st.session_state:
#             st.session_state.reflections = []
#         st.session_state.reflections.append(reflection)
#         st.success("Thank you for your reflection!")

#     if 'reflections' in st.session_state and st.session_state.reflections:
#         st.subheader("All Reflections:")
#         for i, ref in enumerate(st.session_state.reflections, 1):
#             st.write(f"{i}. {ref}")

# else:
#     st.warning("Please select at least one relevant or partially relevant target to continue.")

import streamlit as st
import pandas as pd
import time
import ast

# Load SDG data
@st.cache_data
def load_sdg_data():
  df = pd.read_csv('sdg_data.csv', encoding='utf-8')
  if 'Sub_goals' not in df.columns:
    df['Sub_goals'] = [[] for _ in range(len(df))]
  else:
    df['Sub_goals'] = df['Sub_goals'].apply(lambda x: x if isinstance(x, list) else ast.literal_eval(x))
  return df

sdg_data = load_sdg_data()

st.title("SDG Workshop Simulator")

# Step 1: Introduction and Warm-up
st.header("1. Introduction and Warm-up")
st.write("Discuss the following questions with your team:")
st.write("- How do you measure sustainability?")
st.write("- Whose vote counts in sustainability decisions?")
st.write("- How are the UN goals valid across borders? Locally and internationally?")

# Step 2: SDG Targets Review and Relevance Selection
st.header("2. SDG Targets Review and Relevance Selection")
st.write("Review all 17 SDGs and their targets, and select the relevance of each target to your project.")

# Initialize session state for timer
if 'start_time' not in st.session_state:
  st.session_state.start_time = time.time()

# Display timer
elapsed_time = int(time.time() - st.session_state.start_time)
remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
st.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

# Display SDGs and targets, and relevance selection for targets
for _, row in sdg_data.iterrows():
  with st.expander(f"{row['Goal']}"):
    st.write(row['Description'])

    if row['Sub_goals']:
      st.write("Targets:")
      for i, sub_goal in enumerate(row['Sub_goals']):
        st.write(f"- {sub_goal}")
        # Target relevance selection
        target_relevance = st.radio(
          f"Relevance of Target {i+1}",
          ["Not Relevant", "Partially Relevant", "Relevant"],  # Default: Not Relevant
          key=f"target_relevance_{row['Goal']}_{i}"
        )

# Step 3: Targets Summary
st.header("3. Targets Summary")
st.write("Here's a summary of all targets and their relevance:")

summary_data = []
for _, row in sdg_data.iterrows():
  if row['Sub_goals']:
    for i, sub_goal in enumerate(row['Sub_goals']):
      relevance = st.session_state.get(f"target_relevance_{row['Goal']}_{i}", "Not Evaluated")
      summary_data.append({
        "Goal": row['Goal'],
        "Target": sub_goal,
        "Relevant": 1 if relevance == "Relevant" else 0,
        "Partially Relevant": 1 if relevance == "Partially Relevant" else 0,
        "Not Relevant": 1 if relevance == "Not Relevant" else 0
      })

summary_df = pd.DataFrame(summary_data, columns=["Goal", "Target", "Relevant", "Partially Relevant", "Not Relevant"])
st.dataframe(summary_df)

# Filter relevant and partially relevant targets
relevant_targets = summary_df[(summary_df["Relevant"] == 1) | (summary_df["Partially Relevant"] == 1)]

# Step 4: Action Planning
if not relevant_targets.empty:
  st.header("4. Action Planning")
  st.write("Develop concrete plans for implementing the selected targets.")
  for _, target in relevant_targets.iterrows():

    # Expandable section for each target
    with st.expander(f"Action Plan for Target: {target['Target']}"):
      st.write("Here, you can brainstorm and define specific actions to achieve this target in the context of your project.")
      # Add input fields for users to define action plan elements
      action_text = st.text_input








