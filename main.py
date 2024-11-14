import openai
import streamlit as st
import os
import random

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

# Initialize session state for navigation and selections
if "page" not in st.session_state:
    st.session_state.page = "home"
if "lifestyle_goal" not in st.session_state:
    st.session_state.lifestyle_goal = None

# Define a function to set page and reset selections
def set_page(page):
    st.session_state.page = page
    st.session_state.lifestyle_goal = None

# Define a function to return to the homepage
def return_to_homepage():
    set_page("home")

# Define function to navigate back within Healthy Lifestyle section
def go_back():
    st.session_state.lifestyle_goal = None

# Home page with options to navigate to main features
if st.session_state.page == "home":
    st.title("WellNest")
    st.subheader("Welcome!")
    st.write("Select a wellness area to get started:")

    # Navigation buttons
    if st.button("Healthy Eating", on_click=set_page, args=("Healthy Eating",)):
        pass
    if st.button("Healthy Lifestyle", on_click=set_page, args=("Healthy Lifestyle",)):
        pass
    if st.button("Healthy Mindsets", on_click=set_page, args=("Healthy Mindsets",)):
        pass

# ---------------------- Healthy Eating Section ----------------------
if st.session_state.page == "Healthy Eating":
    st.header("Healthy Eating")
    st.write("Healthy eating is a foundation for wellness. Here are some resources to help you make informed nutritional choices based on your goals.")

    # Prompt user to select a goal for personalized recommendations
    st.subheader("What's Your Nutrition Goal?")
    nutrition_goal = st.selectbox("Choose your goal:", ["Select a goal", "Gain Muscle", "Lose Weight", "Maintain Weight", "Be Mindful of Diet"])

    # Provide goal-specific information
    if nutrition_goal != "Select a goal":
        st.write(f"### Goal: {nutrition_goal}")
        goal_info = {
            "Gain Muscle": "Increasing protein intake supports muscle recovery and growth. Consistency in diet and strength training is key!",
            "Lose Weight": "Focusing on a calorie deficit along with balanced macronutrients can aid in fat loss while preserving muscle.",
            "Maintain Weight": "Eating a balanced mix of macronutrients supports steady energy and optimal body function.",
            "Be Mindful of Diet": "Choosing nutrient-dense foods promotes overall wellness and helps you meet your daily nutrition needs."
        }
        st.write(goal_info[nutrition_goal])

    # Embed the macronutrient calculator with height 780
    st.write("Use the macronutrient calculator below to calculate your specific macronutrient needs based on height, weight, and activity level.")
    st.components.v1.iframe("https://www.calculator.net/macro-calculator.html", height=780, width=700)

    # Link to campus dining options
    st.write("Once you know your macronutrient needs, check out [Bentley University Dining Services](https://bentley.sodexomyway.com/en-us/locations/the-921) for menu options that align with your goals.")

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
        "Get Active": "Engage in leisurely, low-intensity activities like walking, yoga, or swimming to gently improve fitness at your own pace."
    }

    # Display buttons and descriptions with dynamic sizing
    if not st.session_state.lifestyle_goal:
        st.write("**Choose Your Goal:**")
        for goal, description in goal_options.items():
            col1, col2 = st.columns([1, 6])  # Adjust spacing to position descriptions correctly
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
                "resource": f"[Dana Center](https://events.bentley.edu/dana_center_331)",
                "location": "Lower Campus",
                "hours": """
                Fitness Center:
                - Monday: 7am - 11pm
                - Tuesday: 7am - 11pm
                - Wednesday: 7am - 11pm
                - Thursday: 7am - 11pm
                - Friday: 7am - 7pm
                - Saturday: 9am - 7pm
                - Sunday: 9am - 11pm
                """,
                "suggestion": "Building strength involves exercises focused on muscle endurance and power. Here are some activities to try:",
                "options": ["Weightlifting", "Push-ups", "Squats", "Deadlifts"],
                "prompt": "Create a workout plan for strength training using both weights and bodyweight exercises."
            },
            "Increase Endurance": {
                "resource": f"[Dana Center](https://events.bentley.edu/dana_center_331)",
                "location": "Lower Campus",
                "hours": """
                Fitness Center:
                - Monday: 7am - 11pm
                - Tuesday: 7am - 11pm
                - Wednesday: 7am - 11pm
                - Thursday: 7am - 11pm
                - Friday: 7am - 7pm
                - Saturday: 9am - 7pm
                - Sunday: 9am - 11pm

                Pool:
                - Monday & Wednesday: 7am-9am, 11am-1pm, 8:15pm-10:15pm
                - Tuesday & Thursday: 11am-1pm, 8:15pm-10:15pm
                - Friday: 7am-9am, 11am-1pm
                - Saturday: 12pm - 3pm
                - Sunday: 12pm - 4pm
                """,
                "suggestion": "Endurance training helps build stamina. Consider trying these cardio-focused exercises:",
                "options": ["Running on treadmill", "Cycling", "Stair climbing", "Swimming"],
                "prompt": "Create a cardio workout plan focused on building endurance."
            },
            "Just Getting Started": {
                "resource": f"[Dana Center](https://events.bentley.edu/dana_center_331)",
                "location": "Lower Campus",
                "hours": """
                Fitness Center:
                - Monday: 7am - 11pm
                - Tuesday: 7am - 11pm
                - Wednesday: 7am - 11pm
                - Thursday: 7am - 11pm
                - Friday: 7am - 7pm
                - Saturday: 9am - 7pm
                - Sunday: 9am - 11pm

                Pool:
                - Monday & Wednesday: 7am-9am, 11am-1pm, 8:15pm-10:15pm
                - Tuesday & Thursday: 11am-1pm, 8:15pm-10:15pm
                - Friday: 7am-9am, 11am-1pm
                - Saturday: 12pm - 3pm
                - Sunday: 12pm - 4pm
                """,
                "suggestion": "If you're new to exercise, try these beginner-friendly activities to get started:",
                "options": ["Light cardio", "Bodyweight exercises", "Stretching", "Swimming", "Group sports"],
                "prompt": "Suggest beginner-friendly workouts for strength, endurance, and team-based activities."
            },
            "Join a Team or Group Activity": {
                "resource": "Dana Center",
                "location": "Lower Campus",
                "hours": "Check the schedule for intramural activities.",
                "suggestion": "Joining a group activity can make exercise fun and social. Current offerings include:",
                "options": ["Co-ed & Men's Soccer", "Flag Football", "Ultimate Frisbee", "Men's and Women's Basketball", "Co-ed Volleyball", "Recreational Events"],
                "learn_more_url": "https://bentley.dserec.com/online/intramurals_widget"
            },
            "Get Active": {
                "resource": f"[Dana Center](https://events.bentley.edu/dana_center_331)",
                "location": "Lower Campus",
                "hours": """
                Fitness Center:
                - Monday: 7am - 11pm
                - Tuesday: 7am - 11pm
                - Wednesday: 7am - 11pm
                - Thursday: 7am - 11pm
                - Friday: 7am - 7pm
                - Saturday: 9am - 7pm
                - Sunday: 9am - 11pm

                Pool:
                - Monday & Wednesday: 7am-9am, 11am-1pm, 8:15pm-10:15pm
                - Tuesday & Thursday: 11am-1pm, 8:15pm-10:15pm
                - Friday: 7am-9am, 11am-1pm
                - Saturday: 12pm - 3pm
                - Sunday: 12pm - 4pm
                """,
                "suggestion": "Engage in a variety of physical activities, from swimming to team sports to light cardio.",
                "options": ["Walking", "Yoga", "Swimming", "Stretching", "Cycling"],
                "prompt": "Suggest low-intensity, leisurely activities to help someone get active."
            }
        }

        # Display resource details, suggestion, and options
        resource_info = resources_suggestions[goal]
        st.subheader(f"{resource_info['resource']}")
        st.write(f"**Location**: {resource_info['location']}")
        st.write("**Hours:**")
        st.write(resource_info['hours'])
        st.write(resource_info["suggestion"])
        st.write("**Activities to Try:**")
        st.write("- " + "\n- ".join(resource_info["options"]))

        # Generate a workout plan or Learn More button based on goal
        if goal == "Join a Team or Group Activity":
            st.markdown(
                f'<a href="{resource_info["learn_more_url"]}" target="_blank"><button>Learn More</button></a>',
                unsafe_allow_html=True
            )
        else:
            if st.button("Generate a Workout Plan"):
                workout_plan = get_chatgpt_response(resource_info["prompt"], max_tokens=75)
                st.write(workout_plan)

        # ChatGPT for additional fitness questions
        user_input_lifestyle = st.text_input("Have a question about fitness or staying active?")
        if user_input_lifestyle:
            response = get_chatgpt_response(user_input_lifestyle, max_tokens=50)
            st.write(response)

        # Back button to reset the goal selection
        if st.button("Back", on_click=go_back):
            pass

        # Option to return to the homepage
        if st.button("Back to Homepage", key="return_home_lifestyle"):
            return_to_homepage()

