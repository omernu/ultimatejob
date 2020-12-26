from django.db import migrations, transaction
from ultimatejobweb.models import job, company


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatejobweb', '0002_test_data_company'),
    ]

    def generate_data(apps, schema_editor):
        company1 = company(id = 1)
        
        jobs = [
          (company1, 'Production Engineer','https://www.facebook.com/careers/jobs/1672813472870915/'),]
        
        with transaction.atomic():
            for company, job_title, description_url in jobs:
                job(company=company, job_title=job_title, description_url=description_url).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
