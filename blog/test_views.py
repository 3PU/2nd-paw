from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import BlogPost

class TestViews(TestCase):
    
    def test_get_blogpost_page(self):
        page = self.client.get("/blog/all_blogposts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogposts.html")