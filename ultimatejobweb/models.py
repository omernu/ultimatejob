from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=128)
    company_search_url = models.URLField()
    company_logo = models.TextField()
    function_name = models.TextField()

    def get(self):
        return self.company_name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=128)
    description_url = models.URLField()


# Create your models here.
