
# 🧠 AcePrep – AI-Powered Interview Cheat Sheet Generator

AcePrep is a full-stack FastAPI application that helps job seekers prepare for interviews by generating tailored, AI-powered cheat sheets – complete with smart tips and a branded PDF export.

---

## 🚀 Features

✅ Paste your resume + job description  
✅ Get 15–20 tailored interview questions  
✅ Includes “Smart Tips” for each question  
✅ Branded PDF export  
✅ Email delivery via SendGrid  
✅ Mock Stripe checkout page  
✅ Production-grade FastAPI backend  
✅ Ready to deploy (Docker, Railway, etc.)

---

## 📸 Screenshots (add yours!)
- 🎯 `/` – Upload your resume and job details
- 📄 `/generate` – View cheat sheet + tips
- 💳 `/mock-checkout` – Simulated Stripe flow
- 📨 PDF emailed upon generation

---

## 🛠 Tech Stack

- Python 3.10+
- FastAPI
- Jinja2 templates
- SendGrid API
- Together.ai (LLM backend)
- Stripe (mock integrated)
- PDF generation with `reportlab`
- Resume parsing: `pdfplumber`, `python-docx`

---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/NateDiesel/AcePrep.git
cd AcePrep

python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

---

## 🌐 Live Demo

> Coming soon via [Railway](https://railway.app/)

---

## 📧 Want to try it?

- Clone this repo
- Paste your resume and job title
- Get a tailored PDF emailed to you
