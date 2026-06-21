import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

def classify_intent(message: str) -> str:
    prompt = f"""
    You are an intent classifier for an enterprise chatbot.
    Classify the user message into exactly one of these categories:
    IT, HR, Finance, Unknown

    Rules:
    - IT: laptop, VPN, software, hardware, access, password, network
    - HR: leave, payroll, policy, onboarding, resignation, attendance
    - Finance: invoice, reimbursement, expense, budget, payment
    - Unknown: anything that doesn't fit above

    User message: "{message}"

    Reply with just the category name. Nothing else.
    """

    response = model.generate_content(prompt)
    intent = response.text.strip()
    return intent
