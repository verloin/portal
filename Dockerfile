# pull official base image
FROM python:3.9.6-alpine

# create and set work directory
WORKDIR /var/www/portal

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project data
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .






