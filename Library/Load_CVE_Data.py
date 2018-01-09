import json

def Load_JSON_From_File(json_file):
    json_data=open(json_file)
    data = json.load(json_data)
    json_data.close()
    return data
