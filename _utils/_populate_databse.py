#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pymongo
import json

client = pymongo.MongoClient("mongodb://127.0.0.1");

types = [
    'region',
    'department',
    'city',
    'arrondissement',
]

locations = client.job_doe_commons.nomenclature_location.find({})


for location in locations:
    if 'type' not in location:
        pass

    item = location
    del item['_id']

    for _type in types:
        if _type in item['components']:
            del item['components'][_type]['_id']
            _id = item['components'][_type]['id_insee']

    # {"index":{"_id":"21540"}}
    print('{{"index":{{"_id": "{}"}}}}'.format(_id))
    print(json.dumps(item))
    del item
    del location
