from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect
from .forms import SignUpFroms


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
            return redirect('personal_area')
    else:
        form = AuthenticationForm()
    return render(request, r"sign_in.html", {'form': form})


def personal_area(request):
    return render(request, r"personal_area.html")


def available_jobs(request):
    return render(request, r"available_jobs.html")
