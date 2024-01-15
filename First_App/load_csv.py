import csv
from .models import *
from django.db.models import Q

def import_data_csv(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "C#" in row['name']:
                salary_from = int(float(row['salary_from'])) if row['salary_from'].strip() else 0
                salary_to = int(float(row['salary_to'])) if row['salary_to'].strip() else 0
                existing_vacancy = Vacancies.objects.filter(
                    Q(name=row['name']) &
                    Q(key_skills=row['key_skills']) &
                    Q(salary_from=salary_from) &
                    Q(salary_to=salary_to) &
                    Q(salary_currency=row['salary_currency']) &
                    Q(area_name=row['area_name']) &
                    Q(published_at=row['published_at'])
                ).exists()
                if not existing_vacancy:
                    vacancies = Vacancies(name=row['name'],
                                          key_skills=row['key_skills'],
                                          salary_from=salary_from,
                                          salary_to=salary_to,
                                          salary_currency=row['salary_currency'],
                                          area_name=row['area_name'],
                                          published_at=row['published_at'])
                    try:
                        vacancies.save()
                    except Exception as e:
                        print(f"Error saving vacancy: {e}")
