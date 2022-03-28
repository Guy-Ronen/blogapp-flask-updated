from flask_blog.models import User
import pytest
import itertools


letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

all_combos = list(itertools.combinations(letters,2)) 
all_combos = [(''.join(combo), ''.join(combo)+ 'gmail.com',''.join(combo)) for combo in all_combos]


@pytest.mark.parametrize(('username , email ,password'), all_combos)
def test_new_user(username, email,password):
    user = User(username=username,email=email, password=password)
    assert user.email == email
    assert user.username == username
    assert user.password == password
    assert isinstance(user.password,str)