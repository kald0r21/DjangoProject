from django.db import models

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Shelter(models.Model):
    names = models.CharField(max_length=32)

    def __str__(self):
        return self.names