from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.database import Base


class AILLMTopic(Base):
    __tablename__ = "ai_llm_topics"

    id = Column(Integer, primary_key=True, index=True)
    topic_name = Column(String(200), nullable=False)
    category = Column(String(100), default="Core")   # Core / RAG / Agents / Production
    order_index = Column(Integer, default=0)
    status = Column(String(20), default="Not Started")  # Not Started / In Progress / Done
    depth = Column(Integer, default=1)    # 1=Surface, 2=Comfortable, 3=Deep
    notes = Column(Text, default="")
    resources = Column(Text, default="")
    interview_talking_point = Column(Text, default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
