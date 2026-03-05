"""
Resume Screening AI — starter code.

Ranks resumes against a job description using semantic similarity.
"""

from pathlib import Path
import re
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Load embedding model (runs locally, no API key needed)
MODEL_NAME = "all-MiniLM-L6-v2"
embedder = SentenceTransformer(MODEL_NAME)


def extract_text_from_file(filepath: str) -> str:
    """Extract plain text from a .txt file (extend for PDF/DOCX)."""
    return Path(filepath).read_text(encoding="utf-8")


def clean_text(text: str) -> str:
    """Basic text cleaning."""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def score_resume(resume_text: str, job_description: str) -> float:
    """
    Score a resume against a job description using cosine similarity.

    Returns a score between 0.0 and 1.0.
    """
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(job_description)

    embeddings = embedder.encode([resume_clean, jd_clean], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return float(similarity)


def rank_resumes(resume_texts: list[str], job_description: str) -> list[dict]:
    """
    Rank a list of resumes against a job description.

    Returns a sorted list of dicts with index and score.
    """
    scores = [
        {"index": i, "score": score_resume(text, job_description)}
        for i, text in enumerate(resume_texts)
    ]
    return sorted(scores, key=lambda x: x["score"], reverse=True)


if __name__ == "__main__":
    # Example usage
    jd = """
    We are looking for a Python Backend Engineer with 2+ years experience.
    Required skills: Python, FastAPI, PostgreSQL, Docker, REST APIs.
    Nice to have: Redis, Kubernetes, AWS.
    """

    resumes = [
        "Experienced Django and Flask developer. Built REST APIs, PostgreSQL, Linux.",
        "Data scientist with Python, Pandas, NumPy, Machine Learning, Scikit-learn.",
        "Backend engineer: FastAPI, Python, PostgreSQL, Docker, AWS, Redis, Kubernetes.",
        "Frontend developer: React, TypeScript, CSS, HTML, Node.js.",
    ]

    results = rank_resumes(resumes, jd)
    print("Resume Rankings:")
    for rank, result in enumerate(results, 1):
        print(f"  Rank {rank}: Resume #{result['index'] + 1} — Score: {result['score']:.3f}")
