from fastapi import APIRouter, HTTPException, UploadFile, Form, File
from fastapi.responses import JSONResponse
from pypdf import PdfReader
from app.config.settings import SETTINGS
from typing import Optional
from io import BytesIO
from app.utils.pdf_reader import extract_pdf_text
from app.services.llm import get_ais_summary,get_bank_statement_summary
import enum

router = APIRouter()

class LoanType(str, enum.Enum):
    HOME = "home"
    PERSONAL = "personal"
    CAR = "car"
    EDUCATION = "education"


# extract the pdf's information and pass it to the llm
@router.post("/submit")
async def submit_loan(
    first_name: str = Form(...),
    middle_name: Optional[str] = Form(None),
    last_name: str = Form(...),
    loan_type: LoanType = Form(...),
    pan_id: str = Form(...),
    ais: UploadFile =  File(...),
    loan_description: str = Form(...),
    bank_statement: UploadFile = File(...)
):
    bank_statement_text = await extract_pdf_text(bank_statement)
    ais_text = await extract_pdf_text(ais)
    bank_summary = await get_bank_statement_summary(bank_statement_text)
    ais_summary = await get_ais_summary(ais_text)
    print(bank_summary)

    return JSONResponse(
        status_code=200, 
        content={"status": "success", "message": "File uploaded successfully"}
    )


@router.get("/status")
async def check_status():
    return JSONResponse(status_code=200, content={"status": "error", "message": "Your loan application is pending"})
