from django.db import migrations, transaction
from ultimatejobweb.models import job, company


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatejobweb', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        company1 = company(1, '"https://careers-redhat.icims.com/jobs/search?ss=1&in_iframe=1&searchKeyword=',
                           'logo1', 'function1')
        company2 = company(2, 'https://www.amazon.jobs/en/', 'logo2', 'function2')

        jobs = [
          (company1, 'DevOps', 'Production Engineer',
           'https://www.facebook.com/careers/jobs/1672813472870915/'),
          (company2, 'DevOps', 'Production Engineer',
           'https://www.facebook.com/careers/jobs/712878282607325/'),
        ]

        companies = [
          ('Facebook', '"https://careers-redhat.icims.com/jobs/search?ss=1&in_iframe=1&searchKeyword=',
           'logo1', 'function1'),
          ('Amazon', 'https://www.amazon.jobs/en/', 'logo2', 'function2'),
        ]

        with transaction.atomic():
            for CompanyName, CompanySearchUrl, CompanyLogo, FunctionName in companies:
                company(CompanyName=CompanyName, CompanySearchUrl=CompanySearchUrl, CompanyLogo=CompanyLogo,
                        FunctionName=FunctionName).save()

            for CompanyName, SearchKey, JobTitle, DescriptionURL in jobs:
                job(CompanyName=CompanyName, SearchKey=SearchKey, JobTitle=JobTitle,
                    DescriptionURL=DescriptionURL).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
