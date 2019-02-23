import json

with open('distro.json', 'r') as f:
    distros_dict = json.load(f)

for key, value in distros_dict.items():
    if key == "resources":
        print(value)