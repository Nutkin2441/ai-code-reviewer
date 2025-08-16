import requests

API_ENDPOINT = "https://www.manitobahydro.ca1.qualtrics.com/jfe/form/SV_0BapPHRymFlm86"

def get_ai_suggestions(file_path):
    with open(file_path, "r") as f:
        code_content = f.read()
    
    payload = {
        "code": code_content,
        "filename": file_path
    }
    try:
        response = requests.post(API_ENDPOINT, json=payload, timeout=30)
        response.raise_for_status()
        try:
            data = response.json()
            return data.get("suggestions", "No suggestions returned.")
        except Exception:
            return response.text
    except Exception as e:
        return f"Error communicating with AI API: {e}"

def run_ai_review(code_files):
    results = []
    for file in code_files:
        suggestion = get_ai_suggestions(file)
        results.append(f"{file}: {suggestion}")
    return results
