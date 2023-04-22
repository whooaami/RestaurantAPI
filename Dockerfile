FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /restaurant_service

COPY requirements.txt /restaurant_service/
RUN pip3 install -r requirements.txt

COPY . /restaurant_service/
