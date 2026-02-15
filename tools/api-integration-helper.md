# API Integration Helper

## Context
Use this to integrate third-party APIs.

## Prompt

You are a senior backend engineer.

Integrate the following API into a {{LANGUAGE}} application:

API Description:
{{DESCRIBE_API}}

Requirements:
- Use environment variables for API keys
- Handle rate limits
- Handle errors gracefully
- Provide example request & response
- Include retry logic if needed

Return:
1. Integration Code
2. Setup Instructions
3. Explanation of Flow
