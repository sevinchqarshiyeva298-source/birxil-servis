FROM python:3.11-slim

WORKDIR /srv/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV SERVICE_VER=1.0
ENV STAGE_NAME=docker-container

EXPOSE 5000

CMD ["python", "main.py"]
