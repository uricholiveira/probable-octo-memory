FROM node:lts-buster

LABEL maintener="Urich Oliveira"

COPY . /app

WORKDIR /app/

RUN cd /app

RUN yarn global add @quasar/cli

RUN yarn install

RUN quasar build

EXPOSE 8080
