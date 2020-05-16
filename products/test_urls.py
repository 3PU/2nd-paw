from django.test import TestCase
from django.urls import reverse, resolve
from products.views import all_products, products_animal_cat, products_animal_dog, products_category_clothes, products_category_toys, products_category_supplies, product_detail, donate_product, make_donation

class TestUrls(TestCase):
    
    def test_all_products_url_is_resolved(self):
        url = reverse("all_products")
        self.assertEquals(resolve(url).func, all_products)
    
    def test_products_animal_cat_url_is_resolved(self):
        url = reverse("products_animal_cat")
        self.assertEquals(resolve(url).func, products_animal_cat)

    def test_products_animal_dog_url_is_resolved(self):
        url = reverse("products_animal_dog")
        self.assertEquals(resolve(url).func, products_animal_dog)

    def test_cproducts_category_clothes_url_is_resolved(self):
        url = reverse("products_category_clothes")
        self.assertEquals(resolve(url).func, products_category_clothes)

    def test_products_category_toys_url_is_resolved(self):
        url = reverse("products_category_toys")
        self.assertEquals(resolve(url).func, products_category_toys)

    def test_products_category_supplies_url_is_resolved(self):
        url = reverse("products_category_supplies")
        self.assertEquals(resolve(url).func, products_category_supplies)

    def test_product_detail_url_is_resolved(self):
        url = reverse("product_detail", args=[1])
        self.assertEquals(url, "/products/1/")

    def test_donate_product_url_is_resolved(self):
        url = reverse("donate_product")
        self.assertEquals(resolve(url).func, donate_product)

    def test_make_donation_url_is_resolved(self):
        url = reverse("make_donation")
        self.assertEquals(resolve(url).func, make_donation)