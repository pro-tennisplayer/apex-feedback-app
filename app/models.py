from sqlalchemy import Column, Integer, String, Text, DateTime, func
from .database import Base

class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, nullable=False)
    comments = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
