# Write Unit Tests

## Context
Use this to generate comprehensive unit tests.

## Prompt

You are a senior QA engineer.

Write comprehensive {{TEST_FRAMEWORK}} unit tests for:

Language:
{{LANGUAGE}}

Code:
"""
{{INSERT_CODE}}
"""

Requirements:
- Cover edge cases
- Include negative tests
- Mock dependencies where needed
- Aim for high coverage

Return:
1. Test File
2. Explanation of Test Strategy
