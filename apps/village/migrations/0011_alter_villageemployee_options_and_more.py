# Generated by Django 4.2.9 on 2024-02-26 20:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps_village", "0010_villageemployee"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="villageemployee",
            options={"verbose_name": "Агенты", "verbose_name_plural": "Агенты"},
        ),
        migrations.AlterModelOptions(
            name="villageengineeringservices",
            options={
                "verbose_name": "Инженерные коммуникации",
                "verbose_name_plural": "Инженерные коммуникации",
            },
        ),
    ]
