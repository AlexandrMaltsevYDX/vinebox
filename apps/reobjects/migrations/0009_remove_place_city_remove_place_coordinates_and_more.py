# Generated by Django 4.2.9 on 2024-02-05 13:45

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("apps_reobjects", "0008_remove_reobject_coordinates_reobject_place_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="place",
            name="city",
        ),
        migrations.RemoveField(
            model_name="place",
            name="coordinates",
        ),
        migrations.RemoveField(
            model_name="place",
            name="country",
        ),
        migrations.RemoveField(
            model_name="place",
            name="district",
        ),
        migrations.RemoveField(
            model_name="place",
            name="region",
        ),
        migrations.RemoveField(
            model_name="place",
            name="street",
        ),
        migrations.RemoveField(
            model_name="place",
            name="tag",
        ),
        migrations.RemoveField(
            model_name="reobject",
            name="place",
        ),
        migrations.DeleteModel(
            name="City",
        ),
        migrations.DeleteModel(
            name="Coordinates",
        ),
        migrations.DeleteModel(
            name="Country",
        ),
        migrations.DeleteModel(
            name="District",
        ),
        migrations.DeleteModel(
            name="Place",
        ),
        migrations.DeleteModel(
            name="Region",
        ),
        migrations.DeleteModel(
            name="Street",
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
    ]
