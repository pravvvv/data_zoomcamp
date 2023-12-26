# Examples of Data Pipelines







# Docker
[Docker Part 1](https://github.com/pravvvv/data_zoomcamp/blob/main/Tools%20materials/Docker%20docs%20-%20Part%201%20-%20Containerizing%2C%20Updating%20and%20Sharing%20the%20Application.md)
&nbsp; &nbsp; &nbsp; &nbsp; [Docker Part 2](https://github.com/pravvvv/data_zoomcamp/blob/main/Tools%20materials/Docker%20docs%20-%20Part%202%20-%20Persist%20the%20DB%2C%20Use%20bind%20mounts.md)
- Docker Daemon (dockerd)
    - listens to API calls
    - manages Docker containers, images, networks and volumes
    - communication with other docker services

- Docker client (docker)
    - primary way that docker users interact with docker
    - docker run is an example

- Docker registries
    - stores docker images
    - Docker hub is a public registry
    - docker push is used to push image to configured registry

- Docker objects
    - Image
        - Image can be based on another image
        - To build an image you could use Dockerfile
        - Whenever a dockerfile is build the image is built in layers
        - Whenever a dockerfile is modified only the changes in the layers are made where changes happened
    - Containers
        - Runnable instance of an image
        - One could create, start, stop, move or delete a container using docker API/CLI
        - defined by image and all the configuration options
        - When containers are removed everything related to its persistant storage also disappear

- Example docker commands 
    - docker run hello_world
    - docker run -it ubuntu bash # image name = ubuntu , argument = bash
    - docker run -it python:3.9 # it = interactive
    - docker run -it --entrypoint=bash python:3.9
    - docker build -t test:pandas .
    - docker run -it test:pandas
    - docker stop my_image:latest # stop the container, here latest is the tag and my_image is the repository name
    - docker rmi my_image:latest -f # forcefully remove the image

- Docker File
```
FROM <IMAGE_NAME>
RUN <commands>
WORKDIR
ENTRYPOINT ['bash']
```
# Why should we care about Docker?
- Local experiments
- Integration tests (CI /CD)
- Reproducability
- Running pipelines on the cloud (AWS Batch, Kubernetes jobs)
- Spark
- Serverless(AWS Lambda, Google functions)


