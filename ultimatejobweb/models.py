from django.db import models


class company(models.Model):
    CompanyName = models.CharField(max_length=128)
    CompanySearchUrl = models.URLField()
    CompanyLogo = models.TextField()
    FunctionName = models.TextField()


class job(models.Model):
    CompanyName = models.ForeignKey(company, on_delete=models.CASCADE)
    SearchKey = models.CharField(max_length=128)
    JobTitle = models.CharField(max_length=128)
    DescriptionURL = models.URLField()

    def __iter__(self):
        return iter(self.JobTitle)

# Create your models here.
