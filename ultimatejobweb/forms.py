from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class SignUpFroms(UserCreationForm):
    email = forms.EmailField()
    profession = forms.CharField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "profession", "password1", "password2"]
