import json

def read_from_db():
    with open('db.json', 'r') as opendb:
        json_object = json.load(opendb)
    
    return json_object

def write_to_db(json_object):
    with open("db.json", "w") as opendb:
        json.dump(json_object, opendb)