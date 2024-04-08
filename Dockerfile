FROM python:3.11.8-alpine3.18
WORKDIR /project
ADD . /project
RUN apt-get update && \
    apt-get install tesseract-ocr tesseract-ocr-fra && \
    pip install --no-cache-dir --default-timeout=100 -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]