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
#     return df

# sdg_data = load_sdg_data()

# st.title("SDG Workshop Simulator")

# # Step 1: Introduction and Warm-up
# st.header("1. Introduction and Warm-up")
# st.write("Discuss the following questions with your team:")
# st.write("- How do you measure sustainability?")
# st.write("- Whose vote counts in sustainability decisions?")
# st.write("- How are the UN goals valid across borders? Locally and internationally?")

# # Step 2: SDG and Sub-goal Review and Relevance Selection
# st.header("2. SDG and Sub-goal Review and Relevance Selection")
# st.write("Review all 17 SDGs and their targets, and select their relevance to your project.")

# # Initialize session state for timer
# if 'start_time' not in st.session_state:
#     st.session_state.start_time = time.time()

# # Display timer
# elapsed_time = int(time.time() - st.session_state.start_time)
# remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
# st.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

# # Display SDGs, sub-goals, and relevance selection
# for _, row in sdg_data.iterrows():
#     with st.expander(f"{row['Goal']}"):
#         st.write(row['Description'])
        
#         # SDG relevance selection
#         sdg_relevance = st.radio(
#             f"Relevance of {row['Goal']}",
#             ["Relevant", "Partially Relevant", "Not Relevant"],
#             key=f"sdg_relevance_{row['Goal']}"
#         )
        
#         if 'Sub_goals' in row and row['Sub_goals']:
#             st.write("Targets:")
#             try:
#                 sub_goals = ast.literal_eval(row['Sub_goals'])
#                 for i, sub_goal in enumerate(sub_goals):
#                     st.write(f"- {sub_goal}")
#                     # Target relevance selection
#                     target_relevance = st.radio(
#                         f"Relevance of Target {i+1}",
#                         ["Relevant", "Partially Relevant", "Not Relevant"],
#                         key=f"target_relevance_{row['Goal']}_{i}"
#                     )
#             except:
#                 st.write("No targets available")

# # Step 3: Goal Prioritization
# st.header("3. Goal Prioritization")
# st.write("Prioritize the SDGs you marked as Relevant or Partially Relevant.")

# relevant_sdgs = [
#     goal for goal in sdg_data['Goal']
#     if st.session_state.get(f"sdg_relevance_{goal}") in ["Relevant", "Partially Relevant"]
# ]

# prioritized_sdgs = st.multiselect(
#     "Prioritize SDGs:",
#     relevant_sdgs,
#     default=relevant_sdgs
# )

# # Step 4: Action Planning
# if prioritized_sdgs:
#     st.header("4. Action Planning")
#     st.write("Develop concrete plans for implementing the selected SDGs.")
#     for sdg in prioritized_sdgs:
#         st.subheader(f"Action Plan for {sdg}")
#         action = st.text_area(f"Actions for {sdg}:", key=f"action_{sdg}")
#         timeline = st.date_input(f"Timeline for {sdg}:", key=f"timeline_{sdg}")
#         responsible = st.text_input(f"Responsible person/team for {sdg}:", key=f"responsible_{sdg}")

#     # Step 5: Sustainability Reporting
#     st.header("5. Sustainability Reporting")
#     st.write("Based on your selections, here's a preliminary sustainability report:")
#     for sdg in prioritized_sdgs:
#         st.subheader(sdg)
#         st.write(f"Relevance: {st.session_state.get(f'sdg_relevance_{sdg}', 'Not specified')}")
#         st.write(f"Actions: {st.session_state.get(f'action_{sdg}', 'Not specified')}")
#         st.write(f"Timeline: {st.session_state.get(f'timeline_{sdg}', 'Not specified')}")
#         st.write(f"Responsible: {st.session_state.get(f'responsible_{sdg}', 'Not specified')}")

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
#     st.warning("Please select and prioritize at least one SDG to continue.")

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
        
#         if 'Sub_goals' in row and row['Sub_goals']:
#             st.write("Targets:")
#             try:
#                 sub_goals = ast.literal_eval(row['Sub_goals'])
#                 for i, sub_goal in enumerate(sub_goals):
#                     st.write(f"- {sub_goal}")
#                     # Target relevance selection
#                     target_relevance = st.radio(
#                         f"Relevance of Target {i+1}",
#                         ["Relevant", "Partially Relevant", "Not Relevant"],
#                         key=f"target_relevance_{row['Goal']}_{i}"
#                     )
#             except:
#                 st.write("No targets available")

