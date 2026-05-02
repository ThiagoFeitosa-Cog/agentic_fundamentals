# QA Plan

## Test Cases

## Health Check
Endpoint: GET /
Expected: status ok
Result: Passed

## Candidate Recommendation
Endpoint: POST /recommend
Expected: ranked candidates with matched skills, score, and recommendation label
Result: Passed

## Edge Cases
- Candidate with no matching skills should receive lower score.
- Candidate with multiple matching skills should rank higher.
- Empty or invalid payload should be rejected by FastAPI validation.

## Status
Build phase validated for course mini-project purposes.