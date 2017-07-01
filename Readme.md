# Overview

This project helps initialize a sandbox environment to develop for [NetScaler ADC 12.0](nitro-python-1.0/docs/html/index.html) and [NetScaler MAS 12.0](nitro-python-1.0/doc/index.html) Nitro API in Python. 

This project creates a Docker environment for sandboxing and can be deployed as a [single container](#Docker-Run) to interrogate MPX, VPX, and MAS via a [Web based IDE](https://c9.io/) or via a [sandbox environemnt](#Docker-Compose) to interrogate CPX within the defalt Docker network using docker-compose.

# Prerequisits 

1. It is assumed you have installed docker on your machine. If you have not installed docker on your machine, pelase refer to docker's official website to [get started](https://docs.docker.com/engine/installation/)

2. It is required to have a MPX, VPX, or MAS to send API calls to, otherwise use the [docker-compose](#Docker-Compose) method to spin up a CPX on the Docker Network to do some light testing with NITRO API. 


# Build Docker Image

You can pull the main docker image from [DockerHub](https://hub.docker.com/r/mayankt/nitro-ide/) or build your own by doing the following: 

```
git clone https://github.com/MayankTahil/nitro-ide.git
sudo docker build -t mayankt/nitro-ide ./nitro-ide
```

You should see the docker image stored locally using the command `sudo docker images`

```
REPOSITORY				TAG                 IMAGE ID            CREATED             SIZE
mayankt/nitro-ide	   latest            cbd5efd1a833         1 minute ago         982 MB
```

# Run your Docker Image

Simply enter in the following command to run your IDE sandbox environment

````
sudo docker run -dt \ 
--name=nitro-ide \
-p 8080:80 \
-p 8081:8000 \
-v /GitProjects:/workspace \
mayankt/nitro-ide
```
Here is the breakdown of the command from above: 

* `docker run -dt` : This will run the container detached with a terminal in the background
* `-p 8080:80` : This will expose port `8080` on the host and map it to port `80` on the contianer for access to **[Cloud 9 IDE](https://c9.io/)**
* `-p 8081:8000` : This will expose port `8081` on the host and mapt it to port `8000` on the container for access to [git webui](https://github.com/alberthier/git-webui) which allows for [repository managemet](#Repository-UI) via the browser.
* `-v /GitProjects:/workspace` : This will mount the local path on your host at `/Gitprojects` to the local directory within the container at `/workspace`. You can replace the local host directory with any full path on your machine where your projects may be stored. You will be able to edit the same files inside the container via the IDE and locally on your machine if you choose. 
* `mayankt/nitro-ide:latest` : This identifies the `latest` tagged image from dockerhub to use when running the container. You can also check out image [tags](https://hub.docker.com/r/mayankt/nitro-ide/tags/) as this project further develops and accomidates newer versions of NetScaler. 

# Compose an Environment 

If you are looking for a self contained sandbox to try out NITRO commands via NetScaler's Python SDK, you can compose an environment on your machine with the following containers on the docker network: 

1. [Webserver-A](https://hub.docker.com/r/mayankt/webserver/)
2. [Webserver-B](https://hub.docker.com/r/mayankt/webserver/)
3. [NetScaler CPX](https://www.citrix.com/products/netscaler-adc/cpx-express.html)
4. [Nitro-IDE](https://hub.docker.com/r/mayankt/nitro-ide/)

To use `docker-compose` do the following on your host machine: 

```
git archive --remote=git://github.com/MayankTahil/nitro-ide.git HEAD:/ docker-compose.yaml 
```
