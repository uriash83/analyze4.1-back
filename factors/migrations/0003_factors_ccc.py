# Generated by Django 3.1 on 2020-08-25 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factors', '0002_remove_factors_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='factors',
            name='ccc',
            field=models.CharField(default='0000000', editable=False, max_length=100),
        ),
    ]
