# Django Channels Vue.js Example

An example of connecting a Django Channels application to Vue.js

## Setup

    pip install -r channels-app/requirements.txt
    python3 channels-app/manage.py migrate

## Requirements

Redis:

    docker run -p 6379:6379 redis

## Running Django Channels

    python3 channels-app/manage.py runserver

## Running UI

    cd vue-app
    yarn serve

Head to http://localhost:8080/
