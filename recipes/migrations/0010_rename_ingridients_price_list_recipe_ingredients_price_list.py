# Generated by Django 5.0.2 on 2024-02-28 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0009_recipe_ingridients_price_list_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="ingridients_price_list",
            new_name="ingredients_price_list",
        ),
    ]
