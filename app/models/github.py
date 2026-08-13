from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base


class GithubProject(Base):
    __tablename__ = "github_projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    description = Column(Text, default="")
    tech_stack = Column(Text, default="")
    status = Column(String(20), default="Not Started")  # Not Started / In Progress / Done
    github_url = Column(String(300), default="")
    demo_url = Column(String(300), default="")
    order_index = Column(Integer, default=0)
    tasks = relationship("GithubTask", back_populates="project", cascade="all, delete-orphan")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    @property
    def completion_pct(self):
        if not self.tasks:
            return 0
        done = sum(1 for t in self.tasks if t.done)
        return round((done / len(self.tasks)) * 100)


class GithubTask(Base):
    __tablename__ = "github_tasks"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("github_projects.id"), nullable=False)
    project = relationship("GithubProject", back_populates="tasks")
    task_name = Column(String(300), nullable=False)
    category = Column(String(50), default="General")
    done = Column(Boolean, default=False)
    notes = Column(Text, default="")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
