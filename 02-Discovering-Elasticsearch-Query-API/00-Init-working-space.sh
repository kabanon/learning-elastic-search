#!/bin/bash

# Delete index
http DELETE 127.0.0.1:9200/rome/

# Bulk operation
http POST 127.0.0.1:9200/rome/_doc/_bulk < ../00-Samples/rome_code.json
