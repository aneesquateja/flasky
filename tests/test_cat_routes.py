def test_get_all_cats_with_no_records(client):
    #act
    response = client.get("/cats")
    response_body = response.get_json()
    
    #assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_cat_succeeds(client, two_saved_cats):
    response = client.get("cats/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name" : "Luna",
        "color" : "ash",
        "personality": "Tomato Queen"
    }

def test_create_one_cat_in_empty_db(client):
    response = client.post("/cats", json={
        "name" : "Garfield",
        "color" : "ornage",
        "personality" : "Likes Lasagna, hates Mondays"
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id" : 1,
        "name" : "Garfield",
        "color" : "ornage",
        "personality" : "Likes Lasagna, hates Mondays"
    }

    
