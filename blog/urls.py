from django.conf.urls import url
from .views import get_blog_posts, create_blog_post

urlpatterns = [
    url(r'^all_blogposts/$', get_blog_posts, name='get_blog_posts'),
    url(r'^create_blogpost/$', create_blog_post, name='create_blog_post'),
]
