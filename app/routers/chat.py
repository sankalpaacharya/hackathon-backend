from fastapi import APIRouter
from pydantic import BaseModel



router = APIRouter()

class ChatRequest(BaseModel):
    request_id:str
    query:str


@router.get("/")
async def chat(request:ChatRequest):
    pass