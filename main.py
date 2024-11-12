import openai
import streamlit as st
import os

# Fetch OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define ChatGPT interaction function with improved error handling
def get_chatgpt_response(user_input):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.write(f"Error: {e}")
        return "There was an error retrieving the response. Please try again."

# Initialize session state to track the selected page and sub-steps
if "page" not in st.session_state:
    st.session_state.page = "home"

# Back button function
def go_back():
    if "eating_goal" in st.session_state:
        del st.session_state["eating_goal"]
    if "lifestyle_goal" in st.session_state:
        del st.session_state["lifestyle_goal"]
    if "mindset_activity" in st.session_state:
        del st.session_state["mindset_activity"]
    st.session_state.page = "home"

# Homepage with title, prompt, and buttons to navigate to main features
if st.session_state.page == "home":
    st.title("Bentley Wellness Support")
    st.subheader("Welcome!")
    st.write("Select a wellness area to get started:")

    # Navigation buttons with session state updates
    if st.button("Healthy Eating"):
        st.session_state.page = "Healthy Eating"
    elif st.button("Healthy Lifestyle"):
        st.session_state.page = "Healthy Lifestyle"
    elif st.button("Healthy Mindsets"):
        st.session_state.page = "Healthy Mindsets"

# ---------------------- Healthy Eating Section ----------------------
if st.session_state.page == "Healthy Eating":
    st.header("Healthy Eating")
    st.write("Let’s start by understanding your dietary goals and helping you find balanced meals that fit your needs.")
    
    # Display goal buttons for Healthy Eating
    if "eating_goal" not in st.session_state:
        if st.button("Be more mindful about my diet"):
            st.session_state.eating_goal = "Mindful"
        elif st.button("Build muscle"):
            st.session_state.eating_goal = "Build Muscle"
        elif st.button("Lose fat"):
            st.session_state.eating_goal = "Lose Fat"
        elif st.button("Gain weight"):
            st.session_state.eating_goal = "Gain Weight"
        elif st.button("Maintain my physique"):
            st.session_state.eating_goal = "Maintain Physique"

    # Display information based on selected goal
    if "eating_goal" in st.session_state:
        goal_blurb = {
            "Mindful": "Mindful eating focuses on balance and portion control, helping you feel more energized and in tune with your body’s needs. Consistency is key to cultivating healthy habits that last.",
            "Build Muscle": "Building muscle requires a higher intake of protein to support muscle repair and growth. Consistency in your protein intake and workouts can fast-track your progress.",
            "Lose Fat": "To lose fat, a caloric deficit with a balanced intake of protein, carbs, and fats is essential. Staying consistent with this approach helps your body efficiently burn fat over time.",
            "Gain Weight": "Gaining weight healthily involves a caloric surplus with balanced nutrients. Focusing on protein and complex carbs ensures steady, sustainable gains when done consistently.",
            "Maintain Physique": "Maintaining your physique requires balanced macronutrients to support energy needs. Staying consistent helps your body remain steady and balanced."
        }
        st.write(goal_blurb[st.session_state.eating_goal])

        # Macronutrient Calculator prompt
        st.write("Once you have your macronutrients from the [Macro Calculator](https://www.calculator.net/macro-calculator.html), explore the daily menu to find food options that align with your intake goals.")
        if st.button("View Dining Options on Campus"):
            st.write("Explore today's meals at [Bentley Dining Services](https://bentley.sodexomyway.com/en-us/locations/the-921).")

        # ChatGPT for additional questions
        user_input_eating = st.text_input("Have a question about healthy eating?")
        if user_input_eating:
            response = get_chatgpt_response(user_input_eating)
            st.write(response)

    # Back Button
    if st.button("Back"):
        go_back()

# ---------------------- Healthy Lifestyle Section ----------------------
if st.session_state.page == "Healthy Lifestyle":
    st.header("Healthy Lifestyle")
    st.write("Staying active is a great way to support both mental and physical well-being. Let’s find activities that fit your lifestyle goals.")

    # Display goal buttons for Healthy Lifestyle
    if "lifestyle_goal" not in st.session_state:
        if st.button("Support my fitness and energy"):
            st.session_state.lifestyle_goal = "Fitness and Energy"
        elif st.button("Have fun and stay active"):
            st.session_state.lifestyle_goal = "Fun and Active"
        elif st.button("Try something new"):
            st.session_state.lifestyle_goal = "Try New"
        elif st.button("Build strength and endurance"):
            st.session_state.lifestyle_goal = "Strength and Endurance"

    # Display information based on selected activity goal
    if "lifestyle_goal" in st.session_state:
        activity_blurb = {
            "Fitness and Energy": "Engaging in cardio activities such as jogging, swimming, or brisk walking supports cardiovascular health and energy levels.",
            "Fun and Active": "Enjoy activities like joining an intramural team or spending time in outdoor spaces for a fun approach to fitness.",
            "Try New": "Explore new exercises like yoga or bodyweight training for a fresh approach to movement.",
     
