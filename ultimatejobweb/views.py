from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def homepage(request):
    return render(request, r"web/ultimate_job_homepage.html")
# Create your views here.


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('homepage')
    return render(request, r"web/signup.html", {'form': form})
