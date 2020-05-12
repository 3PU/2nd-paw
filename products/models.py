from django.db import models

class Product(models.Model):
    category_choices = (
        ("Clothes", "Clothes"),
        ("Toys", "Toys"),
        ("Supplies", "Supplies"),
    )
    animal_choices = (
        ("Cat", "Cat"),
        ("Dog", "Dog"),
    )
    condition_choices = (
        ("New", "New"),
        ("Used", "Used"),
    )

    title = models.CharField(max_length=75)
    category = models.CharField(max_length=100, choices=category_choices)
    animal = models.CharField(max_length=20, choices=animal_choices)
    condition = models.CharField(max_length=20, choices=condition_choices)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.title