import streamlit as st
import pandas as pd
import time

# Load SDG data (you'd need to create this CSV file with goals and sub-goals)
@st.cache_data
def load_sdg_data():
    return pd.read_csv('sdg_data.csv')

sdg_data = load_sdg_data()

st.title("SDG Workshop Simulator")

# Step 1: Introduction and Warm-up
st.header("1. Introduction and Warm-up")
st.write("Discuss the following questions with your team:")
st.write("- How do you measure sustainability?")
st.write("- Whose vote counts in sustainability decisions?")
st.write("- How are the UN goals valid across borders? Locally and internationally?")

# Step 2: SDG and Sub-goal Review
st.header("2. SDG and Sub-goal Review (60 minutes)")
st.write("Review all 17 SDGs and 169 sub-goals in the next hour.")

# Initialize session state for timer
if 'start_time' not in st.session_state:
    st.session_state.start_time = time.time()

# Display timer
elapsed_time = int(time.time() - st.session_state.start_time)
remaining_time = max(3600 - elapsed_time, 0)  # 3600 seconds = 1 hour
st.write(f"Time remaining: {remaining_time // 60} minutes {remaining_time % 60} seconds")

# Display SDGs and sub-goals
for _, row in sdg_data.iterrows():
    with st.expander(f"{row['Goal']}"):
        st.write(row['Description'])
        st.write("Sub-goals:")
        sub_goals = eval(row['Sub_goals'])  # Assuming sub-goals are stored as a string representation of a list
        for sub_goal in sub_goals:
            st.write(f"- {sub_goal}")

# SDG Selection
selected_sdgs = st.multiselect(
    "Select relevant SDGs for your project:",
    sdg_data['Goal'].unique()
)

# Step 3: Goal Prioritization
if selected_sdgs:
    st.header("3. Goal Prioritization")
    st.write("Prioritize the selected SDGs by dragging them into order.")
    prioritized_sdgs = st.multiselect(
        "Prioritize SDGs:",
        selected_sdgs,
        default=selected_sdgs
    )

    # Step 4: Action Planning
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
    st.warning("Please select at least one SDG to continue.")
