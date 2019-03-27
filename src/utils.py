import json


# load json file
def load_json_config(file_name):
    f = open(file_name, 'r')
    result = json.load(f, 'utf-8')
    print result
    return result
