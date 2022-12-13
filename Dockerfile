FROM python:3.7-buster
RUN pip3 install pipenv
RUN mkdir -p /app
COPY /address_json/. /app
WORKDIR /app
RUN pipenv install
