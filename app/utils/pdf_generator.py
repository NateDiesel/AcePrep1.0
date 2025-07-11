
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch
from datetime import datetime
import os

def mock_gpt_interview_questions(context_text):
    return [
        "Tell me about yourself.",
        "What are your greatest strengths related to this role?",
        "How have your past roles prepared you for this position?",
        "Describe a challenging work situation and how you overcame it.",
        "Why do you want to work at this company?",
        "What do you know about our organization?",
        "How do you handle tight deadlines or pressure?",
        "Describe a time you showed leadership.",
        "Where do you see yourself in five years?",
        "How do you prioritize tasks when everything feels urgent?",
        "Tell me about a time you disagreed with a coworker.",
        "What makes you a strong candidate for this role?",
        "What are your salary expectations?",
        "Do you prefer working alone or on a team?",
        "How do you stay current in your industry?",
        "Give an example of a successful project you led.",
        "What motivates you in your career?",
        "How would your colleagues describe you?",
        "Describe a time you failed and what you learned.",
        "What questions do you have for us?"
    ]

def suggested_questions_by_interviewer():
    return {
        "HR": [
            "How would you describe the company culture?",
            "What are the next steps after this interview?"
        ],
        "Manager": [
            "What are the biggest challenges the team is facing?",
            "How is performance typically measured in this role?"
        ],
        "CEO": [
            "What’s your long-term vision for the company?",
            "How does this role contribute to the overall mission?"
        ]
    }

def generate_cheat_sheet(job_title, job_description, job_role, company_name, user_name, output_path):
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='SectionHeader', fontSize=14, spaceAfter=10, spaceBefore=20, leading=16, alignment=1))
    story = []

    story.append(Paragraph("AcePrep™ Interview Cheat Sheet", styles['Title']))
    story.append(Paragraph("by Content365.xyz", styles['Normal']))
    story.append(Spacer(1, 0.3 * inch))

    story.append(Paragraph(f"<b>Candidate:</b> {user_name}", styles['Normal']))
    story.append(Paragraph(f"<b>Job Title:</b> {job_title}", styles['Normal']))
    story.append(Paragraph(f"<b>Company:</b> {company_name}", styles['Normal']))
    story.append(Paragraph(f"<b>Interview Role:</b> {job_role}", styles['Normal']))
    story.append(Spacer(1, 0.3 * inch))

    # Job Description Summary
    story.append(Paragraph("Job & Resume Summary", styles['SectionHeader']))
    story.append(Paragraph(job_description[:2500], styles['Normal']))

    # Tailored Interview Questions
    story.append(Paragraph("Top Interview Questions (Tailored)", styles['SectionHeader']))
    for q in mock_gpt_interview_questions(job_description):
        story.append(Paragraph(f"• {q}", styles['Normal']))

    # Suggested Questions to Ask Interviewers
    story.append(Paragraph("Questions to Ask the Interviewer", styles['SectionHeader']))
    suggestions = suggested_questions_by_interviewer()
    for role, qs in suggestions.items():
        story.append(Paragraph(f"<b>{role}</b>", styles['Heading3']))
        for q in qs:
            story.append(Paragraph(f"- {q}", styles['Normal']))

    story.append(Spacer(1, 0.4 * inch))
    story.append(Paragraph(f"Generated on {datetime.now().strftime('%B %d, %Y')}", styles['Normal']))

    doc = SimpleDocTemplate(output_path, pagesize=LETTER)
    doc.build(story)
