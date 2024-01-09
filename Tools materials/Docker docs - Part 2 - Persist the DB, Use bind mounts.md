# Containers from same image
- Start a ubuntu container with a file named /data.txt with a random number between 1 and 1000
    - command for  random number between 1 and 1000
        - shuf -i 1 1000 -n 1
    - command to write to /data.txt
        - -o /data.txt
    - command to watch a file to keep the container running. tail will watch the file indefinitely
        - tail -f /dev/null
    - To run a container and execute the above commands we could write them in a single line
        - docker run -d --name container_001 ubuntu bash -c "shuf -i 1-1000 -n 1 -o /data.txt && tail -f /dev/null"
    - Run another container
        - docker run -d --name container_002 ubuntu bash -c "tail -f /dev/null"
    - To check whether the container is running successfully use this to check the value of /data.txt
        - docker exec container_001 cat /data.txt  #### Result should be a random number
        - docker exec container_002 cat /data.txt  #### Result should be an error
    - Once you get the results remove the containers using
        - docker rm -f <container_name>
        - docker rm <container_name> #### will not remove running containers


