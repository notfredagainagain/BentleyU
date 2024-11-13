import openai
import streamlit as st
import os

# Fetch OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# ChatGPT interaction function using ChatCompletion API with token limit
def get_chatgpt_response(user_input, max_tokens=50):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=max_tokens
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"There was an error retrieving the response: {e}"

# Initialize session state to track the selected page and sub-steps
if "page" not in st.session_state:
    st.session_state.page = "home"
if "lifestyle_goal" not in st.session_state:
    st.session_state.lifestyle_goal = None

# Define a function to reset the session state and navigate to the homepage
def return_to_homepage():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.page = "home"

# Define a back button function to go to the previous page
def go_back():
    st.session_state.lifestyle_goal = None

# Homepage with title, prompt, and buttons to navigate to main features
if st.session_state.page == "home":
    st.title("WellNest")
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
    st.write("Let's calculate your macronutrient needs to support your health goals.")
    
    # Embed the macronutrient calculator
    st.components.v1.iframe("https://www.calculator.net/macro-calculator.html", height=850, width=700)

    # Return to Homepage button
    if st.button("Back to Homepage"):
        return_to_homepage()

# ---------------------- Healthy Lifestyle Section ----------------------
if st.session_state.page == "Healthy Lifestyle":
    st.header("Healthy Lifestyle")
    st.write("Staying active is a great way to support both mental and physical well-being. Let’s find activities that fit your lifestyle goals.")

    # Define goal options with descriptions
    goal_options = {
        "Build Strength": "Increase your muscle strength and endurance through weightlifting or bodyweight exercises.",
        "Increase Endurance": "Focus on cardio activities to improve stamina and overall cardiovascular health.",
        "Just Getting Started": "New to exercise? Start with a variety of light activities across strength, endurance, and fun group sports.",
        "Join a Team or Group Activity": "Looking for a social workout? Join a team or group sport for a fun, interactive way to stay active.",
        "Get Active": "Engage in leisurely, low-intensity activities like walking or yoga to gently improve fitness at your own pace."
    }

    # Display buttons and descriptions if no goal is selected yet
    if not st.session_state.lifestyle_goal:
        st.write("**Choose Your Goal:**")
        for goal, description in goal_options.items():
            col1, col2 = st.columns([1, 4])
            with col1:
                if st.button(goal):
                    st.session_state.lifestyle_goal = goal
            with col2:
                st.write(description)

    # Provide resources and exercise suggestions based on selected goal
    if st.session_state.lifestyle_goal:
        goal = st.session_state.lifestyle_goal
        st.write(f"You selected: **{goal}**")

        # Define resources and suggestions based on the selected goal
        resources_suggestions = {
            "Build Strength": {
                "resource": f"[Dana Center Fitness Center](https://events.bentley.edu/dana_center_331)",
                "location": "Lower Campus",
                "hours": "Sunday 9am-11pm\nMonday-Thursday 7am-11pm\nFriday 7am-7pm\nSaturday 9am-7pm",
                "suggestion": "You can focus on strength training with weights or bodyweight exercises. Options include weightlifting, push-ups, and bodyweight exercises to build strength.",
                "prompt": "Create a workout plan for strength training using both weights and bodyweight exercises."
            },
            "Increase Endurance": {
                "resource": f"[Dana Center Fitness Center - Cardio Section](https://events.bentley.edu/dana_center_331)",
                "location": "Lower Campus",
                "hours": "Sunday 9am-11pm\nMonday-Thursday 7am-11pm\nFriday 7am-7pm\nSaturday 9am-7pm",
                "suggestion": "Try cardio activities like running on the treadmill, cycling, or stair climbing to boost stamina and endurance.",
                "prompt": "Create a cardio workout plan focused on building endurance."
            },
            "Just Getting Started": {
                "resource": f"[Dana Center Fitness Center](https://events.bentley.edu/dana_center_331) & Campus Facilities",
                "location": "Lower Campus",
                "hours": "Fitness Center: Sunday 9am-11pm\nMonday-Thursday 7am-11pm\nFriday 7am-7pm\nSaturday 9am-7pm\n"
                          "Pool: Mon/Wed 7am-9am, 11am-1pm, 8:15pm-10:15pm\nTues/Thurs 11am-1pm, 8:15pm-10:15pm\n"
                          "Friday 7am-9am, 11am-1pm\nSaturday 12pm-3pm\nSunday 12pm-4pm",
                "suggestion": "Explore options like light cardio, weightlifting, bodyweight exercises, or even team sports to find what you enjoy most and get moving.",
                "prompt": "Suggest beginner-friendly workouts for strength, endurance, and team-based activities."
            },
            "Join a Team or Group Activity": {
                "resource": "Intramural and Club Sports",
                "location": "Varies by sport",
                "hours": "Varies by sport",
                "suggestion": "Join a recreational team or club to enjoy social fitness activities like basketball, soccer, or hiking clubs.",
                "prompt": "List team sports or group activities that promote social interaction and fitness."
            },
            "Get Active": {
                "resource": f"[Dana Center Pool](https://events.bentley.edu/dana_center_pool_996) and Green Spaces",
                "location": "Lower Campus",
                "hours": "Pool: Mon/Wed 7am-9am, 11am-1pm, 8:15pm-10:15pm\nTues/Thurs 11am-1pm, 8:15pm-10:15pm\n"
                          "Friday 7am-9am, 11am-1pm\nSaturday 12pm-3pm\nSunday 12pm-4pm",
                "suggestion": "Engage in low-intensity activities like walking, stretching, or swimming in the Dana Center Pool to gently improve fitness and stay active.",
                "prompt": "Suggest low-intensity, leisurely activities to help someone get active."
            }
        }

        # Display resource details and suggestion
        resource_info = resources_suggestions[goal]
        st.subheader(f"Resource: {resource_info['resource']}")
        st.write(f"**Location**: {resource_info['location']}")
        st.write(f"**Hours**:\n{resource_info['hours']}")
        st.write(f"**Suggested Exercise**: {resource_info['suggestion']}")

        # Generate a workout plan based on user goal and resource
        if st.button("Generate a Workout Plan"):
            workout_plan = get_chatgpt_response(resource_info["prompt"], max_tokens=75)
            st.write(workout_plan)

        # ChatGPT for additional fitness questions
        user_input_lifestyle = st.text_input("Have a question about fitness or staying active?")
        if user_input_lifestyle:
            response = get_chatgpt_response(user_input_lifestyle, max_tokens=50)
            st.write(response)

        # Back button to reset the goal selection
        if st.button("Back"):
            go_back()

        # Option to return to the homepage
        st.write("")  # Add space
        if st.button("Back to Homepage", key="return_home_lifestyle"):
            return_to_homepage()
