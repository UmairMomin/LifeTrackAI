from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.ai_insight import AIInsight
from app.database import get_db
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/ai-insights", tags=["AI Insights"])

class AIInsightCreate(BaseModel):
    suggestion: Optional[str] = None
    priority_score: Optional[int] = None
    summary: Optional[str] = None
    task_id: int

class AIInsightOut(BaseModel):
    id: int
    suggestion: Optional[str]
    priority_score: Optional[int]
    summary: Optional[str]
    task_id: int

    class Config:
        orm_mode = True

@router.post("/", response_model=AIInsightOut)
def create_ai_insight(insight: AIInsightCreate, db: Session = Depends(get_db)):
    new_insight = AIInsight(**insight.dict())
    db.add(new_insight)
    db.commit()
    db.refresh(new_insight)
    return new_insight

@router.get("/{insight_id}", response_model=AIInsightOut)
def get_ai_insight(insight_id: int, db: Session = Depends(get_db)):
    insight = db.query(AIInsight).get(insight_id)
    if not insight:
        raise HTTPException(status_code=404, detail="Insight not found")
    return insight

@router.get("/", response_model=list[AIInsightOut])
def get_all_insights(db: Session = Depends(get_db)):
    return db.query(AIInsight).all()

@router.delete("/{insight_id}")
def delete_insight(insight_id: int, db: Session = Depends(get_db)):
    insight = db.query(AIInsight).get(insight_id)
    if not insight:
        raise HTTPException(status_code=404, detail="Insight not found")
    db.delete(insight)
    db.commit()
    return {"message": "Insight deleted successfully"}
