from fastapi import FastAPI
from app.routes import user, task, ai, ping
from fastapi import Depends
from app.database import create_tables


app = FastAPI(title="LifeTrack AI")

# Route registration
app.include_router(task.router)
app.include_router(ping.router)
app.include_router(ai.router)
app.include_router(user.router)

@app.on_event("startup")
def startup_event():
    create_tables()

@app.get("/")
def root():
    return {"message": "Welcome to LifeTrack AI API"}
