from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=120)
    email =models.CharField(max_length=120)
    phone = models.CharField(max_length=10)
    description = models.TextField()


    def __str__(self):
        return self.name