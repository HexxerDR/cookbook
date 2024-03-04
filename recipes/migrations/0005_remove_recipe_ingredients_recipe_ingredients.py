# Generated by Django 5.0.2 on 2024-02-25 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ingredients", "0001_initial"),
        ("recipes", "0004_recipe_ingredients_alter_recipe_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="ingredients",
        ),
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.ManyToManyField(to="ingredients.ingredient"),
        ),
    ]
