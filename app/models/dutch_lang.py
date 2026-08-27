"""
Dutch Language Learning Progress Model (Nederlands Leren)
Tracks CEFR level progression: A1 → A2 (Inburgering) → B1 (NT2-I) → B2 (NT2-II) → C1 (CNaVT)
Each entry = one skill area (Reading, Writing, Speaking, Listening, Vocab, Grammar)
"""
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base


DUTCH_SKILLS = [
    "Reading (Lezen)",
    "Writing (Schrijven)",
    "Speaking (Spreken)",
    "Listening (Luisteren)",
    "Vocabulary (Woordenschat)",
    "Grammar (Grammatica)",
]

CEFR_LEVELS_DUTCH = ["A1", "A2", "B1", "B2", "C1"]

CEFR_METADATA_DUTCH = {
    "A1": {"label": "Beginner",          "color": "#EF4444", "eu_relevance": "Basic Dutch greetings & everyday phrases", "xp_per_skill": 30},
    "A2": {"label": "Inburgering Basis", "color": "#F97316", "eu_relevance": "Civic integration level (Inburgering A2)",  "xp_per_skill": 60},
    "B1": {"label": "NT2 Programma I",   "color": "#F59E0B", "eu_relevance": "Vocational / Dutch workplace functional",    "xp_per_skill": 100},
    "B2": {"label": "NT2 Programma II",  "color": "#10B981", "eu_relevance": "Higher education & tech engineering fluent",  "xp_per_skill": 150},
    "C1": {"label": "CNaVT Academic",    "color": "#6366F1", "eu_relevance": "Professional native-like fluency",          "xp_per_skill": 250},
}


class DutchLangSkill(Base):
    """Tracks progress for each Dutch language skill area."""
    __tablename__ = "dutch_lang_skills"

    id            = Column(Integer, primary_key=True, index=True)
    skill         = Column(String(60), nullable=False, unique=True)   # Reading, Writing, etc.
    current_level = Column(String(5), default="A1")                   # A1 / A2 / B1 / B2 / C1
    target_level  = Column(String(5), default="B1")                   # Goal level
    notes         = Column(Text, default="")
    resources     = Column(Text, default="")                          # e.g. "NOS Makkelijk Nieuws, Bart de Pau"
    is_certified  = Column(Boolean, default=False)
    updated_at    = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    created_at    = Column(DateTime(timezone=True), server_default=func.now())


class DutchLangCert(Base):
    """Tracks official Dutch certifications earned (NT2, Inburgering, CNaVT)."""
    __tablename__ = "dutch_lang_certs"

    id          = Column(Integer, primary_key=True, index=True)
    cert_name   = Column(String(100), nullable=False)   # e.g. "Staatsexamen NT2 Programma II"
    level       = Column(String(5), nullable=False)     # A1 / A2 / B1 / B2 / C1
    passed      = Column(Boolean, default=False)
    score       = Column(String(20), default="")        # e.g. "Passed / 85%"
    exam_date   = Column(String(20), default="")        # "2026-12"
    notes       = Column(Text, default="")
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
