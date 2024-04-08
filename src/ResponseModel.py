def ResponseModel(ocr_result, message):
    return {
        "ocr_result": ocr_result,
        "code": 200,
        "message": message,
    }
