from lib.post import *

def test_object_created_with_title_content_views_user_id():
    post = Post(1, 'title', 'content', 'views', 1)
    assert post.id == 1
    assert post.title == 'title'
    assert post.content == 'content'
    assert post.views == 'views'
    assert post.user_id == 1
    
def test_object_formats_nicely():
    post = Post(1, 'title', 'content', 'views', 1)
    assert str(post) == "Post(1, title, content, views, 1)"

def test_object_equality():
    post_1 = Post(1, 'title', 'content', 'views', 1)
    post_2 = Post(1, 'title', 'content', 'views', 1)
    assert post_1 == post_2