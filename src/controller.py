from typing import List

from DocumentAI_std.utils.OCR_adapter import OCRAdapter
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from src.ResponseModel import ResponseModel
from src.utils import save_file_to_tmp, delete_file

app = FastAPI()


@app.post("/upload/")
async def upload_file(
    ocr_method: str,
    languages: List[str] = Query(
        None,
        description="List of supported languages. Supported languages are 'fr' (French) and 'en' (English).",
    ),
    file: UploadFile = File(...),
):
    # TODO: - Add in the document which ocr support multiple language
    #       - Rename the URI
    #       - The Fastest is Tesseract
    valid_languages = ["fr", "en"]
    valid_extensions = ["jpg", "jpeg", "png", "gif", "bmp", "tiff"]

    file_extension = file.filename.split(".")[-1]
    if file_extension.lower() not in valid_extensions:
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Invalid file type. Only image files are allowed."},
        )

    if any(lang not in valid_languages for lang in languages):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid language list {languages}. Supported languages are 'fr' (French) and 'en' (English).",
        )

    file_path = save_file_to_tmp(file)

    ocr = OCRAdapter(ocr_method, languages)
    ocr_result = ocr.apply_ocr(file_path).serialize()

    delete_file(file_path)

    return ResponseModel(ocr_result, "success")
