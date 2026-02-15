# Setup CI/CD Pipeline

## Context
Use this to create a full CI/CD workflow.

## Prompt

You are a senior DevOps engineer.

Design a CI/CD pipeline for:

Stack:
{{STACK}}

Deployment Target:
{{AWS | VERCEL | DOCKER | GCP | AZURE | OTHER}}

Requirements:
- Automated testing
- Linting
- Build step
- Deployment step
- Rollback strategy
- Security best practices

Return:
1. Pipeline Configuration
2. Step-by-step Explanation
3. Environment Variables Needed
