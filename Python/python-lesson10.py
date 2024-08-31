import json
with open('./TXT/fruit_inventory111.json', 'r') as json_file:
    loaded_json = json.load(json_file)

originalName = loaded_json['data']['node']['originalName']
print(originalName)
for key, value in loaded_json['data']['node'].items():
    if key == 'originalName':
        print(f'{key} = {value}')

