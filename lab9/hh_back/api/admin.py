from django.contrib import admin
from .models import Company
from .models import Vacancy



admin.site.register(Vacancy)
admin.site.register(Company)