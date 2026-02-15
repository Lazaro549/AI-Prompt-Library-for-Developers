# Structured Output Prompts

## Context
Use this to force deterministic outputs.

## JSON Output Prompt

Return the result strictly in valid JSON format:

{
  "summary": "",
  "issues": [],
  "improvements": [],
  "confidence_score": 0
}

Do not include explanations outside the JSON.

---

## Markdown Table Output Prompt

Return the result as a Markdown table with columns:
| Issue | Severity | Fix |
