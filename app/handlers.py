from app.router import model

def it_handler(message: str) -> str:
    prompt = f"""
    You are an IT support assistant for an enterprise helpdesk.
    A user has reported the following issue:
    "{message}"

    Give a short, helpful, practical response (2-3 sentences) suggesting 
    troubleshooting steps or next actions.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def hr_handler(message: str) -> str:
    prompt = f"""
    You are an HR assistant for an enterprise helpdesk.
    A user has reported the following issue:
    "{message}"

    Give a short, helpful, practical response (2-3 sentences) suggesting 
    troubleshooting steps or next actions.
    """
    response = model.generate_content(prompt)
    return response.text.strip()

def finance_handler(message: str) -> str:
    prompt = f"""
    You are a finance assistant for an enterprise helpdesk.
    A user has reported the following issue:
    "{message}"

    Give a short, helpful, practical response (2-3 sentences) suggesting 
    troubleshooting steps or next actions.
    """
    response = model.generate_content(prompt)
    return response.text.strip()