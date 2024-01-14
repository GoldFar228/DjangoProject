from django.contrib import admin
from .models import *

class VacanciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('title', 'name')

admin.site.register(Vacancies, VacanciesAdmin)

