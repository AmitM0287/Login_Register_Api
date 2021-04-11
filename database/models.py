from django.db import models

# Create your models here.
class UserDetail(models.Model):
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=60)
