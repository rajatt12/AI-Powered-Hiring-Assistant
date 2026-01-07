import streamlit as st
import json
import time
from logic import REQUIRED_FIELDS, generate_technical_questions, analyze_sentiment_and_language


st.set_page_config(page_title="TalentScout Assistant", page_icon="🤖")
st.markdown("""
    <style>
    .stChatMessage { border-radius: 15px; border: 1px solid #e0e0e0; }
    .stProgress > div > div > div > div { background-color: #4CAF50; }
    </style>
    """, unsafe_allow_html=True)

st.title("TalentScout Hiring Assistant")
st.caption("Initial Screening & Technical Assessment [cite: 8]")


if "messages" not in st.session_state:
    # Initial Greeting and Purpose Overview [cite: 20]
    greeting = "Hello! I am the TalentScout Assistant. I'll collect your details and ask technical questions based on your stack."
    st.session_state.messages = [{"role": "assistant", "content": greeting}]
if "candidate_info" not in st.session_state:
    st.session_state.candidate_info = {}
if "step" not in st.session_state:
    st.session_state.step = "gathering"


with st.sidebar:
    st.header("Application Progress")
    progress = len(st.session_state.candidate_info) / len(REQUIRED_FIELDS)
    st.progress(progress)
    if st.button("Reset Conversation"):
        st.session_state.clear()
        st.rerun()


for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if prompt := st.chat_input("Type your message..."):
    
    exit_keywords = ["exit", "quit", "bye", "goodbye", "end"]
    user_words = prompt.lower().split()
    if any(keyword in user_words for keyword in exit_keywords):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        exit_msg = "Thank you for your interest in TalentScout. The session has ended."
        st.session_state.messages.append({"role": "assistant", "content": exit_msg})
        with st.chat_message("assistant"):
            st.markdown(exit_msg)
        st.stop()

    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        
        with st.status("Thinking...", expanded=False):
            
            analysis = analyze_sentiment_and_language(prompt)
            sentiment = analysis.get("sentiment", "neutral")
            
            
            if st.session_state.step == "gathering":
                current_field = next((f for f in REQUIRED_FIELDS if f not in st.session_state.candidate_info), None)
                if current_field:
                    st.session_state.candidate_info[current_field] = prompt
                
                next_f = next((f for f in REQUIRED_FIELDS if f not in st.session_state.candidate_info), None)
                
                if next_f:
                    prefix = "Excellent!" if sentiment == "positive" else "Got it."
                    reply = f"{prefix} Now, please provide your **{next_f}**."
                else:
                    st.session_state.step = "technical"
                    reply = "Thank you! I have all your details. Now, let's move to technical questions."

            
            if st.session_state.step == "technical" and "qs" not in st.session_state:
                stack = st.session_state.candidate_info.get("Tech Stack", "General IT")
                exp = st.session_state.candidate_info.get("Years of Experience", "0")
                st.session_state.qs = generate_technical_questions(stack, exp)
                reply = f"Based on your experience with {stack}, here are your questions:\n\n{st.session_state.qs}"
                st.session_state.step = "finished"
            elif st.session_state.step == "finished":
                reply = "Your screening is complete. Thank you for your time!"

        st.markdown(reply)
        st.session_state.messages.append({"role": "assistant", "content": reply})

#DATA EXPORT
if st.session_state.step == "finished":
    data = json.dumps(st.session_state.candidate_info, indent=4)

    st.download_button("Download My Application (JSON)", data=data, file_name="talent_scout_application.json")
