from django.test import TestCase
from django.urls import reverse, resolve
from checkout.views import checkout


class TestUrls(TestCase):

        def test_checkout_url_is_resolved(self):
            url = reverse("checkout")
            self.assertEquals(resolve(url).func, checkout)
