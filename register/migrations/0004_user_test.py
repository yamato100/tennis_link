# Generated by Django 2.2.3 on 2019-09-06 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_remove_user_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
