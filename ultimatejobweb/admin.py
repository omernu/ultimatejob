from django.contrib import admin
from .models import user, company
from django.apps import apps

# Register your models here.
admin.site.register(user)
admin.site.register(company)
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
