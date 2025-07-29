from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.task import Task
from app.database import get_db
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# ----- Pydantic Schemas -----
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None
    is_completed: bool = False
    user_id: int

class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: Optional[datetime]
    is_completed: bool
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True

# ----- Routes -----

@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.get("/", response_model=list[TaskOut])
def get_all_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"message": "Task deleted successfully"}
