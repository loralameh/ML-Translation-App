# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
ENV FLASK_APP=model.py
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]