from django.db import migrations, transaction
from ultimatejobweb.models import company


class Migration(migrations.Migration):

    dependencies = [('ultimatejobweb', '0001_initial')]

    def generate_data(apps, schema_editor):

        companies = [('Facebook', 'https://www.facebook.com/careers/jobs/?q=',
                      'templates/company logo/FBlogo.png', 'API_FB.py'),
                     ('Red Hat', 'https://careers-redhat.icims.com/jobs/search?ss=1&in_iframe=1&searchLocation=13269--Raanana',
                      'templates/company logo/RHlogo.png', 'API_RH')]

        with transaction.atomic():
            for company_name, company_search_url, company_logo, function_name in companies:
                company(company_name=company_name, company_search_url=company_search_url, company_logo=company_logo,
                        function_name=function_name).save()

    operations = [migrations.RunPython(generate_data), ]
