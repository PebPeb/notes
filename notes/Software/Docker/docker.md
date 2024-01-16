
# Docker


Commands for docker images

``` bash
docker images
docker rmi <image_name_or_ID>
docker image prune
docker build -t <image_name> <Dockerfile_dir>
```

Commands for docker containers

``` bash 

docker ps
docker ps -a
docker rm <container_name_or_ID>

docker start <container_name_or_ID>
docker stop <container_name_or_ID>

```


## Example

-t is used to keep the container running

`docker run --name=my-test-alpine -d -t test `
`docker run --name=my-wireguard-container -p 51820:51820/udp wireguard`


