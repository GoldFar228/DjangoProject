from django.shortcuts import render, redirect
from .load_csv import import_data_csv

#file_path = "C:\Django\vacancies.csv"
#import_data_csv(file_path)

navigation = [{"title": "Главная страница", "url_name": "main"},
              {"title": "Востребованность", "url_name": "demand"},
              {"title": "География", "url_name": "geography"},
              {"title": "Навыки", "url_name": "skills"},
              {"title": "Последние вакансии", "url_name": "last_vacancies"},
              {"title": "добавить пользователя", "url_name": "add_page"}]

def index_page(request):
    context = {"navigation": navigation,
               "title": "Главная страница"}
    return render(request, 'index.html', context=context)

def add_page(request):
    return render(request, 'add.html', context={"title": "Добавить пользователя", "navigation": navigation})

def demand(request):
    context = {"navigation": navigation,
               "title": "Восстребованность"}
    return render(request, "demand.html", context=context)

def geography(request):
    context = {"navigation": navigation,
               "title": "География"}
    return render(request, "geography.html", context=context)

def skills(request):
    context = {"navigation": navigation,
               "title": "Умения"}
    return render(request, "skills.html", context=context)

def last_vacancies(request):
    context = {"navigation": navigation,
               "title": "Последние вакансии"}
    return render(request, "last_vacancies.html", context=context)
