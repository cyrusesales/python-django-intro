from django.db import models
from django.contrib.auth.models import User # add author of the post
# Create your models here.

class Post(models.Model):
    # define our model fields , slug is urls
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    # means not requiring an image if we dont have one
    banner = models.ImageField(default='fallback.png', blank=True)
    # author is the foreign key into 2 tables
    # on_delete thats telling the database how to handle data if this relationship is deleted
    # CASCADE meanse if deleted. it delete all post too
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
