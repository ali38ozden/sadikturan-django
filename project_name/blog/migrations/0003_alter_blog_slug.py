# Generated by Django 4.1.1 on 2022-09-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
