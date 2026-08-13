from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
from app.database import Base


class SystemDesignTopic(Base):
    __tablename__ = "system_design_topics"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50), default="Core")   # Core / Advanced / Infrastructure
    topic_name = Column(String(200), nullable=False)
    order_index = Column(Integer, default=0)
    status = Column(String(20), default="Not Started")  # Not Started / In Progress / Done
    reading_done = Column(Boolean, default=False)
    practical_done = Column(Boolean, default=False)
    notes = Column(Text, default="")
    resources = Column(Text, default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class SystemDesignCase(Base):
    __tablename__ = "system_design_cases"

    id = Column(Integer, primary_key=True, index=True)
    system_name = Column(String(200), nullable=False)
    order_index = Column(Integer, default=0)
    status = Column(String(20), default="Not Started")  # Not Started / In Progress / Done
    key_components = Column(Text, default="")
    diagram_url = Column(String(300), default="")
    notes = Column(Text, default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
