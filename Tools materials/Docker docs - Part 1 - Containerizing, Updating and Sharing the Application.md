 Ref : https://docs.docker.com/get-started/

# Important concepts in Docker
## Container
- Running instance of an image
- One can create, start, stop, move or delete using docker CLI/API
- Portable
- Isolated from other containers
## Image
- Isolated filesystem
- Image must contain everything to run an app:
    - Dependencies, Configs ,Scripts ,Binaries etc.
    - Also contains env variables, default command to run and other metadata
# Containerizing an app
## Prerequisite
- Git client
- Docker desktop
- Visual Studio
- Steps

    1. Clone the getting-started-app repository
    2. Build the app's image
        - In terminal go to the path
        - Create a file "Dockerfile" with the content
    
    
        ```
        # syntax=docker/dockerfile:1

        FROM node:18-alpine
        WORKDIR /app
        COPY . .
        RUN yarn install --production
        CMD ["node", "src/index.js"]
        EXPOSE 3000
        ```

        3. Run the build command 
        docker build -t getting-started .
        4. Start an app container
            * docker run -dp 127.0.0.1:3000:3000 getting-started
                * Flag -d indicates detached and runs in background
                * Flag -p indicates publish. takes the format HOST:CONTAINER
            * check  127.0.0.1:3000
# Update the app
## Update the source code
* Update the code in src/static/js/app.js at 56 line. Replace the line with
```You have no todo items yet! Add one above```
* docker build -t getting-started .
* Remove the old container
    * Using "docker ps" check container name and id
    * docker stop <container_id>
    * docker rm <container_id>
* Start the updated container
    * docker run -dp 127.0.0.1:3000:3000 getting-started

# Share the application
## Push the image to Docker Hub Account
* Create a free account in Docker Hub
* Create a repository with name "getting-started", keep visibility to Public
* Login to Docker using CLI command
    - docker login -u <docker_username>
* Create a tag for the image "getting-started" in local using the command
    - docker tag getting-started <docker_username>/getting-started
    - docker push  <docker_username>/getting-started

# Run image on a new instance
- Go to https://labs.play-with-docker.com/
- Login using Docker credentials and Start
- In the terminal run the command
    - docker run -dp 0.0.0.0:3000:3000 <docker_username>/getting-started
- A popup window will open and specify you want to open the port 3000
