from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.summary
    def less_pub_date(self):
        return self.pub_date.strftime('%b %e %Y')
