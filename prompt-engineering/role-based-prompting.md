# Role-Based Prompting

## Context
Assigning AI a role improves output quality and reliability.

## Prompt Template

You are a {{ROLE}} with {{YEARS}} years of experience.

Your task:
{{TASK_DESCRIPTION}}

Constraints:
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}

Return format:
{{STRUCTURE}}

## Example

You are a senior backend engineer with 10 years of Node.js experience.

Your task:
Refactor this Express middleware for scalability.