# # Step 3: Relevant Targets Summary
# st.header("3. Relevant Targets Summary")
# st.write("Here's a summary of the targets you marked as Relevant or Partially Relevant:")

# relevant_targets = {}
# for _, row in sdg_data.iterrows():
#     if 'Sub_goals' in row and row['Sub_goals']:
#         try:
#             sub_goals = ast.literal_eval(row['Sub_goals'])
#             relevant_sub_goals = [
#                 sub_goal for i, sub_goal in enumerate(sub_goals)
#                 if st.session_state.get(f"target_relevance_{row['Goal']}_{i}") in ["Relevant", "Partially Relevant"]
#             ]
#             if relevant_sub_goals:
#                 relevant_targets[row['Goal']] = relevant_sub_goals
#         except:
#             pass

# for goal, targets in relevant_targets.items():
#     st.subheader(goal)
#     for target in targets:
#         st.write(f"- {target}")

# # Step 4: Action Planning
# if relevant_targets:
#     st.header("4. Action Planning")
#     st.write("Develop concrete plans for implementing the selected targets.")
#     for goal, targets in relevant_targets.items():
#         st.subheader(f"Action Plan for {goal}")
#         for i, target in enumerate(targets):
#             st.write(f"Target: {target}")
#             action = st.text_area(f"Actions for this target:", key=f"action_{goal}_{i}")
#             timeline = st.date_input(f"Timeline for this target:", key=f"timeline_{goal}_{i}")
#             responsible = st.text_input(f"Responsible person/team for this target:", key=f"responsible_{goal}_{i}")

#     # Step 5: Sustainability Reporting
#     st.header("5. Sustainability Reporting")
#     st.write("Based on your selections, here's a preliminary sustainability report:")
#     for goal, targets in relevant_targets.items():
#         st.subheader(goal)
#         for i, target in enumerate(targets):
#             st.write(f"Target: {target}")
#             st.write(f"Actions: {st.session_state.get(f'action_{goal}_{i}', 'Not specified')}")
#             st.write(f"Timeline: {st.session_state.get(f'timeline_{goal}_{i}', 'Not specified')}")
#             st.write(f"Responsible: {st.session_state.get(f'responsible_{goal}_{i}', 'Not specified')}")

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
#     st.warning("Please select at least one relevant target to continue.")

import streamlit as st
import pandas as pd
import time
import ast

# Load SDG data
@st.cache_data
def load_sdg_data():
    df = pd.read_csv('sdg_data.csv')
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
                    ["Relevant", "Partially Relevant", "Not Relevant"],
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
        st.subheader(f"{target['Goal']}")
        st.write(f"Target: {target['Target']}")
        action = st.text_area(f"Actions for this target:", key=f"action_{target['Goal']}_{target['Target']}")
        timeline = st.date_input(f"Timeline for this target:", key=f"timeline_{target['Goal']}_{target['Target']}")
        responsible = st.text_input(f"Responsible person/team for this target:", key=f"responsible_{target['Goal']}_{target['Target']}")

    # Step 5: Sustainability Reporting
    st.header("5. Sustainability Reporting")
    st.write("Based on your selections, here's a preliminary sustainability report:")
    for _, target in relevant_targets.iterrows():
        st.subheader(f"{target['Goal']}")
        st.write(f"Target: {target['Target']}")
        st.write(f"Actions: {{\st.session_state.get(f'action_{target['Goal']}_{target['Target']}', 'Not specified')}}")


        st.write(f"Timeline: {st.session_state.get(f'timeline_{target["Goal"]}_{target["Target"]}', 'Not specified')}")
        st.write(f"Responsible: {st.session_state.get(f'responsible_{target["Goal"]}_{target["Target"]}', 'Not specified')}")

    # Step 6: Reflection and Learning
    st.header("6. Reflection and Learning")
    reflection = st.text_area("Share your key learnings and 'aha' moments from this workshop:")
    if st.button("Submit Reflection"):
        if 'reflections' not in st.session_state:
            st.session_state.reflections = []
        st.session_state.reflections.append(reflection)
        st.success("Thank you for your reflection!")

    if 'reflections' in st.session_state and st.session_state.reflections:
        st.subheader("All Reflections:")
        for i, ref in enumerate(st.session_state.reflections, 1):
            st.write(f"{i}. {ref}")

else:
    st.warning("Please select at least one relevant or partially relevant target to continue.")









