from django.db import migrations, transaction
from ultimatejobweb.models import job, company


class Migration(migrations.Migration):

    dependencies = [
        ('ultimatejobweb', '0002_test_data_company'),
    ]

    def generate_data(apps, schema_editor):
        jobs = [('Production Engineer', 'https://www.facebook.com/careers/v2/jobs/1672813472870915/'),
                ('Offensive Security Engineer Intern, Red Team', 'https://www.facebook.com/careers/v2/jobs/712878282607325/'),
                ('Internal Audit Manager – Infrastructure', 'https://www.facebook.com/careers/v2/jobs/420212419368641/'),
                ('Offensive Security Engineer Intern', 'https://www.facebook.com/careers/v2/jobs/712878282607325/'),
                ('Production Engineer', 'https://www.facebook.com/careers/v2/jobs/207984144060781/'),
                ('Production Engineer', 'https://www.facebook.com/careers/v2/jobs/773785633436218/'),
                ('Production Engineer', 'https://www.facebook.com/careers/v2/jobs/2597607417128369/'),
                ('Production Engineer', 'https://www.facebook.com/careers/v2/jobs/536078547072736/'),
                ('69710 - Software Development Internship - Red Hat Virtualization, Student Position', 'https://global-redhat.icims.com/jobs/69710/software-development-internship---red-hat-virtualization%2c-student-position/job?hub=7&in_iframe=1'),
                ('80964 - Senior DevOps Engineer - TelCo 5G Integration', 'https://global-redhat.icims.com/jobs/80964/senior-devops-engineer---telco-5g-integration/job?hub=7&in_iframe=1'),
                ('83546 - Senior Product Security Engineer - DevSecOps Managed Services', 'https://global-redhat.icims.com/jobs/83546/senior-product-security-engineer---devsecops-managed-services/job?hub=7&in_iframe=1'),
                ('83285 - CI and DevOps Internship', 'https://global-redhat.icims.com/jobs/83285/ci-and-devops-internship/job?hub=7&in_iframe=1'),
                ('69711 - Software Quality Engineering Internship - Local Student Position', 'https://global-redhat.icims.com/jobs/69711/software-quality-engineering-internship---local-student-position/job?hub=7&in_iframe=1'),
                ('81168 - Software Quality Engineer - Storage Red Hat Virtualization', 'https://global-redhat.icims.com/jobs/81168/software-quality-engineer---storage-red-hat-virtualization/job?hub=7&in_iframe=1'),
                ('70227 - Talent Acquisition Recruiter, Engineering Team - 12 month contract', 'https://global-redhat.icims.com/jobs/70227/talent-acquisition-recruiter%2c-engineering-team---12-month-contract/job?hub=7&in_iframe=1'),
                ('83236 - Principal Software Engineer - Object and Data Services (NooBaa)', 'https://global-redhat.icims.com/jobs/83236/principal-software-engineer---object-and-data-services-%28noobaa%29/job?hub=7&in_iframe=1'),
                ('82632 - Sales Renewals Representative', 'https://global-redhat.icims.com/jobs/82632/sales-renewals-representative/job?hub=7&in_iframe=1'),
                ('81944 - Senior Technical Writer', 'https://global-redhat.icims.com/jobs/81944/senior-technical-writer/job?hub=7&in_iframe=1'), ]

        with transaction.atomic():
            n = 0
            i = 1
            for job_title, description_url in jobs:
                n += 1
                if (n==9):
                    i = 2
                company_n = company.objects.get(id=i)
                job(company=company_n, job_title=job_title, description_url=description_url).save()

    operations = [
        migrations.RunPython(generate_data),
    ]
