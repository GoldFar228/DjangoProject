from django.shortcuts import render
from .models import Home, Demand, Skills, Geography
from .utils import get_vacancies


# Create your views here.

def home(request):
    homepage = Home.objects.all()
    return render(
        request,
        'home.html',
        context={
            'homepage': homepage,
        }
    )


def info(request):

    infopage = Demand.objects.all()
    return render(
        request,
        'info.html',
        context={
            'infopage': infopage,
        }
    )


def geography(request):
    geographypage = Geography.objects.all()
    return render(
        request,
        'geography.html',
        context={
            'geographypage': geographypage,
        }
    )


def vacancies(request):
    return render(request, 'vacanvies_template.html',
                  context={'vacancies': get_vacancies(), })


def skills(request):
    skillspage = Skills.objects.all()
    return render(
        request,
        'skills.html',
        context={
            'skillspage': skillspage,
        }
    )


