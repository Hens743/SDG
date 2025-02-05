# import streamlit as st
# import pandas as pd
# import time
# import ast
# import io

# # Load SDG data
# @st.cache_data
# def load_sdg_data():
#     df = pd.read_csv('sdg_data.csv', encoding='utf-8')
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

# # Display timer in the sidebar
# elapsed_time = int(time.time() - st.session_state.start_time)
# remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
# st.sidebar.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

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
#                     ["Not Relevant", "Partially Relevant", "Relevant"],  # Default: Not Relevant
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
#             action_plan = st.session_state.get(f"action_plan_{row['Goal']}_{sub_goal}", "")
#             summary_data.append({
#                 "Goal": row['Goal'],
#                 "Target": sub_goal,
#                 "Relevance": relevance,
#                 "Action Plan": action_plan
#             })

# summary_df = pd.DataFrame(summary_data, columns=["Goal", "Target", "Relevance", "Action Plan"])
# st.dataframe(summary_df)

# # Step 4: Action Planning
# st.header("4. Action Planning")
# st.write("Develop concrete plans for implementing the selected targets.")

# # Initialize empty action_plans if it does not exist
# if 'action_plans' not in st.session_state:
#     st.session_state['action_plans'] = {}

# # Display relevant and partially relevant targets for action planning
# for _, target in summary_df.iterrows():
#     if target['Relevance'] in ["Relevant", "Partially Relevant"]:
#         # Expandable section for each target
#         with st.expander(f"Action Plan for Target: {target['Target']}"):
#             # Add input fields
#             action_plan = st.text_area("", key=f"action_plan_{target['Goal']}_{target['Target']}")
#             st.session_state['action_plans'][f"{target['Goal']}_{target['Target']}"] = action_plan

# # Step 5: Review and Save Action Plans
# st.header("5. Save Action Plans")
# st.write("Download your action plans for future reference.")

# # Convert action plans to a DataFrame
# if 'action_plans' in st.session_state:
#     action_plans_df = pd.DataFrame(list(st.session_state['action_plans'].items()), columns=['Target', 'Action Plan'])
#     # Add button to download the action plans as a CSV file
#     csv = action_plans_df.to_csv(index=False).encode('utf-8')
#     st.download_button(
#         label="Download Action Plans as CSV",
#         data=csv,
#         file_name='action_plans.csv',
#         mime='text/csv'
#     )


# import streamlit as st
# import pandas as pd
# import time
# import ast
# import io

# # Load SDG data
# @st.cache_data
# def load_sdg_data():
#     df = pd.read_csv('sdg_data.csv', encoding='utf-8')
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
# st.write("- Whose voices counts in sustainability decisions?")
# st.write("- How are the UN goals valid across borders? Locally and internationally?")

# # Step 2: SDG Targets Review and Relevance Selection
# st.header("2. SDG Targets Review and Relevance Selection")
# st.write("Review all 17 SDGs and their targets, and select the relevance of each target to your project.")

# # Initialize session state for timer
# if 'start_time' not in st.session_state:
#     st.session_state.start_time = time.time()

# # Display timer in the sidebar
# elapsed_time = int(time.time() - st.session_state.start_time)
# remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
# st.sidebar.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

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
#                     ["Not Relevant", "Partially Relevant", "Relevant"],  # Default: Not Relevant
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
#             action_plan = st.session_state.get(f"action_plan_{row['Goal']}_{sub_goal}", "")
#             summary_data.append({
#                 "Goal": row['Goal'],
#                 "Target": sub_goal,
#                 "Relevance": relevance,
#                 "Action Plan": action_plan
#             })

# summary_df = pd.DataFrame(summary_data, columns=["Goal", "Target", "Relevance", "Action Plan"])
# st.dataframe(summary_df)

# # Step 4: Action Planning
# st.header("4. Action Planning")
# st.write("Develop concrete plans for implementing the selected targets.")

# # Initialize empty action_plans if it does not exist
# if 'action_plans' not in st.session_state:
#     st.session_state['action_plans'] = {}

