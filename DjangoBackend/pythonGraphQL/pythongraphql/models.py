from django.db import models

# Create your models here.
class users(models.Model):
    username = models.TextField(unique=True)
    password = models.TextField()
    email = models.TextField(unique=True)
    dateCreated = models.DateTimeField()
    dateOfBirth = models.DateField()