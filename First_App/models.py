from django.db import models

class Vacancies(models.Model):
    name = models.CharField("Имя", max_length=32)
    key_skills = models.CharField("Умения", max_length=128)
    salary_from = models.IntegerField("Зарплата от")
    salary_to = models.IntegerField("Зарплата до")
    salary_currency = models.CharField("Валюта", max_length=32)
    area_name = models.CharField("Место", max_length=32)
    published_at = models.DateTimeField("Публикация")

    def __str__(self):
        return f"{self.name} {self.key_skills}"

    class Meta:
        verbose_name = "Вакансии"
        verbose_name_plural = "Вакансии"
