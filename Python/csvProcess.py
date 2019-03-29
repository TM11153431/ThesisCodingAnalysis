import csv
import json

arr = []
allTags = []
tagScores = {}

CSVNAME = "../Data/LoremIpsum_1.csv"

with open(CSVNAME) as infile:
    counter = -1
    lines = csv.reader(infile)
    for line in lines:
        counter += 1
        quote = line[1]
        tags = line[5:-1]
        arr.append({"quote": quote, "tags": tags})
        for tag in tags:
            allTags.append(tag)

with open('../Data/processedData.json', 'w') as secondOutfile:
    setTags = set(allTags)
    for tag in setTags:
        tagScores[tag] = {"count": 0, "quotes": []}
    for tag in allTags:
        tagScores[tag]["count"] += 1
    for a in arr:
        for tag in a["tags"]:
            tagScores[tag]["quotes"].append(a["quote"])
    json.dump(tagScores, secondOutfile)
