from sqlalchemy import Column, Integer, String, Date, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class DSATopic(Base):
    __tablename__ = "dsa_topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)
    order_index = Column(Integer, default=0)
    description = Column(Text, default="")
    problems = relationship("DSAProblem", back_populates="topic_rel", cascade="all, delete-orphan")


class DSAProblem(Base):
    __tablename__ = "dsa_problems"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(300), nullable=False)
    difficulty = Column(String(10), nullable=False, default="Medium")  # Easy / Medium / Hard
    topic_id = Column(Integer, ForeignKey("dsa_topics.id"), nullable=False)
    topic_rel = relationship("DSATopic", back_populates="problems")
    status = Column(String(20), default="Not Started")  # Not Started / In Progress / Solved / Needs Review
    pattern = Column(Text, default="")
    mistake = Column(Text, default="")
    time_complexity = Column(String(50), default="")
    space_complexity = Column(String(50), default="")
    solution_snippet = Column(Text, default="")
    confidence = Column(Integer, default=3)  # 1-5
    leetcode_url = Column(String(300), default="")
    solved_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
