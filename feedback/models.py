from django.db import models

# Create your models here.
class Contact(models.Model):
    topic = models.CharField( max_length=2)
    subject = models.TextField()
    day=models.CharField( max_length=2)
    

    def __str__(self):
        return self.name 


