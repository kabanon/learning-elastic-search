#!/bin/bash

# requirements : https://httpie.org

gzip -d bulk.json.gz
http POST 127.0.0.1:9200/data/_doc/_bulk < bulk.json
gzip bulk.json
