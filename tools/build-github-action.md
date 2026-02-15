# Build GitHub Action

## Context
Use this to generate a GitHub Action workflow.

## Prompt

You are a DevOps engineer.

Create a GitHub Actions workflow that:

{{DESCRIBE_WORKFLOW}}

Requirements:
- Use best practices
- Cache dependencies if applicable
- Include error handling
- Trigger on appropriate events
- Be secure (avoid secrets exposure)

Return:
1. Complete YAML workflow file
2. Explanation of each step
3. Required secrets (if any)
