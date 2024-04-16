# TODO: Enable GPU for Dockerfile for easyocr
FROM nvidia/cuda:11.0-base-ubuntu20.04

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES compute,utility

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    vim \
    python3.11 \
    python3-pip \
    && \
    rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    cuda-11-0 \
    libcudnn8=8.0.4.30-1+cuda11.0 \
    libcudnn8-dev=8.0.4.30-1+cuda11.0 \
    && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /project
ADD . /project

RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y tesseract-ocr tesseract-ocr-fra
RUN pip install --no-cache-dir --default-timeout=3600 -r requirements.txt

EXPOSE 8000
CMD ["python", "main.py"]