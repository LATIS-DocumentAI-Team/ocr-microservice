import io

from DocumentAI_std.utils.OCR_adapter import OCRAdapter
from fastapi import FastAPI, UploadFile, File
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from src.utils import save_file_to_tmp, delete_file

app = FastAPI()

@app.post("/upload/")
async def upload_file(ocr_method: str, file: UploadFile = File(...)):
    valid_extensions = ["jpg", "jpeg", "png", "gif", "bmp", "tiff"]

    file_extension = file.filename.split(".")[-1]
    if file_extension.lower() not in valid_extensions:
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Invalid file type. Only image files are allowed."},
        )

    # Read the uploaded file
    file_path = save_file_to_tmp(file)
    ocr = OCRAdapter(ocr_method, ["fr"])
    ocr_result = ocr.apply_ocr(file_path).serialize()

    delete_file(file_path)

    return {"ocr_result": ocr_result}