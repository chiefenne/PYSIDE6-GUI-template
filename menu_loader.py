import json

def load_menus_from_json(json_file):
    with open(json_file, 'r') as f:
        menus = json.load(f)
    return menus
