import json

with open('example.json', 'r') as f:
    array = json.load(f)

print (array["glossary"])
