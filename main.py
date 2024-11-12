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
        st.write(f"Error: {e}")
        return "There was an error retrieving the response. Please try again."

# Initialize session state to track the selected page and sub-steps
if "page" not in st.session_state:
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
            st.session_state.page = "Eating Goal"
        elif st.button("Build muscle"):
            st.session_state.eating_goal = "Build Muscle"
            st.session_state.page = "Eating Goal"
        elif st.button("Lose fat"):
            st.session_state.eating_goal = "Lose Fat"
            st.session_state.page = "Eating Goal"
        elif st.button("Gain weight"):
            st.session_state.eating_goal = "Gain Weight"
            st.session_state.page = "Eating Goal"
        elif st.button("Maintain my physique"):
            st.session_state.eating_goal = "Maintain Physique"
            st.session_state.page = "Eating Goal"

    # Display information based on selected goal
    if st.session_state.page == "Eating Goal":
        if st.session_state.eating_goal == "Mindful":
            st.write("Mindful eating involves choosing foods that nourish your body and practicing portion control.")
        elif st.session_state.eating_goal == "Build Muscle":
            st.write("To build muscle, focus on a higher protein intake to support muscle repair and growth.")
        elif st.session_state.eating_goal == "Lose Fat":
            st.write("Losing fat often involves a caloric deficit combined with a balance of protein, carbs, and fats.")
        elif st.session_state.eating_goal == "Gain Weight":
            st.write("Gaining weight healthily involves a caloric surplus with balanced nutrients.")
        elif st.session_state.eating_goal == "Maintain Physique":
            st.write("Maintaining your physique requires a balanced intake to support your energy needs.")

        # Option to use the macronutrient calculator
        st.write("Use the [Macro Calculator](https://www.calculator.net/macro-calculator.html) to determine your daily needs.")
        if st.button("View Dining Options on Campus"):
            st.write("Explore today's meals at [Bentley Dining Services](https://bentley.sodexomyway.com/en-us/locations/the-921).")

        # ChatGPT for additional questions
        user_input_eating = st.text_input("Have a question about healthy eating?")
        if user_input_eating:
            response = get_chatgpt_response(user_input_eating)
            st.write(response)

        # Cross-Topic Prompt
        if st.button("Explore Healthy Lifestyle"):
            st.session_state.page = "Healthy Lifestyle"

# ---------------------- Healthy Lifestyle Section ----------------------
if st.session_state.page == "Healthy Lifestyle":
    st.header("Healthy Lifestyle")
    st.write("Staying active is a great way to support both mental and physical well-being. Let’s find activities that fit your lifestyle goals.")

    # Display goal buttons for Healthy Lifestyle
    if "lifestyle_goal" not in st.session_state:
        if st.button("Support my fitness and energy"):
            st.session_state.lifestyle_goal = "Fitness and Energy"
            st.session_state.page = "Lifestyle Goal"
        elif st.button("Have fun and stay active"):
            st.session_state.lifestyle_goal = "Fun and Active"
            st.session_state.page = "Lifestyle Goal"
        elif st.button("Try something new"):
            st.session_state.lifestyle_goal = "Try New"
            st.session_state.page = "Lifestyle Goal"
        elif st.button("Build strength and endurance"):
            st.session_state.lifestyle_goal = "Strength and Endurance"
            st.session_state.page = "Lifestyle Goal"

    # Display information based on selected activity goal
    if st.session_state.page == "Lifestyle Goal":
        if st.session_state.lifestyle_goal == "Fitness and Energy":
            st.write("- **Cardio**: Take a walk or run on the campus track.")
            st.write("- **Pool**: Swim at the [campus pool](https://events.bentley.edu/dana_center_pool_996).")
        elif st.session_state.lifestyle_goal == "Fun and Active":
            st.write("- **Intramural Sports**: Join [intramural teams](https://bentleyfalcons.com/sports/2024/6/11/intramural-sports-schedules-standings.aspx).")
            st.write("- **Outdoor Activities**: Enjoy the green spaces around campus.")
        elif st.session_state.lifestyle_goal == "Try New":
            st.write("- **Yoga**: Try yoga or stretching routines outdoors.")
            st.write("- **Active Breaks**: Take the stairs or do a quick stretch.")
        elif st.session_state.lifestyle_goal == "Strength and Endurance":
            st.write("- **Strength Training**: Use the [Dana Center Gym](https://events.bentley.edu/dana_center_331) for strength-building exercises.")
            st.write("- **Bodyweight Exercises**: Practice calisthenics or bodyweight routines on campus.")

        # ChatGPT for additional fitness questions
        user_input_lifestyle = st.text_input("Have a question about fitness or staying active?")
        if user_input_lifestyle:
            response = get_chatgpt_response(user_input_lifestyle)
            st.write(response)

        # Cross-Topic Prompt
        if st.button("Explore Healthy Eating"):
            st.session_state.page = "Healthy Eating"

# ---------------------- Healthy Mindsets Section ----------------------
if st.session_state.page == "Healthy Mindsets":
    st.header("Healthy Mindsets")
    st.write("Mental well-being is essential. Explore these resources to support calmness, focus, and a positive outlook.")

    # Display buttons for mental wellness activity
    if "mindset_activity" not in st.session_state:
        if st.button("Guided relaxation exercise"):
            st.session_state.mindset_activity = "Relaxation"
            st.session_state.page = "Mindset Activity"
        elif st.button("Breathing techniques"):
            st.session_state.mindset_activity = "Breathing"
            st.session_state.page = "Mindset Activity"
        elif st.button("Self-reflection and gratitude"):
            st.session_state.mindset_activity = "Self-Reflection"
            st.session_state.page = "Mindset Activity"

    # Display information based on selected activity
    if st.session_state.page == "Mindset Activity":
        if st.session_state.mindset_activity == "Relaxation":
            st.write("Try this [guided meditation](https://www.youtube.com/watch?v=ZToicYcHIOU) for relaxation.")
        elif st.session_state.mindset_activity == "Breathing":
            st.write("Practice calming techniques like [4-7-8 breathing](https://youtu.be/DbDoBzGY3vo?si=xWVePxgCv6NJVhM-).")
        elif st.session_state.mindset_activity == "Self-Reflection":
            st.write("Start a gratitude journal or reflect on positive moments in your day.")

        # Option for counseling support
        if st.button("Need additional support?"):
            st.write("Consider talking to someone at the [Bentley Counseling Center](https://www.bentley.edu/university-life/student-health/counseling-center).")

        # ChatGPT for mental well-being questions
        user_input_mindsets = st.text_input("Have a question about mental well-being?")
        if user_input_mindsets:
            response = get_chatgpt_response(user_input_mindsets)
            st.write(response)

        # Cross-Topic Prompt
        if st.button("Explore Healthy Lifestyle"):
            st.session_state.page = "Healthy Lifestyle"
