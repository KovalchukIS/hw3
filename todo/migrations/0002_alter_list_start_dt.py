# Generated by Django 4.1.5 on 2023-01-30 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="list",
            name="start_dt",
            field=models.DateTimeField(
                default=django.utils.timezone.now, help_text="Дата и время создания"
            ),
        ),
    ]
