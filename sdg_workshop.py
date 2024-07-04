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

# # Step 2: SDG and Sub-goal Review
# st.header("2. SDG and Sub-goal Review (60 minutes)")
# st.write("Review all 17 SDGs and their sub-goals in the next hour.")

# # Initialize session state for timer
# if 'start_time' not in st.session_state:
#     st.session_state.start_time = time.time()

# # Display timer
# elapsed_time = int(time.time() - st.session_state.start_time)
# remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
# st.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

# # Display SDGs and sub-goals
# for _, row in sdg_data.iterrows():
#     with st.expander(f"{row['Goal']}"):
#         st.write(row['Description'])
#         if 'Sub_goals' in row and row['Sub_goals']:
#             st.write("Sub-goals:")
#             try:
#                 sub_goals = ast.literal_eval(row['Sub_goals'])
#                 for sub_goal in sub_goals:
#                     st.write(f"- {sub_goal}")
#             except:
#                 st.write("No sub-goals available")

# # SDG Selection
# selected_sdgs = st.multiselect(
#     "Select relevant SDGs for your project:",
#     sdg_data['Goal'].unique()
# )

# # Step 3: Goal Prioritization
# if selected_sdgs:
#     st.header("3. Goal Prioritization")
#     st.write("Prioritize the selected SDGs by dragging them into order.")
#     prioritized_sdgs = st.multiselect(
#         "Prioritize SDGs:",
#         selected_sdgs,
#         default=selected_sdgs
#     )

#     # Step 4: Action Planning
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
#     st.warning("Please select at least one SDG to continue.")

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
    return df

sdg_data = load_sdg_data()

st.title("SDG Workshop Simulator")

# Step 1: Introduction and Warm-up
st.header("1. Introduction and Warm-up")
st.write("Discuss the following questions with your team:")
st.write("- How do you measure sustainability?")
st.write("- Whose vote counts in sustainability decisions?")
st.write("- How are the UN goals valid across borders? Locally and internationally?")

# Step 2: SDG and Sub-goal Review and Relevance Selection
st.header("2. SDG and Sub-goal Review and Relevance Selection")
st.write("Review all 17 SDGs and their targets, and select their relevance to your project.")

# Initialize session state for timer
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Display timer
elapsed_time = int(time.time() - st.session_state.start_time)
remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
st.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

# Display SDGs, sub-goals, and relevance selection
for _, row in sdg_data.iterrows():
    with st.expander(f"{row['Goal']}"):
        st.write(row['Description'])
        
        # SDG relevance selection
        sdg_relevance = st.radio(
            f"Relevance of {row['Goal']}",
            ["Relevant", "Partially Relevant", "Not Relevant"],
            key=f"sdg_relevance_{row['Goal']}"
        )
        
        if 'Sub_goals' in row and row['Sub_goals']:
            st.write("Targets:")
            try:
                sub_goals = ast.literal_eval(row['Sub_goals'])
                for i, sub_goal in enumerate(sub_goals):
                    st.write(f"- {sub_goal}")
                    # Target relevance selection
                    target_relevance = st.radio(
                        f"Relevance of Target {i+1}",
                        ["Relevant", "Partially Relevant", "Not Relevant"],
                        key=f"target_relevance_{row['Goal']}_{i}"
                    )
            except:
                st.write("No targets available")

# Step 3: Goal Prioritization
st.header("3. Goal Prioritization")
st.write("Prioritize the SDGs you marked as Relevant or Partially Relevant.")

relevant_sdgs = [
    goal for goal in sdg_data['Goal']
    if st.session_state.get(f"sdg_relevance_{goal}") in ["Relevant", "Partially Relevant"]
]

prioritized_sdgs = st.multiselect(
    "Prioritize SDGs:",
    relevant_sdgs,
    default=relevant_sdgs
)

# Step 4: Action Planning
if prioritized_sdgs:
    st.header("4. Action Planning")
    st.write("Develop concrete plans for implementing the selected SDGs.")
    for sdg in prioritized_sdgs:
        st.subheader(f"Action Plan for {sdg}")
        action = st.text_area(f"Actions for {sdg}:", key=f"action_{sdg}")
        timeline = st.date_input(f"Timeline for {sdg}:", key=f"timeline_{sdg}")
        responsible = st.text_input(f"Responsible person/team for {sdg}:", key=f"responsible_{sdg}")

    # Step 5: Sustainability Reporting
    st.header("5. Sustainability Reporting")
    st.write("Based on your selections, here's a preliminary sustainability report:")
    for sdg in prioritized_sdgs:
        st.subheader(sdg)
        st.write(f"Relevance: {st.session_state.get(f'sdg_relevance_{sdg}', 'Not specified')}")
        st.write(f"Actions: {st.session_state.get(f'action_{sdg}', 'Not specified')}")
        st.write(f"Timeline: {st.session_state.get(f'timeline_{sdg}', 'Not specified')}")
        st.write(f"Responsible: {st.session_state.get(f'responsible_{sdg}', 'Not specified')}")

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
    st.warning("Please select and prioritize at least one SDG to continue.")

