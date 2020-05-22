from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.shortcuts import get_object_or_404

class TestViews(TestCase):
    
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.client.login(username=self.user.username, password='top_secret')

    def test_get_blogpost_page(self):
        page = self.client.get("/blog/all_blogposts/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogposts.html")

    def test_create_blogpost_posted(self):
        page = self.client.post("/blog/create_blogpost/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_blogpost.html")


    def test_create_blogpost_rendered(self):
        page = self.client.get("/blog/create_blogpost/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_blogpost.html")