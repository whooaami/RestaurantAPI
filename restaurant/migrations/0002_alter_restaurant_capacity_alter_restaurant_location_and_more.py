# Generated by Django 4.1 on 2023-04-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="capacity",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="location",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="name",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
