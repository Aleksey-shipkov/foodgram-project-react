# Generated by Django 2.2.16 on 2022-11-18 08:07

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0003_auto_20221116_1934"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="subscriptions",
            name="unique_name_author",
        ),
        migrations.RemoveField(
            model_name="shoppingcart",
            name="ingredients",
        ),
        migrations.AddField(
            model_name="shoppingcart",
            name="recipe",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="food.Recipes",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="recipes",
            name="cooking_time",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(
                        1, message="Время приготовления должно быть не менее 1"
                    )
                ]
            ),
        ),
        migrations.AddConstraint(
            model_name="subscriptions",
            constraint=models.UniqueConstraint(
                fields=("user", "author"), name="unique_user_author"
            ),
        ),
    ]
