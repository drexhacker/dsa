# Generated by Django 3.1.2 on 2020-11-10 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20201109_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='slug',
        ),
    ]
