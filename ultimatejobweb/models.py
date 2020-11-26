from django.db import models
from django.utils import timezone


class user(models.Model):
    emailAndUsername = models.EmailField(max_length=254)
    password = models.CharField(max_length=32)
    firstName = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    profession = models.CharField(max_length=128)

    def __str__(self):
        return self.emailAndusername


class company(models.Model):
    UrlCompany = models.URLField(max_length=200)
    CompanyName = models.CharField(max_length=128)

    def __str__(self):
        return self.CompanyName

# Create your models here.
