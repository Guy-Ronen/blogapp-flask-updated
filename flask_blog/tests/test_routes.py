from flask_blog import create_app

app = create_app()

def test_base_route():
    client = app.test_client()
    url = '/'
    
    response = client.get(url)
    assert b'Let the first' in response.data
    assert response.status_code == 200

