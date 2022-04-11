from flask_blog import create_app
import pytest
app = create_app()

page_examples= [('/',b"Welcome to TooDoo"),('about',b"About Page"),('register',b"Join Today"),('login', B"Welcome Back")]

@pytest.mark.parametrize('url,binary_str',page_examples)
def test_base_route(url,binary_str):
    client = app.test_client()
    
    response = client.get(url)
    assert binary_str in response.data
    assert response.status_code == 200


page_fails= [('home',302),('account',302),('some_random_page',404),('post/new', 302)]
@pytest.mark.parametrize('url,status_code',page_fails)
def test_routes_to_fail(url,status_code):
    client = app.test_client()
    response = client.get(url)
    assert response.status_code == status_code