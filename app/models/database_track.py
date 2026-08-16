from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class DatabaseConcept(Base):
    """High-level database concept / category grouping (e.g. SQL Fundamentals, Joins Deep Dive, NoSQL Engines, Indexing)."""
    __tablename__ = "database_concepts"

    id = Column(Integer, primary_key=True, index=True)
    track = Column(String(50), nullable=False, default="SQL")  # SQL, NOSQL, JOINS_FUNCTIONS, INTERNALS
    category = Column(String(100), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    difficulty = Column(String(20), default="Medium")  # Easy, Medium, Hard
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    items = relationship(
        "DatabaseItem",
        back_populates="concept",
        cascade="all, delete-orphan",
        order_by="DatabaseItem.order_index"
    )


class DatabaseItem(Base):
    """Specific query pattern, syntax topic, function, or sub-concept with progress tracking."""
    __tablename__ = "database_items"

    id = Column(Integer, primary_key=True, index=True)
    concept_id = Column(Integer, ForeignKey("database_concepts.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(250), nullable=False)
    syntax_example = Column(Text, nullable=True)  # Formatted SQL / NoSQL query or syntax example
    status = Column(String(20), default="Not Started")  # Not Started, In Progress, Done
    reading_done = Column(Boolean, default=False)
    practical_done = Column(Boolean, default=False)
    depth = Column(Integer, default=1)  # 1: Surface, 2: Comfortable, 3: Deep
    notes = Column(Text, nullable=True)  # Rich text notes
    sources = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    concept = relationship("DatabaseConcept", back_populates="items")


class DatabaseChallenge(Base):
    """Real-world SQL/NoSQL interview scenarios and schema design challenges."""
    __tablename__ = "database_challenges"

    id = Column(Integer, primary_key=True, index=True)
    track = Column(String(50), default="SQL")  # SQL, NOSQL, SYSTEM
    title = Column(String(200), nullable=False)
    category = Column(String(100), nullable=False)
    difficulty = Column(String(20), default="Medium")  # Easy, Medium, Hard
    scenario = Column(Text, nullable=False)
    schema_definition = Column(Text, nullable=True)  # DDL / JSON schema
    solution_query = Column(Text, nullable=True)  # Reference SQL / Aggregation query
    explanation = Column(Text, nullable=True)
    status = Column(String(20), default="Not Started")  # Not Started, In Progress, Done
    notes = Column(Text, nullable=True)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
