# Generated by Django 2.2.7 on 2019-11-28 06:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0006_auto_20191128_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='give_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 28, 11, 44, 5, 89178)),
        ),
        migrations.AlterField(
            model_name='orders',
            name='take_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 28, 11, 44, 5, 89178)),
        ),
    ]
