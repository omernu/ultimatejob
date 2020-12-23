from django.db import migrations, transaction
from ultimatejobweb.models import Job, Company


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatejobweb', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        company1 = Company(1, '"https://careers-redhat.icims.com/jobs/search?ss=1&in_iframe=1&searchKeyword=',
                           'logo1', 'function1')
        company2 = Company(2, 'https://www.amazon.jobs/en/', 'logo2', 'function2')

        jobs = [
          (company1, 'Production Engineer',
           'https://www.facebook.com/careers/jobs/1672813472870915/'),
          (company2, 'Production Engineer',
           'https://www.facebook.com/careers/jobs/712878282607325/'),
        ]

        companies = [
          ('Facebook', '"https://careers-redhat.icims.com/jobs/search?ss=1&in_iframe=1&searchKeyword=',
           'logo1', 'function1'),
          ('Amazon', 'https://www.amazon.jobs/en/', 'logo2', 'function2'),
        ]

        with transaction.atomic():
            for company_name, company_search_url, company_logo, function_name in companies:
                Company(company_name=company_name, company_search_url=company_search_url, company_logo=company_logo,
                        function_name=function_name).save()

            for company, job_title, description_url in jobs:
                Job(company=company, job_title=job_title, description_url=description_url).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
