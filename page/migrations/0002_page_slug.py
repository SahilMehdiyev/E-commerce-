# Generated by Django 4.2 on 2024-10-27 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
