
cities=[
    { 'id':1, 'name':'Namche Bazar','population':23000},
    { 'id':2, 'name':'Taplejung','population':313000},
    { 'id':3, 'name':'Vedetar','population':79000},
    { 'id':4, 'name':'Lumbini','population':434000}
    ]

def index(req):
    return [c for c in cities], 200
