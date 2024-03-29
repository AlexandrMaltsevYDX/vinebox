# Generated by Django 4.2.9 on 2024-01-29 19:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        (
            "apps_reobjects",
            "0002_category_engineeringservices_fencing_foundation_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ReObject",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("id", models.IntegerField(blank=True, null=True)),
                (
                    "number_of_storeys",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Количество этажей в здании",
                        null=True,
                        verbose_name="Этажность",
                    ),
                ),
                (
                    "floor",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Этаж в здании",
                        null=True,
                        verbose_name="Этаж",
                    ),
                ),
                (
                    "number_of_rooms",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Количество комнат в помещении",
                        null=True,
                        verbose_name="Количество комнат",
                    ),
                ),
                (
                    "total_area",
                    models.FloatField(
                        blank=True,
                        help_text="Общая площадь помещений",
                        null=True,
                        verbose_name="Общая площадь помещений",
                    ),
                ),
                (
                    "living_area",
                    models.FloatField(
                        blank=True,
                        help_text="Жилая площадь в помещении",
                        null=True,
                        verbose_name="Жилая площадь",
                    ),
                ),
                (
                    "kitchen_area",
                    models.FloatField(
                        blank=True,
                        help_text="Площадь кухни в помещении",
                        null=True,
                        verbose_name="Площадь кухни",
                    ),
                ),
                (
                    "land_area",
                    models.FloatField(
                        blank=True,
                        help_text="Площадь участка",
                        null=True,
                        verbose_name="Площадь участка",
                    ),
                ),
                (
                    "buildings_on_site",
                    models.TextField(
                        blank=True,
                        help_text="Здания на участке",
                        max_length=1200,
                        null=True,
                        verbose_name="Здания на участке",
                    ),
                ),
                (
                    "buildings_of_villages",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="Количество домов в поселке",
                        null=True,
                        verbose_name="Количество домов в поселке",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Дом, Квартира, Участок",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.category",
                        verbose_name="Категория объекта",
                    ),
                ),
                (
                    "fencing",
                    models.ForeignKey(
                        blank=True,
                        help_text="Горы, Шморы",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.fencing",
                        verbose_name="Ограждение",
                    ),
                ),
                (
                    "foundation",
                    models.ForeignKey(
                        blank=True,
                        help_text="Блоки, Лента, Плита",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.foundation",
                        verbose_name="Фундамент",
                    ),
                ),
                (
                    "land_category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Коммерческая",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.landcategory",
                        verbose_name="Категория земель",
                    ),
                ),
                (
                    "object_description",
                    models.ForeignKey(
                        blank=True,
                        help_text="Текст в markdown",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.objectdescription",
                        verbose_name="Описание объекта",
                    ),
                ),
                (
                    "ownership",
                    models.ForeignKey(
                        blank=True,
                        help_text="От собственника, Ипотека, и.т.д",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.ownership",
                        verbose_name="Собственность",
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        blank=True,
                        help_text="Укажите месторасположение объекта",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.place",
                        verbose_name="Адрес",
                    ),
                ),
                (
                    "relief_area",
                    models.ForeignKey(
                        blank=True,
                        help_text="Горы, Холмы",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.reliefarea",
                        verbose_name="Рельеф участка",
                    ),
                ),
                (
                    "type_house",
                    models.ForeignKey(
                        blank=True,
                        help_text="Комерческая, ИЖС, Жилая",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.typehouse",
                        verbose_name="Тип объекта",
                    ),
                ),
                (
                    "village_fences",
                    models.ForeignKey(
                        blank=True,
                        help_text="Да, нет",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.villagefences",
                        verbose_name="Ограждение поселка",
                    ),
                ),
                (
                    "wall_material",
                    models.ForeignKey(
                        blank=True,
                        help_text="Кирпич, Панель, Пеноблок",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.wallmaterial",
                        verbose_name="Материал стен",
                    ),
                ),
                (
                    "windows_orientation",
                    models.ForeignKey(
                        blank=True,
                        help_text="Запад, Север, Восток, и.т.д",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.windowsorientation",
                        verbose_name="Ориентация окон",
                    ),
                ),
            ],
            options={
                "verbose_name": "Объекты недвижимости",
                "verbose_name_plural": "Объекты недвижимости",
            },
        ),
        migrations.CreateModel(
            name="ReObjectImage",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("image", models.FileField(upload_to="reobjects/")),
                (
                    "re_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="apps_reobjects.reobject",
                    ),
                ),
            ],
            options={
                "verbose_name": "Фото объекта",
                "verbose_name_plural": "Фото объекта",
            },
        ),
        migrations.CreateModel(
            name="ReObjectEngineeringServices",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "engineering_service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.engineeringservices",
                    ),
                ),
                (
                    "re_object",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="apps_reobjects.reobject",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
