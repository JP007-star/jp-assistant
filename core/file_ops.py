import os

def list_files(path):
    try:
        return "\n".join(os.listdir(path))
    except Exception as e:
        return f"Error: {e}"