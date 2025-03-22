from fastapi import APIRouter
from pydantic import BaseModel



router = APIRouter()



@router.get("/get")
async def get_request(request):
    pass 