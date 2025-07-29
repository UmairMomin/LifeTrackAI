from sqlalchemy import Column, Integer, ForeignKey, DateTime, Interval
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class SessionLog(Base):
    __tablename__ = "session_logs"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime)
    duration = Column(Interval)

    user = relationship("User")
