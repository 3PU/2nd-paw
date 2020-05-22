from django.test import TestCase, Client
from django.shortcuts import get_object_or_404


class TestViews(TestCase):

    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_faq_page(self):
        page = self.client.get("/faq/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "faq.html")

    def test_get_contact_page(self):
        page = self.client.get("/contact/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "contact.html")
