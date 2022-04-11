from flask_blog.models import Post
import pytest
import itertools


letters = ["a", "b","c", "d","e", "f","g", "h","i", "j","k", "l","m", "n",
           "o", "p","q", "r","s", "t","u", "v","w", "x","y", "z",]

all_combos = list(itertools.combinations(letters,2)) 
all_combos = [(''.join(combo),''.join(combo)) for combo in all_combos]


@pytest.mark.parametrize(('title , content'), all_combos)
def test_new_post(title,content):
    post = Post(title=title,content=content)
    assert post.title == title
    assert post.content == content
    assert isinstance(post.title,str)
    assert isinstance(post.content,str)
