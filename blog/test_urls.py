from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import get_blog_posts, create_blog_post

class TestUrls(TestCase):
    
    def test_get_blog_posts_url_is_resolved(self):
        url = reverse("get_blog_posts")
        self.assertEquals(resolve(url).func, get_blog_posts)
    
    def test_create_blog_post_url_is_resolved(self):
        url = reverse("create_blog_post")
        self.assertEquals(resolve(url).func, create_blog_post)