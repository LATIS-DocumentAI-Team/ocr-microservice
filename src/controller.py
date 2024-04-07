import io

from PIL import Image
from fastapi import FastAPI, UploadFile, File
from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

app = FastAPI()

@app.post("/upload/")
async def upload_file(ocr_method: str, file: UploadFile = File(...)):
    valid_extensions = ["jpg", "jpeg", "png", "gif", "bmp", "tiff"]

    # Check if the uploaded file is an image
    file_extension = file.filename.split(".")[-1]
    if file_extension.lower() not in valid_extensions:
        return JSONResponse(
            status_code=HTTP_422_UNPROCESSABLE_ENTITY,
            content={"detail": "Invalid file type. Only image files are allowed."},
        )

    # Read the uploaded file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Apply OCR based on the chosen method
    ocr_result = ""
    if ocr_method.method == "pytesseract":
        ocr_result = pytesseract.image_to_string(image)
    # Add other OCR methods here...

    return {"ocr_result": ocr_result}