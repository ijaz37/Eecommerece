# Generated by Django 4.0.2 on 2022-02-08 19:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_cart_single_total_alter_review_ondate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='single_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='ondate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 0, 2, 39, 627854), verbose_name=datetime.datetime),
        ),
    ]
