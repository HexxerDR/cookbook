# Generated by Django 5.0.2 on 2024-02-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0006_remove_recipe_ingredients_recipe_ingredients_list"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="ingredients_list",
            field=models.JSONField(),
        ),
    ]
