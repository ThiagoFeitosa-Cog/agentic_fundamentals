# Lessons Learned
## Recruitment Assistant

## What Went Well

- The AAMAD structure helped separate Define, Build, and Deliver phases.
- Markdown artifacts made the project easier to organize and review.
- The Application Crew concept made the backend workflow clearer.
- The project was small enough to test end-to-end locally.
- Logging helped confirm that the backend application and recommendation workflow were executing.

## Challenges Encountered

- Some setup commands required environment-specific adjustments.
- CORS needed to be configured because the frontend and backend run on different local origins.
- The course workflow assumes several persona-driven steps, but a simplified version can still demonstrate the core concepts.
- Running the frontend directly through `file://` caused browser security issues, so a local HTTP server was needed.

## Define Phase

The Define phase helped clarify the problem, users, scope, and Application Crew before implementation. The MRD and PRD created a stable foundation for later phases.

## Build Phase

The Build phase transformed the PRD into a working local application with backend, frontend, integration, and QA artifacts. The backend represented the Researcher, Evaluator, and Recommender workflow in a simplified but testable way.

## Deliver Phase

The Deliver phase made the application easier to run, monitor, and document. The runbook is especially useful because it allows another person to install, start, test, and troubleshoot the application without relying on previous chat context.

## AAMAD Framework Observations

AAMAD is useful because it forces structure, traceability, and context separation. This reduces ambiguity when working with AI-assisted development and makes it easier to maintain continuity across phases.

## Agentic Architect Reflections

The Agentic Architect role adds value by reviewing outputs, making tradeoffs, coordinating personas, and ensuring that the project remains aligned with technical, user experience, and business goals.

## Recommendations for Future Projects

- Start with a clear PRD.
- Keep artifacts concise but complete.
- Add logging early.
- Validate frontend-backend integration before expanding features.
- Use Docker earlier if deployment consistency matters.
- Add automated tests once the API contract is stable.

## Skills Developed

- Context engineering
- Multi-agent application planning
- FastAPI implementation
- Local deployment
- Operational documentation
- Logging and basic observability
- Agentic Architect review process