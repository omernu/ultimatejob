from django.db import models
from django.contrib.auth.models import User


class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=128)


class company(models.Model):
    UrlCompany = models.URLField(max_length=200)
    CompanyName = models.CharField(max_length=128)

    def __str__(self):
        return self.CompanyName

# Create your models here.
