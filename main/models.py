import datetime

from django.db import models


# Create your models here


class Home(models.Model):
    text = models.TextField('Текст', default=None)
    image = models.ImageField(
        'img', default=None,
        upload_to='home'
    )


class Demand(models.Model):
    title = models.TextField(
        'Таблица',
        default='demand'
    )
    graph_left = models.ImageField(
        'График №2',
        default=None,
        upload_to='demand'
    )
    graph_right = models.ImageField(
        'График №1',
        default=None,
        upload_to='demand'
    )

class Geography(models.Model):
    title = models.TextField(
        'Таблица',
        default='demand'
    )
    graph_left = models.ImageField(
        'График №2',
        default=None,
        upload_to='demand'
    )
    graph_right = models.ImageField(
        'График №1',
        default=None,
        upload_to='demand'
    )


class Skills(models.Model):
    title = models.TextField(
        'Таблица',
        default='skills'
    )
    graph = models.ImageField(
        'График',
        default=None,
        upload_to='skills'
    )
    text = models.TextField('Текст', default=None)
