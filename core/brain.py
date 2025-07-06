import subprocess

def ask_ai(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", "mistral"],
            input=prompt.encode(),
            capture_output=True,
            timeout=60
        )
        return result.stdout.decode()
    except Exception as e:
        return f"Error: {str(e)}"