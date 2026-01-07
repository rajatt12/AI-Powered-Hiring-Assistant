import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


REQUIRED_FIELDS = [
    "Full Name", "Email Address", "Phone Number", 
    "Years of Experience", "Desired Position", 
    "Current Location", "Tech Stack"
]

def analyze_sentiment_and_language(user_text):
    """
    Bonus Feature: Sentiment Analysis[cite: 99].
    Gauges candidate emotions to provide personalized responses[cite: 101].
    """
    prompt = f"Analyze this text: '{user_text}'. Return ONLY a JSON with keys 'sentiment' (positive/neutral/negative) and 'language' (ISO code)."
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant", 
            messages=[{"role": "user", "content": prompt}],
            response_format={"type": "json_object"}
        )
        return json.loads(response.choices[0].message.content)
    except:
        return {"sentiment": "neutral", "language": "en"}

def generate_technical_questions(tech_stack, experience):
    """
    Generates 3-5 technical questions tailored to the candidate's stack[cite: 35, 37].
    Personalized based on years of experience[cite: 101].
    """
    prompt = (
        f"You are a Senior Technical Recruiter for TalentScout. The candidate has {experience} years "
        f"of experience in: {tech_stack}. Generate 3-5 challenging technical questions."
    )
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": "You are a professional hiring assistant."},
                      {"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating questions: {str(e)}"