# Generated by Django 3.2.9 on 2022-02-01 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20220201_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ondate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 12, 51, 59, 502991), verbose_name=datetime.datetime),
        ),
    ]
