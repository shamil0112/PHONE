from django.db import models

# Create your models here.


class people(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    place = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name