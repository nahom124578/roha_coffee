FROM python:3.12

ENV PYTHONUNBUFFERED 1

WORKDIR /app 

RUN apt-get update && apt-get install -y vim

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app