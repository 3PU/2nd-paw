from django.test import TestCase
from .models import Product

class ProductTests(TestCase):
    """Tests to be run against the Product models"""

    def test_str(self):
        test_title = Product(title='A product')
        self.assertEqual(str(test_title), 'A product')