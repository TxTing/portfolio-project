from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
