# Generated by Django 2.2.6 on 2019-11-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apple', '0002_auto_20191109_1249'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikes',
            name='image',
            field=models.ImageField(default=0, upload_to='bike images'),
            preserve_default=False,
        ),
    ]
