# Generated by Django 4.2.9 on 2024-02-09 10:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0022_remove_reobject_buildings_of_villages"),
    ]

    operations = [
        migrations.RenameField(
            model_name="engineeringservices",
            old_name="value",
            new_name="name",
        ),
    ]
