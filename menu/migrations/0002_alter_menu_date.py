# Generated by Django 4.1 on 2023-04-22 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("menu", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]