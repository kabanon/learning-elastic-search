#!/bin/bash

# Source : https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.2.1
