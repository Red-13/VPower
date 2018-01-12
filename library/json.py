import json

def load_from_file(json_file):
    try:
        json_data=open(json_file,"r",encoding="UTF-8")
    except:
        print("Exception")
    data = json.load(json_data)
    json_data.close()
    return data
