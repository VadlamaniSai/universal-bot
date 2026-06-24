from fastapi import FastAPI
from pydantic import BaseModel
from app.router import classify_intent
from app.handlers import it_handler, hr_handler, finance_handler

app = FastAPI()

conversation_history = {}

class UserMessage(BaseModel):
    user_id: int
    message: str

bot_map = {
    "IT": it_handler,
    "HR": hr_handler,
    "Finance": finance_handler
}

@app.get("/")
def health_check():
    return {"status": "UniversalBot is running"}

@app.post("/chat")
def chat(payload: UserMessage):
    intent = classify_intent(payload.message)
    user_id = payload.user_id
    if user_id not in conversation_history:
        conversation_history[user_id] = []
    conversation_history[user_id].append(payload.message)
    chosen_function = bot_map.get(intent)
    if chosen_function is None:
        return {"response": "Sorry, something went wrong with the query, please rephrase your query"}
    result = chosen_function(payload.message, conversation_history[user_id])
    return {
        "user_id": payload.user_id,
        "received": payload.message,
        "intent": intent,
        "response": result
    }
