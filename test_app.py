
def test_index_route(api):

    response =api.get('/')
    assert response.status == "200 OK"

    assert b"The Top Cities of Nepal" in response.data
