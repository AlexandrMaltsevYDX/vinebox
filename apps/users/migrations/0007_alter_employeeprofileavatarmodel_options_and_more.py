# Generated by Django 4.2.9 on 2024-02-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apps_users", "0006_alter_employeeprofileavatarmodel_uuid_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="employeeprofileavatarmodel",
            options={
                "verbose_name": "Фото Сотрудника",
                "verbose_name_plural": "Фото Сотрудников",
            },
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="description",
            field=models.TextField(blank=True, verbose_name="Описание"),
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="first_name",
            field=models.CharField(blank=True, max_length=255, verbose_name="Имя"),
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="last_name",
            field=models.CharField(blank=True, max_length=255, verbose_name="Фамилия"),
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Номе телефона"
            ),
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="position",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Должность"
            ),
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="telegram_link",
            field=models.CharField(blank=True, max_length=255, verbose_name="Telegram"),
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="whatsapp_link",
            field=models.CharField(blank=True, max_length=255, verbose_name="Whatsapp"),
        ),
        migrations.AlterField(
            model_name="employeeprofilemodel",
            name="work_email",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Рабочий Email"
            ),
        ),
        migrations.DeleteModel(
            name="ReObjectImageModel",
        ),
    ]
