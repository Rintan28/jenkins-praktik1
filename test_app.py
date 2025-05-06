from app import app

def test_hello():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Halo dari Jenkins Multibranch Pipeline RaWRrr!' in response.data