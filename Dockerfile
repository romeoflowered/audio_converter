FROM python:3.10.4

RUN mkdir /audio_converter
WORKDIR /audio_converter

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y ffmpeg

COPY . .

RUN chmod a+x /audio_converter/docker/*.sh

CMD ["gunicorn", "audio_converter.main:app", "--workers", "1", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]
