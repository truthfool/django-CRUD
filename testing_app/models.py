from django.db import models

# Create your models here.


class UserModel(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.firstname
