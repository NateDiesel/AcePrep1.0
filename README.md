# 🧠 AcePrep – AI-Powered Interview Cheat Sheet Generator

AcePrep is your personal AI interview coach. Built with FastAPI and GPT integration, it analyzes your resume and job description to generate smart, tailored interview question packs — complete with a branded PDF export.

---

## 🚀 Features

✅ Upload your **resume (PDF or DOCX)**  
✅ Paste a **job title or LinkedIn/Indeed job link**  
✅ Auto-detects resume-job mismatch  
✅ Dynamically generates:
- 15–20 role-specific interview questions
- 5–10 crossover questions based on your resume
- 3–5 questions to ask your interviewer (HR, Manager, or CEO)

✅ GPT-powered using Together.ai  
✅ PDF export with custom branding  
✅ Email delivery via SendGrid  
✅ Clean Tailwind-based frontend UX  
✅ Stripe-ready mock payment flow  
✅ Built for real-world deployment (Railway, Docker)

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Jinja2 Templates
- Tailwind CSS (via CDN)
- Together.ai (LLM)
- SendGrid (email delivery)
- Stripe (mock integration)
- PDF export with `reportlab`
- Resume parsing via `pdfplumber` and `python-docx`

---

## 📦 Setup Instructions (Local Dev)

```bash
git clone https://github.com/NateDiesel/AcePrep1.0.git
cd AcePrep1.0
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
