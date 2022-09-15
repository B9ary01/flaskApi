
def test_index_route(api):

    response =api.get('/')
    assert response.status == "200 OK"
    assert b"The Top Cities of Nepal" in response.data


def test_cities_post_route(api):
    response=api.post("cities")
    assert response.status=="405 METHOD NOT ALLOWED"
    assert response.status_code==405


def test_new_cities_route(api):
    res=api.post("/city/new")
    assert res.status_code==400
    data={
        "region":"peaks",
        
    }
    res=api.post("/city/new",json=data)
    assert res.status_code==201
    




