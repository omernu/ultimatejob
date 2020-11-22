from django.shortcuts import render


def homepage(request):
    return render(request, r"web/ultimate_job_homepage.html")
# Create your views here.
