from pydantic import BaseModel
from datetime import datetime

class FeedbackCreate(BaseModel):
    user_id: str
    comments: str

class FeedbackResponse(BaseModel):
    id: int
    user_id: str
    comments: str
    created_at: datetime

    class Config:
        from_attributes = True
