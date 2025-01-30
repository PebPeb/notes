
# Docker


# Images

Commands for working with images

``` bash
docker images
docker rmi <image_name_or_ID>
docker image prune
docker build -t <image_name> <Dockerfile_dir>
```

## Containers 
### Running Container

- `docker run <args> <image_name>`: Builds and starts a container from the image
  - `--name <container_name>`: Sets custom name for container
  - `-d`: Runs the container in detached mode
  - `-p <host_port>:<container_port>`: Maps port from host computer to port in the container
  - `-v <host_path>:<container_path>`: Mounts a host directory into the container
  - `/bin/bash`: Opens a bash shell inside the container (this goes after `<image_name>`)

### Working with Containers

Commands for working with docker containers

- `docker ps`: Shows only running containers
- `docker ps -a`: Shows all containers, including stopped ones
- `docker rm <container_name_or_ID>`
- `docker start <container_name_or_ID>`
- `docker stop <container_name_or_ID>`


## Example

-t is used to keep the container running

`docker run --name=my-test-alpine -d -t test `
`docker run --name=my-wireguard-container -p 51820:51820/udp wireguard`