# ---------------------- Healthy Mindsets Section ----------------------
if st.session_state.page == "Healthy Mindsets":
    st.header("Healthy Mindsets")
    st.write("A healthy mind is essential for overall well-being. Let us help you find resources that match your mood.")

    # Mood selection prompt
    st.subheader("How are you feeling today?")
    mood_option = st.selectbox(
        "Describe your current mood to find suitable resources:",
        ["Select an option", "Feeling Stressed", "Having Trouble Sleeping", "Need to Clear My Mind"]
    )

    # Define categorized YouTube links
    video_links = {
        "Need to Clear My Mind": [
            "https://www.youtube.com/watch?v=tqhxMUm7XXU",
            "https://www.youtube.com/watch?v=QHkXvPq2pQE",
            "https://www.youtube.com/watch?v=BVZS8XqNyEY"
        ],
        "Having Trouble Sleeping": [
            "https://www.youtube.com/watch?v=g0jfhRcXtLQ",
            "https://www.youtube.com/watch?v=U6Ay9v7gK9w",
            "https://www.youtube.com/watch?v=DBhadQTCBeo"
        ],
        "Feeling Stressed": [
            "https://www.youtube.com/watch?v=DbDoBzGY3vo",
            "https://www.youtube.com/watch?v=LiUnFJ8P4gM",
            "https://www.youtube.com/watch?v=LU6Oi80n5J4"
        ]
    }

    # Display resources based on selected mood
    if mood_option in video_links:
        st.write(f"### Suggested {mood_option} Resource:")
        selected_video = random.choice(video_links[mood_option])
        st.video(selected_video)

    # Additional university resources for mental health support
    st.write("### Additional Support Resources")
    st.write("For personalized support, you can schedule an appointment with our Counseling Center or explore BetterMynd services.")
    st.markdown(
        "[**Schedule a Counseling Appointment**](https://www.bentley.edu/university-life/student-health/counseling-center-appointment)",
        unsafe_allow_html=True
    )
    st.markdown(
        "[**Learn more about Bentley's Counseling Center**](https://www.bentley.edu/university-life/student-health/counseling-center)",
        unsafe_allow_html=True
    )
    print(""^100)

    # Return to Homepage button
    if st.button("Back to Homepage"):
        return_to_homepage()
