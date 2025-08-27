from fastapi import FastAPI
from .routers import feedback
from .database import Base, engine
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Try to create database tables, but don't crash if it fails
try:
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")
except Exception as e:
    logger.warning(f"Could not create database tables: {e}")
    logger.warning("App will continue without database initialization")

app.include_router(feedback.router)

@app.get("/")
async def root():
    return {"message": "APEX Feedback API is running!"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}
