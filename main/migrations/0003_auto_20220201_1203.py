# Generated by Django 3.2.9 on 2022-02-01 07:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220201_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='discount',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='ondate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 1, 12, 3, 56, 46705), verbose_name=datetime.datetime),
        ),
    ]