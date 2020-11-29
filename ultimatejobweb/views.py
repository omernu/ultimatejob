from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


def homepage(request):
    return render(request, r"web/ultimate_job_homepage.html")
# Create your views here.


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
#login(request, user)
        return redirect('homepage')
    return render(request, r"web/signup.html", {'form': form})
