from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    """Creates a single blogpost"""
    title= models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    animal_name = models.CharField(max_length=100)
    content= models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to="img", blank=True, null=True)

    def __str__(self):
        return self.title