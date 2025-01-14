from django.db import models

# Create your models here.

class Post(models.Model):
    # define our model fields , slug is urls
    title = models.CharField(max_length=75)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    # means not requiring an image if we dont have one
    banner = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title
