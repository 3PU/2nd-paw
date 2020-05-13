from django.conf.urls import url, include
from .views import all_products, products_animal_cat, products_animal_dog, products_category_clothes, products_category_toys, products_category_supplies, product_detail, donate_product, make_donation

urlpatterns = [
    url(r'^all_products/$', all_products, name="all_products"),
    url(r'^all_products/cat/$', products_animal_cat, name="products_animal_cat"),
    url(r'^all_products/dog/$', products_animal_dog, name="products_animal_dog"),
    url(r'^all_products/clothes/$', products_category_clothes, name="products_category_clothes"),
    url(r'^all_products/toys/$', products_category_toys, name="products_category_toys"),
    url(r'^all_products/supplies/$', products_category_supplies, name="products_category_supplies"),
    url(r'^(?P<id>\d+)/$', product_detail, name="product_detail"),
    url(r'^donate_product/$', donate_product, name="donate_product"),
    url(r'^donate_money/$', make_donation, name="make_donation"),
]