# # Display relevant and partially relevant targets for action planning
# for _, target in summary_df.iterrows():
#     if target['Relevance'] in ["Relevant", "Partially Relevant"]:
#         # Expandable section for each target
#         with st.expander(f"Action Plan for Target: {target['Target']}"):
#             # Add input fields
#             action_plan = st.text_area("", key=f"action_plan_{target['Goal']}_{target['Target']}")
#             st.session_state['action_plans'][f"{target['Goal']}_{target['Target']}"] = action_plan

# # Step 5: Review and Save Action Plans
# st.header("5. Save Action Plans")
# st.write("Download your action plans for future reference.")

# # Convert action plans to a DataFrame
# if 'action_plans' in st.session_state:
#     action_plans_df = pd.DataFrame(list(st.session_state['action_plans'].items()), columns=['Target', 'Action Plan'])
#     # Add button to download the action plans as a CSV file
#     csv = action_plans_df.to_csv(index=False).encode('utf-8')
#     st.download_button(
#         label="Download Action Plans as CSV",
#         data=csv,
#         file_name='action_plans.csv',
#         mime='text/csv'
#     )

# # Sidebar button to reset all information
# if st.sidebar.button("Reset Session"):
#     st.session_state.clear()
#     st.experimental_rerun()

import streamlit as st
import pandas as pd
import time
import ast
import io

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
st.write("- Whose voices counts in sustainability decisions?")
st.write("- How are the UN goals valid across borders? Locally and internationally?")

# Step 2: SDG Targets Review and Relevance Selection
st.header("2. SDG Targets Review and Relevance Selection")
st.write("Review all 17 SDGs and their targets, and select the relevance of each target to your project.")

# Initialize session state for timer
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Display timer in the sidebar
elapsed_time = int(time.time() - st.session_state.start_time)
remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
st.sidebar.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

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

# Step 3: Action Planning
st.header("3. Action Planning")
st.write("Develop concrete plans for implementing the selected targets.")

# Initialize empty action_plans if it does not exist
if 'action_plans' not in st.session_state:
    st.session_state['action_plans'] = {}

# Display relevant and partially relevant targets for action planning
for _, row in sdg_data.iterrows():
    for i, sub_goal in enumerate(row['Sub_goals']):
        relevance = st.session_state.get(f"target_relevance_{row['Goal']}_{i}", "Not Evaluated")
        if relevance in ["Relevant", "Partially Relevant"]:
            # Expandable section for each target
            with st.expander(f"Action Plan for Target: {sub_goal}"):
                # Add input fields
                action_plan = st.text_area("", key=f"action_plan_{row['Goal']}_{sub_goal}")
                st.session_state['action_plans'][f"{row['Goal']}_{sub_goal}"] = action_plan

# Step 4: Targets Summary
st.header("4. Targets Summary")
st.write("Here's a summary of all targets and their relevance:")

summary_data = []
for _, row in sdg_data.iterrows():
    if row['Sub_goals']:
        for i, sub_goal in enumerate(row['Sub_goals']):
            relevance = st.session_state.get(f"target_relevance_{row['Goal']}_{i}", "Not Evaluated")
            action_plan = st.session_state.get(f"action_plan_{row['Goal']}_{sub_goal}", "")
            summary_data.append({
                "Goal": row['Goal'],
                "Target": sub_goal,
                "Relevance": relevance,
                "Action Plan": action_plan
            })

summary_df = pd.DataFrame(summary_data, columns=["Goal", "Target", "Relevance", "Action Plan"])
st.dataframe(summary_df)

# Step 5: Save Action Plans
st.header("5. Save Action Plans")
st.write("Download your action plans for future reference.")

# Convert action plans to a DataFrame
if 'action_plans' in st.session_state:
    action_plans_df = pd.DataFrame(list(st.session_state['action_plans'].items()), columns=['Target', 'Action Plan'])
    # Add button to download the action plans as a CSV file
    csv = action_plans_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Action Plans as CSV",
        data=csv,
        file_name='action_plans.csv',
        mime='text/csv'
    )

# Sidebar button to reset all information
if st.sidebar.button("Reset Session"):
    st.session_state.clear()
    st.experimental_rerun()
  





