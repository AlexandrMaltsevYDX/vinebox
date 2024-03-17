# Generated by Django 4.2.9 on 2024-02-13 18:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("apps_users", "0009_alter_employeeprofileavatarmodel_uuid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobTitle",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Название должности",
                    ),
                ),
            ],
            options={
                "verbose_name": "Название должности",
                "verbose_name_plural": "Название должности",
            },
        ),
    ]