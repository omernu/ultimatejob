from django.db import models
from django.contrib.auth.models import User


class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=128)


class User_Search_History(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=128)
    JobTitle = models.CharField(max_length=128)
    ApplyURL = models.URLField()
    
class Jobs(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    CompanyName = models.CharField(max_length=128)
    JobTitle = models.CharField(max_length=128)
    ApplyURL = models.URLField()

    def __str__(self):
        return self.CompanyName

# Create your models here.
