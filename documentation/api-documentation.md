# Generate API Documentation

## Context
Use this to document REST or GraphQL APIs.

## Prompt

You are a technical documentation expert.

Generate API documentation for:

API Name:
{{API_NAME}}

Base URL:
{{BASE_URL}}

Endpoints:
{{ENDPOINT_LIST}}

For each endpoint include:
- HTTP method
- Route
- Description
- Request parameters
- Request example
- Response example
- Error responses
- Authentication requirements

Format in Markdown with clear headings.
