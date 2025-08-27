# FastAPI Feedback API

A FastAPI application that connects to Azure PostgreSQL Flexible Server to store and retrieve user feedback.

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI entry point
│   ├── database.py        # DB connection
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # Database queries
│   └── routers/
│       └── feedback.py    # API endpoints
├── requirements.txt
├── run.sh                 # Linux/Mac startup script
├── run.bat                # Windows startup script
└── README.md
```

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure database connection:**
   Create a `.env` file in the backend directory with:
   ```
   DATABASE_URL=postgresql://username:password@your-server.postgres.database.azure.com:5432/your_database
   ```

3. **Run the application:**
   - **Linux/Mac:** `./run.sh`
   - **Windows:** `run.bat`
   - **Manual:** `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`

## API Endpoints

- **POST** `/feedback` - Create new feedback
  - Body: `{"user_id": "string", "comments": "string"}`
  
- **GET** `/feedback/{user_id}` - Retrieve feedback for a specific user

## Database Schema

The `feedback` table contains:
- `id` (Primary Key)
- `user_id` (String)
- `comments` (Text)
- `created_at` (DateTime, auto-generated)

## Features

- SQLAlchemy ORM for database operations
- Pydantic schemas for request/response validation
- FastAPI automatic API documentation at `/docs`
- Database schema auto-creation on startup
- Environment-based configuration
