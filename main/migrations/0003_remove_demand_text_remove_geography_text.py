# Generated by Django 4.2.7 on 2024-01-17 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_demand_geography_home_skills_delete_lastvacancymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demand',
            name='text',
        ),
        migrations.RemoveField(
            model_name='geography',
            name='text',
        ),
    ]