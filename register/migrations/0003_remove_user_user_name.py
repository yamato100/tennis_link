# Generated by Django 2.2.3 on 2019-09-06 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_user_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
    ]
