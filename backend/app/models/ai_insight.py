from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class AIInsight(Base):
    __tablename__ = "ai_insights"

    id = Column(Integer, primary_key=True, index=True)
    suggestion = Column(Text)
    priority_score = Column(Integer)  # e.g., AI-assigned priority
    summary = Column(Text)

    task_id = Column(Integer, ForeignKey("tasks.id"))
    task = relationship("Task", back_populates="ai_insight")
