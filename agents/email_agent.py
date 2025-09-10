import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

def generate_email_response(email_text, tone):
    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    # Initialize Gemini Pro model
    model = genai.GenerativeModel('gemini-pro')
    
    # Generate response
    response = model.generate_content(prompt)
    return response.text