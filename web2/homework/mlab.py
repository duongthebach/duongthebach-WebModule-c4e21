import mongoengine


# mongodb://<dbuser>:<dbpassword>@ds161092.mlab.com:61092/register
host = "ds161092.mlab.com"
port = 61092
db_name = "register"
user_name = "thebach"
password = "thebach1997"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())