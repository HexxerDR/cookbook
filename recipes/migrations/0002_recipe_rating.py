# Generated by Django 5.0.2 on 2024-02-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="rating",
            field=models.BigIntegerField(default=0),
        ),
    ]
