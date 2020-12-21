from django.db import migrations, transaction
from django.contrib.auth.models import User
from ultimatejobweb.models import Jobs


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatejobweb', '0001_initial'),
    ]

    def generate_data(apps, schema_editor):
        user1 = User.objects.create_user(username='omer', password='sisma1', email='omer@nomer.com')
        user2 = User.objects.create_user(username='rom', password='sisma1', email='rom@nomer.com')
        
        jobs = [
          (user1, 'Facebook', 'Production Engineer',
           'https://www.facebook.com/careers/jobs/1672813472870915/'),
          (user2, 'Facebook', 'Production Engineer',
           'https://www.facebook.com/careers/jobs/712878282607325/'),
        ]

        with transaction.atomic():
            for user, CompanyName, JobTitle, ApplyURL in jobs:
                Jobs(user=user, CompanyName=CompanyName, JobTitle=JobTitle, ApplyURL=ApplyURL).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
