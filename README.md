# Factory Floor Simulator

[![Build Status](https://travis-ci.com/Tomasz-Kluczkowski/factory-simulator.svg?branch=master)](https://travis-ci.com/Tomasz-Kluczkowski/factory-simulator) [![codecov](https://codecov.io/gh/Tomasz-Kluczkowski/factory-simulator/branch/master/graph/badge.svg)](https://codecov.io/gh/Tomasz-Kluczkowski/factory-simulator)

In this project I am simulating a factory floor operation.

This is based on a programming task received on one of the interviews that got me interested and curious.

The rules are as follows:

- Time is discrete and no action can take less than 1 unit of time.
- In the default settings picking up from and dropping objects onto the conveyor belt takes 1 unit of time.
- In the default settings constructing the finished product takes 4 units of time.
- The conveyor belt is empty at start and all slots are free (can be operated on).
- At each slot of the conveyor belt we place a worker on both sides of it.
- Only one worker can operate on any given slot at any given time.

Default materials required to make a product:
- A
- B

Default code for an empty slot on the conveyor belt:
- E

Default code for the finished product:
- P

The default layout of the factory floor:

```
            (worker) (worker) (worker)
A-B-E-E    |   A    |    E   |   E    |     E-E-E-E-P-E-E
            (worker) (worker) (worker)  

             slot0     slot1   slot2

(Feeder)        (Conveyor Belt)             (Receiver)

```
 
Basic principle of operation:
- The feeder supplies materials required to make a finished product.
- Workers at the conveyor belt slots check if they need and can pickup components.
- Once a worker collected all required materials he begins assembling the product.
- When the product is assembled and worker can operate on his conveyor belt slot (it is free and empty) the worker
will drop the product.
- At each finished unit of time, the last item in the conveyor belt is moved to the receiver. We register if it is a 
finished product, component or an empty slot (this is to be able to provide efficiency metrics and optimization in the 
future)


# Kubernetes deployments
Use your web browser to navigate to the server: `factory-simulator.com/home`

Deployment layout:

Currently, the `ingress-service` redirects requests coming from the browser.
All those for `api/` and `static/` are pushed to `django-backend-service` on port 8000 which maps to the django instance.
All other requests (so `/`) are pushed to `angular-front-end-service` on port 4200 which maps to nginx proxy serving the 
static content of the angular app.
The django app connects to the postgres db through postgres-service on port 5432.

## Local Deployment to Kubernetes
I use microk8s on linux. Make sure you have enabled DNS and ingress.

To deploy locally you have to add in `/etc/hosts`:

`127.0.0.1 factory-simulator.com`

This is to be able to access the application in using `factory-simulator.com` address in your browser.

### Preparing images
from project root build and push the backend image:

```
docker build -t kilthar/factory-simulator-django:latest .
docker push kilthar/factory-simulator-django:latest
```

Build and push the frontend image:

```
cd front-end/
docker build -t kilthar/factory-simulator-angular:latest .
docker push kilthar/factory-simulator-angular:latest
```

For convenience just run: `./rebuild_docker_images.sh` which will rebuild front and backend images and push to docker.

### Deployment to kubernetes locally

from root of the project:

Delete existing deployment:

`kubectl delete -f kubernetes/ -R`   

Deploy new version:

`kubectl apply -f kubernetes/ -R`

