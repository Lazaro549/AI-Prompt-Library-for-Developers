import os
import re
from loader import load_prompt
from renderer import render_prompt

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def list_prompts():
    for root, _, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".md") and "prompt_cli" not in root:
                print(os.path.relpath(os.path.join(root, file), BASE_DIR))

def run_prompt(path):
    content = load_prompt(path)
    placeholders = re.findall(r"\{\{(.*?)\}\}", content)

    values = {}
    for ph in set(placeholders):
        values[ph] = input(f"Enter value for {ph}: ")

    final_prompt = render_prompt(content, values)
    print("\n--- Rendered Prompt ---\n")
    print(final_prompt)

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python main.py [list|run <path>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_prompts()
    elif command == "run" and len(sys.argv) == 3:
        run_prompt(sys.argv[2])
    else:
        print("Invalid command.")
