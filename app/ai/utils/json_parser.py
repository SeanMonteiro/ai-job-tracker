import json, re

def extract_json_from_text(text: str):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Extract JSON block from messy response
    match = re.search(r"\{.*\}", text, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass
    
    raise ValueError("Invalid JSON response from AI")
