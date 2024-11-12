import openai
import streamlit as st
import os

# Fetch OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define ChatGPT interaction function
def get_chatgpt_response(user_input):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "There was an error retrieving the response. Please try again."

# Initialize session state to track the selected page
if "page" not in st.session_state:
    st.session_state.page = "home"

# Homepage with title, prompt, and buttons to navigate to main features
if st.session_state.page == "home":
    st.title("Bentley Wellness Support")
    st.subheader("Welcome!")
    st.write("Select a wellness area to get started:")

    # Navigation buttons
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

    # Step 1: Select Dietary Goal
    goal = st.radio("What is your main dietary goal?", 
                    ["Be more mindful about my diet", "Build muscle", "Lose fat", "Gain weight", "Maintain my physique"])
    
    # Display relevant information and macronutrient guidance based on 
