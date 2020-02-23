#!/bin/bash
set -m
docker-compose up --build
#cp ../requirements.txt ./gunicorn/requirements.txt

#if [ "$1" = '-d' ]; then
#  docker-compose up --build -d
#else
#  docker-compose up --build
#fi