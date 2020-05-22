from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def test_registration_post(self):
        page = self.client.post("/accounts/register/")
        self.assertEqual(page.status_code, 200)

    def test_registration_get(self):
        page = self.client.get("/accounts/register/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration.html")

    def test_login_post(self):
        page = self.client.post("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_login_get(self):
        page = self.client.get("/accounts/login/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")


class TestViewsAuthenticatedUser(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.client.login(username=self.user.username, password='top_secret')

    def test_get_registration_page(self):
        page = self.client.post("/accounts/register/")
        self.assertRedirects(page, "/", status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)

    def test_login(self):
        page = self.client.get("/accounts/login/")
        self.assertRedirects(page, "/", status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)

    def test_get_userprofile_page(self):
        page = self.client.get("/accounts/profile/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "profile.html")

    def test_logout(self):
        page = self.client.post("/accounts/logout/")
        self.assertRedirects(page, "/", status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)
