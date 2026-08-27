"""
German Language Learning Progress Model
Tracks CEFR level progression: A1 → A2 → B1 → B2 → C1
Each entry = one skill area (Reading, Writing, Speaking, Listening, Vocab, Grammar)
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base


GERMAN_SKILLS = [
    "Reading",
    "Writing",
    "Speaking",
    "Listening",
    "Vocabulary",
    "Grammar",
]

CEFR_LEVELS = ["A1", "A2", "B1", "B2", "C1"]

CEFR_METADATA = {
    "A1": {"label": "Beginner",         "color": "#EF4444", "eu_relevance": "Basic greetings only",             "xp_per_skill": 30},
    "A2": {"label": "Elementary",       "color": "#F97316", "eu_relevance": "Simple daily interactions",        "xp_per_skill": 60},
    "B1": {"label": "Intermediate",     "color": "#F59E0B", "eu_relevance": "EU Blue Card language requirement", "xp_per_skill": 100},
    "B2": {"label": "Upper-Intermediate","color": "#10B981", "eu_relevance": "German job interview capable",     "xp_per_skill": 150},
    "C1": {"label": "Advanced",         "color": "#6366F1", "eu_relevance": "Native-level professional fluency", "xp_per_skill": 250},
}


class GermanLangSkill(Base):
    """Tracks progress for each German language skill area."""
    __tablename__ = "german_lang_skills"

    id           = Column(Integer, primary_key=True, index=True)
    skill        = Column(String(50), nullable=False, unique=True)   # Reading, Writing, etc.
    current_level = Column(String(5), default="A1")                  # A1 / A2 / B1 / B2 / C1
    target_level  = Column(String(5), default="B1")                  # Goal level
    notes        = Column(Text, default="")
    resources    = Column(Text, default="")                           # e.g. "Goethe A2 Wortliste, Deutsche Welle"
    is_certified  = Column(Boolean, default=False)                    # Has Goethe/TestDaF cert for this skill?
    updated_at   = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    created_at   = Column(DateTime(timezone=True), server_default=func.now())


class GermanLangCert(Base):
    """Tracks official German certifications earned."""
    __tablename__ = "german_lang_certs"

    id          = Column(Integer, primary_key=True, index=True)
    cert_name   = Column(String(100), nullable=False)   # e.g. "Goethe-Zertifikat B1"
    level       = Column(String(5), nullable=False)     # A1 / A2 / B1 / B2 / C1
    passed      = Column(Boolean, default=False)
    score       = Column(String(20), default="")        # e.g. "87/100"
    exam_date   = Column(String(20), default="")        # "2026-11"
    notes       = Column(Text, default="")
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
