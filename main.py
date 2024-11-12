# main.py

import openai
import streamlit as st
import os

# Fetch OpenAI API key from environment variables
openai.api_key = os.getenv("OPEN_AI_KEY")

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

# Main App Structure
st.title("Bentley Wellness Support")

# Initial Prompt for Choosing a Wellness Area
st.subheader("What would you like to focus on today?")
main_option = st.selectbox("Choose an area", ["Healthy Eating", "Healthy Lifestyle", "Healthy Mindsets"])

# ---------------------- Healthy Eating Section ----------------------
if main_option == "Healthy Eating":
    st.header("Healthy Eating")
    st.write("Let’s start by understanding your dietary goals and helping you find balanced meals that fit your needs.")

    # Step 1: Select Dietary Goal
    goal = st.radio("What is your main dietary goal?", 
                    ["Be more mindful about my diet", "Build muscle", "Lose fat", "Gain weight", "Maintain my physique"])
    
    # Display relevant information and macronutrient guidance based on goal
    if goal == "Be more mindful about my diet":
        st.write("Mindful eating involves choosing foods that nourish your body and practicing portion control.")
    elif goal == "Build muscle":
        st.write("To build muscle, focus on a higher protein intake to support muscle repair and growth.")
    elif goal == "Lose fat":
        st.write("Losing fat often involves a caloric deficit combined with a balance of protein, carbs, and fats.")
    elif goal == "Gain weight":
        st.write("Gaining weight healthily involves a caloric surplus with balanced nutrients.")
    elif goal == "Maintain my physique":
        st.write("Maintaining your physique requires a balanced intake to support your energy needs.")

    # Step 2: Macronutrient Calculator
    st.write("Use the [Macro Calculator](https://www.calculator.net/macro-calculator.html) to determine your daily needs.")
    if st.button("View Dining Options on Campus"):
        st.write("Explore today's meals at [Bentley Dining Services](https://bentley.sodexomyway.com/en-us/locations/the-921).")

    # ChatGPT for additional questions
    user_input_eating = st.text_input("Have a question about healthy eating?")
    if user_input_eating:
        response = get_chatgpt_response(user_input_eating)
        st.write(response)

    # Cross-Topic Prompt
    st.write("**Tip:** Staying active can help support your dietary goals and improve overall well-being. [Explore Healthy Lifestyle](#)")

# ---------------------- Healthy Lifestyle Section ----------------------
elif main_option == "Healthy Lifestyle":
    st.header("Healthy Lifestyle")
    st.write("Staying active is a great way to support both mental and physical well-being. Let’s find activities that fit your lifestyle goals.")

    # Step 1: Select Activity Goal
    activity_goal = st.radio("What kind of activity are you interested in?", 
                             ["Support my fitness and energy", "Have fun and stay active", "Try something new", "Build strength and endurance"])

    # Display relevant activities and campus resources based on activity goal
    if activity_goal == "Support my fitness and energy":
        st.write("- **Cardio**: Take a walk or run on the campus track.")
        st.write("- **Pool**: Swim at the [campus pool](https://events.bentley.edu/dana_center_pool_996).")
    elif activity_goal == "Have fun and stay active":
        st.write("- **Intramural Sports**: Join [intramural teams](https://bentleyfalcons.com/sports/2024/6/11/intramural-sports-schedules-standings.aspx).")
        st.write("- **Outdoor Activities**: Enjoy the green spaces around campus.")
    elif activity_goal == "Try something new":
        st.write("- **Yoga**: Try yoga or stretching routines outdoors.")
        st.write("- **Active Breaks**: Take the stairs or do a quick stretch.")
    elif activity_goal == "Build strength and endurance":
        st.write("- **Strength Training**: Use the [Dana Center Gym](https://events.bentley.edu/dana_center_331) for strength-building exercises.")
        st.write("- **Bodyweight Exercises**: Practice calisthenics or bodyweight routines on campus.")

    # ChatGPT for additional fitness questions
    user_input_lifestyle = st.text_input("Have a question about fitness or staying active?")
    if user_input_lifestyle:
        response = get_chatgpt_response(user_input_lifestyle)
        st.write(response)

    # Cross-Topic Prompt
    st.write("**Tip:** Balanced nutrition is key to maximizing the benefits of exercise. [Explore Healthy Eating](#)")

# ---------------------- Healthy Mindsets Section ----------------------
elif main_option == "Healthy Mindsets":
    st.header("Healthy Mindsets")
    st.write("Mental well-being is essential. Explore these resources to support calmness, focus, and a positive outlook.")

    # Step 1: Select a Mental Wellness Activity
    mindset_activity = st.radio("Choose an activity to support your mental well-being", 
                                ["Guided relaxation exercise", "Breathing techniques", "Self-reflection and gratitude"])

    # Display relevant resources based on selected activity
    if mindset_activity == "Guided relaxation exercise":
        st.write("Try this [guided meditation](https://www.youtube.com/watch?v=ZToicYcHIOU) for relaxation.")
    elif mindset_activity == "Breathing techniques":
        st.write("Practice calming techniques like [4-7-8 breathing](https://youtu.be/DbDoBzGY3vo?si=xWVePxgCv6NJVhM-).")
    elif mindset_activity == "Self-reflection and gratitude":
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
    st.write("**Tip:** Physical activity and balanced nutrition can boost mental well-being. [Explore Healthy Lifestyle](#) or [Healthy Eating](#)")

