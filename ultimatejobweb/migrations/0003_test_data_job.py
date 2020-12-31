from django.db import migrations, transaction
from ultimatejobweb.models import job, company


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatejobweb', '0002_test_data_company'),
    ]

    def generate_data(apps, schema_editor):
        jobs = [('Facebook', 'Production Engineer', 'https://www.facebook.com/careers/v2/jobs/1672813472870915/'),
                ('Facebook', 'Offensive Security Engineer Intern, Red Team', 'https://www.facebook.com/careers+\
                /v2/jobs/712878282607325/'),
                ('Facebook', 'Internal Audit Manager – Infrastructure', 'https://www.facebook.com/careers/v2/+\
                jobs/420212419368641/'),
                ('Facebook', 'Offensive Security Engineer Intern', 'https://www.facebook.com/careers/v2/jobs/+\
                712878282607325/'),
                ('Facebook', 'Production Engineer', 'https://www.facebook.com/careers/+\
                v2/jobs/207984144060781/'),
                ('Facebook', 'Production Engineer', 'https://www.facebook.com/careers/v2/+\
                jobs/773785633436218/'),
                ('Facebook', 'Production Engineer', 'https://www.facebook.com/careers/v2/+\
                jobs/2597607417128369/'),
                ('Facebook', 'Production Engineer', 'https://www.facebook.com/careers/v2/+\
                jobs/536078547072736/'),
                ('Red Hat', '69710 - Software Development Internship - Red Hat Virtualization,+\
                 Student Position', 'https://global-redhat.icims.com/jobs/69710/+\
                 software-development-internship---red-hat-virtualization%2c-student+\
                 -position/job?hub=7&in_iframe=1'),
                ('Red Hat', '80964 - Senior DevOps Engineer - TelCo 5G Integration', 'https://global-+\
                redhat.icims.com/jobs/80964/senior-devops-engineer---telco-5g-integration+\
                /job?hub=7&in_iframe=1'),
                ('Red Hat', '83546 - Senior Product Security Engineer - DevSecOps Managed+\
                 Services', 'https://global-redhat.icims.com/jobs/83546/senior-product-security+\
                 -engineer---devsecops-managed-services/job?hub=7&in_iframe=1'),
                ('Red Hat', '83285 - CI and DevOps Internship', 'https://global-redhat.icims.com/+\
                jobs/83285/ci-and-devops-internship/job?hub=7&in_iframe=1'),
                ('Red Hat', '69711 - Software Quality Engineering Internship - Local Student+\
                 Position', 'https://global-redhat.icims.com/jobs/69711/software-quality+\
                 -engineering-internship---local-student-position/job?hub=7&in_iframe=1'),
                ('Red Hat', '81168 - Software Quality Engineer - Storage Red Hat Virtualization', 'https://+\
                global-redhat.icims.com/jobs/81168/software-quality-engineer---storage+\
                -red-hat-virtualization/job?hub=7&in_iframe=1'),
                ('Red Hat', '70227 - Talent Acquisition Recruiter, Engineering Team - 12 month contract', 'https:+\
                //global-redhat.icims.com/jobs/70227/talent-acquisition-recruiter%2c-engineering+\
                -team---12-month-contract/job?hub=7&in_iframe=1'),
                ('Red Hat', '83236 - Principal Software Engineer - Object and Data Services (NooBaa)', 'https:+\
                //global-redhat.icims.com/jobs/83236/principal-software-engineer---object-+\
                and-data-services-%28noobaa%29/job?hub=7&in_iframe=1'),
                ('Red Hat', '82632 - Sales Renewals Representative', 'https://global-redhat.icims.com/jobs/+\
                82632/sales-renewals-representative/job?hub=7&in_iframe=1'),
                ('Red Hat', '81944 - Senior Technical Writer', 'https://global-redhat.icims.com/jobs/81944/+\
                senior-technical-writer/job?hub=7&in_iframe=1'), ]

        with transaction.atomic():
            for company_naim_data, job_title, description_url in jobs:
                company_job = company.objects.get(company_name=company_naim_data)
                job(company=company_job, job_title=job_title, description_url=description_url).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
