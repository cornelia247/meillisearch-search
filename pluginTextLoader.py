import json

with open('plugins.json', 'r') as f:
    data = json.load(f)

with open('plugins.txt', 'w') as f:
    f.write('plugins:\n')
    for plugin in data:
        f.write(f'  - name: {plugin["name"]}\n')
        f.write(f'    version: {plugin["version"]}\n')
