from django.test import TestCase
from django.urls import reverse, resolve
from search.views import do_search

class TestUrls(TestCase):
    
    def test_search_url_is_resolved(self):
        url = reverse("search")
        self.assertEquals(resolve(url).func, do_search)
