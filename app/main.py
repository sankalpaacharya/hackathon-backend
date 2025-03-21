from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import loan


app = FastAPI(title="hackathon-backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(loan.router, tags=["Loan"],prefix="/loan")

@app.get("/")
async def root():
    return {"message": "Hello dashboard"}
