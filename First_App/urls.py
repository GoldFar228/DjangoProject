from django.contrib import admin
from django.urls import path, include

from First_App.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', index_page, name="main"),
    path('add/', add_page, name="add_page"),
    path('demand/', demand, name="demand"),
    path('geography/', geography, name="geography"),
    path('skills/', skills, name="skills"),
    path('last_vacancies/', last_vacancies, name="last_vacancies"),
    path('add/', add_page, name="add_page")
]
