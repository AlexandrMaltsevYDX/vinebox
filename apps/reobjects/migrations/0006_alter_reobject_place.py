# Generated by Django 4.2.9 on 2024-02-05 11:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0005_alter_reobject_object_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reobject",
            name="place",
            field=models.TextField(
                blank=True,
                help_text="Напишите адрес объекта",
                max_length=1200,
                null=True,
                verbose_name="Адрес",
            ),
        ),
    ]
