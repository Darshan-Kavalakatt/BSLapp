from django.db import models

# Create your models here.


class Letter(models.Model):
    letter = models.CharField(max_length=1, unique=True)
    image = models.ImageField()
