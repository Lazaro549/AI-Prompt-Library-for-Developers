import os

def load_prompt(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Prompt file {path} not found")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

