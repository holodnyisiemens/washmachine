# Generated by Django 5.0.6 on 2024-05-28 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]
