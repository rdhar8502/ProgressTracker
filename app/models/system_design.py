from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class SystemDesignConcept(Base):
    __tablename__ = "system_design_concepts"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50), default="Core")   # Core / Advanced / Infrastructure
    concept_name = Column(String(200), nullable=False)
    order_index = Column(Integer, default=0)
    sources = Column(Text, default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship to sub-concepts
    sub_concepts = relationship(
        "SystemDesignSubConcept",
        back_populates="concept",
        cascade="all, delete-orphan",
        order_by="SystemDesignSubConcept.order_index"
    )


class SystemDesignSubConcept(Base):
    __tablename__ = "system_design_sub_concepts"

    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(Integer, ForeignKey("system_design_concepts.id", ondelete="CASCADE"), nullable=False)
    subconcept_name = Column(String(200), nullable=False)
    status = Column(String(20), default="Not Started")  # Not Started / In Progress / Done
    reading_done = Column(Boolean, default=False)
    practical_done = Column(Boolean, default=False)
    notes = Column(Text, default="")
    resources = Column(Text, default="")
    sources = Column(Text, default="")
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationship back to concept
    concept = relationship("SystemDesignConcept", back_populates="sub_concepts")


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
