## TODO: Enable GPU for Dockerfile for easyocr
#FROM nvidia/cuda:12.4.1-devel-ubuntu22.04
##FROM python:3.11.8-alpine
#ENV DEBIAN_FRONTEND noninteractive
#RUN apt-get update --fix-missing
#RUN apt-get install -y software-properties-common
#RUN rm -rf /var/lib/apt/lists/*
#
#
#RUN add-apt-repository ppa:deadsnakes/ppa
#RUN apt-get update
#RUN apt-get install -y python3.11
#RUN apt-get install -y python3-pip
#RUN rm -rf /var/lib/apt/lists/*
#
#RUN python3 --version
#
#WORKDIR /project
#ADD . /project
#
#RUN apt-get update
#RUN pip install numpy==1.26.3
#RUN apt-get install ffmpeg libsm6 libxext6  -y
#RUN apt-get install -y tesseract-ocr tesseract-ocr-fra
#
#RUN pip install --no-cache-dir --default-timeout=3600 -r requirements.txt
#
#
#EXPOSE 8000
#CMD ["python", "main.py"]

FROM python:3.11.8-slim
WORKDIR /project
ADD . /project
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y tesseract-ocr tesseract-ocr-all
RUN pip install --no-cache-dir --default-timeout=3600 -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]