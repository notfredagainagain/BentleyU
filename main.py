# main.py

import openai
import streamlit as st
import os

# Fetch OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Bentley Wellness Support")

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

# Section: Healthy Eating
st.header("Healthy Eating")
st.write("Discover your ideal macronutrient intake and explore dining options to support your goals.")

# Macronutrient Calculator (linked externally)
st.write("Use the [Macro Calculator](https://www.calculator.net/macro-calculator.html) to determine your needs.")
if st.button("View Dining Options on Campus"):
    st.write("Explore meals at [Bentley Dining Services](https://bentley.sodexomyway.com/en-us/locations/the-921).")

# ChatGPT for Healthy Eating questions
user_input_eating = st.text_input("Have a question about healthy eating?")
if user_input_eating:
    response = get_chatgpt_response(user_input_eating)
    st.write(response)

# Section: Healthy Lifestyle
st.header("Healthy Lifestyle")
st.write("Get active with campus resources to stay fit, have fun, and boost your energy.")

# Activity options
st.write("- Visit the [Dana Center Gym](https://events.bentley.edu/dana_center_331)")
st.write("- Swim at the [campus pool](https://events.bentley.edu/dana_center_pool_996)")
st.write("- Join [intramural sports](https://bentleyfalcons.com/sports/2024/6/11/intramural-sports-schedules-standings.aspx)")

# ChatGPT for Healthy Lifestyle questions
user_input_lifestyle = st.text_input("Have a question about fitness or staying active?")
if user_input_lifestyle:
    response = get_chatgpt_response(user_input_lifestyle)
    st.write(response)

# Section: Healthy Mindsets
st.header("Healthy Mindsets")
st.write("Support your mental well-being with guided exercises and resources.")

# Guided resources
st.write("Try a [guided meditation](https://www.youtube.com/watch?v=ZToicYcHIOU) or a [breathing exercise](https://youtu.be/DbDoBzGY3vo?si=xWVePxgCv6NJVhM-).")
st.write("Need support? [Schedule an appointment](https://www.bentley.edu/university-life/student-health/counseling-center) with a campus counselor.")

# ChatGPT for Healthy Mindsets questions
user_input_mindsets = st.text_input("Have a question about mental well-being?")
if user_input_mindsets:
    response = get_chatgpt_response(user_input_mindsets)
    st.write(response)

