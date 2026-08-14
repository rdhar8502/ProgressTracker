from sqlalchemy import Column, Integer, String, Date, DateTime, Float, Text, Enum
from sqlalchemy.sql import func
import enum
from app.database import Base


class CategoryEnum(str, enum.Enum):
    DSA = "DSA"
    SYSTEM_DESIGN = "System Design"
    AI_LLM = "AI/LLM"
    GITHUB = "GitHub"
    LINKEDIN_RESUME = "LinkedIn/Resume"
    APPLICATIONS = "Applications"
    MOCK_INTERVIEW = "Mock Interview"
    READING = "Reading"
    OTHER = "Other"


class DailyLog(Base):
    __tablename__ = "daily_logs"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False, index=True)
    category = Column(String(50), nullable=False)
    sub_topic = Column(String(200), nullable=False, default="")
    hours_spent = Column(Float, nullable=False, default=0.0)
    notes = Column(Text, default="")
    sources = Column(Text, default="")
    problems_solved = Column(Integer, default=0)   # For DSA
    confidence = Column(Integer, default=3)        # 1-5 scale
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
