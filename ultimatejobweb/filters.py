import django_filters
from ultimatejobweb.models import Job


class OrderJob(django_filters.FilterSet):
    class Meta:
        model = Job
        fields = {
                'job_title': ['icontains']
        }
