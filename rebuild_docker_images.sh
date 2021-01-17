#!/usr/bin/env bash

# Create backend docker image and push to docker registry
docker build -t kilthar/factory-simulator-django:latest .
docker push kilthar/factory-simulator-django:latest

# Create frontend docker image and push to docker registry
cd front-end/
docker build -t kilthar/factory-simulator-angular:latest .
docker push kilthar/factory-simulator-angular:latest
