import csv
import json

bulk = []

# Parse CSV data.
with open('./sources/rome_code.csv', 'r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',', quotechar='"')
    for line in lines:
        # Operation.
        op = {
            'index': {
                '_id': "{}{}{}{}".format(line[0], line[1], line[2], line[4])
            }
        }
        # Data.
        data = {
            'family': line[0]
        }
        if line[1] != "":
            data['domain'] = line[1]
        if line[2] != "":
            data['card'] = line[2]
        if line[3] != "":
            data['label'] = line[3]
        if line[4] != "":
            data['id_ogr'] = line[4]
        # Json format.
        bulk.append(json.dumps(op))
        bulk.append(json.dumps(data))

# Generate Json file.
with open('../rome_code.json', 'w') as jsonfile:
    for item in bulk:
        jsonfile.write("{}\n".format(item))

print('-> This is the end...')
