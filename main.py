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
    
    # Embed the macronutrient calculator with height 800
    st.components.v1.iframe("https://www.calculator.net/macro-calculator.html", height=800, width=700)

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
        # Set a uniform button width
        button_width = "200px"
        for goal, description in goal_options.items():
            col1, col2 = st.columns([1, 4])
            with col1:
                button = st.button(goal, key=goal, help=description)
                st.markdown(
                    f"""
                    <style>
                    div.stButton > button:first-child {{
                        width: {button_width};
                        text-align: center;
                    }}
                    </style>
                    """, 
                    unsafe_allow_html=True
                )
                if button:
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
                "hours": """
                | Day       | Time              |
                |-----------|-------------------|
                | Sunday    | 9am - 11pm       |
                | Monday    | 7am - 11pm       |
                | Tuesday   | 7am - 11pm       |
                | Wednesday | 7am - 11pm       |
                | Thursday  | 7am - 11pm       |
                | Friday    | 7am - 7pm        |
                | Saturday  | 9am - 7pm        |
                """,
                "suggestion": "Building strength involves exercises focused on muscle endurance and power. Here are some activities to try:",
                "options": ["Weightlifting", "Push-ups", "Squats", "Deadlifts"],
                "prompt": "Create a workout plan for strength training using both weights and bodyweight exercises."
            },
            "Increase Endurance": {
                "resource": f"[Dana Center Fitness Center - Cardio Section](https://events.bentley.edu/dana_center_331)",
                "location": "Lower Campus",
                "hours": """
                | Day       | Time              |
                |-----------|-------------------|
                | Sunday    | 9am - 11pm       |
                | Monday    | 7am - 11pm       |
                | Tuesday   | 7am - 11pm       |
                | Wednesday | 7am - 11pm       |
                | Thursday  | 7am - 11pm       |
                | Friday    | 7am - 7pm        |
                | Saturday  | 9am - 7pm        |
                """,
                "suggestion": "Endurance training helps build stamina. Consider trying these cardio-focused exercises:",
                "options": ["Running on treadmill", "Cycling", "Stair climbing", "Swimming"],
                "prompt": "Create a cardio workout plan focused on building endurance."
            },
            "Just Getting Started": {
                "resource": f"[Dana Center Fitness Center](https://events.bentley.edu/dana_center_331) & Campus Facilities",
                "location": "Lower Campus",
                "hours": """
                | Facility           | Day          | Time                  |
                |--------------------|--------------|-----------------------|
                | Fitness Center     | See Above    |                       |
                | Pool               | Monday       | 7am-9am, 11am-1pm, 8:15pm-10:15pm |
                |                    | Tuesday      | 11am-1pm, 8:15pm-10:15pm |
                |                    | Wednesday    | 7am-9am, 11am-1pm, 8:15pm-10:15pm |
                |                    | Thursday     | 11am-1pm, 8:15pm-10:15pm |
                |                    | Friday       | 7am-9am, 11am-1pm    |
                |                    | Saturday     | 12pm - 3pm           |
                |                    | Sunday       | 12pm - 4pm           |
                """,
                "suggestion": "If you're new to exercise, try these beginner-friendly activities to get started:",
                "options": ["Light cardio", "Bodyweight exercises", "Stretching", "Group sports"],
                "prompt": "Suggest beginner-friendly workouts for strength, endurance, and team-based activities."
            },
            "Join a Team or Group Activity": {
                "resource": "Intramural and Club Sports",
                "location": "Varies by sport",
                "hours": "Varies by sport",
                "suggestion": "Joining a group activity can make exercise fun and social. Some options include:",
                "options": ["Basketball", "Soccer", "Volleyball", "Hiking clubs"],
                "prompt": "List team sports or group activities that promote social interaction and fitness."
            },
            "Get Active": {
                "resource": f"[Dana Center Pool](https://events.bentley.edu/dana_center_pool_996) and Green Spaces",
                "location": "Lower Campus",
                "hours": """
                | Day       | Time                  |
                |-----------|----------------------|
                | Monday    | 7am-9am, 11am-1pm, 8:15pm-10:15pm |
                | Tuesday   | 11am-1pm, 8:15pm-10:15pm |
                | Wednesday | 7am-9am, 11am-1pm, 8:15pm-10:15pm |
                | Thursday  | 11am-1pm, 8:15pm-10:15pm |
                | Friday    | 7am-9am, 11am-1pm    |
                | Saturday  | 12pm - 3pm           |
                | Sunday    | 12pm - 4pm           |
                """,
                "suggestion": "Low-intensity activities are a great way to stay active without overexertion. Try these:",
                "options": ["Walking", "Yoga", "Swimming", "Stretching"],
                "prompt": "Suggest low-intensity, leisurely activities to help someone get active."
            }
        }

        # Display resource details, suggestion, and options
        resource_info = resources_suggestions[goal]
        st.subheader(f"Resource: {resource_info['resource']}")
        st.write(f"**Location**: {resource_info['location']}")
        st.write(f"**Hours**:\n{resource_info['hours']}")
        st.write(resource_info["suggestion"])
        st.write("**Activities to Try:**")
        st.write(", ".join(resource_info["options"]))

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
