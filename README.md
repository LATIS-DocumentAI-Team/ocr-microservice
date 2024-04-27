# ocr-microservice

This microservice is build to standirze the usage of  OCR engine, It support 3 main ocr, [PAddleOcr](paddle link), [Tesseract](tesseract link), [EasyOCR](easyOCR), it returns the ocr output following the standard format of a Document from [DocumentAI-std](docAi link), an example of the output will be inn this format: 

```json
{
  "ocr_result": {
    "filename": "0c5d743d-d936-40ae-9642-c9db27c6155c.png",
    "elements": [
      {
        "x": 48,
        "y": 45,
        "w": 47,
        "h": 20,
        "content_type": 1,
        "content": "STE"
      },
      {
        "x": 104,
        "y": 47,
        "w": 97,
        "h": 20,
        "content_type": 1,
        "content": "SIDMAC"
      }
    ]
  },
  "code": 200,
  "message": "success"
}
```