# Generated by Django 4.2.9 on 2024-01-30 18:31

from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        (
            "apps_reobjects",
            "0004_alter_reobjectengineeringservices_engineering_service_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ReObjectEngineeringServicesProxy",
            fields=[],
            options={
                "verbose_name": "Коммуникации объекта",
                "verbose_name_plural": "Коммуникации объектов",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps_reobjects.reobjectengineeringservices",),
        ),
        migrations.CreateModel(
            name="ReObjectImageProxy",
            fields=[],
            options={
                "verbose_name": "Фото объекта",
                "verbose_name_plural": "Фото объектов",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps_reobjects.reobjectimage",),
        ),
        migrations.CreateModel(
            name="ReObjectProxy",
            fields=[],
            options={
                "verbose_name": "Объект",
                "verbose_name_plural": "Объекты",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps_reobjects.reobject",),
        ),
    ]
