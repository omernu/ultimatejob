from django.db import migrations, transaction


class Migration(migrations.Migration):

    dependencies = [
     ('ultimatejobweb', '0002_auto_20201212_1919'),
    ]

    def generate_data(apps, schema_editor):
        from ultimatejobweb.models import Jobs

        test_data = [
          ('1', 'omer', 'Facebook', 'Production Engineer',
            'https://www.facebook.com/careers/jobs/1672813472870915/'),
          ('2', 'rom', 'Facebook', 'Production Engineer',
            'https://www.facebook.com/careers/jobs/712878282607325/'),
        ]

        with transaction.atomic():
            for id, user, CompanyName, JobTitle, ApplyURL in test_data:
                Jobs(id=id, user=user, CompanyName=CompanyName, JobTitle=JobTitle, ApplyURL=ApplyURL).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
