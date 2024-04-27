# OCR Microservice

This microservice standardizes the usage of Optical Character Recognition (OCR) engines, providing a unified interface to access multiple OCR engines. It currently supports three main OCR engines:

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR): A deep learning-based OCR engine capable of handling various tasks such as text detection, recognition, and structure analysis.
- [Tesseract](https://github.com/tesseract-ocr/tesseract): An open-source OCR engine that provides accurate text recognition from images.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR): Another deep learning-based OCR engine known for its simplicity and ease of use.

The microservice returns OCR output in a standardized format of a Document following the structure defined by [DocumentAI-std](https://github.com/LATIS-DocumentAI-Group/DocumentAI-std). An example of the output is provided below:

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

## Built with

- [Python3.11](https://www.python.org/downloads/): The microservice is developed using Python 3.11, providing a robust and efficient runtime environment.
- [Fast API](https://fastapi.tiangolo.com/): FastAPI is used to build the RESTful API endpoints, offering high performance and easy-to-use tools for API development.

## Usage

### Locally:

1. **Download the repository:**

```shell
git clone https://github.com/LATIS-DocumentAI-Group/ocr-microservice.git
cd ocr-microservice
```

2. **Install the requirements:**

```shell
pip install -r requirements.txt
```

3. **Run the main file:**

```shell
python main.py
```

### Using Docker

1. **Pull the Docker image:**

```shell
docker pull hamzagbada18/ocr-microservice:latest
```

2. **Run the Docker container:**

```shell
docker run -p 8000:8000 --name ocr-api hamzagbada18/ocr-microservice:latest
```

3. **Access the OpenAPI documentation:**

You can access the [OpenAPI Specification](https://swagger.io/specification/) documentation through the following link: [localhost:8000/docs](http://localhost:8000/docs)

5. **Acces throw REST API**
- `POST /applyOcr/`
- Apply OCR

**Params:**


| Name         | Description                                                                                                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `ocr_method` | This attribute indicates which OCR method will be applied. For Paddle OCR, `ocr_method = paddle`. For Tesseract, `ocr_method = tesseract`. For EasyOCR, `ocr_method = easy`. |
| `languages`  | List of supported languages. Supported languages are `fr` (French) and `en` (English). Note: Paddle OCR accepts only one language.                                           |

6. **Example usage with curl:**

```shell
curl -X 'POST' \
  'http://localhost:8000/applyOcr/?ocr_method=tesseract&languages=en' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@invoiceBLUR.png;type=image/png'
```





