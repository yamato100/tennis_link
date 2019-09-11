# Generated by Django 2.2.3 on 2019-09-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_user_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(blank=True, choices=[(10, '1.0'), (20, '1.5'), (30, '2.0'), (40, '2.5'), (50, '3.0'), (60, '3.5'), (70, '4.0'), (80, '4.5'), (90, '5.0'), (100, '5.5'), (100, '6.0')], null=True, verbose_name='レベル(NTRP)'),
        ),
    ]
