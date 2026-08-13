from sqlalchemy import Column, Integer, String, Date, DateTime, Float, Text
from sqlalchemy.sql import func
from app.database import Base


class UserProfile(Base):
    __tablename__ = "user_profile"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, default="Rahul Dhar")
    target_role = Column(String(200), nullable=False, default="Senior AI / Python Backend Engineer")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    current_company = Column(String(100), default="AllianceTek")
    years_experience = Column(Integer, default=7)
    linkedin_url = Column(String(300), default="")
    github_url = Column(String(300), default="")
    resume_url = Column(String(300), default="")
    # Weekly hour targets
    weekday_target_hours = Column(Float, default=1.5)  # per day
    saturday_target_hours = Column(Float, default=4.0)
    sunday_target_hours = Column(Float, default=3.5)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


class SalaryTarget(Base):
    __tablename__ = "salary_targets"

    id = Column(Integer, primary_key=True, index=True)
    region = Column(String(100), nullable=False)
    currency = Column(String(10), nullable=False)
    salary_min = Column(Float, nullable=False)
    salary_max = Column(Float, nullable=False)
    salary_unit = Column(String(20), default="year")  # year or month
    notes = Column(Text, default="")


class WeeklySchedule(Base):
    __tablename__ = "weekly_schedule"

    id = Column(Integer, primary_key=True, index=True)
    week_number = Column(Integer, nullable=False, unique=True)
    week_start = Column(Date, nullable=False)  # Always Sunday
    week_end = Column(Date, nullable=False)    # Always Saturday
    target_hours = Column(Float, default=15.0)
    theme = Column(String(200), default="")    # Focus topic for the week
    notes = Column(Text, default="")
