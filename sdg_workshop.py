import streamlit as st
import pandas as pd

# Load SDG data (you'd need to create this CSV file)
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
st.write("- How are the UN goals valid across borders?")

# Step 2: SDG Selection
st.header("2. SDG Selection")
st.write("Review the 17 SDGs and select the most relevant ones for your project.")

selected_sdgs = st.multiselect(
    "Select relevant SDGs:",
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
        st.success("Thank you for your reflection!")

else:
    st.warning("Please select at least one SDG to continue.")
