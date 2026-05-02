# Solution Architecture Document (SAD)
## Recruitment Assistant

## Architecture Overview
The Recruitment Assistant is a lightweight multi-agent application with a simple frontend and a FastAPI backend. The backend represents the Application Crew logic through three conceptual agents: Researcher Agent, Evaluator Agent, and Recommender Agent.

## Application Crew
- Researcher Agent: identifies candidate profiles from submitted candidate data.
- Evaluator Agent: compares candidates against required job skills.
- Recommender Agent: ranks candidates and returns structured recommendations.

## Backend
The backend is implemented with FastAPI and exposes:
- GET / for health check
- POST /recommend for candidate evaluation and recommendations

## Frontend
The frontend is a simple HTML/JavaScript interface that calls the backend API and displays recommendation results.

## Integration
The frontend sends a JSON payload to the backend. The backend processes candidate data and returns ranked recommendations.

## Security and Environment
Secrets should be stored in .env and excluded from Git. .env.example documents required configuration.