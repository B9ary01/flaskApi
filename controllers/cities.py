from logging import exception

cities=[
    { 'id':1, 'name':'Namche Bazar','population':23000},
    { 'id':2, 'name':'Taplejung','population':313000},
    { 'id':3, 'name':'Vedetar','population':79000},
    { 'id':4, 'name':'Lumbini','population':434000}
    ]

def index(req):
    return [c for c in cities], 200

def create(req):
    new_city=req.get_json()
    new_city['id']=sorted([c['id'] for c in cities])[-1]+1
    cities.append(new_city)
    return new_city,201


def show(req,uid):
    return find_by_uid(uid), 200


def update(req, uid):
    city=find_by_uid(uid)
    data=req.get_json()
    for key, val in data.items():
        city[key]=val
    return city, 200

def destroy(req,uid):
    city=find_by_uid(uid)
    cities.remove(city)
    return city, 204




def find_by_uid(uid):
    try:
        return next(c for c in cities if c['id']==uid)
    except:
        raise Exception("we do not have this cat with this {uid}")