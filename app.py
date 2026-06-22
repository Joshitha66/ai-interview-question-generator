from openai import OpenAI
import streamlit as st
import os

# Read API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


st.title("🤖 AI Interview Question Generator")
st.write("Generate domain-specific interview questions with difficulty levels.")

domain = st.selectbox("Select Domain", ["Software Engineering", "Data Science", "Machine Learning", "Behavioral"])
skill = st.text_input("Enter Skill (e.g., Supervised Learning, Leadership, Algorithms)")
difficulty = st.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Questions"):
    prompt = f"""
    You are an experienced hiring manager in {domain}.
    Generate 5 interview questions for a candidate.
    Questions should be concise, open-ended, and test {skill}.
    Difficulty level: {difficulty}.
    Format output as a table with columns: Question, Difficulty, Skill Tested.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",   # or "gpt-4o" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    st.write("### Generated Interview Questions")
    st.write(response.choices[0].message.content)
