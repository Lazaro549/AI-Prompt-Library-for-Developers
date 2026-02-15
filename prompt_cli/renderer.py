def render_prompt(content, values):
    for key, val in values.items():
        content = content.replace(f"{{{{{key}}}}}", val)
    return content
