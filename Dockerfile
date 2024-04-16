# TODO: Enable GPU for Dockerfile for easyocr
FROM nvidia/cuda:12.1.1-runtime-ubuntu20.04

RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /project
ADD . /project

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y tesseract-ocr tesseract-ocr-fra
RUN pip install --no-cache-dir --default-timeout=3600 -r requirements.txt


EXPOSE 8000
CMD ["python", "main.py"]