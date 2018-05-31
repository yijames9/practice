import json

filename = "./test.json"

with open(filename, "r") as f:
    loaded_json = json.loads(f.read())
    print loaded_json
