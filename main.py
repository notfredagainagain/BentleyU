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
    # Display the logo at the top of the app
    st.image("WN_logo.png", width=500)  # Adjust the path and width as needed
    
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
    st.write("Eating well is essential to achieving wellness goals. Select a nutrition goal below, and we’ll guide you with helpful resources and tools.")

    # Nutrition goal selection prompt
    st.subheader("What's your Nutrition Goal?")
    nutrition_goal = st.selectbox(
        "Choose your goal to get started:",
        ["Select a goal", "Be Mindful of Diet", "Gain Muscle", "Lose Weight", "Maintain Weight"]
    )

    # Define goal-specific information
    goal_info = {
        "Be Mindful of Diet": "Eating mindfully involves paying attention to your body’s hunger and fullness cues and choosing foods that provide nourishment. Focus on whole, unprocessed foods that give you the energy to get through the day. Incorporate a variety of food groups—such as fruits, vegetables, whole grains, and lean proteins—to ensure you're meeting your nutritional needs. Mindful eating can reduce stress, improve digestion, and help you develop a positive relationship with food over time.",
        "Gain Muscle": "Building muscle requires an increased intake of protein to support muscle recovery and growth. Consuming protein after workouts and spacing it throughout the day aids muscle synthesis. Carbohydrates are also essential to fuel workouts and replenish energy stores, while healthy fats help with hormone production, supporting muscle growth. Focus on nutrient-dense foods that fuel your training and aim for consistent meal timing to optimize your results.",
        "Lose Weight": "Losing weight involves creating a calorie deficit, meaning you consume fewer calories than you burn. Prioritizing protein can help preserve muscle mass during weight loss, while high-fiber foods like vegetables and whole grains help you feel fuller longer. Choosing complex carbohydrates and healthy fats in moderate amounts will provide steady energy. Consistency in eating balanced meals and avoiding processed foods can make a significant difference in reaching and maintaining your goals.",
        "Maintain Weight": "Maintaining weight requires a balanced intake of macronutrients to support steady energy levels and overall health. A mix of protein, complex carbohydrates, and healthy fats will help stabilize your blood sugar and prevent energy crashes. Staying mindful of portion sizes and choosing nutrient-dense foods, such as lean proteins, whole grains, and a variety of fruits and vegetables, will support ongoing health and well-being."
    }

    # Display resources and suggestions based on selected goal
    if nutrition_goal != "Select a goal" and nutrition_goal in goal_info:
        st.write(f"### Goal: {nutrition_goal}")
        st.write(goal_info[nutrition_goal])

        # Macronutrient calculator instructions and calculator
        st.write("Use the macronutrient calculator below to calculate your specific macronutrient needs based on height, weight, and activity level.")
        st.components.v1.iframe("https://www.calculator.net/macro-calculator.html", height=780, width=700)

        # Link to campus dining services
        st.write("Once you have your macronutrient needs, explore the [Bentley University Dining Services](https://bentley.sodexomyway.com/en-us/locations/the-921) to find meals that fit your goals.")

    # Additional campus resources
    st.write("### Additional Nutrition Support")
    st.write("For personalized dietary advice, consider scheduling a session with our on-campus dietitian.")
    st.markdown(
        "[**Book a Session with the Dietitian**](https://outlook.office365.com/book/HayleyRuffRDLDN@sodexo.onmicrosoft.com/)",
        unsafe_allow_html=True
    )

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
        "Endurance Training": "Focus on cardio activities to improve stamina and overall cardiovascular health.",
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
    st.markdown("<br><br>", unsafe_allow_html=True)


    # Return to Homepage button
    if st.button("Back to Homepage"):
        return_to_homepage()
