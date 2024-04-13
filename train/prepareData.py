import json

with open('traindata.json') as f:
    data = json.load(f)

JSON_file = data

with open('output.jsonl', 'w') as outfile:
    for entry in JSON_file:
        json.dump(entry, outfile)
        outfile.write('\n')