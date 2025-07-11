
from app.utils.resume_vs_job_mismatch import detect_resume_job_mismatch
from app.utils.extract_job_description import extract_job_description_from_url
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
import os
import re
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.utils.pdf_generator import generate_cheat_sheet
from app.utils.parser import extract_resume_context, extract_job_description_from_url
from app.utils.payment_and_email import send_pdf_email
from app.utils.stripe_checkout import create_checkout_session

# Load environment variables
load_dotenv()
IS_PREMIUM_MODE = os.getenv("IS_PREMIUM_MODE", "false").lower() == "true"

# App init
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = FastAPI()

# Static + Templates
app.mount("/static", StaticFiles(directory=os.path.abspath(os.path.join(BASE_DIR, "..", "static"))), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Output directories
OUTPUT_DIR = Path(os.path.join(BASE_DIR, "output"))
UPLOAD_DIR = Path(os.path.join(BASE_DIR, "uploads"))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# Helper to sanitize filenames
def sanitize_filename(text: str) -> str:
    return re.sub(r"[^\w\-_.]", "_", text.strip()) or "AcePrep_Document"

# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.get("/create-checkout-session")
async def stripe_checkout(request: Request):
    return create_checkout_session(request)

@app.get("/success")
async def success(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})

@app.get("/mock-checkout")
async def mock_checkout():
    html = """
    <html>
        <head><title>Mock Stripe Checkout</title></head>
        <body style='font-family:sans-serif;text-align:center;padding:50px'>
            <h1>Upgrade to AcePrep Premium</h1>
            <p>Unlock 20 role-specific, AI-tailored interview questions.</p>
            <button style='padding:10px 20px;font-size:18px'>Pay $9.99 (Mock)</button>
        </body>
    </html>
    """
    return HTMLResponse(content=html)

@app.post("/generate")
async def generate(
    request: Request,
    job_link: str = Form(""),
    job_title: str = Form(""),
    job_description: str = Form(""),
    company_name: str = Form(""),
    job_role: str = Form(""),
    user_name: str = Form(""),
    email: str = Form(""),
    resume_file: UploadFile = File(None)
):
    # Premium paywall check
    if IS_PREMIUM_MODE and not email.endswith("@test.com"):
        return templates.TemplateResponse("form.html", {
            "request": request,
            "error": "⚠️ Premium access required. Please purchase before generating your cheat sheet."
        })

    # Extract job info from link if available
    job_data_raw = extract_job_description_from_url(job_link) if job_link else ""
    if isinstance(job_data_raw, dict):
        job_title = job_title or job_data_raw.get("job_title", "")
        job_description = job_description or job_data_raw.get("job_description", "No description provided.")
    else:
        job_description = job_description or job_data_raw  # fallback if returned as plain text

    # Extract resume context
    resume_context = {}
    if resume_file:
        resume_path = UPLOAD_DIR / sanitize_filename(resume_file.filename)
        with open(resume_path, "wb") as f:
            f.write(await resume_file.read())
        resume_context = extract_resume_context(str(resume_path))

    # Final context for PDF
    enriched_description = f"{job_description}\n\n---\n\nRESUME CONTEXT:\n{resume_context.get('raw_text', '')}"

    # Generate cheat sheet PDF
    filename = sanitize_filename(f"{user_name}_{job_title}_AcePrep.pdf")
    output_path = OUTPUT_DIR / filename
    generate_cheat_sheet(job_title, enriched_description, job_role, company_name, user_name, str(output_path))

    # Send via email
    if email:
        send_pdf_email(email, filename, str(output_path))

    return FileResponse(output_path, media_type="application/pdf", filename=filename)
