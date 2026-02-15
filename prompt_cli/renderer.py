import re

def render_prompt(content: str, values: dict) -> str:
    for key, val in values.items():
        content = re.sub(rf"\{{{{\s*{key}\s*}}}}", val, content)
    return content

