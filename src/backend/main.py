import logging
import os
from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="Recruitment Assistant")

# Logging setup
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info("Recruitment Assistant application started")

# CORS setup for local frontend integration
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
    logger.info("Health check requested")

    return {
        "status": "ok",
        "app": "Recruitment Assistant"
    }


@app.post("/recommend")
def recommend_candidates(request: RecruitmentRequest):
    logger.info(
        "Application Crew execution started for role: %s",
        request.role
    )

    ranked_candidates = []

    for candidate in request.candidates:
        candidate_skills = [skill.lower() for skill in candidate.skills]

        matched_skills = [
            skill for skill in request.required_skills
            if skill.lower() in candidate_skills
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

    logger.info(
        "Application Crew execution completed. Recommendations generated: %s",
        len(ranked_candidates)
    )

    return {
        "role": request.role,
        "application_crew": {
            "researcher_agent": "Identified candidate profiles from submitted data.",
            "evaluator_agent": "Evaluated candidates against required skills.",
            "recommender_agent": "Ranked candidates based on fit score."
        },
        "recommendations": ranked_candidates
    }