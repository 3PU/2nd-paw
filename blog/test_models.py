from django.test import TestCase
from .models import BlogPost


class TestBlogPostModel(TestCase):

    def test_blogpost_as_a_string(self):
        post = BlogPost(title="TestTitle")
        self.assertEqual(str(post), "TestTitle")
