from typing import List

from DocumentAI_std.utils.OCR_adapter import OCRAdapter
from fastapi import FastAPI, UploadFile, File, HTTPException, Query
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from src.ResponseModel import ResponseModel
from src.utils import save_file_to_tmp, delete_file

app = FastAPI(
    title="OCR API",
    description="This API applies OCR (Optical Character Recognition) to the provided file and returns the result in a JSON format. "
    "The recognized text is processed and returned as a Document Object following the DocumentAI-std library format.",
    version="1.0.0",
)


@app.post(
    "/applyOcr/",
    tags=["OCR Processing"],
    summary="Apply OCR to the provided file",
    description="This endpoint allows users to apply OCR to an uploaded file. You can specify the OCR method and supported languages. "
    "The recognized text is processed and returned as a JSON object following the Document Object format "
    "from the `DocumentAI-std` library (https://pypi.org/project/DocumentAI-std/).",
)
async def apply_ocr(
    ocr_method: str = Query(
        default="tesseract",
        description="This attribut indicates which ocr method will be applied, for Paddle ocr, `ocr_method = paddle`, "
        "for Tesseract, `ocr_method = tesseract`, for EasyOCR, `ocr_method = easy`",
    ),
    languages: List[str] = Query(
        default=["en"],
        description="List of supported languages. Supported languages are `fr` (French), `en` (English), `de` (German), `ar` (Arabic), `ja` (Japanese), `ch_sim` (Chinese Simplified), and `hi` (Hindi)"
        "Note: Paddle OCR accept only one language (not a list of languages).",
    ),
    file: UploadFile = File(...),
):
    """
    This API endpoint applies OCR (Optical Character Recognition) on the provided file.
    The recognized text is processed and returned as a JSON object following the Document Object format
    from the `DocumentAI-std` library (https://pypi.org/project/DocumentAI-std/).
    The Document Object includes various fields such as the recognized text, entities, and document structure.
    """
    valid_languages = ["fr", "en", "de", "ar", "ja", "ch_sim", "hi"]

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
            detail=f"Invalid language list {languages}. Supported languages are `fr` (French), `en` (English), `de` (German), `ar` (Arabic), `ja` (Japanese), `ch_sim` (Chinese Simplified), and `hi` (Hindi).",
        )

    file_path = save_file_to_tmp(file)

    ocr = OCRAdapter(ocr_method, languages)
    ocr_result = ocr.apply_ocr(file_path).serialize()

    delete_file(file_path)

    return ResponseModel(ocr_result, "success")
