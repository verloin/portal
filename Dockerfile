###########
# BUILDER #
###########


# pull official base image
FROM python:3.9.6-alpine

# create and set work directory
WORKDIR /var/www/portal

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install pip
RUN pip install --upgrade pip

# copy project
COPY . .

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


RUN sed -i 's/\r$//g' ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]






