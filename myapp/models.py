from django.db import models
# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    phone = models.CharField(max_length=12)
    content = models.TextField()

    def __str__(self) :
        return self.name