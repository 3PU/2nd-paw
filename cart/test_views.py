from django.test import TestCase, Client
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def test_get_view_cart_page(self):
        page = self.client.get("/cart/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "cart.html")
