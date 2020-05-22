from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.shortcuts import get_object_or_404
from products.models import Product


class TestViews(TestCase):

    def test_get_all_products_page(self):
        page = self.client.get("/products/all_products/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_cat_products_page(self):
        page = self.client.get("/products/all_products/cat/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_dog_products_page(self):
        page = self.client.get("/products/all_products/dog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_clothes_products_page(self):
        page = self.client.get("/products/all_products/clothes/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_toys_products_page(self):
        page = self.client.get("/products/all_products/toys/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_supplies_products_page(self):
        page = self.client.get("/products/all_products/supplies/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "products.html")

    def test_get_donate_money_page(self):
        page = self.client.get("/products/donate_money/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "donation.html")

    def test_get_product_detail_page(self):
        product = Product(title="TestTitle", price="5")
        product.save()

        page = self.client.get("/products/{0}/".format(product.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "product_detail.html")

    def test_get_product_detail_page_for_product_that_does_not_exist(self):
        page = self.client.get("products/1")
        self.assertEqual(page.status_code, 404)


class TestViewsAuthenticatedUser(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')
        self.client.login(username=self.user.username, password='top_secret')

    def test_get_donate_product_page(self):
        page = self.client.get("/products/donate_product/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "create_product.html")

    def test_create_a_product(self):
        product = Product(title="Create a Test", price="5")
        product.save()

        page = self.client.get("/products/donate_product/")
        response = self.client.post("/products/donate_product/",
                                    {"title": "Create a Test"})
        self.assertTemplateUsed(page, "create_product.html")
