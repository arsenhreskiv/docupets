from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Pet)
admin.site.register(Vet)
admin.site.register(Vaccination)
admin.site.register(Visit)