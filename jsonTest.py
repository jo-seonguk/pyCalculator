import json

json_path = "./test.json"

with open(json_path, 'r') as file:
    data = json.load(file)
    print(type(data))
    print(data)
    print("power: ", data['members'][1]['powers'])

    print(json.dumps(data, indent=2, ensure_ascii=False))

    
