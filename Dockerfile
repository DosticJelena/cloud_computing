FROM python:3.8-alpine

EXPOSE 8000

LABEL maintainer="Jelena Dostic"
LABEL description="Dockerfile"

WORKDIR /usr/src

COPY ./requirements.txt .

RUN apk update && \
apk add postgresql-dev gcc python3-dev musl-dev && \ 
pip install psycopg2 && \
apk update && \
apk add bash && \
pip install -r requirements.txt

COPY . .

CMD cd cloud_rest_api && \
python manage.py makemigrations && \
python manage.py migrate && \
python manage.py runserver 0.0.0.0:8000