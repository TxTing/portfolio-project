from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:50]
    def less_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
