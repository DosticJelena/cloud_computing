FROM python:3.8-alpine

WORKDIR /usr/src

RUN apk update && \
apk add postgresql-dev gcc python3-dev musl-dev && \ 
pip install psycopg2 && \
apk update && \
apk add bash

COPY ./requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8000

COPY . .


EXPOSE 8000
CMD cd cloud_rest_api && python manage.py migrate && python manage.py runserver 0.0.0.0:8000