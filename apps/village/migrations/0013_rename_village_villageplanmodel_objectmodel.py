# Generated by Django 4.2.9 on 2024-03-05 22:07

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps_village", "0012_rename_village_villageimagemodel_objectmodel"),
    ]

    operations = [
        migrations.RenameField(
            model_name="villageplanmodel",
            old_name="village",
            new_name="objectModel",
        ),
    ]
