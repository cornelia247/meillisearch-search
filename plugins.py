import requests
import json

plugins_url = 'https://chrisstore.co/api/v1/plugins/'
output_file = 'plugins.json'

plugins = []
next_page = plugins_url

while next_page:
    response = requests.get(next_page)
    data = response.json()
    items = data['collection']['items']
    for item in items:
        plugin = {}
        for prop in item['data']:
            plugin[prop['name']] = prop['value']
        plugins.append(plugin)
    links = data['collection'].get('links', [])
    next_link = next((link for link in links if link['rel'] == 'next'), None)
    next_page = next_link['href'] if next_link else None

with open(output_file, 'w') as f:
    json.dump(plugins, f)
