from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db

router = APIRouter(tags=["System"])

@router.get("/ping-db", summary="Check DB connectivity")
def ping_database(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"message": "Database connection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")
