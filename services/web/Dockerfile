#pull the oficial base image
FROM python:3.9.0-slim-buster

#set the work directory
WORKDIR /usr/src/app

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#install dependecies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

#copy project
COPY . /usr/src/app
