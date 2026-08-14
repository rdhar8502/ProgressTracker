from sqlalchemy import Column, Integer, String, Text, DateTime, Date
from sqlalchemy.sql import func
from app.database import Base


class PersonalHubItem(Base):
    __tablename__ = "personal_hub_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    category = Column(String(50), nullable=False)  # "Reminder", "Note", "Need to Ask", "Visa & Immigration"
    content = Column(Text, default="")
    source = Column(Text, default="")  # Links, documents, etc.
    status = Column(String(20), default="Pending")  # "Pending", "Completed"
    due_date = Column(Date, nullable=True)  # Optional, useful for reminders
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
