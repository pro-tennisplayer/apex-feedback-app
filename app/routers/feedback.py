from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud, database

router = APIRouter(prefix="/feedback", tags=["feedback"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.FeedbackResponse)
def create_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return crud.create_feedback(db=db, feedback=feedback)

@router.get("/{user_id}", response_model=list[schemas.FeedbackResponse])
def read_feedback(user_id: str, db: Session = Depends(get_db)):
    return crud.get_feedback(db=db, user_id=user_id)
