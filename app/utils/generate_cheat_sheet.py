import re
from app.utils.together import chat_completion

def generate_cheat_sheet(resume_text, job_title, job_description, interviewer_type="Manager"):
    prompt = f"""
You are an expert technical interview coach. Based on the following details, generate a full interview prep pack.

Job Title: {job_title}

Job Description:
{job_description}

Resume Content:
{resume_text}

Instructions:
1. Generate 15–20 tailored interview questions specifically for this role.
2. Generate 5–10 questions that connect the resume background to the job (e.g., from healthcare to tech).
3. Based on the interviewer type ({interviewer_type}), generate 3–5 smart questions the candidate can ask the interviewer.

Label each section:
- Top Interview Questions (Tailored)
- Resume-Based Crossover Questions
- Questions to Ask the Interviewer ({interviewer_type})
"""

    response = chat_completion(prompt)
    return response