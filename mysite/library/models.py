from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=200)
    tagline = models.TextField()

    def __str__(self):
        return self.name
    

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField(default=timezone.now)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline
    
    