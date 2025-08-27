from sqlalchemy.orm import Session
from . import models, schemas

def create_feedback(db: Session, feedback: schemas.FeedbackCreate):
    db_feedback = models.Feedback(user_id=feedback.user_id, comments=feedback.comments)
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedback(db: Session, user_id: str):
    return db.query(models.Feedback).filter(models.Feedback.user_id == user_id).all()
