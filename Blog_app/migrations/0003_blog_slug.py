# Generated by Django 3.2.4 on 2021-06-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
