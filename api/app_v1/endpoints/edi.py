from typing import Literal
from fastapi import APIRouter, UploadFile

from core.edi_parser import X12

router = APIRouter()


@router.post("/parse-file/{format}", tags=["parse-file"], status_code=200)
async def x12_file_translation(
    format_type: Literal["xml", "json"], uploaded_file: UploadFile
):
    obj = X12(format_type.lower(), uploaded_file)

    return await obj.parse_file()
