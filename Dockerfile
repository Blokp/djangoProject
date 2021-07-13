# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN adduser --disabled-login myuser
USER myuser
# run gunicorn
CMD gunicorn djangoProject.wsgi:application --bind 0.0.0.0:$PORT