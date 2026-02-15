import os
import re
import sys
from loader import load_prompt
from renderer import render_prompt
from executor import run_prompt

RESULTS_DIR = "results"
os.makedirs(RESULTS_DIR, exist_ok=True)

def list_prompts():
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".md") and "prompt_cli" not in root:
                print(os.path.relpath(os.path.join(root, file)))

def run_prompt_file(path):
    content = load_prompt(path)
    placeholders = re.findall(r"\{\{(.*?)\}\}", content)

    values = {}
    for ph in set(placeholders):
        values[ph] = input(f"Enter value for {ph}: ")

    final_prompt = render_prompt(content, values)
    print("\n--- Rendered Prompt ---\n")
    print(final_prompt)

    # Ejecutar en OpenAI
    execute = input("\nRun this prompt in OpenAI API? (y/n): ").lower()
    if execute == "y":
        output = run_prompt(final_prompt)
        print("\n--- AI Output ---\n")
        print(output)

        # Guardar resultado
        filename = os.path.join(RESULTS_DIR, os.path.basename(path).replace(".md", "_result.txt"))
        with open(filename, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"\n✅ Output saved to {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py [list|run <path>]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_prompts()
    elif command == "run" and len(sys.argv) == 3:
        run_prompt_file(sys.argv[2])
    else:
        print("Invalid command.")
