from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpFroms
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from ultimatejobweb.models import Job
from ultimatejobweb.filters import OrderJob



def homepage(request):
    return render(request, r"home_page.html")


def sign_up(request):
    form = SignUpFroms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('personal_area')
    return render(request, r"sign_up.html", {'form': form})


def sign_in_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('personal_area')
    else:
        form = AuthenticationForm()
    return render(request, r"sign_in.html", {'form': form})


@login_required(login_url="/sign_in")
def personal_area(request):
    return render(request, r"personal_area.html")


@login_required(login_url="/sign_in")
def available_jobs(request):
    jobs = Job.objects.all()
    jobFilter = OrderJob(request.GET, queryset=jobs)
    jobs = jobFilter.qs
    return render(request, r"available_jobs.html", {'job': jobs, 'jobFilter': jobFilter})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign_in')
