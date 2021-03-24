FROM python:3.9

LABEL maintener="Urich Oliveira"

COPY . /app

WORKDIR /app/

ENV ENV_FOR_DYNACONF='development'

RUN pip install poetry

RUN cd /app && poetry install

EXPOSE 8000
