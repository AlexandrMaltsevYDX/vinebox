# Generated by Django 4.2.9 on 2024-01-28 13:24

from django.db import migrations


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        (
            "apps_reobjects",
            "0002_category_engineeringservices_fencing_foundation_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Service",
            fields=[],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("apps_reobjects.service",),
        ),
    ]
