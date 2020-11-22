from django.db import models
from django.utils import timezone


class homepage(models.Model):
        author = models.CharField(max_length=200)
        text = models.TextField()
        date = models.DateTimeField(default=timezone.now)

# Create your models here.
