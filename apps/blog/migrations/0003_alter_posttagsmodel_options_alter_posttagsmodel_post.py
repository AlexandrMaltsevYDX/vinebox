# Generated by Django 4.2.9 on 2024-02-05 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("apps_blog", "0002_tag_post_author_alter_post_body_alter_post_name_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="posttagsmodel",
            options={
                "verbose_name": "Связанные Тэги",
                "verbose_name_plural": "Связанные Тэги",
            },
        ),
        migrations.AlterField(
            model_name="posttagsmodel",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts",
                to="apps_blog.post",
            ),
        ),
    ]
