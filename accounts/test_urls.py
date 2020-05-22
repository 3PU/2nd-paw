from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import registration, login, userprofile, logout


class TestUrls(TestCase):

    def test_registration_url_is_resolved(self):
        url = reverse("registration")
        self.assertEquals(resolve(url).func, registration)

    def test_login_url_is_resolved(self):
        url = reverse("login")
        self.assertEquals(resolve(url).func, login)

    def test_userprofile_url_is_resolved(self):
        url = reverse("userprofile")
        self.assertEquals(resolve(url).func, userprofile)

    def test_logout_url_is_resolved(self):
        url = reverse("logout")
        self.assertEquals(resolve(url).func, logout)
