import json
from collections import OrderedDict
import re
from operator import itemgetter

def changex()

def changey()

def findjeanne(data):
    for i in data:
        temp = sorted(i["markers"], key = itemgetter("name"))
        for j in temp:
            if j["name"] == "Jeanne":
                return True
    return False

filename = "./test.json"
filename2 = "./test2.json"

with open(filename, "r") as f:
    loaded_json1 = json.loads(f.read(), object_pairs_hook = OrderedDict)

with open(filename2, "r") as f:
    loaded_json2 = json.loads(f.read(), object_pairs_hook = OrderedDict)

print "Set of Names 1:"
for i in loaded_json1["markers"]:
    print i["name"]

print "\nSet of Names 2"
for i in loaded_json2["markers"]:
    print i["name"]

print "\nAre both json files equal: " + str(loaded_json1 == loaded_json2)

print(loaded_json1["markers"])

print "Is Jeanne in either of the jsons: " + str(findjeanne([dict(loaded_json1),dict(loaded_json2)]))

#just a test
