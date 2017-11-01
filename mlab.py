import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds151024.mlab.com:51024/cuagaidaicuong

host = "ds133044.mlab.com"
port = 33044
db_name = "freegifts"
user_name = "hello"
password = "banhbao"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
