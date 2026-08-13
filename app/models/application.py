from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, Float, Date
from sqlalchemy.sql import func
from app.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(200), nullable=False)
    role = Column(String(200), nullable=False)
    location = Column(String(100), default="")
    country = Column(String(50), default="")
    visa_sponsor = Column(Boolean, default=False)
    salary_min = Column(Float, nullable=True)
    salary_max = Column(Float, nullable=True)
    currency = Column(String(10), default="USD")
    stage = Column(String(50), default="Saved")
    # Stages: Saved / Applied / OA / Phone Screen / Technical / Final Round / Offer / Rejected / Withdrawn
    job_url = Column(String(500), default="")
    notes = Column(Text, default="")
    applied_date = Column(Date, nullable=True)
    response_date = Column(Date, nullable=True)
    follow_up_date = Column(Date, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
