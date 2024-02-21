FROM python:3.10.8-slim-buster

MAINTAINER Aquib Javed "aquibjavedt007@gmail.com"

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP gta/main.py

CMD ["flask", "run", "--host=0.0.0.0"]
