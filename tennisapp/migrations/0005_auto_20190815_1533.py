# Generated by Django 2.2.3 on 2019-08-15 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tennisapp', '0004_auto_20190815_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tennismodel',
            name='date',
        ),
        migrations.RemoveField(
            model_name='tennismodel',
            name='endtime',
        ),
        migrations.RemoveField(
            model_name='tennismodel',
            name='starttime',
        ),
    ]
