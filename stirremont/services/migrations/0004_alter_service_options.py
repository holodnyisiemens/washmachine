# Generated by Django 5.0.6 on 2024-06-17 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_alter_service_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
    ]
