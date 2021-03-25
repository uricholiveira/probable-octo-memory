FROM node:lts-buster as build-stage

LABEL maintener="Urich Oliveira"

COPY . /app

WORKDIR /app/

RUN cd /app

RUN yarn global add @quasar/cli

RUN yarn install

RUN quasar build


FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist/spa /app
COPY nginx.conf /etc/nginx/nginx.conf
