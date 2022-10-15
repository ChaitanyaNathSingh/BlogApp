from django.db import models
from django.template.defaultfilters import truncatechars

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=10)
    genre = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    publish_date = models.DateField(null=True,blank=True)
    description = models.CharField(max_length=300)

    class Meta:
        ordering = ['title']
    
    def __str__(self):
        return self.name

    @property
    def short_description(self):
        return truncatechars(self.description, 100)

