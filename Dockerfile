# Dockerfile

# Pull base image
FROM python:3.7-alpine

# Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
#RUN mkdir /code
WORKDIR /app_code

# Copy project
#COPY . /app/
#COPY code/requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

COPY ./requirements.txt /app_code/
RUN pip install --no-cache-dir -r requirements.txt



#RUN pip install psycopg2
COPY . /app_code/
# Install dependencies
#COPY docker/gunicorn/check_connection.py /script/
#COPY docker/gunicorn/create_django_admin_user.py /script/
#
#COPY docker/gunicorn/entrypoint.sh /script/
#RUN ["chmod", "+x", "/script/entrypoint.sh"]

#ARG GUNICORN_VERSION
#
#RUN pip install --no-cache-dir gunicorn==$GUNICORN_VERSION
#
#COPY requirements.txt /app/
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY check_connection.py /script/
#COPY create_django_admin_user.py /script/
#
#COPY entrypoint.sh /script/
#RUN ["chmod", "+x", "/script/entrypoint.sh"]
