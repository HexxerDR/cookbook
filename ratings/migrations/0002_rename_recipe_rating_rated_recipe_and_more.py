# Generated by Django 5.0.2 on 2024-02-23 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ratings", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="rating",
            old_name="recipe",
            new_name="rated_recipe",
        ),
        migrations.RenameField(
            model_name="rating",
            old_name="user",
            new_name="rating_user",
        ),
    ]
