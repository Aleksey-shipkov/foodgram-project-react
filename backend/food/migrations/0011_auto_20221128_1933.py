# Generated by Django 2.2.16 on 2022-11-28 16:33

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("food", "0010_auto_20221127_1248"),
    ]

    operations = [
        migrations.AlterField(
            model_name="favorite",
            name="recipe",
            field=models.ForeignKey(
                help_text="Укажите рецепт",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="favorites",
                to="food.Recipes",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AlterField(
            model_name="favorite",
            name="user",
            field=models.ForeignKey(
                help_text="Укажите пользователя",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="ingredients",
            name="measurement_unit",
            field=models.CharField(
                help_text="Укажите ед. измерения",
                max_length=200,
                verbose_name="Ед. измерения",
            ),
        ),
        migrations.AlterField(
            model_name="ingredients",
            name="name",
            field=models.CharField(
                help_text="Укажите название",
                max_length=200,
                verbose_name="Название",
            ),
        ),
        migrations.AlterField(
            model_name="ingredientsrecipe",
            name="amount",
            field=models.IntegerField(
                help_text="Укажите количество",
                validators=[
                    django.core.validators.MinValueValidator(
                        1,
                        message="Минимальное кол-во должно быть не меньше 1!",
                    )
                ],
                verbose_name="Кол-во",
            ),
        ),
        migrations.AlterField(
            model_name="ingredientsrecipe",
            name="ingredient",
            field=models.ForeignKey(
                help_text="Укажите ингредиент",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="in_recipe",
                to="food.Ingredients",
                verbose_name="Ингредиент",
            ),
        ),
        migrations.AlterField(
            model_name="ingredientsrecipe",
            name="recipe",
            field=models.ForeignKey(
                help_text="Укажите рецепт",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipe",
                to="food.Recipes",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="author",
            field=models.ForeignKey(
                help_text="Укажите автора рецепта",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recipes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="cooking_time",
            field=models.PositiveSmallIntegerField(
                help_text="Укажите время готовки",
                validators=[
                    django.core.validators.MinValueValidator(
                        1, message="Время приготовления должно быть не менее 1"
                    )
                ],
                verbose_name="Время приготовления",
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="image",
            field=models.ImageField(
                help_text="Добавьте картинку",
                upload_to="",
                verbose_name="Картинка",
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="ingredients",
            field=models.ManyToManyField(
                help_text="Укажите ингредиенты",
                through="food.IngredientsRecipe",
                to="food.Ingredients",
                verbose_name="Ингредиенты",
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="name",
            field=models.CharField(
                help_text="Укажите название",
                max_length=200,
                verbose_name="Название",
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="pub_date",
            field=models.DateTimeField(
                auto_now_add=True,
                help_text="Укажите дату",
                verbose_name="Дата публикации",
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="tags",
            field=models.ManyToManyField(
                help_text="Укажите теги", to="food.Tag", verbose_name="Теги"
            ),
        ),
        migrations.AlterField(
            model_name="recipes",
            name="text",
            field=models.TextField(
                help_text="Добавьте описание", verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="shoppingcart",
            name="recipe",
            field=models.ForeignKey(
                help_text="Укажите рецепт",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="shopping_cart",
                to="food.Recipes",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AlterField(
            model_name="shoppingcart",
            name="user",
            field=models.ForeignKey(
                help_text="Укажите пользователя",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Пользователь",
            ),
        ),
        migrations.AlterField(
            model_name="subscriptions",
            name="author",
            field=models.ForeignKey(
                help_text="Укажите автора",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
        migrations.AlterField(
            model_name="subscriptions",
            name="user",
            field=models.ForeignKey(
                help_text="Укажите подписчика",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="follower",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Подписчик",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="color",
            field=models.CharField(
                help_text="Укажите цвет", max_length=7, verbose_name="Цвет"
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(
                help_text="Укажите название",
                max_length=200,
                verbose_name="Название",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.SlugField(
                help_text="Укажите Slug", unique=True, verbose_name="Slug"
            ),
        ),
    ]
