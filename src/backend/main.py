from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Recruitment Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Candidate(BaseModel):
    name: str
    skills: List[str]
    experience_years: int


class RecruitmentRequest(BaseModel):
    role: str
    required_skills: List[str]
    candidates: List[Candidate]


@app.get("/")
def health_check():
    return {"status": "ok", "app": "Recruitment Assistant"}


@app.post("/recommend")
def recommend_candidates(request: RecruitmentRequest):
    ranked_candidates = []

    for candidate in request.candidates:
        matched_skills = [
            skill for skill in request.required_skills
            if skill.lower() in [s.lower() for s in candidate.skills]
        ]

        score = len(matched_skills) * 10 + candidate.experience_years

        ranked_candidates.append({
            "name": candidate.name,
            "matched_skills": matched_skills,
            "experience_years": candidate.experience_years,
            "score": score,
            "recommendation": "Strong fit" if score >= 20 else "Potential fit"
        })

    ranked_candidates.sort(key=lambda item: item["score"], reverse=True)

    return {
        "role": request.role,
        "application_crew": {
            "researcher_agent": "Identified candidate profiles from submitted data.",
            "evaluator_agent": "Evaluated candidates against required skills.",
            "recommender_agent": "Ranked candidates based on fit score."
        },
        "recommendations": ranked_candidates
    }