# Generated by Django 4.2.7 on 2023-11-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notebook',
            name='slug',
            field=models.SlugField(default=1, unique=True, verbose_name='Slug name'),
            preserve_default=False,
        ),
    ]
