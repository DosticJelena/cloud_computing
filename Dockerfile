FROM python:3.8-alpine

RUN apk update \
    && apk add postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR counter_app

COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

RUN cd cloud_rest_api

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]