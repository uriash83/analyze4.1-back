# Generated by Django 3.1 on 2020-09-19 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('factors', '0003_factors_ccc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factors',
            name='ccc',
        ),
    ]