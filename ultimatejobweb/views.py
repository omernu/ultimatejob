from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .forms import SignUpFroms
from .models import job


def homepage(request):
    return render(request, r"home_page.html")


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, r"sign_up.html", {'form': form})


def sign_up(request):
    form = SignUpFroms(request.POST)
    if form.is_valid():
        form.save()
        return redirect('personal_area')
    return render(request, r"sign_up.html", {'form': form})


def personal_area(request):
    return render(request, r"personal_area.html")


def sign_in(request):
    return render(request, r"sign_in.html")


def available_jobs(request):
    return render(request, r"available_jobs.html", {'job': job})
