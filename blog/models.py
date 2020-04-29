from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """Creates a single blogpost"""
    title= models.CharField(max_length=200)
    author = models.ForeignKey(User, related_name="blog_posts", on_delete=models.CASCADE)
    animal_name = models.CharField(max_length=100)
    content= models.TextField()
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __str__(self):
        return self.title