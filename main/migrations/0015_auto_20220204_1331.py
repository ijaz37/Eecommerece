# Generated by Django 3.2.9 on 2022-02-04 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20220204_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='card_number',
            field=models.CharField(max_length=1999),
        ),
        migrations.AlterField(
            model_name='payment',
            name='expired_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 13, 31, 38, 298424), verbose_name=datetime.datetime),
        ),
        migrations.AlterField(
            model_name='review',
            name='ondate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 4, 13, 31, 38, 293484), verbose_name=datetime.datetime),
        ),
    ]
