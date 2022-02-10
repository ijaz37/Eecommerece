# Generated by Django 4.0.2 on 2022-02-08 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_review_ondate_shopinghistory'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='single_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='ondate',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 8, 23, 38, 30, 595069), verbose_name=datetime.datetime),
        ),
    ]