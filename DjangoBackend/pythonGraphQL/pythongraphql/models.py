from django.db import models

# Create your models here.
class users(models.Model):
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
    dateCreated = models.DateTimeField()
    dateOfBirth = models.DateField()