from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    """Tests to be run against the Product models"""

    def test_str(self):
        test_name = Product(name='A product')
        self.assertEqual(str(test_name), 'A product')