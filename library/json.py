import json

def load_from_file(json_file):
    json_data=open(json_file)
    data = json.load(json_data)
    json_data.close()
    return data
