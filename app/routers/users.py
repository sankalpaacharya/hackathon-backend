from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.supabase import get_org_requests


router = APIRouter()

@router.get("/get")
async def get_users(org_id:str):
    response = get_org_requests("a3c5a7d8-0ce4-480e-8c5f-eb66f52d91ba")
    return JSONResponse(status_code=200,content=response.data)

    
    