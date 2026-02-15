# Dockerize a Project

## Context
Use this to containerize an application.

## Prompt

You are a DevOps engineer.

Create a production-ready Docker setup for:

Language/Framework:
{{STACK}}

Project Description:
{{DESCRIBE_PROJECT}}

Requirements:
- Optimized Dockerfile
- Use multi-stage builds if applicable
- Minimize image size
- Include .dockerignore
- Provide run instructions

Return:
1. Dockerfile
2. docker-compose.yml (if needed)
3. Explanation
