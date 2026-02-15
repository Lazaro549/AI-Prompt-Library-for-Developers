# Prompt Debugging Framework

## Context
Use this when AI gives inconsistent, vague, or incorrect responses.

## Prompt

You are a senior AI prompt engineer.

Analyze the following:

Prompt:
"""
{{INSERT_PROMPT}}
"""

Output:
"""
{{INSERT_AI_OUTPUT}}
"""

Identify:
- Why the output may be incorrect or weak
- Ambiguities in the prompt
- Missing constraints
- Improvements needed

Then provide a revised prompt.

## Tips
- Always specify format
- Add constraints
- Reduce open-ended instructions
