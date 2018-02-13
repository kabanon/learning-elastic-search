# Learning Elasticsearch

## Working environment
- Ubuntu 16.04
- Docker 17.12.0-ce
- Elasticsearch 6.2.1

## Install docker
```bash
#!/bin/bash
# Source : https://docs.docker.com/install/linux/docker-ce/ubuntu/

# Uninstall old docker
# Older versions of Docker were called docker or docker-engine. If these are installed, uninstall them:
sudo apt-get remove docker docker-engine docker.io
# Set up the repository
# Install packages to allow apt to use a repository over HTTPS:
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
# Add Docker’s official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.
sudo apt-key fingerprint 0EBFCD88
# Set up the stable repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# Update the apt package index.
sudo apt-get update
# Install Docker
sudo apt-get install docker-ce
# Check installation
sudo docker run hello-world
```
## Get Elasticsearch docker image
```bash
#!/bin/bash
# Source : https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
sudo docker pull docker.elastic.co/elasticsearch/elasticsearch:6.2.1
```
## Run Elasticsearch
```bash
#!/bin/bash
sudo docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.1
```
