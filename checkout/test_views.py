from django.test import TestCase, Client
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def test_checkout(self):
        page = self.client.get("/checkout/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "checkout.html")
