# Release Notes

## Version 1.0.0 - Initial Mini-Project Release

## Features

- Candidate recommendation endpoint
- Simple frontend interface
- Conceptual Application Crew workflow
- Candidate scoring and ranking
- Basic logging
- Local deployment instructions
- Dockerfile for containerized execution
- Operational runbook
- Execution results documentation

## Deployment

Supported deployment methods:

- Local FastAPI backend
- Static frontend served with Python HTTP server
- Docker container for backend

## Known Issues

- Application Crew is represented with deterministic backend logic for mini-project purposes.
- Full CrewAI AOP tracing is documented but not enabled in this simplified version.
- No persistent database or ATS integration.
- Frontend is intentionally minimal for course completion purposes.

## Next Steps

- Add real CrewAI agents.
- Add persistent candidate storage.
- Improve frontend design.
- Add automated tests.
- Enable CrewAI tracing in a full production version.