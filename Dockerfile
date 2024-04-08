FROM python:3.11.8-slim
WORKDIR /project
ADD . /project
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install -y tesseract-ocr tesseract-ocr-fra
RUN pip install --no-cache-dir --default-timeout=3600 -r requirements.txt
EXPOSE 8000
CMD ["python", "main.py"]