# TalentScout – Hiring Assistant Chatbot 🤖

## 1. Project Overview

The **TalentScout Hiring Assistant Chatbot** is an intelligent AI-powered screening assistant built for TalentScout, a recruitment agency focused on technology roles. The chatbot supports the initial candidate screening process by:

- Providing greeting and explaining its purpose  
- Collecting required personal and professional details  
- Generating 3–5 technical questions based on the candidate’s declared tech stack  
- Maintaining coherent and context-aware conversation flow  
- Offering fallback responses for unexpected or out-of-scope inputs  
- Ending the session gracefully when exit keywords are detected  
- Allowing export of collected data in JSON format

### Tech Choices Used in This Implementation

- Backend LLM provider: **Groq (Llama models)**  
- Frontend/UI: **Streamlit**  
- Core language: **Python**  
- Environment management: **dotenv**  
- Data handling: local simulated JSON export

---

## 2. Implemented Features

### A. Information Gathering Module

The bot collects the following mandatory fields:

- Full Name  
- Email Address  
- Phone Number  
- Years of Experience  
- Desired Position  
- Current Location  
- Tech Stack

Progress is displayed in sidebar using a Streamlit progress bar.

### B. Technical Question Generation

- Utilizes `llama-3.3-70b-versatile` model through Groq client  
- Questions are personalized based on:
  - Declared technologies  
  - Years of experience  
- Returns 3–5 challenging recruiter-style questions

### C. Bonus: Sentiment & Language Analysis

- A dedicated function calls `llama-3.1-8b-instant` with JSON response format  
- Detects:
  - sentiment → positive / neutral / negative  
  - language → ISO code  
- Used to adapt assistant tone (e.g., “Excellent!” prefix)

### D. Fallback & Domain Restriction

- The chatbot refuses to answer anything outside hiring workflow  
- Out-of-scope queries trigger meaningful redirection message  
- Session ends immediately on keywords:
  - exit, quit, bye, goodbye, end

### E. Data Export

- After completion, user can download:
  - `talent_scout_application.json`  
- Implemented using `st.download_button`

---

## 4. Usage Guide

### Conversation Flow

1. Candidate opens the app  
2. Bot greets and explains screening  
3. Candidate provides details step-by-step  
4. Tech Stack is declared  
5. Bot generates 3–5 technical questions  
6. Candidate responds  
7. Bot confirms completion and next steps  
8. User downloads JSON application

### Reset Option

- Sidebar button clears session  
- `st.rerun()` restarts flow

---

## 5. Architectural Design

```
├── app.py                    → Streamlit UI & workflow
├── logic.py                  → REQUIRED_FIELDS list
├── requirements.txt
├── readme.md
└── talent_scout_application.json        → simulated storage 
```

### Design Decisions

- Separation of logic from UI  
- Use of Groq models instead of OpenAI  
- JSON-only sentiment prompting  
- Session state to maintain context  
- No real database — only simulated export

---

## 6. Code Quality Practices

- Modular functions  
- Docstrings added  
- Error handling with try/except  
- Public Git recommended  
- Cloud deploy optional

---

## 7. Challenges Observed & Fixes

| Issue in Code | Change in README |
|----|----|
| variable mix `candidate_info` vs `candidate_info` | Documented strict flow |
| citation strings left in UI | removed from design |
| experience parsed as text | handled in prompt |
| gradio vs streamlit confusion | updated to Streamlit |

---

## 8. Future Improvements

- Email validation regex  
- Actual DB using MySQL  
- Multilingual screening  
- Sentiment analytics dashboard  
- Cloud hosting

---

## 9. Conclusion

The chatbot demonstrates:

- Streamlit-based candidate interaction  
- Groq + Llama LLM integration  
- Prompt engineering  
- Context management  
- Fallback restriction  
- JSON export

**Author:**  
Rajatveer Singh  
AI/ML Intern
