from django.db import migrations, transaction
from ultimatejobweb.models import job, company


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatejobweb', '0002_test_data_company'),
    ]

    def generate_data(apps, schema_editor):      
        jobs = [('Production Engineer','https://www.facebook.com/careers/jobs/1672813472870915/'),
                ('Product M','https://www.facebook.com/careers/jobs/16732472870915/')]
        
        with transaction.atomic():
            n=0
            for job_title, description_url in jobs:
                n += 1
                company_n = company.objects.get(id=n)
                job(company=company_n, job_title=job_title, description_url=description_url).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
