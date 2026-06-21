def it_handler(message: str) -> str:
    return {"response": f"here is the solution for your problem {message}"}

def hr_handler(message: str) -> str:
    return {"response": f"here is the answer for your question {message}"}

def finance_handler(message: str) -> str:
    return {"response": f"here is the answer for your query {message}"}