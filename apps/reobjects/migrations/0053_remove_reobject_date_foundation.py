# Generated by Django 4.2.9 on 2024-03-12 20:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "apps_reobjects",
            "0052_remove_reobject_coordinates_alter_reobject_area_flat_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reobject",
            name="date_foundation",
        ),
    ]